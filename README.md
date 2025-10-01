# 📊 Data Visualization Dashboard

A beautiful, interactive data visualization web application built with Streamlit, featuring multiple chart types and dynamically generated dummy data.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28.1-FF4B4B.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://github.com/yourusername/data-stuff/workflows/CI%2FCD%20Pipeline/badge.svg)

## ✨ Features

- **📈 Multiple Visualization Types**

  - Time Series Analysis with trend and seasonality
  - Interactive Scatter Plots with grouping
  - Statistical Distributions (Normal, Exponential)
  - Categorical Data (Bar Charts, Pie Charts)
  - Correlation Heatmaps
  - Sine Wave Patterns & 3D Surfaces

- **🎨 Interactive Controls**

  - Dynamic parameter adjustment
  - Real-time data regeneration
  - Zoom, pan, and hover interactions
  - Multiple visualization styles

- **📊 Data Generation**

  - Sine waves with customizable frequency, amplitude, and phase
  - Time series with trend, seasonality, and noise
  - Correlated scatter data
  - Various probability distributions
  - Correlation matrices

- **🧪 Comprehensive Testing**
  - 40+ unit tests
  - Test coverage for all data generation functions
  - CI/CD pipeline with GitHub Actions
  - Automated testing on Python 3.9, 3.10, and 3.11

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/data-stuff.git
cd data-stuff
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 🧪 Running Tests

Run the test suite with coverage:

```bash
pytest test_app.py -v --cov=app --cov-report=term-missing
```

Run tests with detailed output:

```bash
python -m pytest test_app.py -v
```

## 📦 Project Structure

```
data-stuff/
│
├── app.py                      # Main Streamlit application
├── test_app.py                 # Comprehensive test suite
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
├── .streamlit/
│   └── config.toml            # Streamlit configuration
│
└── .github/
    └── workflows/
        └── ci.yml             # GitHub Actions CI/CD pipeline
```

## 🎯 Visualization Pages

### 1. Overview

Dashboard homepage with key metrics and sample visualizations.

### 2. Time Series Analysis

- Interactive time series plots
- Category-based filtering
- Statistical metrics (mean, std, min, max)
- Raw data table view

### 3. Scatter Plot Analysis

- Customizable number of points
- Group-based coloring
- Size-based bubble charts
- Correlation calculations

### 4. Distribution Analysis

- Histogram comparisons
- Box plots
- Violin plots
- Normal and Exponential distributions

### 5. Categorical Data

- Bar charts
- Pie charts
- Grouped bar charts
- Interactive data tables

### 6. Correlation Analysis

- Interactive heatmaps
- Customizable matrix size
- Seaborn alternative visualization
- Full correlation matrix display

### 7. Wave Patterns

- Sine wave generator with controls
- Multiple wave comparisons
- 3D surface plots
- Frequency, amplitude, and phase adjustments

## 🌐 Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Ensure all files are committed to your GitHub repository
2. Make sure `requirements.txt` is up to date
3. Verify the app runs locally without errors

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `yourusername/data-stuff`
5. Set the main file path: `app.py`
6. Click "Deploy!"

Your app will be live at: `https://yourusername-data-stuff.streamlit.app`

### Step 3: Configuration (Optional)

Create a `.streamlit/config.toml` file for custom settings:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
```

### Deployment Tips

- **Free Tier Limits**: Streamlit Cloud free tier includes:
  - 1 GB of RAM
  - 1 CPU
  - Unlimited public apps
- **Environment Variables**: Add secrets in Streamlit Cloud dashboard under "App settings" → "Secrets"

- **Custom Domain**: Configure custom domains in the Streamlit Cloud settings

- **Automatic Updates**: Push to GitHub to automatically redeploy

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web framework for data apps
- **[Plotly](https://plotly.com/)** - Interactive visualization library
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **[NumPy](https://numpy.org/)** - Numerical computing
- **[Matplotlib](https://matplotlib.org/)** - Static plotting
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical visualization
- **[Pytest](https://pytest.org/)** - Testing framework

## 🔄 CI/CD Pipeline

The project includes a comprehensive GitHub Actions workflow that:

- **Tests**: Runs on Python 3.9, 3.10, and 3.11
- **Code Quality**: Linting with flake8, black, and isort
- **Security**: Safety and Bandit security scans
- **Coverage**: Uploads coverage reports to Codecov
- **Build**: Verifies app can be imported and creates deployment artifacts

## 📝 Adding New Visualizations

To add a new visualization page:

1. Create a data generation function:

```python
def generate_your_data():
    # Your data generation logic
    return df
```

2. Create a display function:

```python
def show_your_visualization():
    st.header("Your Visualization")
    data = generate_your_data()
    fig = px.your_chart(data, ...)
    st.plotly_chart(fig, use_container_width=True)
```

3. Add to navigation in `main()`:

```python
page = st.sidebar.radio(
    "Select Visualization Type",
    [..., "Your Visualization"]
)
```

4. Add routing logic:

```python
elif page == "Your Visualization":
    show_your_visualization()
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🧪 Testing Guidelines

When contributing, ensure:

- All tests pass: `pytest test_app.py -v`
- Code coverage remains high: `pytest --cov=app`
- New features include corresponding tests
- Code follows PEP 8 style guidelines

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📧 Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/data-stuff](https://github.com/yourusername/data-stuff)

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Plotly for interactive visualizations
- The open-source community

---

Made with ❤️ and Python

