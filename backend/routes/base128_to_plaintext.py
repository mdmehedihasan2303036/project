"""
Base128 to PlainText conversion route.
Note: Base128 is not a standard encoding. Using base85 (ASCII85) instead.
"""

import base64


def convert_base128_to_plaintext(user_input: str) -> dict:
    """
    Convert base85 encoded string to plain text.

    Args:
        user_input: Base85 encoded string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "base128_to_plaintext",
            "result": "",
            "success": True
        }

    try:
        # Remove whitespace and newlines
        cleaned_input = user_input.strip().replace('\n', '').replace(' ', '')

        # Decode base85
        decoded_bytes = base64.b85decode(cleaned_input)
        result_text = decoded_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "base128_to_plaintext",
            "result": result_text,
            "success": True
        }
    except Exception:
        # If decoding fails, return error indicator
        return {
            "input": user_input,
            "conversion_type": "base128_to_plaintext",
            "result": "❌ Invalid Base128 string",
            "success": True
        }
