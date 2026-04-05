"""
PlainText to Base64 conversion route.
"""

import base64


def convert_plaintext_to_base64(user_input: str) -> dict:
    """
    Convert plain text to base64 encoded string.

    Args:
        user_input: Plain text string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base64",
            "result": "",
            "success": True
        }

    try:
        # Encode to bytes then to base64
        encoded_bytes = user_input.encode('utf-8')
        base64_bytes = base64.b64encode(encoded_bytes)
        result_text = base64_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base64",
            "result": result_text,
            "success": True
        }
    except Exception as e:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base64",
            "result": f"❌ Encoding error: {str(e)}",
            "success": True
        }
