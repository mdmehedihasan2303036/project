# CryptInfoBD

CryptInfoBD is a desktop crypto-conversion toolkit built with Python and PyQt6.
It combines classic number-system conversion, text encoding/decoding, and RSA numeric operations in one UI.

## GitHub Repository

- Production repository: https://github.com/mdmehedihasan2303036/project.git

## Tech Stack

- Python 3.10+
- PyQt6 (`requirements.txt`)
- Modular backend routes with centralized validation and custom exceptions

## Complete App Features

Total conversion tools currently available in the UI: **22**

### A) Number and Text Conversions (14)
1. Decimal to Binary
2. Decimal to Hexadecimal
3. Decimal to Octal
4. Binary to Decimal
5. Hexadecimal to Decimal
6. Octal to Decimal
7. Symbol / Word to Decimal
8. Decimal to Text
9. Hexadecimal to Text
10. Octal to Text
11. Binary to Text
12. Text to Hexadecimal
13. Text to Octal
14. Text to Binary

### B) Base Encoding Conversions (6)
1. Base64 to PlainText
2. PlainText to Base64
3. Base32 to PlainText
4. PlainText to Base32
5. Base128 to PlainText
6. PlainText to Base128

### C) RSA Tools (2)
1. Use e and d to RSA (encrypt form)
2. Use e and d to Msg (decrypt form)

## User Flow (End-to-End)

1. Run app using `python run.py` or `start.bat`.
2. Login page opens first.
3. User provides valid email format + non-empty password.
4. Main screen opens with 3 dropdown groups:
   - Number/Text group
   - Base Encoding group
   - RSA group
5. Router switches to matching page.
6. Page validates input and calls backend conversion module.
7. Result or validation error is rendered in output area.
8. User can copy output and logout from each page.

## Architecture and Advanced Design Details

### 1) Layered Architecture
- `frontend/` handles only UI and interaction logic.
- `backend/` handles conversion logic and validation.
- `run.py` is launcher and path bootstrapper.

### 2) Router-Based Multi-Page UI
- `frontend/router.py` extends `QStackedWidget`.
- Pages are registered using conversion keys.
- Navigation is key-based and controlled by dropdown signals.

### 3) Signal/Slot Driven Interaction (PyQt6)
- Dropdown emits conversion keys.
- Pages expose `logout_requested` signal.
- App window connects signals to router and login/main view switching.

### 4) Component Reuse
- Shared UI components live in `frontend/components/`.
- Input, output, dropdowns, and error display are reused across pages.

### 5) Validation + Exception Model
- Input validation functions are centralized in `backend/utils/validators.py`.
- Domain exceptions are defined in `backend/utils/exceptions.py`.
- Pages display friendly error text; app avoids hard crashes for invalid user input.

### 6) Conversion Isolation
- Each conversion has its own backend route module in `backend/routes/`.
- This makes debugging, testing, and feature extension straightforward.

## Backend: Module-by-Module Usage

### Core Backend Files
- `backend/main.py`: unified converter interface for core conversion set.
- `backend/utils/validators.py`: decimal/binary/hex/octal/symbol validators.
- `backend/utils/exceptions.py`: custom exception classes used by routes/pages.

### Route Modules and Purpose
- `backend/routes/decimal_to_binary.py`: decimal -> binary
- `backend/routes/decimal_to_hexadecimal.py`: decimal -> hexadecimal
- `backend/routes/decimal_to_octal.py`: decimal -> octal
- `backend/routes/binary_to_decimal.py`: binary -> decimal
- `backend/routes/hexadecimal_to_decimal.py`: hexadecimal -> decimal
- `backend/routes/octal_to_decimal.py`: octal -> decimal
- `backend/routes/symbol_to_decimal.py`: char/string -> decimal code points
- `backend/routes/decimal_to_text.py`: decimal sequence -> text
- `backend/routes/hexadecimal_to_text.py`: hex sequence -> text
- `backend/routes/octal_to_text.py`: octal sequence -> text
- `backend/routes/binary_to_text.py`: binary sequence -> text
- `backend/routes/text_to_hexadecimal.py`: text -> hex values
- `backend/routes/text_to_octal.py`: text -> octal values
- `backend/routes/text_to_binary.py`: text -> binary values
- `backend/routes/base64_to_plaintext.py`: Base64 decode
- `backend/routes/plaintext_to_base64.py`: Base64 encode
- `backend/routes/base32_to_plaintext.py`: Base32 decode
- `backend/routes/plaintext_to_base32.py`: Base32 encode
- `backend/routes/base128_to_plaintext.py`: Base128 decode
- `backend/routes/plaintext_to_base128.py`: Base128 encode
- `backend/routes/rsa_conversion.py`: RSA numeric encrypt/decrypt using modular exponentiation

