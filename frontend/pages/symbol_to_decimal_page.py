"""
Symbol/Word to Decimal (ASCII/Unicode) conversion page.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from frontend.components.input_field import InputField
from frontend.components.output_field import OutputField
from backend.routes.symbol_to_decimal import convert_symbol_to_decimal
from backend.utils.exceptions import CryptInfoBDException


class SymbolToDecimalPage(QWidget):
    """
    Page for converting symbols/words to their ASCII/Unicode decimal values.
    """

    # Signal emitted when logout is requested
    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        """Initialize the Symbol to Decimal page."""
        super().__init__(parent)

        # Create layout
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("Symbol / Word to Decimal Converter")
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
        self.input_field = InputField("Enter symbols or words (e.g., Hello World)\nSupports multiple lines and unlimited text...")

        # Convert button
        self.convert_button = QPushButton("Convert to Decimal")
        self.convert_button.setMinimumHeight(40)
        self.convert_button.setMaximumWidth(350)
        self.convert_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: #27ae60;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)

        # Output field
        output_label = QLabel("Result:")
        output_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #34495e;")
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
        """Perform the symbol to decimal conversion."""
        # Reset output style
        self.output_field.set_default_style()

        # Get input
        user_input = self.input_field.get_text()

        if not user_input:
            self.output_field.clear_result()
            return

        try:
            # Call backend conversion function
            result = convert_symbol_to_decimal(user_input)

            if result["success"]:
                # Display result
                self.output_field.set_result(result["result"])
                self.output_field.set_success_style()
            else:
                # Should not reach here with current backend implementation
                self.output_field.set_result(f"❌ VALUE IS INVALID\n\nError: {result.get('error', 'Conversion failed')}")
                self.output_field.setStyleSheet("""
                    QTextEdit {
                        font-size: 14px;
                        padding: 8px;
                        border: 2px solid #e74c3c;
                        border-radius: 5px;
                        background-color: #fadbd8;
                        color: #c0392b;
                        font-weight: bold;
                    }
                """)

        except CryptInfoBDException as e:
            # Display validation/conversion error
            self.output_field.set_result(f"❌ VALUE IS INVALID\n\nError: {str(e)}")
            self.output_field.setStyleSheet("""
                QTextEdit {
                    font-size: 14px;
                    padding: 8px;
                    border: 2px solid #e74c3c;
                    border-radius: 5px;
                    background-color: #fadbd8;
                    color: #c0392b;
                    font-weight: bold;
                }
            """)
        except Exception as e:
            # Unexpected error
            self.output_field.set_result(f"❌ VALUE IS INVALID\n\nUnexpected error: {str(e)}")
            self.output_field.setStyleSheet("""
                QTextEdit {
                    font-size: 14px;
                    padding: 8px;
                    border: 2px solid #e74c3c;
                    border-radius: 5px;
                    background-color: #fadbd8;
                    color: #c0392b;
                    font-weight: bold;
                }
            """)

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
