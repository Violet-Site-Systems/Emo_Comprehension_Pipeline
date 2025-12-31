# Build and Installation Guide

This guide covers building, installing, and developing the Emotional Comprehension Pipeline.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- git (for development)

## Quick Start

### Installation

Install the package in your environment:

```bash
pip install -e .
```

Or install with development dependencies:

```bash
pip install -e ".[dev]"
```

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Violet-Site-Systems/Emo_Comprehension_Pipeline.git
cd Emo_Comprehension_Pipeline
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### 4. Set Up Pre-commit Hooks

```bash
pre-commit install
```

## Building the Package

### Build Distribution Packages

```bash
python -m build
```

This creates both wheel and source distribution files in the `dist/` directory.

### Using Make

If you have `make` available:

```bash
make build
```

## Running Tests

### Basic Test Run

```bash
pytest
```

### With Coverage

```bash
pytest --cov=emo_comprehension --cov-report=term-missing --cov-report=html
```

### Using Make

```bash
make test        # With coverage
make test-quick  # Without coverage
```

## Code Quality

### Formatting

Format code with Black and isort:

```bash
black src tests
isort src tests
```

Or using Make:

```bash
make format
```

### Linting

Run all linters:

```bash
flake8 src tests
black --check src tests
isort --check-only src tests
```

Or using Make:

```bash
make lint
```

### Type Checking

Run mypy type checker:

```bash
mypy src
```

Or using Make:

```bash
make type-check
```

### Run All Checks

```bash
make all
```

This runs formatting, linting, type checking, and tests.

## Make Commands

The project includes a Makefile with useful commands:

```bash
make help           # Show all available commands
make install        # Install package in production mode
make install-dev    # Install with development dependencies
make test           # Run tests with coverage
make test-quick     # Run tests without coverage
make lint           # Run all linters
make format         # Format code
make type-check     # Run type checking
make clean          # Clean build artifacts
make build          # Build distribution packages
make pre-commit     # Run pre-commit hooks on all files
make all            # Run format, lint, type-check, and test
```

## Project Structure

```
Emo_Comprehension_Pipeline/
├── src/
│   └── emo_comprehension/          # Main package
│       ├── __init__.py
│       ├── core/                    # Core modules
│       │   ├── analyzer.py          # Emotional analysis
│       │   ├── comprehension.py     # Deep comprehension
│       │   └── response.py          # Response generation
│       └── utils/                   # Utility functions
├── tests/                           # Test suite
│   ├── test_analyzer.py
│   ├── test_comprehension.py
│   ├── test_response.py
│   └── test_utils.py
├── docs/                            # Documentation
├── examples/                        # Example usage
├── pyproject.toml                   # Project configuration
├── requirements.txt                 # Core dependencies
├── requirements-dev.txt             # Development dependencies
├── Makefile                         # Build automation
└── .pre-commit-config.yaml         # Pre-commit hooks
```

## Continuous Integration

The project includes GitHub Actions workflows for:

- **CI** (`.github/workflows/ci.yml`): Runs tests, linting, and type checking on multiple Python versions and operating systems
- **Release** (`.github/workflows/release.yml`): Automatically publishes to PyPI when a release is created

## Troubleshooting

### Import Errors

If you encounter import errors, ensure you've installed the package in editable mode:

```bash
pip install -e .
```

### Test Failures

Ensure all dependencies are installed:

```bash
pip install -e ".[dev]"
```

### Pre-commit Hook Failures

Run hooks manually to fix issues:

```bash
pre-commit run --all-files
```

## Next Steps

- Read the [API documentation](api.md) for usage examples
- Check [examples/](../examples/) for sample implementations
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines
