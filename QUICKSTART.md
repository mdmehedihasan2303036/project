# CryptInfoBD - Quick Start Guide

## Installation & Setup

1. **Navigate to the project directory:**
   ```bash
   cd "c:\Users\Mehedi\OneDrive\Desktop\versity Project\CryptInfoBD\project"
   ```

2. **Install dependencies (if not already installed):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

## How to Use

1. **Select Conversion Type** - Use the dropdown menu at the top
2. **Enter Your Input** - Type your value in the input field
3. **Convert** - Click the button or press Enter
4. **View Result** - See the converted value in the output field

## Conversion Examples

### Decimal to Binary
- Input: `42`
- Result: `101010`

### Hexadecimal to Decimal
- Input: `FF` or `0xFF`
- Result: `255`

### Symbol to Decimal
- Input: `A`
- Result: `65`
- Input: `Hello`
- Result: `[72, 101, 108, 108, 111]`

### Binary to Decimal
- Input: `1010`
- Result: `10`

### Decimal to Hexadecimal
- Input: `255`
- Result: `FF`

### Decimal to Octal
- Input: `64`
- Result: `100`

### Octal to Decimal
- Input: `77` or `0o77`
- Result: `63`

## Features

✅ Clean, modern UI
✅ Real-time input validation
✅ Friendly error messages
✅ Keyboard shortcuts (Enter to convert)
✅ No crashes on invalid input
✅ Separate backend and frontend architecture

## Troubleshooting

**Problem: "ModuleNotFoundError: No module named 'PyQt6'"**
- Solution: Run `pip install PyQt6`

**Problem: "ModuleNotFoundError: No module named 'backend'"**
- Solution: Always run using `python run.py` from the project directory

**Problem: Application window doesn't open**
- Make sure you have Python 3.10+ installed
- Make sure PyQt6 is installed
- Try running from the command line to see error messages

## Project Structure

```
project/
├── backend/          # Python backend (conversion logic)
├── frontend/         # PyQt6 frontend (UI)
├── run.py           # Application launcher
├── requirements.txt  # Python dependencies
└── README.md        # Full documentation
```

## Support

For issues or questions, refer to the main README.md file.
