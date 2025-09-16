#!/bin/bash

# PWD Tools - Installation and Launcher Script
# For macOS and Linux users

echo "========================================"
echo "   PWD Tools - Raksha Bandhan"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    echo "Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ Python and pip are available"
echo ""

# Navigate to the application directory
cd "$(dirname "$0")/Excel_se_EMD"

echo "Installing required packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Packages installed successfully"
else
    echo "❌ Failed to install packages. Please check the error above."
    exit 1
fi

echo ""
echo "Choose your application:"
echo "1. Streamlit App (Recommended - Modern Interface)"
echo "2. Flask App (Traditional Web Interface)"
echo "3. Exit"
echo ""

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "Starting Streamlit App..."
        echo "The app will open in your default web browser"
        echo "To stop the app, press Ctrl+C in this terminal"
        echo ""
        streamlit run streamlit_app.py
        ;;
    2)
        echo "Starting Flask App..."
        echo "The app will be available at: http://localhost:5000"
        echo "To stop the app, press Ctrl+C in this terminal"
        echo ""
        python3 app.py
        ;;
    3)
        echo "Thank you for using PWD Tools!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac
