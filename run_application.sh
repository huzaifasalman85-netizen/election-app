#!/bin/bash

echo "============================================================"
echo "PREFECT BODY ELECTIONS - DESKTOP APPLICATION"
echo "The Educators Professional's Campus"
echo "============================================================"
echo ""
echo "Starting the voting system..."
echo ""
echo "If this is your first time running the application,"
echo "please ensure you have installed Python and the required packages."
echo "See INSTALL.md for detailed instructions."
echo ""
read -p "Press Enter to continue..."
echo ""
echo "Starting application..."

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 desktop_app_simple.py
elif command -v python &> /dev/null; then
    python desktop_app_simple.py
else
    echo "Error: Python not found. Please install Python 3.11 or higher."
    echo "Visit https://python.org to download Python."
    read -p "Press Enter to exit..."
    exit 1
fi

