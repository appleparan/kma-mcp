"""Unit tests for MCP server integration."""

import pytest


class TestMCPServerImport:
    """Test MCP server module can be imported."""

    def test_import_mcp_server(self) -> None:
        """Test that mcp_server module can be imported."""
        import kma_mcp.mcp_server as mcp_server

        assert mcp_server is not None
        assert hasattr(mcp_server, 'mcp')
        assert hasattr(mcp_server, 'API_KEY')

    def test_mcp_instance_exists(self) -> None:
        """Test that FastMCP instance exists."""
        from kma_mcp.mcp_server import mcp

        assert mcp is not None
        assert hasattr(mcp, 'name')
        assert mcp.name == 'KMA ASOS Weather Data'

    def test_api_key_from_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that API key is loaded from environment."""
        monkeypatch.setenv('KMA_API_KEY', 'test_api_key_123')

        # Reload module to pick up new env var
        import importlib

        import kma_mcp.mcp_server

        importlib.reload(kma_mcp.mcp_server)

        assert kma_mcp.mcp_server.API_KEY == 'test_api_key_123'


class TestMCPServerConfiguration:
    """Test MCP server configuration."""

    def test_server_name(self) -> None:
        """Test server has correct name."""
        from kma_mcp.mcp_server import mcp

        assert mcp.name == 'KMA ASOS Weather Data'

    def test_module_has_required_attributes(self) -> None:
        """Test module exports required attributes."""
        import kma_mcp.mcp_server as mcp_server

        # Check for MCP instance
        assert hasattr(mcp_server, 'mcp')

        # Check for API key variable
        assert hasattr(mcp_server, 'API_KEY')
