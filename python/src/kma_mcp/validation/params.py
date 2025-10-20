"""Pydantic validators for KMA API parameters."""

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, field_validator

from kma_mcp.validation.exceptions import (
    InvalidCoordinateError,
    InvalidDateError,
    InvalidStationError,
    InvalidTimeError,
)


class DateParam(BaseModel):
    """Validates date in YYYYMMDD format.

    Example:
        >>> date_param = DateParam(value='20250101')
        >>> date_param.value
        '20250101'
        >>> DateParam(value='20250230')  # Invalid date
        InvalidDateError: Invalid date: 20250230
    """

    value: Annotated[str, Field(pattern=r'^\d{8}$', examples=['20250101'])]

    @field_validator('value')
    @classmethod
    def validate_date(cls, v: str) -> str:
        """Validate that the date string represents a valid date."""
        if len(v) != 8 or not v.isdigit():
            msg = f'Date must be 8 digits in YYYYMMDD format, got: {v}'
            raise InvalidDateError(msg)

        try:
            datetime.strptime(v, '%Y%m%d')  # noqa: DTZ007
        except ValueError as e:
            msg = f'Invalid date: {v}'
            raise InvalidDateError(msg) from e

        return v

    def __str__(self) -> str:
        """Return string representation of the date."""
        return self.value


class DateTimeParam(BaseModel):
    """Validates datetime in YYYYMMDDHHmm format.

    Example:
        >>> dt_param = DateTimeParam(value='202501011200')
        >>> dt_param.value
        '202501011200'
        >>> DateTimeParam(value='202501012560')  # Invalid time
        InvalidTimeError: Invalid datetime: 202501012560
    """

    value: Annotated[str, Field(pattern=r'^\d{12}$', examples=['202501011200'])]

    @field_validator('value')
    @classmethod
    def validate_datetime(cls, v: str) -> str:
        """Validate that the datetime string represents a valid datetime."""
        if len(v) != 12 or not v.isdigit():
            msg = f'Datetime must be 12 digits in YYYYMMDDHHmm format, got: {v}'
            raise InvalidTimeError(msg)

        try:
            datetime.strptime(v, '%Y%m%d%H%M')  # noqa: DTZ007
        except ValueError as e:
            msg = f'Invalid datetime: {v}'
            raise InvalidTimeError(msg) from e

        return v

    def __str__(self) -> str:
        """Return string representation of the datetime."""
        return self.value


class YearParam(BaseModel):
    """Validates year in YYYY format.

    Example:
        >>> year = YearParam(value=2025)
        >>> year.value
        2025
        >>> YearParam(value=1800)  # Too old
        InvalidDateError: Year must be between 1900 and 2100, got: 1800
    """

    value: Annotated[int, Field(ge=1900, le=2100, examples=[2025])]

    def __str__(self) -> str:
        """Return string representation of the year."""
        return str(self.value)


class StationParam(BaseModel):
    """Validates station ID.

    Station ID can be:
    - 0: All stations
    - 1-999: ASOS/AWS station number
    - 47001-47999: WMO station code (for upper-air stations)

    Example:
        >>> stn = StationParam(value=108)
        >>> stn.value
        108
        >>> stn = StationParam(value=0)  # All stations
        >>> stn.value
        0
    """

    value: Annotated[int, Field(ge=0, le=99999, examples=[0, 108, 47122])]

    @field_validator('value')
    @classmethod
    def validate_station(cls, v: int) -> int:
        """Validate station ID range."""
        if v < 0 or v > 99999:
            msg = f'Station ID must be between 0 and 99999, got: {v}'
            raise InvalidStationError(msg)
        return v

    def __str__(self) -> str:
        """Return string representation of the station ID."""
        return str(self.value)


class LatitudeParam(BaseModel):
    """Validates latitude coordinate.

    Valid range for Korea region: 33.0 to 43.0

    Example:
        >>> lat = LatitudeParam(value=37.5)
        >>> lat.value
        37.5
    """

    value: Annotated[
        float,
        Field(
            ge=33.0,
            le=43.0,
            examples=[37.5],
            description='Latitude in decimal degrees (Korea region: 33-43)',
        ),
    ]

    @field_validator('value')
    @classmethod
    def validate_latitude(cls, v: float) -> float:
        """Validate latitude is within Korea region."""
        if not (33.0 <= v <= 43.0):
            msg = f'Latitude must be between 33.0 and 43.0 for Korea region, got: {v}'
            raise InvalidCoordinateError(msg)
        return v

    def __str__(self) -> str:
        """Return string representation of the latitude."""
        return str(self.value)


class LongitudeParam(BaseModel):
    """Validates longitude coordinate.

    Valid range for Korea region: 124.0 to 132.0

    Example:
        >>> lon = LongitudeParam(value=127.0)
        >>> lon.value
        127.0
    """

    value: Annotated[
        float,
        Field(
            ge=124.0,
            le=132.0,
            examples=[127.0],
            description='Longitude in decimal degrees (Korea region: 124-132)',
        ),
    ]

    @field_validator('value')
    @classmethod
    def validate_longitude(cls, v: float) -> float:
        """Validate longitude is within Korea region."""
        if not (124.0 <= v <= 132.0):
            msg = f'Longitude must be between 124.0 and 132.0 for Korea region, got: {v}'
            raise InvalidCoordinateError(msg)
        return v

    def __str__(self) -> str:
        """Return string representation of the longitude."""
        return str(self.value)
