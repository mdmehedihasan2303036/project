"""
CryptInfoBD - Desktop Application for Number System Conversions
Main application file.

This is the entry point for the CryptInfoBD desktop application.
To run: python run.py
"""

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Import components
from frontend.components.dropdown import ConversionDropdown
from frontend.components.base_dropdown import BaseConversionDropdown
from frontend.components.rsa_dropdown import RSAConversionDropdown
from frontend.router import Router

# Import all pages
from frontend.pages.login_page import LoginPage
from frontend.pages.decimal_to_binary_page import DecimalToBinaryPage
from frontend.pages.decimal_to_hex_page import DecimalToHexPage
from frontend.pages.decimal_to_octal_page import DecimalToOctalPage
from frontend.pages.binary_to_decimal_page import BinaryToDecimalPage
from frontend.pages.hex_to_decimal_page import HexToDecimalPage
from frontend.pages.octal_to_decimal_page import OctalToDecimalPage
from frontend.pages.symbol_to_decimal_page import SymbolToDecimalPage
from frontend.pages.decimal_to_text_page import DecimalToTextPage
from frontend.pages.hex_to_text_page import HexToTextPage
from frontend.pages.octal_to_text_page import OctalToTextPage
from frontend.pages.binary_to_text_page import BinaryToTextPage
from frontend.pages.text_to_hex_page import TextToHexPage
from frontend.pages.text_to_octal_page import TextToOctalPage
from frontend.pages.text_to_binary_page import TextToBinaryPage
from frontend.pages.base64_to_plaintext_page import Base64ToPlaintextPage
from frontend.pages.plaintext_to_base64_page import PlaintextToBase64Page
from frontend.pages.base32_to_plaintext_page import Base32ToPlaintextPage
from frontend.pages.plaintext_to_base32_page import PlaintextToBase32Page
from frontend.pages.base128_to_plaintext_page import Base128ToPlaintextPage
from frontend.pages.plaintext_to_base128_page import PlaintextToBase128Page
from frontend.pages.rsa_encrypt_page import RSAEncryptPage
from frontend.pages.rsa_decrypt_page import RSADecryptPage


