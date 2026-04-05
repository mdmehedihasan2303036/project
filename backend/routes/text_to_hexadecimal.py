"""
Text to Hexadecimal conversion route.
Converts text characters to their hexadecimal ASCII codes.
"""


def convert_text_to_hexadecimal(user_input: str) -> dict:
    """
    Convert text characters to hexadecimal ASCII codes.

    Args:
        user_input: Text string to convert

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "text_to_hexadecimal",
            "result": "",
            "success": True
        }

    result_numbers = []

    for char in user_input:
        # Get ASCII value and convert to hex
        decimal_value = ord(char)
        hex_value = hex(decimal_value)[2:].upper()  # Remove '0x' prefix
        result_numbers.append(hex_value)

    # Join with spaces
    result_text = ' '.join(result_numbers)

    return {
        "input": user_input,
        "conversion_type": "text_to_hexadecimal",
        "result": result_text,
        "success": True
    }
