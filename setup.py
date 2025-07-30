#!/usr/bin/env python3

"""
COT Positions Analyzer
Setup script for easy installation
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing COT Analyzer dependencies...")
    
    requirements = [
        "streamlit>=1.47.1",
        "pandas>=2.3.1", 
        "plotly>=6.2.0",
        "requests>=2.32.4",
        "numpy>=2.3.2",
        "cot-reports>=0.1.3"
    ]
    
    for requirement in requirements:
        print(f"Installing {requirement}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
    
    print("\n✅ All dependencies installed successfully!")
    print("\nTo run the COT Analyzer:")
    print("  streamlit run app.py")
    print("\nThe app will open in your browser at http://localhost:8501")

if __name__ == "__main__":
    install_requirements()