class CryptInfoBDApp(QMainWindow):
    """
    Main application window for CryptInfoBD.
    Manages the dropdown navigation and page routing.
    """

    def __init__(self):
        """Initialize the main application window."""
        super().__init__()

        # Set window properties
        self.setWindowTitle("CryptInfoBD - Number System Converter")
        self.setMinimumSize(500, 500)
        self.resize(800, 650)

        # Get screen size and center window
        from PyQt6.QtGui import QGuiApplication
        screen = QGuiApplication.primaryScreen().availableGeometry()
        # Allow window to be resized up to 90% of screen size
        self.setMaximumSize(int(screen.width() * 0.9), int(screen.height() * 0.9))

        # Create stacked widget to switch between login and main app
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create login page
        self.login_page = LoginPage()
        self.login_page.login_successful.connect(self._on_login_success)
        self.stacked_widget.addWidget(self.login_page)

        # Create main app widget
        self.main_app_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 20)
        main_layout.setSpacing(2)

        # Application header
        header = QLabel("CryptInfoBD")
        header.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #ffffff;
                padding: 10px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:0.5 #2c3e50, stop:1 #8e44ad);
                letter-spacing: 2px;
            }
        """)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Subtitle
        subtitle = QLabel("Crypto Conversion Tool")
        subtitle.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #34495e;
                padding: 3px 20px;
                font-weight: 600;
            }
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Dropdown label
        dropdown_label = QLabel("Select Conversion:")
        dropdown_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #34495e;
                padding: 3px 20px 0px 20px;
            }
        """)
        dropdown_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create container for three dropdowns (horizontal)
        from PyQt6.QtWidgets import QHBoxLayout
        dropdown_container = QWidget()
        dropdown_layout = QHBoxLayout()
        dropdown_layout.addStretch()

        # Number conversion dropdown
        self.dropdown = ConversionDropdown()
        dropdown_layout.addWidget(self.dropdown)

        dropdown_layout.addSpacing(20)

        # Base encoding dropdown
        self.base_dropdown = BaseConversionDropdown()
        dropdown_layout.addWidget(self.base_dropdown)

        dropdown_layout.addSpacing(20)

        # RSA conversion dropdown
        self.rsa_dropdown = RSAConversionDropdown()
        dropdown_layout.addWidget(self.rsa_dropdown)

        dropdown_layout.addStretch()
        dropdown_layout.setContentsMargins(20, 0, 20, 0)
        dropdown_container.setLayout(dropdown_layout)

        # Create router (stacked widget for pages)
        self.router = Router()

        # Initialize and register all pages
        self._setup_pages()

        # Add widgets to main layout
        main_layout.addWidget(header)
        main_layout.addWidget(subtitle)
        main_layout.addWidget(dropdown_label)
        main_layout.addWidget(dropdown_container)
        main_layout.addWidget(self.router)

        self.main_app_widget.setLayout(main_layout)
        self.stacked_widget.addWidget(self.main_app_widget)

        # Show login page first
        self.stacked_widget.setCurrentWidget(self.login_page)

        # Connect dropdown signals to router navigation with handlers
        self.dropdown.conversion_changed.connect(self._on_number_conversion_changed)
        self.base_dropdown.conversion_changed.connect(self._on_base_conversion_changed)
        self.rsa_dropdown.conversion_changed.connect(self._on_rsa_conversion_changed)

        # Navigate to first page by default
        first_conversion = self.dropdown.get_current_conversion_type()
        self.router.navigate_to(first_conversion)

        # Set application style
        self._set_app_style()

    def _on_number_conversion_changed(self, conversion_type):
        """Handle number conversion dropdown change."""
        # Block signals temporarily to avoid triggering other dropdowns
        self.base_dropdown.blockSignals(True)
        self.base_dropdown.setCurrentIndex(0)
        self.base_dropdown.blockSignals(False)
        self.rsa_dropdown.blockSignals(True)
        self.rsa_dropdown.setCurrentIndex(0)
        self.rsa_dropdown.blockSignals(False)
        self.router.navigate_to(conversion_type)

    def _on_base_conversion_changed(self, conversion_type):
        """Handle base conversion dropdown change."""
        # Block signals temporarily to avoid triggering other dropdowns
        self.dropdown.blockSignals(True)
        self.dropdown.setCurrentIndex(0)
        self.dropdown.blockSignals(False)
        self.rsa_dropdown.blockSignals(True)
        self.rsa_dropdown.setCurrentIndex(0)
        self.rsa_dropdown.blockSignals(False)
        self.router.navigate_to(conversion_type)

    def _on_rsa_conversion_changed(self, conversion_type):
        """Handle RSA conversion dropdown change."""
        # Block signals temporarily to avoid triggering other dropdowns
        self.dropdown.blockSignals(True)
        self.dropdown.setCurrentIndex(0)
        self.dropdown.blockSignals(False)
        self.base_dropdown.blockSignals(True)
        self.base_dropdown.setCurrentIndex(0)
        self.base_dropdown.blockSignals(False)
        self.router.navigate_to(conversion_type)

    def _on_login_success(self):
        """Handle successful login - switch to main app."""
        self.stacked_widget.setCurrentWidget(self.main_app_widget)

    def _on_logout(self):
        """Handle logout - switch back to login page."""
        self.login_page.reset_form()
        self.stacked_widget.setCurrentWidget(self.login_page)

    def _setup_pages(self):
        """Initialize and register all conversion pages with the router."""
        # Create page instances
        decimal_to_binary_page = DecimalToBinaryPage()
        decimal_to_hex_page = DecimalToHexPage()
        decimal_to_octal_page = DecimalToOctalPage()
        binary_to_decimal_page = BinaryToDecimalPage()
        hex_to_decimal_page = HexToDecimalPage()
        octal_to_decimal_page = OctalToDecimalPage()
        symbol_to_decimal_page = SymbolToDecimalPage()
        decimal_to_text_page = DecimalToTextPage()
        hex_to_text_page = HexToTextPage()
        octal_to_text_page = OctalToTextPage()
        binary_to_text_page = BinaryToTextPage()
        text_to_hex_page = TextToHexPage()
        text_to_octal_page = TextToOctalPage()
        text_to_binary_page = TextToBinaryPage()
        base64_to_plaintext_page = Base64ToPlaintextPage()
        plaintext_to_base64_page = PlaintextToBase64Page()
        base32_to_plaintext_page = Base32ToPlaintextPage()
        plaintext_to_base32_page = PlaintextToBase32Page()
        base128_to_plaintext_page = Base128ToPlaintextPage()
        plaintext_to_base128_page = PlaintextToBase128Page()
        rsa_encrypt_page = RSAEncryptPage()
        rsa_decrypt_page = RSADecryptPage()

        # Connect logout signals from all pages
        decimal_to_binary_page.logout_requested.connect(self._on_logout)
        decimal_to_hex_page.logout_requested.connect(self._on_logout)
        decimal_to_octal_page.logout_requested.connect(self._on_logout)
        binary_to_decimal_page.logout_requested.connect(self._on_logout)
        hex_to_decimal_page.logout_requested.connect(self._on_logout)
        octal_to_decimal_page.logout_requested.connect(self._on_logout)
        symbol_to_decimal_page.logout_requested.connect(self._on_logout)
        decimal_to_text_page.logout_requested.connect(self._on_logout)
        hex_to_text_page.logout_requested.connect(self._on_logout)
        octal_to_text_page.logout_requested.connect(self._on_logout)
        binary_to_text_page.logout_requested.connect(self._on_logout)
        text_to_hex_page.logout_requested.connect(self._on_logout)
        text_to_octal_page.logout_requested.connect(self._on_logout)
        text_to_binary_page.logout_requested.connect(self._on_logout)
        base64_to_plaintext_page.logout_requested.connect(self._on_logout)
        plaintext_to_base64_page.logout_requested.connect(self._on_logout)
        base32_to_plaintext_page.logout_requested.connect(self._on_logout)
        plaintext_to_base32_page.logout_requested.connect(self._on_logout)
        base128_to_plaintext_page.logout_requested.connect(self._on_logout)
        plaintext_to_base128_page.logout_requested.connect(self._on_logout)
        rsa_encrypt_page.logout_requested.connect(self._on_logout)
        rsa_decrypt_page.logout_requested.connect(self._on_logout)

        # Register pages with router
        self.router.register_page("decimal_to_binary", decimal_to_binary_page)
        self.router.register_page("decimal_to_hexadecimal", decimal_to_hex_page)
        self.router.register_page("decimal_to_octal", decimal_to_octal_page)
        self.router.register_page("binary_to_decimal", binary_to_decimal_page)
        self.router.register_page("hexadecimal_to_decimal", hex_to_decimal_page)
        self.router.register_page("octal_to_decimal", octal_to_decimal_page)
        self.router.register_page("symbol_to_decimal", symbol_to_decimal_page)
        self.router.register_page("decimal_to_text", decimal_to_text_page)
        self.router.register_page("hexadecimal_to_text", hex_to_text_page)
        self.router.register_page("octal_to_text", octal_to_text_page)
        self.router.register_page("binary_to_text", binary_to_text_page)
        self.router.register_page("text_to_hexadecimal", text_to_hex_page)
        self.router.register_page("text_to_octal", text_to_octal_page)
        self.router.register_page("text_to_binary", text_to_binary_page)
        self.router.register_page("base64_to_plaintext", base64_to_plaintext_page)
        self.router.register_page("plaintext_to_base64", plaintext_to_base64_page)
        self.router.register_page("base32_to_plaintext", base32_to_plaintext_page)
        self.router.register_page("plaintext_to_base32", plaintext_to_base32_page)
        self.router.register_page("base128_to_plaintext", base128_to_plaintext_page)
        self.router.register_page("plaintext_to_base128", plaintext_to_base128_page)
        self.router.register_page("rsa_encrypt", rsa_encrypt_page)
        self.router.register_page("rsa_decrypt", rsa_decrypt_page)

    def _set_app_style(self):
        """Set global application styling."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #2c3e50;
            }
        """)


def main():
    """
    Main entry point for the CryptInfoBD application.
    Creates and runs the Qt application.
    """
    # Create Qt application
    app = QApplication(sys.argv)

    # Set application metadata
    app.setApplicationName("CryptInfoBD")
    app.setOrganizationName("CryptInfoBD")
    app.setApplicationVersion("1.0.0")

    # Create and show main window
    window = CryptInfoBDApp()
    window.show()

    # Run application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
