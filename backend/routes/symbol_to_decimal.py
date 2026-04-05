"""
Symbol/Word to Decimal (ASCII/Unicode) conversion route.
"""

from ..utils.validators import validate_symbol_input


def convert_symbol_to_decimal(symbol_input: str) -> dict:
    """
    Convert symbols or words to their ASCII/Unicode decimal values.

    Args:
        symbol_input: String containing symbols, characters, or words

    Returns:
        Dictionary with conversion result
    """
    symbol_clean = validate_symbol_input(symbol_input)

    # Convert each character to its Unicode decimal value
    decimal_values = [ord(char) for char in symbol_clean]

    # Return single value if only one character, otherwise return list
    if len(decimal_values) == 1:
        result = str(decimal_values[0])
    else:
        result = str(decimal_values)

    return {
        "input": symbol_input.strip(),
        "conversion_type": "symbol_to_decimal",
        "result": result,
        "success": True
    }
