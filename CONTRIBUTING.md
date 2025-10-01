# Contributing to Data Visualization Dashboard

Thank you for your interest in contributing to this project! 🎉

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/data-stuff.git
   cd data-stuff
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

### Making Changes

1. **Create a new branch** for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and test them locally:

   ```bash
   streamlit run app.py
   ```

3. **Write or update tests** for your changes:

   ```bash
   pytest test_app.py -v
   ```

4. **Ensure all tests pass** and coverage is maintained:
   ```bash
   pytest test_app.py --cov=app --cov-report=term-missing
   ```

### Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions explaining their purpose
- Keep functions focused and modular

### Testing Guidelines

- Write tests for all new functionality
- Ensure tests are independent and can run in any order
- Use descriptive test names that explain what is being tested
- Test edge cases and error conditions

Example test structure:

```python
def test_your_feature():
    """Test description of what this test validates"""
    # Arrange
    data = generate_test_data()

    # Act
    result = your_function(data)

    # Assert
    assert result.shape == (expected_rows, expected_cols)
    assert not result.isnull().any().any()
```

### Commit Guidelines

- Write clear, concise commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issues when applicable

Good commit messages:

```
Add scatter plot customization options
Fix correlation matrix diagonal values
Update README with deployment instructions
```

### Pull Request Process

1. **Update documentation** if you've made changes to functionality
2. **Ensure all tests pass** in the CI pipeline
3. **Update the README** if you've added new features
4. **Submit your PR** with a clear description of changes

PR Description Template:

```markdown
## Description

Brief description of what this PR does

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing

- [ ] All tests pass locally
- [ ] Added new tests for new features
- [ ] Manual testing completed

## Screenshots (if applicable)

Add screenshots of UI changes
```

## Types of Contributions

### 🐛 Bug Fixes

Found a bug? Please:

1. Check if it's already reported in Issues
2. Create a new issue with reproduction steps
3. Submit a PR with the fix and tests

### ✨ New Features

Want to add a feature?

1. Open an issue first to discuss the feature
2. Wait for approval/feedback
3. Implement the feature with tests
4. Submit a PR

### 📝 Documentation

Documentation improvements are always welcome:

- Fix typos
- Clarify instructions
- Add examples
- Improve code comments

### 🧪 Tests

Help improve test coverage:

- Add tests for untested code
- Improve existing test cases
- Add integration tests

### 🎨 UI/UX Improvements

Make the app more beautiful:

- Improve styling
- Enhance user experience
- Add animations
- Improve accessibility

## Adding New Visualizations

To add a new visualization type:

1. **Create a data generation function** in `app.py`:

   ```python
   def generate_new_data_type():
       """Generate data for your visualization"""
       # Your logic here
       return dataframe
   ```

2. **Add tests** for your data generation function:

   ```python
   def test_generate_new_data_type():
       """Test new data generation"""
       df = generate_new_data_type()
       assert isinstance(df, pd.DataFrame)
       # More assertions
   ```

3. **Create a display function**:

   ```python
   def show_new_visualization():
       st.header("Your Visualization Title")
       data = generate_new_data_type()
       # Create and display your chart
   ```

4. **Add navigation option** in the sidebar
5. **Update README** with the new feature

## Code Review Process

All PRs will be reviewed for:

- Code quality and style
- Test coverage
- Documentation
- Performance implications
- Security considerations

## Questions?

Feel free to:

- Open an issue for questions
- Start a discussion
- Reach out to maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on what is best for the community

Thank you for contributing! 🙏
