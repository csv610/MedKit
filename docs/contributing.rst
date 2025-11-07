Contributing to MedKit
======================

Thank you for your interest in contributing to MedKit! This guide will help you get started.

Code of Conduct
---------------

Please note that this project is released with a `Contributor Code of Conduct <CODE_OF_CONDUCT.md>`_. By participating in this project you agree to abide by its terms.

Getting Started
---------------

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a virtual environment
4. Install development dependencies
5. Make your changes
6. Run tests
7. Submit a pull request

Setting Up Development Environment
-----------------------------------

.. code-block:: bash

   # Clone repository
   git clone https://github.com/your-username/medkit.git
   cd medkit

   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install development dependencies
   pip install -r requirements-dev.txt

Documentation
--------------

When adding new modules, please include:

1. **Module docstring** with:
   - Overview of module purpose
   - QUICK START section
   - COMMON USES section
   - Example usage

2. **Class docstrings** with:
   - Description of the class
   - Attributes with types
   - Example of instantiation

3. **Method docstrings** with:
   - Description of what the method does
   - Args and their types
   - Return type and description
   - Raises (exceptions)
   - Example usage

Example Documentation Template:

.. code-block:: python

   \"\"\"
   module_name - Brief description

   Longer description of what this module does and common use cases.

   QUICK START:
       from module_name import SomeClass
       obj = SomeClass()
       result = obj.method()

   COMMON USES:
       1. First common use
       2. Second common use
   \"\"\"

   class MyClass:
       \"\"\"
       Description of the class.

       Attributes:
           attr1 (str): Description
           attr2 (int): Description

       Example:
           obj = MyClass(attr1="value")
       \"\"\"

       def my_method(self, param: str) -> str:
           \"\"\"
           Description of method.

           Args:
               param (str): Description of parameter

           Returns:
               str: Description of return value

           Example:
               result = obj.my_method("input")
           \"\"\"

Code Style
----------

- Follow PEP 8 style guide
- Use type hints in function signatures
- Write docstrings for all public functions and classes
- Keep functions focused and modular

Testing
-------

Before submitting a pull request:

.. code-block:: bash

   # Run tests
   pytest

   # Check code style
   flake8 src/

   # Build documentation
   cd docs && make html

Pull Request Process
--------------------

1. Update documentation to reflect any changes
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Create a clear PR description
6. Reference any related issues

Types of Contributions
----------------------

Bug Reports
~~~~~~~~~~~

- Use GitHub Issues with a clear title
- Include steps to reproduce
- Provide expected vs actual behavior
- Include your environment details

Feature Requests
~~~~~~~~~~~~~~~~

- Clearly describe the use case
- Explain why this feature is needed
- Provide examples of how it would be used

Documentation Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix typos and unclear passages
- Add missing examples
- Improve organization
- Add new guides and tutorials

Code Contributions
~~~~~~~~~~~~~~~~~~

- Bug fixes and performance improvements
- New features
- New modules
- Tests and test coverage

Reporting Issues
----------------

When reporting a bug:

- Use a clear, descriptive title
- Describe the exact steps to reproduce
- Provide specific examples
- Describe observed vs expected behavior
- Include your environment (Python version, OS, etc.)
- Include relevant code snippets

License
-------

By contributing to MedKit, you agree that your contributions will be licensed under its MIT License.

Questions or Need Help?
-----------------------

- Check existing issues and discussions
- Open a new discussion for questions
- Ask in the community forums
