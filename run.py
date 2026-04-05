"""
CryptInfoBD - Desktop Application Launcher
Run this script to start the application.
"""

import sys
import os

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Now import and run the app
from frontend.app import main

if __name__ == "__main__":
    main()
