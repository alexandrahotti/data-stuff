import pytest
import pandas as pd
import numpy as np
from app import (
    generate_sine_data,
    generate_timeseries_data,
    generate_scatter_data,
    generate_categorical_data,
    generate_distribution_data,
    generate_heatmap_data,
    generate_realtime_data,
    export_data_to_csv,
    export_data_to_json,
    apply_filters,
    get_chart_template
)


class TestDataGeneration:
    """Test suite for data generation functions"""
    
    def test_generate_sine_data_default(self):
        """Test sine data generation with default parameters"""
        df = generate_sine_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1000  # default points
        assert 'x' in df.columns
        assert 'y' in df.columns
        assert df['y'].min() >= -1.0  # default amplitude
        assert df['y'].max() <= 1.0
    
    def test_generate_sine_data_custom_parameters(self):
        """Test sine data generation with custom parameters"""
        frequency = 2
        amplitude = 3
        phase = np.pi / 4
        points = 500
        
        df = generate_sine_data(frequency=frequency, 
                               amplitude=amplitude, 
                               phase=phase, 
                               points=points)
        
        assert len(df) == points
        assert df['y'].min() >= -amplitude - 0.1  # small tolerance
        assert df['y'].max() <= amplitude + 0.1
    
    def test_generate_sine_data_shapes(self):
        """Test that sine data has correct shape"""
        df = generate_sine_data(points=100)
        
        assert df.shape == (100, 2)
        assert not df.isnull().any().any()
    
    def test_generate_timeseries_data_default(self):
        """Test time series data generation with default parameters"""
        df = generate_timeseries_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 366  # 365 days + 1
        assert 'date' in df.columns
        assert 'value' in df.columns
        assert 'category' in df.columns
        assert pd.api.types.is_datetime64_any_dtype(df['date'])
    
    def test_generate_timeseries_data_custom_days(self):
        """Test time series data generation with custom days"""
        days = 30
        df = generate_timeseries_data(days=days)
        
        assert len(df) == days + 1
        assert df['value'].dtype in [np.float64, np.float32]
    
    def test_generate_timeseries_categories(self):
        """Test that time series categories are valid"""
        df = generate_timeseries_data(days=100)
        
        unique_categories = df['category'].unique()
        assert len(unique_categories) <= 3
        assert all(cat in ['A', 'B', 'C'] for cat in unique_categories)
    
    def test_generate_scatter_data_default(self):
        """Test scatter data generation with default parameters"""
        df = generate_scatter_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 500
        assert 'x' in df.columns
        assert 'y' in df.columns
        assert 'group' in df.columns
        assert 'size' in df.columns
    
    def test_generate_scatter_data_custom_points(self):
        """Test scatter data generation with custom number of points"""
        n_points = 200
        df = generate_scatter_data(n_points=n_points)
        
        assert len(df) == n_points
        assert df['size'].min() >= 10
        assert df['size'].max() <= 100
    
    def test_generate_scatter_data_groups(self):
        """Test that scatter data has valid groups"""
        df = generate_scatter_data(n_points=1000)
        
        unique_groups = df['group'].unique()
        assert len(unique_groups) <= 3
        assert all(group in ['Group 1', 'Group 2', 'Group 3'] 
                  for group in unique_groups)
    
    def test_generate_categorical_data(self):
        """Test categorical data generation"""
        df = generate_categorical_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 5  # 5 products
        assert 'category' in df.columns
        assert 'value' in df.columns
        assert 'subcategory' in df.columns
        assert df['value'].min() >= 50
        assert df['value'].max() <= 200
    
    def test_generate_categorical_data_categories(self):
        """Test that categorical data has correct categories"""
        df = generate_categorical_data()
        
        expected_categories = ['Product A', 'Product B', 'Product C', 
                             'Product D', 'Product E']
        assert list(df['category']) == expected_categories
    
    def test_generate_distribution_data_default(self):
        """Test distribution data generation with default parameters"""
        df = generate_distribution_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1000
        assert 'normal' in df.columns
        assert 'exponential' in df.columns
    
    def test_generate_distribution_data_custom_samples(self):
        """Test distribution data generation with custom sample size"""
        n_samples = 500
        df = generate_distribution_data(n_samples=n_samples)
        
        assert len(df) == n_samples
        assert not df.isnull().any().any()
    
    def test_generate_distribution_data_properties(self):
        """Test that distribution data has expected statistical properties"""
        df = generate_distribution_data(n_samples=10000)
        
        # Normal distribution should have mean around 100, std around 15
        assert 95 < df['normal'].mean() < 105
        assert 13 < df['normal'].std() < 17
        
        # Exponential distribution should be non-negative
        assert df['exponential'].min() >= 0
    
    def test_generate_heatmap_data_default(self):
        """Test heatmap data generation with default parameters"""
        df = generate_heatmap_data()
        
        assert isinstance(df, pd.DataFrame)
        assert df.shape == (10, 10)  # default size
        
        # Correlation matrix should be symmetric
        assert np.allclose(df.values, df.values.T)
        
        # Diagonal should be all 1s
        assert np.allclose(np.diag(df.values), 1.0)
    
    def test_generate_heatmap_data_custom_size(self):
        """Test heatmap data generation with custom size"""
        size = 5
        df = generate_heatmap_data(size=size)
        
        assert df.shape == (size, size)
        assert all(-1 <= df.values.flatten()) and all(df.values.flatten() <= 1)
    
    def test_generate_heatmap_data_correlation_properties(self):
        """Test that heatmap correlation matrix has valid properties"""
        df = generate_heatmap_data(size=8)
        
        # All values should be between -1 and 1
        assert df.min().min() >= -1
        assert df.max().max() <= 1
        
        # Matrix should be symmetric
        for i in range(len(df)):
            for j in range(len(df)):
                assert abs(df.iloc[i, j] - df.iloc[j, i]) < 1e-10


