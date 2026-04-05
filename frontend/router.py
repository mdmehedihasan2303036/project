"""
Router for managing page navigation in CryptInfoBD.
"""

from PyQt6.QtWidgets import QStackedWidget


class Router(QStackedWidget):
    """
    Router widget that manages page switching based on conversion type.
    Uses QStackedWidget to display one page at a time.
    """

    def __init__(self, parent=None):
        """Initialize the router."""
        super().__init__(parent)

        # Dictionary to map conversion types to page indices
        self.page_map = {}

    def register_page(self, conversion_type: str, page_widget):
        """
        Register a page for a specific conversion type.

        Args:
            conversion_type: Identifier for the conversion (e.g., "decimal_to_binary")
            page_widget: The page widget to display for this conversion
        """
        # Add the page to the stacked widget
        index = self.addWidget(page_widget)

        # Map the conversion type to the page index
        self.page_map[conversion_type] = index

    def navigate_to(self, conversion_type: str):
        """
        Navigate to the page for the specified conversion type.

        Args:
            conversion_type: Identifier for the conversion to navigate to
        """
        if conversion_type in self.page_map:
            page_index = self.page_map[conversion_type]
            self.setCurrentIndex(page_index)
        else:
            print(f"Warning: No page registered for conversion type '{conversion_type}'")

    def get_current_page(self):
        """Get the currently displayed page widget."""
        return self.currentWidget()
