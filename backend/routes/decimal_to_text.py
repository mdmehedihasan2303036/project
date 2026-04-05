"""
Decimal to Text conversion route.
Converts decimal numbers (ASCII codes) to their text representation.
"""

from backend.utils.validators import validate_decimal_input
from backend.utils.exceptions import ValidationError, OutOfRangeError


def convert_decimal_to_text(user_input: str) -> dict:
    """
    Convert decimal numbers to text characters.
    Numbers out of ASCII range (0-127) are replaced with '❌'.

    Args:
        user_input: Decimal number(s) separated by spaces or commas

    Returns:
        Dictionary with conversion result

    Raises:
        ValidationError: If input format is invalid
    """
    # Split by spaces, commas, or newlines
    numbers = user_input.replace(',', ' ').replace('\n', ' ').split()

    result_chars = []

    for num_str in numbers:
        num_str = num_str.strip()
        if not num_str:
            continue

        try:
            decimal_value = int(num_str)

            # Check ASCII range - use '❌' for out of range
            if decimal_value < 0 or decimal_value > 127:
                result_chars.append('❌')
            else:
                # Convert to character
                char = chr(decimal_value)
                result_chars.append(char)

        except ValueError:
            # For invalid numbers, also use '❌'
            result_chars.append('❌')

    result_text = ''.join(result_chars)

    return {
        "input": user_input,
        "conversion_type": "decimal_to_text",
        "result": result_text,
        "success": True
    }
