"""
Decimal to Octal conversion route.
"""

from ..utils.validators import validate_decimal_input


def convert_decimal_to_octal(decimal_input: str) -> dict:
    """
    Convert a decimal number to octal representation.

    Args:
        decimal_input: String representation of decimal number

    Returns:
        Dictionary with conversion result
    """
    decimal_value = validate_decimal_input(decimal_input)

    octal_result = oct(decimal_value)[2:]  # Remove '0o' prefix

    return {
        "input": decimal_input.strip(),
        "conversion_type": "decimal_to_octal",
        "result": octal_result,
        "success": True
    }
