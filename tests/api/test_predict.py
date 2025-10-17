"""Tests for prediction endpoints."""

import pytest
from fastapi import status
from fastapi.testclient import TestClient


class TestPredictEndpoints:
    """Test cases for prediction endpoints."""

    def test_predict_endpoint_success(self, client: TestClient, sample_prediction_data):
        """Test successful prediction request.

        Args:
            client: FastAPI test client.
            sample_prediction_data: Sample input data for predictions.
        """
        request_data = {'data': sample_prediction_data, 'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert 'predictions' in data
        assert 'model_name' in data
        assert 'processing_time' in data

        assert data['model_name'] == 'test_model'
        assert len(data['predictions']) == len(sample_prediction_data)
        assert isinstance(data['processing_time'], float)
        assert data['processing_time'] >= 0

    def test_predict_endpoint_with_default_model(self, client: TestClient, sample_prediction_data):
        """Test prediction request with default model.

        Args:
            client: FastAPI test client.
            sample_prediction_data: Sample input data for predictions.
        """
        request_data = {'data': sample_prediction_data}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['model_name'] == 'test_model'  # From test settings

    def test_predict_endpoint_batch_size_limit(self, client: TestClient):
        """Test prediction request exceeding batch size limit.

        Args:
            client: FastAPI test client.
        """
        # Create data exceeding max_batch_size (10 in test settings)
        large_data = [{'feature': i} for i in range(15)]

        request_data = {'data': large_data, 'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        data = response.json()
        assert 'Batch size' in data['detail']
        assert 'exceeds maximum' in data['detail']

    def test_predict_endpoint_empty_data(self, client: TestClient):
        """Test prediction request with empty data.

        Args:
            client: FastAPI test client.
        """
        request_data = {'data': [], 'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['predictions'] == []

    def test_predict_endpoint_invalid_request(self, client: TestClient):
        """Test prediction request with invalid data structure.

        Args:
            client: FastAPI test client.
        """
        # Missing required 'data' field
        request_data = {'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_list_models_endpoint(self, client: TestClient):
        """Test list models endpoint.

        Args:
            client: FastAPI test client.
        """
        response = client.get('/api/v1/models')

        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert 'test_model' in data

    def test_predict_endpoint_content_type(self, client: TestClient, sample_prediction_data):
        """Test that prediction endpoint returns correct content type.

        Args:
            client: FastAPI test client.
            sample_prediction_data: Sample input data for predictions.
        """
        request_data = {'data': sample_prediction_data, 'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.headers['content-type'] == 'application/json'

    @pytest.mark.parametrize('data_size', [1, 5, 10])
    def test_predict_endpoint_various_batch_sizes(self, client: TestClient, data_size):
        """Test prediction endpoint with various valid batch sizes.

        Args:
            client: FastAPI test client.
            data_size: Size of the data batch to test.
        """
        test_data = [{'feature': i} for i in range(data_size)]

        request_data = {'data': test_data, 'model_name': 'test_model'}

        response = client.post('/api/v1/predict', json=request_data)

        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert len(data['predictions']) == data_size
