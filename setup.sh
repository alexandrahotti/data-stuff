#!/bin/bash

# Setup script for Data Visualization Dashboard

echo "🚀 Setting up Data Visualization Dashboard..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip -q

echo ""

# Install requirements
echo "📦 Installing dependencies..."
pip install -r requirements.txt -q

echo ""

# Run tests
echo "🧪 Running tests..."
pytest test_app.py -v --cov=app

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the app:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the app: streamlit run app.py"
echo ""
echo "To run tests:"
echo "  pytest test_app.py -v"
echo ""
echo "Happy visualizing! 📊"

