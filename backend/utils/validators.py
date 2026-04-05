"""
Validation utilities for the CryptInfoBD backend.
"""

from .exceptions import InvalidInputError, OutOfRangeError


def validate_decimal_input(value: str) -> int:
    """
    Validate and convert a decimal string input to integer.

    Args:
        value: String representation of a decimal number

    Returns:
        Integer value of the input

    Raises:
        InvalidInputError: If input is not a valid decimal number
        OutOfRangeError: If input is out of acceptable range
    """
    value = value.strip()

    if not value:
        raise InvalidInputError("Input cannot be empty")

    try:
        decimal_value = int(value)
    except ValueError:
        raise InvalidInputError(f"'{value}' is not a valid decimal number")

    if decimal_value < 0:
        raise OutOfRangeError("Decimal value must be non-negative")

    if decimal_value > 2**32 - 1:
        raise OutOfRangeError("Decimal value exceeds maximum allowed (4294967295)")

    return decimal_value


def validate_binary_input(value: str) -> str:
    """
    Validate a binary string input.

    Args:
        value: String representation of a binary number

    Returns:
        Valid binary string (cleaned)

    Raises:
        InvalidInputError: If input is not a valid binary number
    """
    value = value.strip()

    if not value:
        raise InvalidInputError("Input cannot be empty")

    if not all(c in '01' for c in value):
        raise InvalidInputError("Binary input must contain only 0 and 1")

    if len(value) > 32:
        raise OutOfRangeError("Binary value exceeds 32 bits")

    return value


def validate_hexadecimal_input(value: str) -> str:
    """
    Validate a hexadecimal string input.

    Args:
        value: String representation of a hexadecimal number

    Returns:
        Valid hexadecimal string (cleaned and uppercase)

    Raises:
        InvalidInputError: If input is not a valid hexadecimal number
    """
    value = value.strip().upper()

    if not value:
        raise InvalidInputError("Input cannot be empty")

    # Remove '0x' or '0X' prefix if present
    if value.startswith('0X'):
        value = value[2:]

    if not value:
        raise InvalidInputError("Hexadecimal input invalid after removing prefix")

    try:
        int(value, 16)
    except ValueError:
        raise InvalidInputError(f"'{value}' is not a valid hexadecimal number")

    return value


def validate_octal_input(value: str) -> str:
    """
    Validate an octal string input.

    Args:
        value: String representation of an octal number

    Returns:
        Valid octal string (cleaned)

    Raises:
        InvalidInputError: If input is not a valid octal number
    """
    value = value.strip()

    if not value:
        raise InvalidInputError("Input cannot be empty")

    # Remove '0o' or '0O' prefix if present
    if value.startswith(('0o', '0O')):
        value = value[2:]

    if not value:
        raise InvalidInputError("Octal input invalid after removing prefix")

    if not all(c in '01234567' for c in value):
        raise InvalidInputError("Octal input must contain only digits 0-7")

    try:
        int(value, 8)
    except ValueError:
        raise InvalidInputError(f"'{value}' is not a valid octal number")

    return value


def validate_symbol_input(value: str) -> str:
    """
    Validate symbol/word input for ASCII/Unicode conversion.

    Args:
        value: String containing symbols or words

    Returns:
        Valid symbol string (cleaned)

    Raises:
        InvalidInputError: If input is empty
    """
    value = value.strip()

    if not value:
        raise InvalidInputError("Input cannot be empty")

    return value
