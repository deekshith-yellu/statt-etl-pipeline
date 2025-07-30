#!/bin/bash

# run.sh - Script to check requirements and run the statt_etl_pipeline

set -e  # Exit on any error

echo "🚀 Starting statt_etl_pipeline setup and execution..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo "❌ Error: pip is not available"
    echo "Please install pip and try again"
    exit 1
fi

echo "✅ pip found"

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found"
    echo "Please ensure requirements.txt is in the current directory"
    exit 1
fi

echo "✅ requirements.txt found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade pip in virtual environment
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip

# Install requirements
echo "📦 Installing required packages..."
pip install -r requirements.txt

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found"
    echo "Please ensure main.py is in the current directory"
    exit 1
fi

echo "✅ main.py found"

# Run the main script
echo "🏃 Running main.py..."
python3 main.py

echo "🎉 Script execution completed successfully!"
echo "📄 Check proposed_regulations.json for the output"