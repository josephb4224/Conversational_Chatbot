#!/usr/bin/env python3
# A launcher script for running streamlit_app.py
# Then turning this script into an EXE using PythonToExe:

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(BASE_DIR, "streaming_app.py")

env = os.environ.copy()
# Ensure local imports from the project root work when launching
env["PYTHONPATH"] = BASE_DIR
cmd = [sys.executable, "-m", "streamlit", "run", app_path]
subprocess.run(cmd, env=env)


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