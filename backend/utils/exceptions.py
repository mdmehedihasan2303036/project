"""
Custom exceptions for the CryptInfoBD backend.
"""


class CryptInfoBDException(Exception):
    """Base exception for all CryptInfoBD errors."""
    pass


class ValidationError(CryptInfoBDException):
    """Raised when input validation fails."""
    pass


class ConversionError(CryptInfoBDException):
    """Raised when a conversion operation fails."""
    pass


class InvalidInputError(ValidationError):
    """Raised when input format is invalid."""
    pass


class OutOfRangeError(ValidationError):
    """Raised when input value is out of acceptable range."""
    pass
