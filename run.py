#!/usr/bin/env python3

"""
COT Positions Analyzer
Quick start script
"""

import subprocess
import sys
import os

def main():
    """Run the COT analyzer application"""
    
    # Check if streamlit is installed
    try:
        import streamlit
    except ImportError:
        print("Streamlit not found. Please run setup.py first:")
        print("  python setup.py")
        sys.exit(1)
    
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("Error: app.py not found in current directory")
        sys.exit(1)
    
    print("Starting COT Positions Analyzer...")
    print("The app will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the application")
    
    # Run streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()