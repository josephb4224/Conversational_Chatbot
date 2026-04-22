#!/usr/bin/env python3
# A launcher script for running streamlit_app.py
# Then turning this script into an EXE using PythonToExe:

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(BASE_DIR, "streaming_app.py")

subprocess.run([
    "python",
    "-m",
    "streamlit",
    "run",
    app_path
])

import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = os.environ.copy()

# Force local execution context
env["PYTHONPATH"] = BASE_DIR

subprocess.run([
    "streamlit",
    "run",
    os.path.join(BASE_DIR, "streamlit_app.py")
], env=env)


# Forcing PyInstaller to include Streamlit:
#pyinstaller --onefile --hidden-import=streamlit streamlit_app.py

# Streamlit has many internal files, so use '--collect-all' to bundle everything
#pyinstaller --onefile --noconsole --collect-all streamlit launcher.py

# Tell PyInstaller to “Include this module even if you don’t detect it”.
# pyinstaller ^
#   --onefile ^
#   --noconsole ^
#   --collect-all streamlit ^
#   --hidden-import=streamlit ^
#   --hidden-import=streamlit.web ^
#   --hidden-import=streamlit.runtime ^
#   streamlit_app.py