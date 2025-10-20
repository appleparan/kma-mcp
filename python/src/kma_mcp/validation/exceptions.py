"""Custom exceptions for KMA API validation."""


class KMAValidationError(ValueError):
    """Base exception for KMA API validation errors."""

    pass


class InvalidDateError(KMAValidationError):
    """Raised when a date parameter is invalid."""

    pass


class InvalidTimeError(KMAValidationError):
    """Raised when a time parameter is invalid."""

    pass


class InvalidStationError(KMAValidationError):
    """Raised when a station ID is invalid."""

    pass


class InvalidCoordinateError(KMAValidationError):
    """Raised when latitude or longitude is invalid."""

    pass
