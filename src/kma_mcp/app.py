"""FastAPI application factory and main app instance."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kma_mcp.api.routes import health, predict
from kma_mcp.api.settings import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        settings: Optional settings instance. If not provided, will use get_settings().

    Returns:
        FastAPI: Configured FastAPI application instance.
    """
    if settings is None:
        settings = get_settings()

    app = FastAPI(
        title='kma-mcp',
        description='MCP server for Korea Meteorological Administration API access',
        version='0.1.0',
        docs_url='/docs' if settings.debug else None,
        redoc_url='/redoc' if settings.debug else None,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # Include routers
    app.include_router(health.router, prefix='/api/v1', tags=['health'])
    app.include_router(predict.router, prefix='/api/v1', tags=['prediction'])

    return app


# Create app instance
app = create_app()
