# Source Code

This directory contains the core source code for the Emotional Comprehension Pipeline.

## Structure

```
emo_comprehension/
├── __init__.py              # Package initialization
├── core/                    # Core functionality
│   ├── __init__.py
│   ├── analyzer.py          # Emotional analysis
│   ├── comprehension.py     # Deep comprehension
│   └── response.py          # Response generation
└── utils/                   # Utility functions
    └── __init__.py
```

## Modules

### Core Modules

- **analyzer.py**: Emotional analysis and state detection
- **comprehension.py**: Deep emotional comprehension using neuro-symbolic approaches
- **response.py**: Emotionally aligned response generation

### Utils

- **utils/**: Shared utility functions for configuration, normalization, and validation

## Development

- Follow the project's ethical guidelines
- Write clean, maintainable code
- Include appropriate tests in `tests/`
- Document complex logic with docstrings
- Consider neurodivergent accessibility in design
- Run `make format` before committing
- Ensure tests pass with `make test`

## Type Checking

The package includes `py.typed` for full type checking support. Use type hints in all new code.
