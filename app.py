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

# Custom CSS for enhanced styling with animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding: 0rem 1rem;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stPlotlyChart {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .stPlotlyChart:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        padding-bottom: 20px;
        font-weight: 700;
        animation: slideInDown 0.6s ease-out;
    }
    
    @keyframes slideInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 0 0 10px rgba(102, 126, 234, 0); }
    }
    
    /* Data table styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        background-color: #f5f7fa;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
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


def generate_realtime_data(n_points=50):
    """Generate data for animated/realtime visualization"""
    timestamps = pd.date_range(start=datetime.now() - timedelta(minutes=n_points-1), 
                               periods=n_points, freq='1min')
    
    values = np.cumsum(np.random.randn(n_points)) + 100
    categories = np.random.choice(['Sensor A', 'Sensor B', 'Sensor C'], n_points)
    
    return pd.DataFrame({
        'timestamp': timestamps,
        'value': values,
        'category': categories,
        'status': np.random.choice(['Normal', 'Warning', 'Critical'], n_points, p=[0.7, 0.2, 0.1])
    })


def export_data_to_csv(df, filename="data_export"):
    """Convert dataframe to CSV for download"""
    return df.to_csv(index=False).encode('utf-8')


def export_data_to_json(df, filename="data_export"):
    """Convert dataframe to JSON for download"""
    return df.to_json(orient='records', date_format='iso').encode('utf-8')


# Main App
def main():
    st.title("📊 Data Visualization Dashboard")
    st.markdown("### Interactive visualizations with dummy data")
    
    # Sidebar
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.radio(
        "Select Visualization Type",
        ["Overview", "Time Series", "Scatter Plots", "Distributions", 
         "Categorical Data", "Correlation Analysis", "Wave Patterns", "Animated Charts", "Data Export"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 About")
    st.sidebar.info(
        "This dashboard demonstrates various data visualization techniques "
        "using Plotly, Matplotlib, and Seaborn with dynamically generated dummy data."
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚡ Quick Actions")
    
    # Theme toggle (visual indicator)
    theme = st.sidebar.selectbox("🎨 Color Scheme", ["Default", "Dark Mode", "Light Mode"])
    
    # Data refresh
    if st.sidebar.button("🔄 Refresh All Data"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Statistics")
    st.sidebar.metric("Total Views", "12.5K", "+2.3K")
    st.sidebar.metric("Active Users", "847", "+123")
    
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
    elif page == "Animated Charts":
        show_animated_charts()
    elif page == "Data Export":
        show_data_export()


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


def show_animated_charts():
    st.header("🎬 Animated Charts & Real-Time Data")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>✨ New Feature!</h3>
        <p>Explore animated visualizations and simulated real-time data streams.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Controls
    col1, col2 = st.columns(2)
    
    with col1:
        n_points = st.slider("Number of data points", 20, 100, 50)
        animation_speed = st.slider("Animation speed (ms)", 50, 500, 100)
    
    with col2:
        chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Scatter", "Area"])
        show_status = st.checkbox("Show status indicators", value=True)
    
    # Generate data
    data = generate_realtime_data(n_points=n_points)
    
    # Create animated chart
    st.subheader("Simulated Real-Time Data Stream")
    
    if chart_type == "Line":
        fig = px.line(data, x='timestamp', y='value', color='category',
                     title='Real-Time Sensor Data',
                     template='plotly_white')
    elif chart_type == "Bar":
        fig = px.bar(data, x='timestamp', y='value', color='category',
                    title='Real-Time Sensor Data',
                    template='plotly_white')
    elif chart_type == "Scatter":
        fig = px.scatter(data, x='timestamp', y='value', color='category',
                        size=[10]*len(data),
                        title='Real-Time Sensor Data',
                        template='plotly_white')
    else:  # Area
        fig = px.area(data, x='timestamp', y='value', color='category',
                     title='Real-Time Sensor Data',
                     template='plotly_white')
    
    fig.update_layout(height=500, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)
    
    # Status indicators
    if show_status:
        st.subheader("📊 Status Overview")
        
        col1, col2, col3 = st.columns(3)
        
        status_counts = data['status'].value_counts()
        
        with col1:
            normal_count = status_counts.get('Normal', 0)
            st.metric("🟢 Normal", normal_count, 
                     f"{(normal_count/len(data)*100):.1f}%")
        
        with col2:
            warning_count = status_counts.get('Warning', 0)
            st.metric("🟡 Warning", warning_count, 
                     f"{(warning_count/len(data)*100):.1f}%")
        
        with col3:
            critical_count = status_counts.get('Critical', 0)
            st.metric("🔴 Critical", critical_count, 
                     f"{(critical_count/len(data)*100):.1f}%")
    
    # Animated scatter with frames
    st.subheader("🎯 Time-Based Animation")
    
    # Create frames for animation
    data['frame'] = pd.cut(range(len(data)), bins=10, labels=range(10))
    
    fig = px.scatter(data, x='timestamp', y='value', 
                    color='category', size='value',
                    animation_frame='frame',
                    title='Animated Time Series',
                    template='plotly_white',
                    range_y=[data['value'].min()-10, data['value'].max()+10])
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Live data table
    if st.checkbox("Show live data table"):
        st.dataframe(data[['timestamp', 'value', 'category', 'status']].tail(20), 
                    use_container_width=True)


def show_data_export():
    st.header("📥 Data Export & Download")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>💾 Export Your Data</h3>
        <p>Generate and download data in multiple formats for further analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Data selection
    st.subheader("1️⃣ Select Data Type")
    
    data_type = st.selectbox(
        "Choose the type of data to export",
        ["Time Series", "Sine Wave", "Scatter Data", "Distribution Data", 
         "Categorical Data", "Correlation Matrix", "Real-Time Data"]
    )
    
    # Generate selected data
    st.subheader("2️⃣ Configure Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if data_type == "Time Series":
            days = st.slider("Days of data", 30, 730, 365)
            data = generate_timeseries_data(days=days)
            preview_data = data
            
        elif data_type == "Sine Wave":
            frequency = st.slider("Frequency", 0.5, 5.0, 1.0, 0.1)
            amplitude = st.slider("Amplitude", 0.5, 3.0, 1.0, 0.1)
            points = st.slider("Number of points", 100, 5000, 1000)
            data = generate_sine_data(frequency=frequency, amplitude=amplitude, points=points)
            preview_data = data
            
        elif data_type == "Scatter Data":
            n_points = st.slider("Number of points", 100, 5000, 500)
            data = generate_scatter_data(n_points=n_points)
            preview_data = data
            
        elif data_type == "Distribution Data":
            n_samples = st.slider("Number of samples", 500, 10000, 1000)
            data = generate_distribution_data(n_samples=n_samples)
            preview_data = data
            
        elif data_type == "Categorical Data":
            data = generate_categorical_data()
            preview_data = data
            
        elif data_type == "Correlation Matrix":
            size = st.slider("Matrix size", 5, 20, 10)
            data = generate_heatmap_data(size=size)
            preview_data = data
            
        else:  # Real-Time Data
            n_points = st.slider("Number of points", 20, 200, 50)
            data = generate_realtime_data(n_points=n_points)
            preview_data = data
    
    with col2:
        export_format = st.selectbox(
            "Export format",
            ["CSV", "JSON", "Excel (XLSX)"]
        )
        
        include_index = st.checkbox("Include index", value=False)
        
        st.metric("Data Points", len(data))
        st.metric("Columns", len(data.columns) if hasattr(data, 'columns') else 'N/A')
    
    # Preview
    st.subheader("3️⃣ Preview Data")
    
    with st.expander("📊 View Data Preview", expanded=True):
        st.dataframe(preview_data.head(50), use_container_width=True)
    
    # Statistics
    with st.expander("📈 Data Statistics"):
        if hasattr(preview_data, 'describe'):
            st.dataframe(preview_data.describe(), use_container_width=True)
    
    # Download section
    st.subheader("4️⃣ Download Data")
    
    col1, col2, col3 = st.columns(3)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"{data_type.lower().replace(' ', '_')}_{timestamp}"
    
    with col1:
        if export_format == "CSV":
            csv_data = export_data_to_csv(data)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv_data,
                file_name=f"{filename_base}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    with col2:
        if export_format == "JSON":
            json_data = export_data_to_json(data)
            st.download_button(
                label="⬇️ Download JSON",
                data=json_data,
                file_name=f"{filename_base}.json",
                mime="application/json",
                use_container_width=True
            )
    
    with col3:
        if export_format == "Excel (XLSX)":
            st.info("📝 Excel export requires openpyxl package")
            st.code("pip install openpyxl", language="bash")
    
    # Bulk export option
    st.subheader("5️⃣ Bulk Export (All Data Types)")
    
    if st.button("📦 Generate All Datasets", use_container_width=True):
        with st.spinner("Generating all datasets..."):
            all_datasets = {
                "time_series": generate_timeseries_data(),
                "sine_wave": generate_sine_data(),
                "scatter": generate_scatter_data(),
                "distribution": generate_distribution_data(),
                "categorical": generate_categorical_data(),
            }
            
            st.success("✅ All datasets generated!")
            
            for name, dataset in all_datasets.items():
                csv = export_data_to_csv(dataset)
                st.download_button(
                    label=f"⬇️ Download {name.replace('_', ' ').title()}",
                    data=csv,
                    file_name=f"{name}_{timestamp}.csv",
                    mime="text/csv",
                    key=f"download_{name}"
                )


if __name__ == "__main__":
    main()

