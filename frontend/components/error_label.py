"""
Error label component for displaying error messages.
"""

from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


class ErrorLabel(QLabel):
    """
    Label widget for displaying error messages.
    """

    def __init__(self, parent=None):
        """Initialize the error label."""
        super().__init__(parent)

        self.setWordWrap(True)
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Style the error label
        self.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #e74c3c;
                background-color: #fadbd8;
                border: 1px solid #e74c3c;
                border-radius: 5px;
                padding: 8px;
            }
        """)

    def show_error(self, message: str):
        """Display an error message."""
        self.setText(f"⚠ {message}")
        self.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #e74c3c;
                background-color: #fadbd8;
                border: 1px solid #e74c3c;
                border-radius: 5px;
                padding: 8px;
            }
        """)

    def clear_error(self):
        """Clear the error label."""
        self.setText("")
        self.setStyleSheet("""
            QLabel {
                font-size: 12px;
                background-color: transparent;
                border: none;
                padding: 8px;
            }
        """)
