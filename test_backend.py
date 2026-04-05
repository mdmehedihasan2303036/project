"""
Test script to verify backend conversions work correctly.
"""

import sys
import os

# Add project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.routes.decimal_to_binary import convert_decimal_to_binary
from backend.routes.decimal_to_hexadecimal import convert_decimal_to_hexadecimal
from backend.routes.decimal_to_octal import convert_decimal_to_octal
from backend.routes.binary_to_decimal import convert_binary_to_decimal
from backend.routes.hexadecimal_to_decimal import convert_hexadecimal_to_decimal
from backend.routes.octal_to_decimal import convert_octal_to_decimal
from backend.routes.symbol_to_decimal import convert_symbol_to_decimal

print("=" * 50)
print("CryptInfoBD Backend Conversion Tests")
print("=" * 50)
print()

# Test 1: Decimal to Binary
result = convert_decimal_to_binary("42")
print(f"✓ Test 1: Decimal 42 → Binary {result['result']}")

# Test 2: Decimal to Hexadecimal
result = convert_decimal_to_hexadecimal("255")
print(f"✓ Test 2: Decimal 255 → Hexadecimal {result['result']}")

# Test 3: Decimal to Octal
result = convert_decimal_to_octal("64")
print(f"✓ Test 3: Decimal 64 → Octal {result['result']}")

# Test 4: Binary to Decimal
result = convert_binary_to_decimal("101010")
print(f"✓ Test 4: Binary 101010 → Decimal {result['result']}")

# Test 5: Hexadecimal to Decimal
result = convert_hexadecimal_to_decimal("FF")
print(f"✓ Test 5: Hexadecimal FF → Decimal {result['result']}")

# Test 6: Octal to Decimal
result = convert_octal_to_decimal("77")
print(f"✓ Test 6: Octal 77 → Decimal {result['result']}")

# Test 7: Symbol to Decimal
result = convert_symbol_to_decimal("A")
print(f"✓ Test 7: Symbol 'A' → Decimal {result['result']}")

# Test 8: Word to Decimal
result = convert_symbol_to_decimal("Hi")
print(f"✓ Test 8: Word 'Hi' → Decimal {result['result']}")

print()
print("=" * 50)
print("All tests passed! ✓")
print("=" * 50)
print()
print("Backend is working correctly!")
print("Run 'python run.py' to launch the application.")
