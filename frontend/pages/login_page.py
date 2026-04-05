"""
Login Page for CryptInfoBD Application.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class LoginPage(QWidget):
    """
    Login page widget for user authentication.
    Emits login_successful signal when user successfully logs in.
    """

    # Signal emitted when login is successful
    login_successful = pyqtSignal()

    def __init__(self):
        """Initialize the login page."""
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """Set up the login page UI."""
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

        # Add vertical stretch to center content
        main_layout.addStretch()

        # Create login container (centered card)
        login_container = QFrame()
        login_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #3498db;
                border-radius: 15px;
                padding: 45px;
            }
        """)
        login_container.setMaximumWidth(550)
        login_container.setMinimumWidth(500)

        container_layout = QVBoxLayout()
        container_layout.setSpacing(25)

        # Title
        title = QLabel("Welcome to CryptInfoBD")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
                padding: 15px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:0.5 #2980b9, stop:1 #8e44ad);
                border-radius: 10px;
                letter-spacing: 1px;
            }
        """)

        # Email field
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setMinimumHeight(45)
        self.email_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
                background-color: #f8f9fa;
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: white;
                color: black;
            }
        """)

        # Password field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setMinimumHeight(45)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
                background-color: #f8f9fa;
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: white;
                color: black;
            }
        """)

        # Connect Enter key press to login
        self.password_input.returnPressed.connect(self._handle_login)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setMinimumHeight(50)
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 5px;
                font-size: 15px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.login_button.clicked.connect(self._handle_login)

        # Error label (hidden by default)
        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setStyleSheet("color: #e74c3c; font-size: 12px;")
        self.error_label.hide()

        # Add widgets to container layout
        container_layout.addWidget(title)
        container_layout.addWidget(self.email_input)
        container_layout.addWidget(self.password_input)
        container_layout.addWidget(self.error_label)
        container_layout.addWidget(self.login_button)

        login_container.setLayout(container_layout)

        # Create horizontal layout to center the login container
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(login_container)
        h_layout.addStretch()

        # Add to main layout
        main_layout.addLayout(h_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

        # Set background color
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
            }
        """)

    def _handle_login(self):
        """Handle login button click."""
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        # Hide previous error
        self.error_label.hide()

        # Validate inputs
        if not email or not password:
            self.error_label.setText("Please enter both email and password")
            self.error_label.show()
            return

        # Validate email format
        if "@" not in email or "." not in email.split("@")[-1]:
            self.error_label.setText("Please enter a valid email address")
            self.error_label.show()
            return

        # Accept any valid email and password
        self.login_successful.emit()

    def reset_form(self):
        """Reset the login form (useful when showing login page again)."""
        self.email_input.clear()
        self.password_input.clear()
        self.error_label.hide()
        self.email_input.setFocus()
