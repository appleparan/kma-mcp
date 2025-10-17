"""Pytest configuration and fixtures for API tests."""

import pytest
from fastapi.testclient import TestClient

from kma_mcp.api.settings import Settings, get_settings


@pytest.fixture
def test_settings() -> Settings:
    """Create test settings with overrides for testing.

    Returns:
        Settings: Test configuration settings.
    """
    return Settings(
        debug=True,
        log_level='DEBUG',
        api_host='127.0.0.1',
        api_port=5000,
        cors_origins=['http://localhost:3000'],
        max_workers=1,
        model_name='test_model',
        model_path='tests/fixtures/models/',
        max_batch_size=10,
        timeout_seconds=5.0,
    )


@pytest.fixture
def app(test_settings: Settings):
    """Create FastAPI app instance for testing.

    Args:
        test_settings: Test configuration settings.

    Yields:
        FastAPI: Test FastAPI application instance.
    """

    # Override settings for testing
    def get_test_settings():
        return test_settings

    # Create app with test settings
    from kma_mcp.app import create_app

    app = create_app(settings=test_settings)

    # Override the settings dependency
    app.dependency_overrides[get_settings] = get_test_settings

    yield app

    # Clean up
    app.dependency_overrides.clear()


@pytest.fixture
def client(app):
    """Create test client for API testing.

    Args:
        app: FastAPI application instance.

    Returns:
        TestClient: FastAPI test client.
    """
    return TestClient(app)


@pytest.fixture
def sample_prediction_data():
    """Sample data for prediction tests.

    Returns:
        list: Sample input data for predictions.
    """
    return [
        {'feature1': 1.0, 'feature2': 2.0},
        {'feature1': 3.0, 'feature2': 4.0},
        {'feature1': 5.0, 'feature2': 6.0},
    ]
