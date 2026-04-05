"""
Input field component for user input.
"""

from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QKeyEvent


class InputField(QTextEdit):
    """
    Custom multi-line input field for conversions.
    Supports unlimited text input across multiple lines.
    Emits signal when Ctrl+Enter is pressed.
    """

    # Signal emitted when Ctrl+Enter is pressed
    enter_pressed = pyqtSignal()

    def __init__(self, placeholder: str = "Enter value...", parent=None):
        """
        Initialize the input field.

        Args:
            placeholder: Placeholder text to display
            parent: Parent widget
        """
        super().__init__(parent)

        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(150)
        self.setMaximumHeight(300)

        # Style the input field with black text and light blue background
        self.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: #e8f4f8;
                color: #000000;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QTextEdit:focus {
                border: 2px solid #3498db;
            }
        """)

    def keyPressEvent(self, event: QKeyEvent):
        """Handle key press events."""
        # Emit signal when Ctrl+Enter is pressed
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter) and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.enter_pressed.emit()
        else:
            super().keyPressEvent(event)

    def get_text(self) -> str:
        """Get the current text value."""
        return self.toPlainText().strip()

    def set_text(self, text: str):
        """Set the text value."""
        self.setPlainText(text)
