#!/bin/bash

# Quick start script for Data Visualization Dashboard

echo "📊 Starting Data Visualization Dashboard..."
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
fi

# Check if dependencies are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt -q
    echo "✅ Dependencies installed"
    echo ""
fi

# Run the app
echo "🚀 Launching Streamlit app..."
echo ""
streamlit run app.py

