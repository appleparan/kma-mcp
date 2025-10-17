"""Tests for FastAPI application setup and configuration."""

from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestApp:
    """Test cases for FastAPI application configuration."""

    def test_app_creation(self, app: FastAPI):
        """Test that the FastAPI app is created correctly.

        Args:
            app: FastAPI application instance.
        """
        assert isinstance(app, FastAPI)
        assert app.title == 'kma-mcp'
        assert app.description == 'MCP server for Korea Meteorological Administration API access'
        assert app.version == '0.1.0'

    def test_app_debug_mode_in_tests(self, app: FastAPI):
        """Test that debug mode enables docs in test environment.

        Args:
            app: FastAPI application instance.
        """
        # In test environment, debug should be True and docs should be enabled
        assert app.docs_url == '/docs'
        assert app.redoc_url == '/redoc'

    def test_cors_middleware_configured(self, client: TestClient):
        """Test that CORS middleware is properly configured.

        Args:
            client: FastAPI test client.
        """
        # Test CORS headers with actual GET request to verify CORS headers are added
        response = client.get('/api/v1/health', headers={'Origin': 'http://localhost:3000'})

        # Should return 200 and have CORS headers
        assert response.status_code == 200
        # Check if Access-Control-Allow-Origin header is present (added by CORS middleware)
        assert (
            'Access-Control-Allow-Origin' in response.headers
            or 'access-control-allow-origin' in response.headers
        )

    def test_api_routes_registered(self, client: TestClient):
        """Test that all API routes are properly registered.

        Args:
            client: FastAPI test client.
        """
        # Test health routes
        response = client.get('/api/v1/health')
        assert response.status_code == 200

        response = client.get('/api/v1/health/ready')
        assert response.status_code == 200

        # Test prediction routes
        response = client.get('/api/v1/models')
        assert response.status_code == 200

        # Test predict endpoint exists (will need valid data to succeed)
        response = client.post('/api/v1/predict', json={'data': []})
        assert response.status_code == 200  # Empty data should work

    def test_openapi_schema_available(self, client: TestClient):
        """Test that OpenAPI schema is available.

        Args:
            client: FastAPI test client.
        """
        response = client.get('/openapi.json')
        assert response.status_code == 200

        schema = response.json()
        assert 'openapi' in schema
        assert 'info' in schema
        assert schema['info']['title'] == 'kma-mcp'
        assert schema['info']['version'] == '0.1.0'

    def test_docs_endpoints_available_in_debug(self, client: TestClient):
        """Test that documentation endpoints are available in debug mode.

        Args:
            client: FastAPI test client.
        """
        # Test Swagger UI
        response = client.get('/docs')
        assert response.status_code == 200
        assert 'text/html' in response.headers['content-type']

        # Test ReDoc
        response = client.get('/redoc')
        assert response.status_code == 200
        assert 'text/html' in response.headers['content-type']