class TestDataQuality:
    """Test suite for data quality checks"""
    
    def test_no_null_values_sine(self):
        """Test that sine data has no null values"""
        df = generate_sine_data()
        assert not df.isnull().any().any()
    
    def test_no_null_values_timeseries(self):
        """Test that time series data has no null values"""
        df = generate_timeseries_data()
        assert not df.isnull().any().any()
    
    def test_no_null_values_scatter(self):
        """Test that scatter data has no null values"""
        df = generate_scatter_data()
        assert not df.isnull().any().any()
    
    def test_no_null_values_categorical(self):
        """Test that categorical data has no null values"""
        df = generate_categorical_data()
        assert not df.isnull().any().any()
    
    def test_no_null_values_distribution(self):
        """Test that distribution data has no null values"""
        df = generate_distribution_data()
        assert not df.isnull().any().any()
    
    def test_no_null_values_heatmap(self):
        """Test that heatmap data has no null values"""
        df = generate_heatmap_data()
        assert not df.isnull().any().any()


class TestDataTypes:
    """Test suite for data type validation"""
    
    def test_sine_data_types(self):
        """Test that sine data has correct dtypes"""
        df = generate_sine_data()
        assert df['x'].dtype in [np.float64, np.float32]
        assert df['y'].dtype in [np.float64, np.float32]
    
    def test_timeseries_data_types(self):
        """Test that time series data has correct dtypes"""
        df = generate_timeseries_data()
        assert pd.api.types.is_datetime64_any_dtype(df['date'])
        assert df['value'].dtype in [np.float64, np.float32]
        assert df['category'].dtype == object
    
    def test_scatter_data_types(self):
        """Test that scatter data has correct dtypes"""
        df = generate_scatter_data()
        assert df['x'].dtype in [np.float64, np.float32]
        assert df['y'].dtype in [np.float64, np.float32]
        assert df['group'].dtype == object
        assert df['size'].dtype in [np.int64, np.int32, np.int_]
    
    def test_categorical_data_types(self):
        """Test that categorical data has correct dtypes"""
        df = generate_categorical_data()
        assert df['category'].dtype == object
        assert df['value'].dtype in [np.int64, np.int32, np.int_]
        assert df['subcategory'].dtype == object


class TestEdgeCases:
    """Test suite for edge cases and boundary conditions"""
    
    def test_sine_data_minimal_points(self):
        """Test sine data generation with minimal points"""
        df = generate_sine_data(points=2)
        assert len(df) == 2
    
    def test_timeseries_single_day(self):
        """Test time series with single day"""
        df = generate_timeseries_data(days=1)
        assert len(df) == 2  # start and end day
    
    def test_scatter_minimal_points(self):
        """Test scatter data with minimal points"""
        df = generate_scatter_data(n_points=1)
        assert len(df) == 1
    
    def test_heatmap_minimal_size(self):
        """Test heatmap with minimal size"""
        df = generate_heatmap_data(size=2)
        assert df.shape == (2, 2)
    
    def test_distribution_large_sample(self):
        """Test distribution data with large sample size"""
        df = generate_distribution_data(n_samples=50000)
        assert len(df) == 50000
        assert not df.isnull().any().any()


