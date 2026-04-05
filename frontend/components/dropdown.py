"""
Dropdown component for conversion selection.
"""

from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal


class ConversionDropdown(QComboBox):
    """
    Dropdown widget for selecting conversion type.
    Emits signal when selection changes.
    """

    # Signal emitted when conversion type changes
    conversion_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        """Initialize the dropdown with conversion options."""
        super().__init__(parent)

        # Add conversion options with user-friendly labels
        self.conversion_options = {
            "Decimal to Binary": "decimal_to_binary",
            "Decimal to Hexadecimal": "decimal_to_hexadecimal",
            "Decimal to Octal": "decimal_to_octal",
            "Binary to Decimal": "binary_to_decimal",
            "Hexadecimal to Decimal": "hexadecimal_to_decimal",
            "Octal to Decimal": "octal_to_decimal",
            "Symbol / Word to Decimal": "symbol_to_decimal",
            "Decimal to Text": "decimal_to_text",
            "Hexadecimal to Text": "hexadecimal_to_text",
            "Octal to Text": "octal_to_text",
            "Binary to Text": "binary_to_text",
            "Text to Hexadecimal": "text_to_hexadecimal",
            "Text to Octal": "text_to_octal",
            "Text to Binary": "text_to_binary"
        }

        # Add items to dropdown
        self.addItems(self.conversion_options.keys())

        # Set maximum visible items to 4 (rest will need scrolling)
        self.setMaxVisibleItems(4)

        # Connect signal
        self.currentTextChanged.connect(self._on_selection_changed)

        # Style the dropdown - smaller and centered
        self.setMaximumWidth(400)
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QComboBox {
                font-size: 14px;
                font-weight: bold;
                padding: 8px 15px;
                border: none;
                border-radius: 8px;
                background-color: #16a085;
                color: #ffffff;
            }
            QComboBox:hover {
                background-color: #138d75;
            }
            QComboBox:focus {
                background-color: #138d75;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
                background: transparent;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid #ffffff;
                margin-right: 8px;
            }
            QComboBox QAbstractItemView {
                border: 2px solid #16a085;
                border-radius: 5px;
                background-color: #ffffff;
                color: #2c3e50;
                selection-background-color: #16a085;
                selection-color: #ffffff;
                padding: 5px;
                font-size: 13px;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px;
                color: #2c3e50;
                border: none;
                outline: none;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #e3f2fd;
                color: #2c3e50;
                border: none;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #16a085;
                color: #ffffff;
                border: none;
            }
        """)

    def _on_selection_changed(self, text: str):
        """Handle dropdown selection change."""
        if text in self.conversion_options:
            conversion_type = self.conversion_options[text]
            self.conversion_changed.emit(conversion_type)

    def get_current_conversion_type(self) -> str:
        """Get the currently selected conversion type."""
        current_text = self.currentText()
        return self.conversion_options.get(current_text, "")
