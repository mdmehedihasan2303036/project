"""
Decimal to Binary conversion route.
"""

from ..utils.validators import validate_decimal_input


def convert_decimal_to_binary(decimal_input: str) -> dict:
    """
    Convert a decimal number to binary representation.

    Args:
        decimal_input: String representation of decimal number

    Returns:
        Dictionary with conversion result
    """
    decimal_value = validate_decimal_input(decimal_input)

    if decimal_value == 0:
        binary_result = "0"
    else:
        binary_result = bin(decimal_value)[2:]  # Remove '0b' prefix

    return {
        "input": decimal_input.strip(),
        "conversion_type": "decimal_to_binary",
        "result": binary_result,
        "success": True
    }
