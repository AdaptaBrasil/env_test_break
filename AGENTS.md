# Agent Instructions for env_test_break

This is a Python utilities library with comprehensive testing and CI/CD automation using GitHub Actions.

## Quick Start Commands

### Testing
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src

# Run specific test file
pytest tests/unit/test_utilities.py

# Run tests with verbose output
pytest -v
```

### Development
```bash
# Install project with poetry
poetry install

# Run main script
python main.py

# Build package
poetry build
```

## Project Structure & Conventions

```
env_test_break/
├── src/util/           # Core utilities (math operations)
├── tests/unit/         # Unit test suite (matches src/ structure)
├── main.py             # Entry point demonstrating utility usage
├── pyproject.toml      # Poetry project configuration
└── README.md
```

### Key Conventions

1. **Module Organization**: 
   - All utility functions live in `src/util/utilities.py`
   - Organized by functionality (math operations: add, sub, mul, div, sqrt, pow)

2. **Testing**:
   - Unit tests in `tests/unit/test_utilities.py` 
   - Test functions named `test_*` (pytest convention)
   - Tests cover both happy paths and error cases (e.g., division by zero, negative sqrt)

3. **Error Handling**:
   - Functions raise `ValueError` with descriptive messages for invalid inputs
   - Always include error handling in new utility functions

4. **Python Version**: Requires Python 3.12+ (see `pyproject.toml`)

## GitHub Actions Workflows

Two CI/CD workflows run on every push:
- **Ubuntu 24.04**: Tests on Linux (`run_ubuntu_2404_python_versions.yml`)
- **Windows 2022**: Tests on Windows (`run_windows_2022_python_versions.yml`)

Both workflows run the full test suite and validate cross-platform compatibility.

## When Adding New Features

1. **Add utility function** to `src/util/utilities.py`
2. **Add corresponding test** to `tests/unit/test_utilities.py` (minimum: happy path + error cases)
3. **Run tests locally**: `pytest` should pass 100%
4. **Update main.py** if the function should be demonstrated
5. **Push to trigger** GitHub Actions validation

## Notes for AI Agents

- This is an **experimental repository** (`env_test_break`) - focus on clear, testable code
- All functions are pure utilities without external dependencies (except pytest for testing)
- Keep `utilities.py` focused on mathematical operations
- Maintain test coverage - add tests before or alongside new features
