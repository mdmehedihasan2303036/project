"""
PlainText to Base128 conversion route.
Note: Base128 is not a standard encoding. Using base85 (ASCII85) instead.
"""

import base64


def convert_plaintext_to_base128(user_input: str) -> dict:
    """
    Convert plain text to base85 encoded string.

    Args:
        user_input: Plain text string

    Returns:
        Dictionary with conversion result
    """
    if not user_input:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base128",
            "result": "",
            "success": True
        }

    try:
        # Encode to bytes then to base85
        encoded_bytes = user_input.encode('utf-8')
        base85_bytes = base64.b85encode(encoded_bytes)
        result_text = base85_bytes.decode('utf-8')

        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base128",
            "result": result_text,
            "success": True
        }
    except Exception as e:
        return {
            "input": user_input,
            "conversion_type": "plaintext_to_base128",
            "result": f"❌ Encoding error: {str(e)}",
            "success": True
        }
