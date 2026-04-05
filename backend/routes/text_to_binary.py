"""
Text to Binary conversion route.
Converts text characters to their binary ASCII codes.
"""


def convert_text_to_binary(user_input: str) -> dict:
    """
    Convert text characters to binary ASCII codes.

    Args:
        user_input: Text string to convert

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "text_to_binary",
            "result": "",
            "success": True
        }

    result_numbers = []

    for char in user_input:
        # Get ASCII value and convert to binary
        decimal_value = ord(char)
        binary_value = bin(decimal_value)[2:]  # Remove '0b' prefix
        result_numbers.append(binary_value)

    # Join with spaces
    result_text = ' '.join(result_numbers)

    return {
        "input": user_input,
        "conversion_type": "text_to_binary",
        "result": result_text,
        "success": True
    }
