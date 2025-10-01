import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stPlotlyChart {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 10px;
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 20px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


def generate_sine_data(frequency=1, amplitude=1, phase=0, points=1000):
    """Generate sine wave data"""
    x = np.linspace(0, 4 * np.pi, points)
    y = amplitude * np.sin(frequency * x + phase)
    return pd.DataFrame({'x': x, 'y': y})


def generate_timeseries_data(days=365):
    """Generate time series data with trend and seasonality"""
    dates = pd.date_range(start=datetime.now() - timedelta(days=days), 
                          end=datetime.now(), freq='D')
    
    trend = np.linspace(100, 200, len(dates))
    seasonal = 20 * np.sin(np.linspace(0, 4 * np.pi, len(dates)))
    noise = np.random.normal(0, 10, len(dates))
    values = trend + seasonal + noise
    
    return pd.DataFrame({
        'date': dates,
        'value': values,
        'category': np.random.choice(['A', 'B', 'C'], len(dates))
    })


def generate_scatter_data(n_points=500):
    """Generate correlated scatter data"""
    x = np.random.randn(n_points)
    y = 2 * x + np.random.randn(n_points) * 0.5
    colors = np.random.choice(['Group 1', 'Group 2', 'Group 3'], n_points)
    sizes = np.random.randint(10, 100, n_points)
    
    return pd.DataFrame({
        'x': x,
        'y': y,
        'group': colors,
        'size': sizes
    })


def generate_categorical_data():
    """Generate categorical data for bar charts"""
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    values = np.random.randint(50, 200, len(categories))
    
    return pd.DataFrame({
        'category': categories,
        'value': values,
        'subcategory': np.random.choice(['Type 1', 'Type 2'], len(categories))
    })


def generate_distribution_data(n_samples=1000):
    """Generate data for distribution plots"""
    normal_data = np.random.normal(100, 15, n_samples)
    exponential_data = np.random.exponential(50, n_samples)
    
    return pd.DataFrame({
        'normal': normal_data,
        'exponential': exponential_data
    })


def generate_heatmap_data(size=10):
    """Generate correlation matrix data"""
    data = np.random.randn(100, size)
    df = pd.DataFrame(data, columns=[f'Var_{i+1}' for i in range(size)])
    return df.corr()


# Main App
def main():
    st.title("📊 Data Visualization Dashboard")
    st.markdown("### Interactive visualizations with dummy data")
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select Visualization Type",
        ["Overview", "Time Series", "Scatter Plots", "Distributions", 
         "Categorical Data", "Correlation Analysis", "Wave Patterns"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "This dashboard demonstrates various data visualization techniques "
        "using Plotly, Matplotlib, and Seaborn with dynamically generated dummy data."
    )
    
    # Page routing
    if page == "Overview":
        show_overview()
    elif page == "Time Series":
        show_timeseries()
    elif page == "Scatter Plots":
        show_scatter()
    elif page == "Distributions":
        show_distributions()
    elif page == "Categorical Data":
        show_categorical()
    elif page == "Correlation Analysis":
        show_correlation()
    elif page == "Wave Patterns":
        show_wave_patterns()


def show_overview():
    st.header("Dashboard Overview")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Total Data Points", value="10,000+", delta="1,234")
    with col2:
        st.metric(label="Visualizations", value="15+", delta="3")
    with col3:
        st.metric(label="Chart Types", value="7", delta="2")
    with col4:
        st.metric(label="Interactivity", value="100%", delta="20%")
    
    st.markdown("---")
    
    # Quick overview with sample charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sample Time Series")
        ts_data = generate_timeseries_data(days=90)
        fig = px.line(ts_data, x='date', y='value', 
                      title='Time Series Preview',
                      template='plotly_white')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sample Distribution")
        dist_data = generate_distribution_data(500)
        fig = px.histogram(dist_data, x='normal', 
                          title='Distribution Preview',
                          template='plotly_white')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📈 Interactive Charts")
        st.write("Zoom, pan, and hover over data points for detailed information")
    
    with col2:
        st.markdown("#### 🎨 Multiple Styles")
        st.write("Various chart types including line, scatter, bar, and heatmaps")
    
    with col3:
        st.markdown("#### 🔄 Dynamic Data")
        st.write("Regenerate data on the fly with customizable parameters")


def show_timeseries():
    st.header("Time Series Analysis")
    
    # Controls
    col1, col2 = st.columns(2)
    with col1:
        days = st.slider("Number of days", 30, 730, 365)
    with col2:
        show_category = st.checkbox("Show by category", value=False)
    
    # Generate and plot data
    data = generate_timeseries_data(days=days)
    
    if show_category:
        fig = px.line(data, x='date', y='value', color='category',
                     title='Time Series by Category',
                     template='plotly_white')
    else:
        fig = px.line(data, x='date', y='value',
                     title='Time Series Data',
                     template='plotly_white')
    
    fig.update_layout(height=500, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistics
    st.subheader("Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mean", f"{data['value'].mean():.2f}")
    with col2:
        st.metric("Std Dev", f"{data['value'].std():.2f}")
    with col3:
        st.metric("Min", f"{data['value'].min():.2f}")
    with col4:
        st.metric("Max", f"{data['value'].max():.2f}")
    
    # Show data table
    if st.checkbox("Show raw data"):
        st.dataframe(data.head(100), use_container_width=True)


def show_scatter():
    st.header("Scatter Plot Analysis")
    
    # Controls
    col1, col2 = st.columns(2)
    with col1:
        n_points = st.slider("Number of points", 100, 2000, 500)
    with col2:
        color_by_group = st.checkbox("Color by group", value=True)
    
    # Generate and plot data
    data = generate_scatter_data(n_points=n_points)
    
    if color_by_group:
        fig = px.scatter(data, x='x', y='y', color='group', size='size',
                        title='Scatter Plot with Groups',
                        template='plotly_white',
                        hover_data=['size'])
    else:
        fig = px.scatter(data, x='x', y='y', size='size',
                        title='Scatter Plot',
                        template='plotly_white',
                        hover_data=['size'])
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation
    correlation = data['x'].corr(data['y'])
    st.metric("Correlation (X vs Y)", f"{correlation:.3f}")


def show_distributions():
    st.header("Distribution Analysis")
    
    # Controls
    n_samples = st.slider("Number of samples", 500, 5000, 1000)
    
    # Generate data
    data = generate_distribution_data(n_samples=n_samples)
    
    # Create tabs for different distribution views
    tab1, tab2, tab3 = st.tabs(["Histograms", "Box Plots", "Violin Plots"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(data, x='normal', 
                             title='Normal Distribution',
                             template='plotly_white',
                             nbins=50)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.histogram(data, x='exponential', 
                             title='Exponential Distribution',
                             template='plotly_white',
                             nbins=50)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = go.Figure()
        fig.add_trace(go.Box(y=data['normal'], name='Normal'))
        fig.add_trace(go.Box(y=data['exponential'], name='Exponential'))
        fig.update_layout(title='Box Plots Comparison', 
                         template='plotly_white',
                         height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        fig = go.Figure()
        fig.add_trace(go.Violin(y=data['normal'], name='Normal', box_visible=True))
        fig.add_trace(go.Violin(y=data['exponential'], name='Exponential', box_visible=True))
        fig.update_layout(title='Violin Plots Comparison', 
                         template='plotly_white',
                         height=500)
        st.plotly_chart(fig, use_container_width=True)


def show_categorical():
    st.header("Categorical Data Analysis")
    
    # Generate data
    data = generate_categorical_data()
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Bar Chart", "Pie Chart", "Grouped Bar"])
    
    with tab1:
        fig = px.bar(data, x='category', y='value',
                    title='Bar Chart',
                    template='plotly_white',
                    color='value',
                    color_continuous_scale='Blues')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.pie(data, values='value', names='category',
                    title='Pie Chart',
                    template='plotly_white')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        fig = px.bar(data, x='category', y='value', color='subcategory',
                    title='Grouped Bar Chart',
                    template='plotly_white',
                    barmode='group')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Show data
    st.subheader("Data Table")
    st.dataframe(data, use_container_width=True)


def show_correlation():
    st.header("Correlation Analysis")
    
    # Controls
    matrix_size = st.slider("Number of variables", 5, 15, 10)
    
    # Generate data
    corr_data = generate_heatmap_data(size=matrix_size)
    
    # Create heatmap
    fig = px.imshow(corr_data,
                   title='Correlation Heatmap',
                   template='plotly_white',
                   color_continuous_scale='RdBu',
                   aspect='auto',
                   zmin=-1, zmax=1)
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Alternative visualization with seaborn
    st.subheader("Alternative Visualization (Seaborn)")
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_data, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, ax=ax)
    plt.title('Correlation Matrix with Annotations')
    st.pyplot(fig)


def show_wave_patterns():
    st.header("Wave Patterns & Sine Waves")
    
    # Controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        frequency = st.slider("Frequency", 0.5, 5.0, 1.0, 0.1)
    with col2:
        amplitude = st.slider("Amplitude", 0.5, 3.0, 1.0, 0.1)
    with col3:
        phase = st.slider("Phase", 0.0, 2*np.pi, 0.0, 0.1)
    
    # Generate wave data
    wave_data = generate_sine_data(frequency=frequency, 
                                   amplitude=amplitude, 
                                   phase=phase)
    
    # Plot single wave
    fig = px.line(wave_data, x='x', y='y',
                 title=f'Sine Wave (f={frequency}, A={amplitude}, φ={phase:.2f})',
                 template='plotly_white')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Multiple waves comparison
    st.subheader("Multiple Waves Comparison")
    
    waves = []
    for i, (f, a) in enumerate([(1, 1), (2, 0.5), (3, 0.3)]):
        wave = generate_sine_data(frequency=f, amplitude=a, points=1000)
        wave['wave'] = f'Wave {i+1} (f={f}, A={a})'
        waves.append(wave)
    
    combined_waves = pd.concat(waves)
    
    fig = px.line(combined_waves, x='x', y='y', color='wave',
                 title='Multiple Sine Waves',
                 template='plotly_white')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # 3D surface plot
    st.subheader("3D Wave Surface")
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
    fig.update_layout(title='3D Sine Wave Surface',
                     scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                     height=600)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()

