# CryptInfoBD - Architecture Diagram

## Application Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │           Dropdown: "Select Conversion"                   │ │
│  │  [Decimal to Binary ▼]                                    │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    ROUTER                                 │ │
│  │         (QStackedWidget Navigation)                       │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │               CURRENT PAGE                                │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │  Input Field: [Enter value...]                      │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │  [Convert Button]                                   │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │  Output Field: [Result displays here...]           │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │  Error Label: ⚠ [Errors show here]                 │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    [User Clicks Convert]
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                              │
│                     (PyQt6 Pages)                               │
│                                                                 │
│  • decimal_to_binary_page.py                                   │
│  • decimal_to_hex_page.py                                      │
│  • decimal_to_octal_page.py                                    │
│  • binary_to_decimal_page.py                                   │
│  • hex_to_decimal_page.py                                      │
│  • octal_to_decimal_page.py                                    │
│  • symbol_to_decimal_page.py                                   │
│                                                                 │
│  [Calls Backend Function]                                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND LAYER                               │
│                   (Pure Python Logic)                           │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                 VALIDATORS                                │ │
│  │  • validate_decimal_input()                               │ │
│  │  • validate_binary_input()                                │ │
│  │  • validate_hexadecimal_input()                           │ │
│  │  • validate_octal_input()                                 │ │
│  │  • validate_symbol_input()                                │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│                         [If Valid]                              │
│                              ↓                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              CONVERSION ROUTES                            │ │
│  │  • convert_decimal_to_binary()                            │ │
│  │  • convert_decimal_to_hexadecimal()                       │ │
│  │  • convert_decimal_to_octal()                             │ │
│  │  • convert_binary_to_decimal()                            │ │
│  │  • convert_hexadecimal_to_decimal()                       │ │
│  │  • convert_octal_to_decimal()                             │ │
│  │  • convert_symbol_to_decimal()                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│                    [Returns Dictionary]                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                  {
                    "input": "42",
                    "conversion_type": "decimal_to_binary",
                    "result": "101010",
                    "success": true
                  }
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                              │
│                   (Displays Result)                             │
│                                                                 │
│  [Updates Output Field with Result]                            │
│  [Shows Success/Error Message]                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                     [User Sees Result!]
```

## Component Hierarchy

```
CryptInfoBDApp (Main Window)
│
├── Header Label
│
├── Dropdown (ConversionDropdown)
│   └── [Emits conversion_changed signal]
│
└── Router (QStackedWidget)
    │
    ├── DecimalToBinaryPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    ├── DecimalToHexPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    ├── DecimalToOctalPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    ├── BinaryToDecimalPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    ├── HexToDecimalPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    ├── OctalToDecimalPage
    │   ├── InputField
    │   ├── Convert Button
    │   ├── OutputField
    │   └── ErrorLabel
    │
    └── SymbolToDecimalPage
        ├── InputField
        ├── Convert Button
        ├── OutputField
        └── ErrorLabel
```

## Data Flow Diagram

```
┌──────────┐
│   User   │
└────┬─────┘
     │ Types input
     ↓
┌─────────────────┐
│  Input Field    │
└────┬────────────┘
     │ Presses Enter / Clicks Button
     ↓
┌──────────────────┐
│  Page Handler    │ ← Frontend Layer
└────┬─────────────┘
     │ Calls backend function
     ↓
┌──────────────────┐
│   Validator      │ ← Backend Layer
└────┬─────────────┘
     │ If valid
     ↓
┌──────────────────┐
│  Converter       │ ← Backend Layer
└────┬─────────────┘
     │ Returns result dict
     ↓
┌──────────────────┐
│  Page Handler    │ ← Frontend Layer
└────┬─────────────┘
     │ Updates UI
     ↓
┌──────────────────┐
│  Output Field    │
└────┬─────────────┘
     │ Displays result
     ↓
┌──────────┐
│   User   │ Sees result!
└──────────┘
```

## Error Flow Diagram

```
┌──────────┐
│   User   │
└────┬─────┘
     │ Enters invalid input
     ↓
┌─────────────────┐
│  Input Field    │
└────┬────────────┘
     │
     ↓
┌──────────────────┐
│  Page Handler    │
└────┬─────────────┘
     │ Calls backend
     ↓
┌──────────────────┐
│   Validator      │
└────┬─────────────┘
     │ Raises Exception!
     ↓
┌──────────────────┐
│  Exception       │ (InvalidInputError, etc.)
└────┬─────────────┘
     │ Caught by page
     ↓
┌──────────────────┐
│  Page Handler    │
└────┬─────────────┘
     │ Shows error
     ↓
┌──────────────────┐
│  Error Label     │
└────┬─────────────┘
     │ ⚠ Displays friendly message
     ↓
┌──────────┐
│   User   │ Corrects input
└──────────┘
```

## File Organization

```
project/
│
├── run.py                  ← Entry Point
│
├── backend/                ← Backend Layer (No UI)
│   ├── routes/            ← Conversion Logic
│   └── utils/             ← Validation & Exceptions
│
└── frontend/               ← Frontend Layer (UI Only)
    ├── app.py             ← Main Window
    ├── router.py          ← Page Navigation
    ├── components/        ← Reusable Widgets
    └── pages/             ← Conversion Pages
```

## Key Design Principles

1. **Separation of Concerns**
   - Backend = Logic only
   - Frontend = UI only
   - Clear boundaries

2. **Single Responsibility**
   - One page per conversion
   - One route per conversion
   - One component per UI element

3. **DRY (Don't Repeat Yourself)**
   - Reusable components
   - Centralized validation
   - Shared error handling

4. **Fail-Safe**
   - Validate all inputs
   - Never crash
   - Always provide feedback

5. **Modular**
   - Easy to add new conversions
   - Easy to modify existing ones
   - Easy to test
