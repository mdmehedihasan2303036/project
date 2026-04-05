"""
Octal to Text conversion route.
Converts octal numbers (ASCII codes) to their text representation.
"""

from backend.utils.validators import validate_octal_input
from backend.utils.exceptions import ValidationError, OutOfRangeError


def convert_octal_to_text(user_input: str) -> dict:
    """
    Convert octal numbers to text characters.
    Numbers out of ASCII range (0-177 octal) are replaced with '❌'.

    Args:
        user_input: Octal number(s) separated by spaces or commas

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

        # Remove 0o or 0O prefix if present
        if num_str.lower().startswith('0o'):
            num_str = num_str[2:]

        try:
            decimal_value = int(num_str, 8)

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
        "conversion_type": "octal_to_text",
        "result": result_text,
        "success": True
    }
