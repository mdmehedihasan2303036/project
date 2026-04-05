"""
Base64 to PlainText conversion route.
"""

import base64


def convert_base64_to_plaintext(user_input: str) -> dict:
    """
    Convert base64 encoded string to plain text.

    Args:
        user_input: Base64 encoded string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "base64_to_plaintext",
            "result": "",
            "success": True
        }

    try:
        # Remove whitespace and newlines
        cleaned_input = user_input.strip().replace('\n', '').replace(' ', '')

        # Decode base64
        decoded_bytes = base64.b64decode(cleaned_input)
        result_text = decoded_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "base64_to_plaintext",
            "result": result_text,
            "success": True
        }
    except Exception:
        # If decoding fails, return error indicator
        return {
            "input": user_input,
            "conversion_type": "base64_to_plaintext",
            "result": "❌ Invalid Base64 string",
            "success": True
        }
