"""
Base Conversion Dropdown component.
"""

from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal


class BaseConversionDropdown(QComboBox):
    """
    Dropdown widget for selecting base conversion type.
    Emits signal when selection changes.
    """

    # Signal emitted when conversion type changes
    conversion_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        """Initialize the dropdown with base conversion options."""
        super().__init__(parent)

        # Add base conversion options
        self.conversion_options = {
            "Base64 to PlainText": "base64_to_plaintext",
            "PlainText to Base64": "plaintext_to_base64",
            "Base32 to PlainText": "base32_to_plaintext",
            "PlainText to Base32": "plaintext_to_base32",
            "Base128 to PlainText": "base128_to_plaintext",
            "PlainText to Base128": "plaintext_to_base128"
        }

        # Add items to dropdown
        self.addItems(self.conversion_options.keys())

        # Set maximum visible items
        self.setMaxVisibleItems(4)

        # Connect signal
        self.currentTextChanged.connect(self._on_selection_changed)

        # Style the dropdown
        self.setMaximumWidth(400)
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QComboBox {
                font-size: 14px;
                font-weight: bold;
                padding: 8px 15px;
                border: none;
                border-radius: 8px;
                background-color: #9b59b6;
                color: #ffffff;
            }
            QComboBox:hover {
                background-color: #8e44ad;
            }
            QComboBox:focus {
                background-color: #8e44ad;
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
                border: 2px solid #9b59b6;
                border-radius: 5px;
                background-color: #ffffff;
                color: #2c3e50;
                selection-background-color: #9b59b6;
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
                background-color: #9b59b6;
                color: #ffffff;
                border: none;
            }
        """)

    def _on_selection_changed(self, text):
        """Handle selection change event."""
        conversion_type = self.conversion_options.get(text)
        if conversion_type:
            self.conversion_changed.emit(conversion_type)

    def get_current_conversion_type(self):
        """Get the currently selected conversion type key."""
        current_text = self.currentText()
        return self.conversion_options.get(current_text)
