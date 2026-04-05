"""
Text to Octal conversion route.
Converts text characters to their octal ASCII codes.
"""


def convert_text_to_octal(user_input: str) -> dict:
    """
    Convert text characters to octal ASCII codes.

    Args:
        user_input: Text string to convert

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "text_to_octal",
            "result": "",
            "success": True
        }

    result_numbers = []

    for char in user_input:
        # Get ASCII value and convert to octal
        decimal_value = ord(char)
        octal_value = oct(decimal_value)[2:]  # Remove '0o' prefix
        result_numbers.append(octal_value)

    # Join with spaces
    result_text = ' '.join(result_numbers)

    return {
        "input": user_input,
        "conversion_type": "text_to_octal",
        "result": result_text,
        "success": True
    }
