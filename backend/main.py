"""
Backend main module for CryptInfoBD.
Provides unified interface to all conversion functions.
"""

from .routes.decimal_to_binary import convert_decimal_to_binary
from .routes.decimal_to_hexadecimal import convert_decimal_to_hexadecimal
from .routes.decimal_to_octal import convert_decimal_to_octal
from .routes.binary_to_decimal import convert_binary_to_decimal
from .routes.hexadecimal_to_decimal import convert_hexadecimal_to_decimal
from .routes.octal_to_decimal import convert_octal_to_decimal
from .routes.symbol_to_decimal import convert_symbol_to_decimal
from .utils.exceptions import CryptInfoBDException


class BackendConverter:
    """
    Main converter class providing a unified interface to all conversion operations.
    """

    @staticmethod
    def convert(conversion_type: str, user_input: str) -> dict:
        """
        Execute a conversion based on the conversion type.

        Args:
            conversion_type: Type of conversion to perform
            user_input: User input to convert

        Returns:
            Dictionary with conversion result
        """
        converters = {
            "decimal_to_binary": convert_decimal_to_binary,
            "decimal_to_hexadecimal": convert_decimal_to_hexadecimal,
            "decimal_to_octal": convert_decimal_to_octal,
            "binary_to_decimal": convert_binary_to_decimal,
            "hexadecimal_to_decimal": convert_hexadecimal_to_decimal,
            "octal_to_decimal": convert_octal_to_decimal,
            "symbol_to_decimal": convert_symbol_to_decimal,
        }

        if conversion_type not in converters:
            raise ValueError(f"Unknown conversion type: {conversion_type}")

        try:
            result = converters[conversion_type](user_input)
            return result
        except CryptInfoBDException as e:
            return {
                "input": user_input,
                "conversion_type": conversion_type,
                "result": None,
                "success": False,
                "error": str(e)
            }

    @staticmethod
    def get_available_conversions() -> list:
        """Get list of all available conversions."""
        return [
            "decimal_to_binary",
            "decimal_to_hexadecimal",
            "decimal_to_octal",
            "binary_to_decimal",
            "hexadecimal_to_decimal",
            "octal_to_decimal",
            "symbol_to_decimal",
        ]
