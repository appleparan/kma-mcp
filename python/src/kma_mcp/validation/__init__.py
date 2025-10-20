"""Input validation for KMA API parameters.

This module provides Pydantic-based validation for all KMA API parameters
including dates, times, station IDs, and coordinates.
"""

from kma_mcp.validation.exceptions import (
    InvalidCoordinateError,
    InvalidDateError,
    InvalidStationError,
    InvalidTimeError,
    KMAValidationError,
)
from kma_mcp.validation.params import (
    DateParam,
    DateTimeParam,
    LatitudeParam,
    LongitudeParam,
    StationParam,
    YearParam,
)

__all__ = [
    # Parameter validators
    'DateParam',
    'DateTimeParam',
    'InvalidCoordinateError',
    'InvalidDateError',
    'InvalidStationError',
    'InvalidTimeError',
    # Exceptions
    'KMAValidationError',
    'LatitudeParam',
    'LongitudeParam',
    'StationParam',
    'YearParam',
]
