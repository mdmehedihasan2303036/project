"""
Binary to Text conversion route.
Converts binary numbers (ASCII codes) to their text representation.
"""

from backend.utils.validators import validate_binary_input
from backend.utils.exceptions import ValidationError, OutOfRangeError


def convert_binary_to_text(user_input: str) -> dict:
    """
    Convert binary numbers to text characters.
    Numbers out of ASCII range (0-1111111 binary) are replaced with '❌'.

    Args:
        user_input: Binary number(s) separated by spaces or commas

    Returns:
        Dictionary with conversion result
    """
    # Split by spaces, commas, or newlines
    numbers = user_input.replace(',', ' ').replace('\n', ' ').split()

    result_chars = []

    for num_str in numbers:
        num_str = num_str.strip()
        if not num_str:
            continue

        # Remove 0b or 0B prefix if present
        if num_str.lower().startswith('0b'):
            num_str = num_str[2:]

        try:
            decimal_value = int(num_str, 2)

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
        "conversion_type": "binary_to_text",
        "result": result_text,
        "success": True
    }
