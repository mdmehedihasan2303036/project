"""
PlainText to Base128 conversion page.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from frontend.components.input_field import InputField
from frontend.components.output_field import OutputField
from backend.routes.plaintext_to_base128 import convert_plaintext_to_base128


class PlaintextToBase128Page(QWidget):
    """
    Page for converting plaintext to Base128 representation.
    """

    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        """Initialize the PlainText to Base128 page."""
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel("PlainText to Base128 Converter")
        title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_field = InputField("Enter text to convert...")

        self.convert_button = QPushButton("Convert to Base128")
        self.convert_button.setMinimumHeight(40)
        self.convert_button.setMaximumWidth(350)
        self.convert_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: #e67e22;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
            QPushButton:pressed {
                background-color: #ba4a00;
            }
        """)

        self.output_field = OutputField()

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

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.logout_button)
        button_layout.addStretch()

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)
        layout.addSpacing(5)
        layout.addWidget(self.output_field)
        layout.addLayout(button_layout)
        layout.addStretch()

        self.setLayout(layout)

        self.convert_button.clicked.connect(self.perform_conversion)
        self.input_field.enter_pressed.connect(self.perform_conversion)
        self.input_field.textChanged.connect(self.on_input_changed)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.logout_button.clicked.connect(self.logout_requested.emit)

    def perform_conversion(self):
        """Perform the plaintext to Base128 conversion."""
        self.output_field.set_default_style()

        user_input = self.input_field.get_text()

        if not user_input:
            self.output_field.clear_result()
            return

        try:
            result = convert_plaintext_to_base128(user_input)

            if result["success"]:
                self.output_field.set_result(result["result"])
                self.output_field.set_success_style()
            else:
                self.output_field.clear_result()

        except Exception as e:
            self.output_field.set_result(f"Error: {str(e)}")
            self.output_field.set_success_style()

    def on_input_changed(self):
        """Handle input field changes."""
        pass

    def copy_to_clipboard(self):
        """Copy output field content to clipboard."""
        text = self.output_field.get_text()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.copy_button.setText("✔ Copied!")
            QTimer.singleShot(1500, lambda: self.copy_button.setText("📋 Copy"))
