"""
RSA Encryption page - Use e and d to RSA.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                              QPushButton, QLineEdit, QTextEdit, QApplication)
from PyQt6.QtCore import Qt, pyqtSignal
from backend.routes.rsa_conversion import rsa_encrypt


class RSAEncryptPage(QWidget):
    """
    Page for RSA encryption using e and N parameters.
    Formula: Cipher = (Msg)^e mod N
    """

    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        """Initialize the RSA encryption page."""
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("Use e and d to RSA")
        title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Instructions
        instructions = QLabel(
            'Enter a message (in numeric form) here. Click button to encode. '
            'Break your message into small chunks so that the "Msg" codes are not larger than N.'
        )
        instructions.setWordWrap(True)
        instructions.setStyleSheet("""
            QLabel {
                font-size: 11px;
                color: #34495e;
                padding: 5px 20px;
                background-color: #f0f0f0;
                border-radius: 5px;
                border-left: 3px solid #3498db;
            }
        """)
        instructions.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Message input (large text area)
        self.msg_input = QTextEdit()
        self.msg_input.setPlaceholderText("Enter text to convert...")
        self.msg_input.setMinimumHeight(150)
        self.msg_input.setStyleSheet("""
            QTextEdit {
                font-size: 13px;
                border: 2px solid #3498db;
                border-radius: 5px;
                padding: 10px;
                background-color: #f0f8ff;
                color: #000000;
            }
            QTextEdit:focus {
                border: 2px solid #2980b9;
                background-color: white;
                color: #000000;
            }
        """)

        # Parameters layout with proper spacing
        params_container = QWidget()
        params_layout = QHBoxLayout()
        params_layout.setSpacing(30)
        params_layout.setContentsMargins(0, 15, 0, 15)

        # e input with label
        e_widget = QWidget()
        e_widget.setFixedWidth(250)
        e_widget.setStyleSheet("background-color: transparent;")
        e_v_layout = QVBoxLayout()
        e_v_layout.setSpacing(8)
        e_v_layout.setContentsMargins(0, 0, 0, 0)

        e_label = QLabel("e value:")
        e_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50;")

        self.e_input = QLineEdit()
        self.e_input.setPlaceholderText("Enter e")
        self.e_input.setFixedSize(240, 45)
        self.e_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 10px 12px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
                background-color: #f0f8ff;
            }
        """)

        e_v_layout.addWidget(e_label)
        e_v_layout.addWidget(self.e_input)
        e_widget.setLayout(e_v_layout)

        # d input with label
        d_widget = QWidget()
        d_widget.setFixedWidth(250)
        d_widget.setStyleSheet("background-color: transparent;")
        d_v_layout = QVBoxLayout()
        d_v_layout.setSpacing(8)
        d_v_layout.setContentsMargins(0, 0, 0, 0)

        d_label = QLabel("d value:")
        d_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50;")

        self.d_input = QLineEdit()
        self.d_input.setPlaceholderText("Enter d")
        self.d_input.setFixedSize(240, 45)
        self.d_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 10px 12px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
                background-color: #f0f8ff;
            }
        """)

        d_v_layout.addWidget(d_label)
        d_v_layout.addWidget(self.d_input)
        d_widget.setLayout(d_v_layout)

        # N input with label
        n_widget = QWidget()
        n_widget.setFixedWidth(250)
        n_widget.setStyleSheet("background-color: transparent;")
        n_v_layout = QVBoxLayout()
        n_v_layout.setSpacing(8)
        n_v_layout.setContentsMargins(0, 0, 0, 0)

        n_label = QLabel("N value:")
        n_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50;")

        self.n_input = QLineEdit()
        self.n_input.setPlaceholderText("Enter N")
        self.n_input.setFixedSize(240, 45)
        self.n_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 10px 12px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
                background-color: #f0f8ff;
            }
        """)

        n_v_layout.addWidget(n_label)
        n_v_layout.addWidget(self.n_input)
        n_widget.setLayout(n_v_layout)

        params_layout.addWidget(e_widget)
        params_layout.addWidget(d_widget)
        params_layout.addWidget(n_widget)
        params_container.setLayout(params_layout)

        # Convert button
        button_container = QWidget()
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.convert_button = QPushButton("Convert to RSA")
        self.convert_button.setMinimumHeight(45)
        self.convert_button.setMaximumWidth(400)
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

        button_layout.addWidget(self.convert_button)
        button_layout.addStretch()
        button_container.setLayout(button_layout)

        # Output text area
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setMinimumHeight(150)
        self.output_field.setStyleSheet("""
            QTextEdit {
                font-size: 13px;
                border: 2px solid #95a5a6;
                border-radius: 5px;
                padding: 10px;
                background-color: #f8f9fa;
                color: #000000;
            }
        """)

        # Bottom buttons (Copy and Logout)
        bottom_buttons = QWidget()
        bottom_layout = QHBoxLayout()

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

        bottom_layout.addWidget(self.copy_button)
        bottom_layout.addSpacing(10)
        bottom_layout.addWidget(self.logout_button)
        bottom_layout.addStretch()
        bottom_buttons.setLayout(bottom_layout)

        # Add all widgets to main layout
        layout.addWidget(title)
        layout.addWidget(instructions)
        layout.addWidget(self.msg_input)
        layout.addWidget(params_container)
        layout.addWidget(button_container)
        layout.addWidget(self.output_field)
        layout.addWidget(bottom_buttons)
        layout.addStretch()

        self.setLayout(layout)

        # Connect signals
        self.convert_button.clicked.connect(self._on_convert)
        self.copy_button.clicked.connect(self._on_copy)
        self.logout_button.clicked.connect(self.logout_requested.emit)

    def _on_convert(self):
        """Handle convert button click."""
        msg_text = self.msg_input.toPlainText().strip()
        e_text = self.e_input.text().strip()
        n_text = self.n_input.text().strip()

        # Clear previous output
        self.output_field.clear()

        # Encryption mode
        result = rsa_encrypt(msg_text, e_text, n_text)
        if result.get("success"):
            self.output_field.setPlainText(result.get("result", ""))
        else:
            self.output_field.setPlainText(f"Error: {result.get('error', 'Unknown error')}")

    def _on_copy(self):
        """Copy output to clipboard."""
        clipboard = QApplication.clipboard()
        text = self.output_field.toPlainText()
        if text:
            clipboard.setText(text)
