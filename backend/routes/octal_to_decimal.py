"""
Octal to Decimal conversion route.
"""

from ..utils.validators import validate_octal_input


def convert_octal_to_decimal(octal_input: str) -> dict:
    """
    Convert an octal number to decimal representation.

    Args:
        octal_input: String representation of octal number

    Returns:
        Dictionary with conversion result
    """
    octal_clean = validate_octal_input(octal_input)

    decimal_result = int(octal_clean, 8)

    return {
        "input": octal_input.strip(),
        "conversion_type": "octal_to_decimal",
        "result": str(decimal_result),
        "success": True
    }
