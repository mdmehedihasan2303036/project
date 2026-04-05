"""
Binary to Decimal conversion route.
"""

from ..utils.validators import validate_binary_input


def convert_binary_to_decimal(binary_input: str) -> dict:
    """
    Convert a binary number to decimal representation.

    Args:
        binary_input: String representation of binary number

    Returns:
        Dictionary with conversion result
    """
    binary_clean = validate_binary_input(binary_input)

    decimal_result = int(binary_clean, 2)

    return {
        "input": binary_input.strip(),
        "conversion_type": "binary_to_decimal",
        "result": str(decimal_result),
        "success": True
    }
