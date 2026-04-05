"""
Base32 to PlainText conversion route.
"""

import base64


def convert_base32_to_plaintext(user_input: str) -> dict:
    """
    Convert base32 encoded string to plain text.

    Args:
        user_input: Base32 encoded string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "base32_to_plaintext",
            "result": "",
            "success": True
        }

    try:
        # Remove whitespace and newlines
        cleaned_input = user_input.strip().replace('\n', '').replace(' ', '').upper()

        # Decode base32
        decoded_bytes = base64.b32decode(cleaned_input)
        result_text = decoded_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "base32_to_plaintext",
            "result": result_text,
            "success": True
        }
    except Exception:
        # If decoding fails, return error indicator
        return {
            "input": user_input,
            "conversion_type": "base32_to_plaintext",
            "result": "❌ Invalid Base32 string",
            "success": True
        }
