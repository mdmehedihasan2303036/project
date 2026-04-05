"""
Decimal to Hexadecimal conversion route.
"""

from ..utils.validators import validate_decimal_input


def convert_decimal_to_hexadecimal(decimal_input: str) -> dict:
    """
    Convert a decimal number to hexadecimal representation.

    Args:
        decimal_input: String representation of decimal number

    Returns:
        Dictionary with conversion result
    """
    decimal_value = validate_decimal_input(decimal_input)

    hex_result = hex(decimal_value)[2:].upper()  # Remove '0x' prefix and uppercase

    return {
        "input": decimal_input.strip(),
        "conversion_type": "decimal_to_hexadecimal",
        "result": hex_result,
        "success": True
    }
