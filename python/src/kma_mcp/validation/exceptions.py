"""Custom exceptions for KMA API validation."""


class KMAValidationError(ValueError):
    """Base exception for KMA API validation errors."""


class InvalidDateError(KMAValidationError):
    """Raised when a date parameter is invalid."""


class InvalidTimeError(KMAValidationError):
    """Raised when a time parameter is invalid."""


class InvalidStationError(KMAValidationError):
    """Raised when a station ID is invalid."""


class InvalidCoordinateError(KMAValidationError):
    """Raised when latitude or longitude is invalid."""
