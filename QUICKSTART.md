# 🚀 Quick Start Guide

Get your Data Visualization Dashboard up and running in minutes!

## Prerequisites

- Python 3.9 or higher
- pip package manager
- Git (for deployment)

## Option 1: Automated Setup (Recommended)

### macOS/Linux

```bash
./setup.sh
```

This script will:

- Create a virtual environment
- Install all dependencies
- Run tests to verify everything works

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest test_app.py -v
```

## Option 2: Manual Setup

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/data-stuff.git
cd data-stuff
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Running the App

### Quick Launch (after setup)

```bash
./run.sh  # macOS/Linux
```

Or manually:

```bash
source venv/bin/activate  # Activate virtual environment
streamlit run app.py
```

## Testing

### Run All Tests

```bash
pytest test_app.py -v
```

### Run Tests with Coverage

```bash
pytest test_app.py --cov=app --cov-report=term-missing
```

### Run Specific Test Class

```bash
pytest test_app.py::TestDataGeneration -v
```

## Project Structure

```
data-stuff/
│
├── app.py                   # Main Streamlit application
├── test_app.py              # Test suite (32 tests)
├── requirements.txt         # Python dependencies
│
├── setup.sh                 # Automated setup script
├── run.sh                   # Quick launch script
│
├── README.md                # Full documentation
├── QUICKSTART.md            # This file
├── CONTRIBUTING.md          # Contribution guidelines
├── LICENSE                  # MIT License
│
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD
│
├── .streamlit/
│   └── config.toml         # Streamlit configuration
│
└── .gitignore              # Git ignore rules
```

## Features Overview

### 📊 Visualizations Available

1. **Overview Dashboard** - Metrics and quick previews
2. **Time Series Analysis** - Trend and seasonality plots
3. **Scatter Plot Analysis** - Correlated data with groups
4. **Distribution Analysis** - Histograms, box plots, violin plots
5. **Categorical Data** - Bar charts, pie charts
6. **Correlation Analysis** - Heatmaps and correlation matrices
7. **Wave Patterns** - Sine waves and 3D surfaces

### 🎨 Customization Options

- Adjust number of data points
- Change frequencies, amplitudes, phases
- Toggle grouping and categories
- Interactive zoom and pan
- Hover for detailed information

## Common Issues

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

### Module Not Found Error

Make sure your virtual environment is activated:

```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### Tests Failing

Reinstall dependencies:

```bash
pip install -r requirements.txt --force-reinstall
```

## Deployment to Streamlit Cloud

### Quick Deployment Steps

1. **Push to GitHub**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/data-stuff.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**

   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `yourusername/data-stuff`
   - Main file path: `app.py`
   - Click "Deploy!"

3. **Access Your App**
   - Your app will be live at: `https://yourusername-data-stuff.streamlit.app`
   - Share the URL with anyone!

### Deployment Notes

- **Free tier includes**: 1GB RAM, 1 CPU, unlimited public apps
- **Automatic updates**: Push to GitHub to redeploy
- **Custom domains**: Available in Streamlit Cloud settings
- **Environment variables**: Configure in App Settings → Secrets

## Next Steps

1. **Explore the App**: Try all visualization types
2. **Customize**: Modify data generation functions in `app.py`
3. **Add Features**: See `CONTRIBUTING.md` for guidelines
4. **Deploy**: Share your app with the world!

## Quick Commands Reference

```bash
# Setup and run
./setup.sh              # Initial setup
./run.sh                # Launch app

# Development
streamlit run app.py    # Run app manually
pytest test_app.py -v   # Run tests

# Git
git status              # Check changes
git add .               # Stage changes
git commit -m "msg"     # Commit changes
git push                # Push to GitHub
```

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/data-stuff/issues)
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Python Help**: [python.org](https://www.python.org)

## Tips for Success

✅ **Start Simple**: Explore existing visualizations before customizing
✅ **Test Often**: Run `pytest` after making changes
✅ **Read Docs**: Check the full README.md for detailed information
✅ **Stay Updated**: Pull latest changes regularly if collaborating

---

**Ready to visualize data? Run `./run.sh` and let's go! 🚀**