## Frontend: Module-by-Module Usage

### App Shell and Navigation
- `frontend/app.py`: main window, login-to-main switching, dropdown signal wiring, page registration
- `frontend/router.py`: page registry + key-driven navigation

### Reusable Components
- `frontend/components/dropdown.py`: number/text conversion dropdown
- `frontend/components/base_dropdown.py`: base encoding dropdown
- `frontend/components/rsa_dropdown.py`: RSA dropdown
- `frontend/components/input_field.py`: reusable input widget
- `frontend/components/output_field.py`: reusable output display
- `frontend/components/error_label.py`: reusable error state label

### UI Pages and Backend Mapping
- `frontend/pages/decimal_to_binary_page.py` -> `backend/routes/decimal_to_binary.py`
- `frontend/pages/decimal_to_hex_page.py` -> `backend/routes/decimal_to_hexadecimal.py`
- `frontend/pages/decimal_to_octal_page.py` -> `backend/routes/decimal_to_octal.py`
- `frontend/pages/binary_to_decimal_page.py` -> `backend/routes/binary_to_decimal.py`
- `frontend/pages/hex_to_decimal_page.py` -> `backend/routes/hexadecimal_to_decimal.py`
- `frontend/pages/octal_to_decimal_page.py` -> `backend/routes/octal_to_decimal.py`
- `frontend/pages/symbol_to_decimal_page.py` -> `backend/routes/symbol_to_decimal.py`
- `frontend/pages/decimal_to_text_page.py` -> `backend/routes/decimal_to_text.py`
- `frontend/pages/hex_to_text_page.py` -> `backend/routes/hexadecimal_to_text.py`
- `frontend/pages/octal_to_text_page.py` -> `backend/routes/octal_to_text.py`
- `frontend/pages/binary_to_text_page.py` -> `backend/routes/binary_to_text.py`
- `frontend/pages/text_to_hex_page.py` -> `backend/routes/text_to_hexadecimal.py`
- `frontend/pages/text_to_octal_page.py` -> `backend/routes/text_to_octal.py`
- `frontend/pages/text_to_binary_page.py` -> `backend/routes/text_to_binary.py`
- `frontend/pages/base64_to_plaintext_page.py` -> `backend/routes/base64_to_plaintext.py`
- `frontend/pages/plaintext_to_base64_page.py` -> `backend/routes/plaintext_to_base64.py`
- `frontend/pages/base32_to_plaintext_page.py` -> `backend/routes/base32_to_plaintext.py`
- `frontend/pages/plaintext_to_base32_page.py` -> `backend/routes/plaintext_to_base32.py`
- `frontend/pages/base128_to_plaintext_page.py` -> `backend/routes/base128_to_plaintext.py`
- `frontend/pages/plaintext_to_base128_page.py` -> `backend/routes/plaintext_to_base128.py`
- `frontend/pages/rsa_encrypt_page.py` -> `backend/routes/rsa_conversion.py` (`rsa_encrypt`)
- `frontend/pages/rsa_decrypt_page.py` -> `backend/routes/rsa_conversion.py` (`rsa_decrypt`)

### Login Page
- `frontend/pages/login_page.py`
- Validates email format and non-empty password.
- Emits success signal to open main app view.

## Project Structure

```text
CryptInfoBD/
|-- backend/
|   |-- main.py
|   |-- routes/
|   |-- utils/
|-- frontend/
|   |-- app.py
|   |-- router.py
|   |-- components/
|   |-- pages/
|-- run.py
|-- start.bat
|-- requirements.txt
|-- test_backend.py
|-- README.md
```

## Setup and Run

### Install
```bash
pip install -r requirements.txt
```

### Launch
```bash
python run.py
```

### Windows Shortcut
- Double-click `start.bat`

## Testing

Run smoke tests for backend conversions:

```bash
python test_backend.py
```

Current test script validates primary number conversion pipeline and symbol-to-decimal behavior.

## Related Docs

- `QUICKSTART.md`
- `PROJECT_OVERVIEW.md`
- `ARCHITECTURE.md`
- `HOW_TO_RUN.txt`
- `VISUAL_GUIDE.md`

## License

Educational project.
