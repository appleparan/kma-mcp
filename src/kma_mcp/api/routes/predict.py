"""Prediction endpoints."""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from kma_mcp.api.settings import Settings, get_settings

router = APIRouter()
settings = get_settings()


class PredictionRequest(BaseModel):
    """Prediction request model."""

    data: list[Any] = Field(..., description='Input data for prediction')
    model_name: str | None = Field(None, description='Model name to use for prediction')


class PredictionResponse(BaseModel):
    """Prediction response model."""

    predictions: list[Any] = Field(..., description='Model predictions')
    model_name: str = Field(..., description='Model used for prediction')
    processing_time: float = Field(..., description='Processing time in seconds')


@router.post('/predict', response_model=PredictionResponse)
async def predict(
    request: PredictionRequest,
    settings: Settings = Depends(get_settings),  # noqa: B008
) -> PredictionResponse:
    """Make predictions using the specified model.

    Args:
        request: Prediction request containing input data.
        settings: Application settings.

    Returns:
        PredictionResponse: Prediction results.

    Raises:
        HTTPException: If prediction fails or input is invalid.
    """
    import time

    start_time = time.time()

    # Validate batch size
    if len(request.data) > settings.max_batch_size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Batch size {len(request.data)} exceeds maximum {settings.max_batch_size}',
        )

    try:
        # Use default model if not specified
        model_name = request.model_name or settings.model_name

        # TODO: Implement actual model prediction logic here
        # For now, return dummy predictions
        predictions = [f'prediction_{i}' for i in range(len(request.data))]

        processing_time = time.time() - start_time

        return PredictionResponse(
            predictions=predictions,
            model_name=model_name,
            processing_time=processing_time,
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Prediction failed: {e!s}'
        ) from e


@router.get('/models', response_model=list[str])
async def list_models(settings: Settings = Depends(get_settings)) -> list[str]:  # noqa: B008
    """List available models.

    Args:
        settings: Application settings.

    Returns:
        list[str]: List of available model names.
    """
    # TODO: Implement actual model listing logic
    return [settings.model_name, 'model_v1', 'model_v2']