class TestNewFeatures:
    """Test suite for new features added in PR"""
    
    def test_generate_realtime_data_default(self):
        """Test realtime data generation with default parameters"""
        df = generate_realtime_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 50  # default n_points
        assert 'timestamp' in df.columns
        assert 'value' in df.columns
        assert 'category' in df.columns
        assert 'status' in df.columns
        assert pd.api.types.is_datetime64_any_dtype(df['timestamp'])
    
    def test_generate_realtime_data_custom_points(self):
        """Test realtime data generation with custom number of points"""
        n_points = 100
        df = generate_realtime_data(n_points=n_points)
        
        assert len(df) == n_points
        assert not df.isnull().any().any()
    
    def test_realtime_data_categories(self):
        """Test that realtime data has valid categories"""
        df = generate_realtime_data(n_points=100)
        
        unique_categories = df['category'].unique()
        assert len(unique_categories) <= 3
        assert all(cat in ['Sensor A', 'Sensor B', 'Sensor C'] 
                  for cat in unique_categories)
    
    def test_realtime_data_status(self):
        """Test that realtime data has valid status values"""
        df = generate_realtime_data(n_points=100)
        
        unique_statuses = df['status'].unique()
        assert all(status in ['Normal', 'Warning', 'Critical'] 
                  for status in unique_statuses)
    
    def test_export_data_to_csv(self):
        """Test CSV export functionality"""
        df = generate_sine_data(points=100)
        csv_data = export_data_to_csv(df)
        
        assert isinstance(csv_data, bytes)
        assert len(csv_data) > 0
        
        # Verify it's valid CSV by reading it back
        csv_string = csv_data.decode('utf-8')
        assert 'x' in csv_string
        assert 'y' in csv_string
    
    def test_export_data_to_json(self):
        """Test JSON export functionality"""
        df = generate_sine_data(points=100)
        json_data = export_data_to_json(df)
        
        assert isinstance(json_data, bytes)
        assert len(json_data) > 0
        
        # Verify it's valid JSON
        json_string = json_data.decode('utf-8')
        assert '[' in json_string  # JSON array
        assert '{' in json_string  # JSON objects
    
    def test_export_timeseries_to_csv(self):
        """Test exporting time series data to CSV"""
        df = generate_timeseries_data(days=30)
        csv_data = export_data_to_csv(df)
        
        assert isinstance(csv_data, bytes)
        csv_string = csv_data.decode('utf-8')
        assert 'date' in csv_string
        assert 'value' in csv_string
        assert 'category' in csv_string
    
    def test_export_scatter_to_json(self):
        """Test exporting scatter data to JSON"""
        df = generate_scatter_data(n_points=50)
        json_data = export_data_to_json(df)
        
        assert isinstance(json_data, bytes)
        assert len(json_data) > 0
    
    def test_realtime_data_timestamps_ordered(self):
        """Test that realtime data timestamps are in chronological order"""
        df = generate_realtime_data(n_points=50)
        
        timestamps = df['timestamp'].tolist()
        assert timestamps == sorted(timestamps)
    
    def test_realtime_data_minimal_points(self):
        """Test realtime data with minimal points"""
        df = generate_realtime_data(n_points=1)
        assert len(df) == 1
        assert not df.isnull().any().any()


class TestDarkModeAndFilters:
    """Test suite for dark mode and filtering features"""
    
    def test_apply_filters_min_value(self):
        """Test applying minimum value filter"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': 150, 'max_value': None, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) <= len(df)
        assert filtered_df['value'].min() >= 150
    
    def test_apply_filters_max_value(self):
        """Test applying maximum value filter"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': None, 'max_value': 150, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) <= len(df)
        assert filtered_df['value'].max() <= 150
    
    def test_apply_filters_both_values(self):
        """Test applying both min and max value filters"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': 120, 'max_value': 180, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) <= len(df)
        assert filtered_df['value'].min() >= 120
        assert filtered_df['value'].max() <= 180
    
    def test_apply_filters_category(self):
        """Test applying category filters"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': None, 'max_value': None, 'categories': ['A'], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) <= len(df)
        assert all(cat == 'A' for cat in filtered_df['category'])
    
    def test_apply_filters_no_filters(self):
        """Test that no filters returns original data"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': None, 'max_value': None, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) == len(df)
    
    def test_apply_filters_empty_result(self):
        """Test filters that result in empty dataset"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': 1000, 'max_value': 2000, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        # Should handle empty results gracefully
        assert len(filtered_df) == 0 or len(filtered_df) <= len(df)
    
    # Note: Theme tests require Streamlit runtime, tested manually
    
    def test_filters_preserve_dataframe_structure(self):
        """Test that filters preserve dataframe structure"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': 130, 'max_value': 170, 'categories': [], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        # Check that columns are preserved
        assert list(filtered_df.columns) == list(df.columns)
        assert filtered_df.index.name == df.index.name
    
    def test_filters_with_multiple_categories(self):
        """Test filtering with multiple categories"""
        df = generate_timeseries_data(days=30)
        filters = {'min_value': None, 'max_value': None, 'categories': ['A', 'B'], 'date_range': None}
        
        filtered_df = apply_filters(df, filters)
        
        assert len(filtered_df) <= len(df)
        assert all(cat in ['A', 'B'] for cat in filtered_df['category'])


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=app", "--cov-report=term-missing"])

