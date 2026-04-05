# CryptInfoBD - Number System Converter

A complete desktop application for converting between different number systems (decimal, binary, hexadecimal, octal) and converting symbols/words to their ASCII/Unicode decimal values.

## Features

- **Decimal to Binary** - Convert decimal numbers to binary representation
- **Decimal to Hexadecimal** - Convert decimal numbers to hexadecimal
- **Decimal to Octal** - Convert decimal numbers to octal
- **Binary to Decimal** - Convert binary numbers to decimal
- **Hexadecimal to Decimal** - Convert hexadecimal to decimal
- **Octal to Decimal** - Convert octal to decimal
- **Symbol/Word to Decimal** - Convert characters and words to ASCII/Unicode decimal values

## Tech Stack

### Backend
- Python 3.10+
- Pure Python modules
- Clean separation of concerns
- Comprehensive input validation
- Custom exception handling

### Frontend
- PyQt6 for desktop UI
- Page-based navigation
- Dropdown routing system
- Responsive error handling

## Project Structure

```
project/
├── backend/
│   ├── main.py                    # Backend entry point
│   ├── routes/                    # Conversion logic modules
│   │   ├── decimal_to_binary.py
│   │   ├── decimal_to_hexadecimal.py
│   │   ├── decimal_to_octal.py
│   │   ├── binary_to_decimal.py
│   │   ├── hexadecimal_to_decimal.py
│   │   ├── octal_to_decimal.py
│   │   └── symbol_to_decimal.py
│   └── utils/                     # Utilities
│       ├── validators.py          # Input validation
│       └── exceptions.py          # Custom exceptions
├── frontend/
│   ├── app.py                     # Main application entry point
│   ├── router.py                  # Page routing logic
│   ├── pages/                     # Individual conversion pages
│   │   ├── decimal_to_binary_page.py
│   │   ├── decimal_to_hex_page.py
│   │   ├── decimal_to_octal_page.py
│   │   ├── binary_to_decimal_page.py
│   │   ├── hex_to_decimal_page.py
│   │   ├── octal_to_decimal_page.py
│   │   └── symbol_to_decimal_page.py
│   └── components/                # Reusable UI components
│       ├── dropdown.py
│       ├── input_field.py
│       ├── output_field.py
│       └── error_label.py
└── requirements.txt
```

## Installation

1. **Prerequisites**
   - Python 3.10 or higher
   - pip (Python package manager)

2. **Install Dependencies**
   ```bash
   cd project
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python run.py
```

Or with the full path:

```bash
cd "c:\Users\Mehedi\OneDrive\Desktop\versity Project\CryptInfoBD\project"
python run.py
```

## Usage

1. **Launch the application** - Run `python frontend/app.py`
2. **Select conversion type** - Use the dropdown menu to choose your desired conversion
3. **Enter input** - Type your value in the input field
4. **Convert** - Click the "Convert" button or press Enter
5. **View result** - The converted value appears in the output field

### Examples

- **Decimal to Binary**: Input `42` → Output `101010`
- **Hexadecimal to Decimal**: Input `FF` → Output `255`
- **Symbol to Decimal**: Input `Hello` → Output `[72, 101, 108, 108, 111]`

## Features Highlights

### Input Validation
- Comprehensive validation for each number system
- Clear error messages for invalid inputs
- Range checking for decimal values

### User-Friendly Interface
- Clean, modern design
- Color-coded conversion buttons
- Real-time error feedback
- Keyboard shortcuts (Enter to convert)

### Error Handling
- Never crashes on invalid input
- Friendly error messages
- Visual feedback for success/failure

## Architecture

### Backend
- **Pure logic layer** - No UI code in backend
- **Modular design** - Each conversion in its own file
- **Type hints** - Full type annotation throughout
- **Custom exceptions** - Structured error handling

### Frontend
- **Component-based** - Reusable UI components
- **Page routing** - Clean navigation between conversions
- **Separation of concerns** - Clear distinction from backend

## Development

### Adding a New Conversion

1. Create conversion logic in `backend/routes/new_conversion.py`
2. Create page in `frontend/pages/new_conversion_page.py`
3. Register page in `frontend/app.py`
4. Add option to dropdown in `frontend/components/dropdown.py`

### Code Standards
- Type hints on all functions
- Docstrings for all modules and functions
- No global variables
- Centralized validation
- Clean separation between backend and frontend

## Requirements

- Python 3.10+
- PyQt6 6.4.0+

## License

Created for educational purposes as part of the CryptInfoBD project.

## Author

Built by a senior full-stack desktop application engineer
