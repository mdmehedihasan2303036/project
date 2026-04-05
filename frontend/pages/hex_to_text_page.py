"""
Hexadecimal to Text conversion page.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from frontend.components.input_field import InputField
from frontend.components.output_field import OutputField
from backend.routes.hexadecimal_to_text import convert_hexadecimal_to_text
from backend.utils.exceptions import CryptInfoBDException


class HexToTextPage(QWidget):
    """
    Page for converting hexadecimal ASCII codes to text.
    """

    # Signal emitted when logout is requested
    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        """Initialize the Hexadecimal to Text page."""
        super().__init__(parent)

        # Create layout
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("Hexadecimal to Text Converter")
        title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Input field
        self.input_field = InputField("Enter hex ASCII codes (e.g., 48 65 6C 6C 6F)\\nSeparate multiple codes with spaces")

        # Convert button
        self.convert_button = QPushButton("Convert to Text")
        self.convert_button.setMinimumHeight(40)
        self.convert_button.setMaximumWidth(350)
        self.convert_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: #9b59b6;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
            QPushButton:pressed {
                background-color: #7d3c98;
            }
        """)

        # Output field
        self.output_field = OutputField()

        # Copy button
        self.copy_button = QPushButton("📋 Copy")
        self.copy_button.setMinimumHeight(30)
        self.copy_button.setMaximumWidth(120)
        self.copy_button.setStyleSheet("""
            QPushButton {
                font-size: 11px;
                font-weight: bold;
                color: white;
                background-color: #16a085;
                border: none;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #138d75;
            }
            QPushButton:pressed {
                background-color: #117a65;
            }
        """)

        # Logout button
        self.logout_button = QPushButton("🚪 Logout")
        self.logout_button.setMinimumHeight(30)
        self.logout_button.setMaximumWidth(120)
        self.logout_button.setStyleSheet("""
            QPushButton {
                font-size: 11px;
                font-weight: bold;
                color: white;
                background-color: #e74c3c;
                border: none;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)

        # Create horizontal layout for copy and logout buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.logout_button)
        button_layout.addStretch()

        # Add widgets to layout
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)
        layout.addSpacing(5)
        layout.addWidget(self.output_field)
        layout.addLayout(button_layout)
        layout.addStretch()

        self.setLayout(layout)

        # Connect signals
        self.convert_button.clicked.connect(self.perform_conversion)
        self.input_field.enter_pressed.connect(self.perform_conversion)
        self.input_field.textChanged.connect(self.on_input_changed)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.logout_button.clicked.connect(self.logout_requested.emit)

    def perform_conversion(self):
        """Perform the hexadecimal to text conversion."""
        # Reset output style
        self.output_field.set_default_style()

        # Get input
        user_input = self.input_field.get_text()

        if not user_input:
            self.output_field.clear_result()
            return

        try:
            # Call backend conversion function
            result = convert_hexadecimal_to_text(user_input)

            if result["success"]:
                # Display result (numbers out of range shown as 'x')
                self.output_field.set_result(result["result"])
                self.output_field.set_success_style()
            else:
                # Should not reach here with current backend implementation
                self.output_field.clear_result()

        except Exception as e:
            # For any error, show the result with 'x' for invalid values
            # This shouldn't happen now since we handle all cases
            self.output_field.set_result(f"Error: {str(e)}")
            self.output_field.set_success_style()

    def on_input_changed(self):
        """Handle input field changes."""
        pass

    def copy_to_clipboard(self):
        """Copy output field content to clipboard."""
        from PyQt6.QtWidgets import QApplication
        text = self.output_field.get_text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.copy_button.setText("✔ Copied!")
            from PyQt6.QtCore import QTimer
            QTimer.singleShot(1500, lambda: self.copy_button.setText("📋 Copy"))
