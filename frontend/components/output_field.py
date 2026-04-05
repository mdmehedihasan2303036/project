"""
Output field component for displaying conversion results.
"""

from PyQt6.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard
from PyQt6.QtWidgets import QApplication


class OutputField(QTextEdit):
    """
    Read-only output field for displaying conversion results.
    """

    def __init__(self, parent=None):
        """Initialize the output field."""
        super().__init__(parent)

        # Make it read-only
        self.setReadOnly(True)
        self.setMinimumHeight(120)
        self.setMaximumHeight(250)

        # Style the output field
        self.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: #ecf0f1;
            }
        """)

    def set_result(self, result: str):
        """
        Set the result text.

        Args:
            result: Result text to display
        """
        self.setText(result)

    def clear_result(self):
        """Clear the output field."""
        self.clear()

    def get_text(self) -> str:
        """Get the current text from output field."""
        return self.toPlainText()

    def set_success_style(self):
        """Apply success styling to output field."""
        self.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 8px;
                border: 2px solid #27ae60;
                border-radius: 5px;
                background-color: #d5f4e6;
                color: #1e8449;
            }
        """)

    def set_default_style(self):
        """Apply default styling to output field."""
        self.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: #ecf0f1;
            }
        """)
