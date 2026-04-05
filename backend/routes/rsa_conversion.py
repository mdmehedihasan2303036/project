"""
RSA encryption and decryption operations.
Implements RSA algorithm with user-provided e, d, and N values.
"""

from backend.utils.exceptions import CryptInfoBDException


def rsa_encrypt(message: str, e: str, n: str) -> dict:
    """
    Encrypt a message using RSA algorithm.
    Cipher = (Message)^e mod N

    Args:
        message: The numeric message to encrypt
        e: The public exponent
        n: The modulus N

    Returns:
        Dictionary with encrypted result
    """
    try:
        # Validate inputs
        if not message.strip() or not e.strip() or not n.strip():
            raise CryptInfoBDException("All fields (Message, e, N) are required")

        # Convert to integers
        try:
            msg = int(message.strip())
            exp_e = int(e.strip())
            modulus_n = int(n.strip())
        except ValueError:
            raise CryptInfoBDException("Message, e, and N must be valid integers")

        # Validate values
        if modulus_n <= 0:
            raise CryptInfoBDException("N must be a positive integer")
        if exp_e <= 0:
            raise CryptInfoBDException("e must be a positive integer")
        if msg < 0:
            raise CryptInfoBDException("Message must be non-negative")
        if msg >= modulus_n:
            raise CryptInfoBDException(f"Message must be less than N ({modulus_n})")

        # Perform RSA encryption: Cipher = (Msg)^e mod N
        cipher = pow(msg, exp_e, modulus_n)

        return {
            "result": str(cipher),
            "success": True,
            "operation": "RSA Encryption",
            "formula": f"Cipher = ({msg})^{exp_e} mod {modulus_n} = {cipher}"
        }

    except CryptInfoBDException as e:
        return {
            "result": "",
            "success": False,
            "error": str(e)
        }
    except Exception as e:
        return {
            "result": "",
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }


def rsa_decrypt(cipher: str, d: str, n: str) -> dict:
    """
    Decrypt a cipher using RSA algorithm.
    Message = (Cipher)^d mod N

    Args:
        cipher: The encrypted cipher to decrypt
        d: The private exponent
        n: The modulus N

    Returns:
        Dictionary with decrypted result
    """
    try:
        # Validate inputs
        if not cipher.strip() or not d.strip() or not n.strip():
            raise CryptInfoBDException("All fields (Cipher, d, N) are required")

        # Convert to integers
        try:
            cipher_int = int(cipher.strip())
            exp_d = int(d.strip())
            modulus_n = int(n.strip())
        except ValueError:
            raise CryptInfoBDException("Cipher, d, and N must be valid integers")

        # Validate values
        if modulus_n <= 0:
            raise CryptInfoBDException("N must be a positive integer")
        if exp_d <= 0:
            raise CryptInfoBDException("d must be a positive integer")
        if cipher_int < 0:
            raise CryptInfoBDException("Cipher must be non-negative")
        if cipher_int >= modulus_n:
            raise CryptInfoBDException(f"Cipher must be less than N ({modulus_n})")

        # Perform RSA decryption: Msg = (Cipher)^d mod N
        message = pow(cipher_int, exp_d, modulus_n)

        return {
            "result": str(message),
            "success": True,
            "operation": "RSA Decryption",
            "formula": f"Message = ({cipher_int})^{exp_d} mod {modulus_n} = {message}"
        }

    except CryptInfoBDException as e:
        return {
            "result": "",
            "success": False,
            "error": str(e)
        }
    except Exception as e:
        return {
            "result": "",
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }
