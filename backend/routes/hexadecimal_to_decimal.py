"""
Hexadecimal to Decimal conversion route.
"""

from ..utils.validators import validate_hexadecimal_input


def convert_hexadecimal_to_decimal(hex_input: str) -> dict:
    """
    Convert a hexadecimal number to decimal representation.

    Args:
        hex_input: String representation of hexadecimal number

    Returns:
        Dictionary with conversion result
    """
    hex_clean = validate_hexadecimal_input(hex_input)

    decimal_result = int(hex_clean, 16)

    return {
        "input": hex_input.strip(),
        "conversion_type": "hexadecimal_to_decimal",
        "result": str(decimal_result),
        "success": True
    }
