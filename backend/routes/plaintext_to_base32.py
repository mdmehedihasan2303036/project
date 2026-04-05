"""
PlainText to Base32 conversion route.
"""

import base64


def convert_plaintext_to_base32(user_input: str) -> dict:
    """
    Convert plain text to base32 encoded string.

    Args:
        user_input: Plain text string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base32",
            "result": "",
            "success": True
        }

    try:
        # Encode to bytes then to base32
        encoded_bytes = user_input.encode('utf-8')
        base32_bytes = base64.b32encode(encoded_bytes)
        result_text = base32_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base32",
            "result": result_text,
            "success": True
        }
    except Exception as e:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base32",
            "result": f"❌ Encoding error: {str(e)}",
            "success": True
        }
