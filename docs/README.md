# MedKit Documentation

This directory contains the source documentation for MedKit, automatically generated from Python docstrings using Sphinx.

## Documentation Structure

```
docs/
├── conf.py                 # Sphinx configuration
├── index.rst              # Documentation home page
├── quick_start.rst        # Quick start guide
├── installation.rst       # Installation instructions
├── tutorials.rst          # Practical tutorials
├── contributing.rst       # Contribution guidelines
├── development_setup.rst  # Development environment setup
├── api/                   # API reference documentation
│   ├── modules.rst       # Module index
│   ├── medical_speciality.rst
│   ├── disease_info.rst
│   ├── rxnorm_client.rst
│   └── ...              # Other module API docs
├── modules/              # Documentation by category
│   ├── medical_reference.rst
│   ├── drug_information.rst
│   ├── diagnostic_tools.rst
│   ├── mental_health_tools.rst
│   └── ui_interfaces.rst
└── _build/              # Generated HTML (after build)
    └── html/            # HTML documentation
        └── index.html   # Start here
```

## Building Documentation

### Prerequisites

Install Sphinx and required extensions:

```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
```

### Build HTML Documentation

```bash
cd docs
make clean
make html
```

The HTML documentation will be generated in `docs/_build/html/`.

### View Documentation

Open `docs/_build/html/index.html` in your web browser, or use a local web server:

```bash
cd docs/_build/html
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Documentation Features

### Automatic API Documentation

The documentation automatically extracts docstrings from Python modules using Sphinx's `autodoc` extension. This includes:

- **Classes**: All class definitions, attributes, and methods
- **Functions**: All functions with parameters, return types, and examples
- **Enums**: Enumeration values and descriptions
- **Type Hints**: Automatically included in the documentation

### Google-Style Docstrings

MedKit uses Google-style docstrings processed by the `Napoleon` extension:

```python
def my_function(param1: str, param2: int) -> bool:
    """
    Brief description of the function.

    Longer description if needed.

    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2

    Returns:
        bool: Description of return value

    Raises:
        ValueError: When something is wrong

    Example:
        >>> result = my_function("test", 42)
        >>> print(result)
        True
    """
```

### Code Examples

Each module documentation includes:

- **QUICK START**: Basic usage examples
- **COMMON USES**: Typical use cases
- **Examples**: Code examples in docstrings

### Source Code Links

The documentation includes links to source code, allowing readers to jump directly to the implementation.

## Customizing Documentation

### Adding New Modules

1. **Write comprehensive docstrings** in your Python module
2. **Create an API reference file** in `docs/api/`:

```rst
my_module - My Module Description
==================================

.. automodule:: my_module
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
```

3. **Update `docs/api/modules.rst`** to include your new module

### Modifying Configuration

Edit `docs/conf.py` to change:

- Theme and styling
- Sphinx extensions
- autodoc options
- Napoleon settings

### Building Other Formats

Generate PDF documentation:

```bash
cd docs
make latexpdf
```

Generate EPUB (e-book):

```bash
cd docs
make epub
```

## Documentation Standards

### Writing Docstrings

All public functions and classes should have docstrings including:

1. **Brief description** (one-line summary)
2. **Longer description** (if needed)
3. **Args section**: Parameters and types
4. **Returns section**: Return value and type
5. **Raises section**: Exceptions that may be raised
6. **Example section**: Usage example

### Module Docstrings

Module-level docstrings should include:

```python
"""
module_name - Brief description

Longer description of module purpose.

QUICK START:
    Example of how to quickly get started

COMMON USES:
    1. First common use case
    2. Second common use case

DATA MODELS:
    - ModelName: Description
    - ModelName: Description
"""
```

### Examples

Include practical examples in docstrings:

```python
Example:
    >>> client = RxNormClient()
    >>> rxcui = client.get_identifier("aspirin")
    >>> print(rxcui)
    207381
```

## Live Documentation Server

For development with live reload:

```bash
pip install sphinx-autobuild
cd docs
sphinx-autobuild . _build/html
```

Open http://localhost:8000 and the documentation will automatically rebuild when files change.

## Continuous Integration

Documentation can be automatically built and deployed on:

- **GitHub Pages**: Push to gh-pages branch
- **ReadTheDocs**: Connect your repository
- **Custom servers**: Use CI/CD pipelines

### ReadTheDocs Integration

1. Go to https://readthedocs.org/
2. Connect your GitHub repository
3. Documentation builds automatically on each push

## Troubleshooting

### Missing Module Documentation

If module appears to have no content:

1. Check that `sys.path` is correctly set in `conf.py`
2. Verify module is importable from the docs directory
3. Ensure the module has proper docstrings

### Build Warnings

Review build warnings in the console output. Common issues:

- **Undefined references**: Check cross-reference syntax
- **Missing source files**: Verify file paths
- **Unknown lexer**: Check code block language specification

### CSS/Styling Issues

If documentation looks incorrect:

1. Clear the build cache: `make clean`
2. Rebuild: `make html`
3. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

## More Information

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [ReStructuredText Guide](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Napoleon Documentation](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)

## Questions?

For questions about the documentation:

1. Check the Quick Start guide
2. Review existing documentation
3. Open an issue on GitHub
4. Ask in community discussions
