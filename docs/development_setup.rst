Development Setup Guide
=======================

This guide will help you set up your development environment for MedKit.

Prerequisites
-------------

- Python 3.8 or higher
- Git
- pip or conda
- Text editor or IDE (VS Code, PyCharm, etc.)

Environment Setup
-----------------

1. Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/your-repo/medkit.git
   cd medkit

2. Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using venv:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

Using conda:

.. code-block:: bash

   conda create -n medkit python=3.10
   conda activate medkit

3. Install Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install -r requirements.txt
   pip install -r requirements-dev.txt

Development Dependencies
------------------------

Essential tools for development:

- **pytest**: Testing framework
- **flake8**: Code style checking
- **black**: Code formatting
- **sphinx**: Documentation generation
- **sphinx-rtd-theme**: Documentation theme

Installing development tools:

.. code-block:: bash

   pip install pytest flake8 black sphinx sphinx-rtd-theme

Project Structure
-----------------

.. code-block:: text

   medkit/
   ├── src/                      # Source code
   │   ├── medical_speciality.py
   │   ├── disease_info.py
   │   ├── rxnorm_client.py
   │   └── ...
   ├── tests/                    # Test files
   │   ├── test_*.py
   ├── docs/                     # Documentation
   │   ├── conf.py
   │   ├── index.rst
   │   └── ...
   ├── requirements.txt          # Production dependencies
   ├── requirements-dev.txt      # Development dependencies
   └── README.md

Development Workflow
--------------------

1. Create a Feature Branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git checkout -b feature/your-feature-name

2. Make Your Changes
~~~~~~~~~~~~~~~~~~~~~

- Write code following PEP 8
- Add comprehensive docstrings
- Include type hints
- Write tests for new functionality

3. Run Tests
~~~~~~~~~~~~

.. code-block:: bash

   pytest tests/

4. Check Code Style
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   flake8 src/

5. Format Code
~~~~~~~~~~~~~~

.. code-block:: bash

   black src/

6. Update Documentation
~~~~~~~~~~~~~~~~~~~~~~~

If adding new modules or features:

.. code-block:: bash

   cd docs
   make html
   # View docs in _build/html/index.html

7. Commit and Push
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git add .
   git commit -m "Clear description of changes"
   git push origin feature/your-feature-name

8. Submit Pull Request
~~~~~~~~~~~~~~~~~~~~~~

Go to GitHub and create a pull request with:

- Clear title and description
- Reference to related issues
- Summary of changes

Testing
-------

Writing Tests
~~~~~~~~~~~~~

Tests should:

- Test one thing per test function
- Use descriptive names (test_<function>_<scenario>)
- Be isolated and independent
- Use fixtures for setup/teardown

Example:

.. code-block:: python

   import pytest
   from src.medical_speciality import MedicalSpecialist

   def test_specialist_creation():
       specialist = MedicalSpecialist(
           specialty_name="Cardiology",
           category=...,
           ...
       )
       assert specialist.specialty_name == "Cardiology"

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   pytest

   # Run specific test file
   pytest tests/test_medical_speciality.py

   # Run with verbose output
   pytest -v

   # Run with coverage report
   pytest --cov=src/

Documentation
--------------

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd docs
   make html

View the documentation:

- Open ``docs/_build/html/index.html`` in your browser

Live Documentation Server
~~~~~~~~~~~~~~~~~~~~~~~~~

For development with live reload:

.. code-block:: bash

   pip install sphinx-autobuild
   cd docs
   sphinx-autobuild . _build/html

Then open http://localhost:8000

IDE Setup
---------

VS Code
~~~~~~~

1. Install Python extension
2. Select virtual environment as interpreter
3. Configure linting (flake8):

   .. code-block:: json

      {
          "python.linting.flake8Enabled": true,
          "python.linting.flake8Path": "flake8",
      }

4. Configure formatting (black):

   .. code-block:: json

      {
          "python.formatting.provider": "black",
      }

PyCharm
~~~~~~~

1. Open project
2. Set Project Interpreter to your venv
3. Configure Code Style to PEP 8
4. Enable inspections

Version Control
---------------

Branch Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~

- ``feature/description``: New features
- ``fix/description``: Bug fixes
- ``docs/description``: Documentation updates
- ``refactor/description``: Code refactoring

Commit Messages
~~~~~~~~~~~~~~~

Use clear, descriptive commit messages:

.. code-block:: text

   Add medical specialty database functionality

   - Implement MedicalSpecialistDatabase class
   - Add search_by_condition method
   - Add comprehensive docstrings

Release Process
---------------

Preparing a Release
~~~~~~~~~~~~~~~~~~~

1. Update version number in ``__init__.py``
2. Update CHANGELOG.md
3. Update version in ``docs/conf.py``
4. Run full test suite
5. Build documentation
6. Create git tag

.. code-block:: bash

   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0

Troubleshooting
---------------

Import Errors
~~~~~~~~~~~~~

If modules aren't found:

.. code-block:: bash

   # Reinstall in development mode
   pip install -e .

API Errors
~~~~~~~~~~

If tests fail due to API issues:

- Check GEMINI_API_KEY is set
- Verify API key is valid
- Check rate limits

Environment Issues
~~~~~~~~~~~~~~~~~~

If tests fail with environment errors:

.. code-block:: bash

   # Reinstall dependencies
   pip install --upgrade -r requirements-dev.txt

   # Clear cache
   pip cache purge

Getting Help
------------

- Check existing issues on GitHub
- Ask in development discussions
- Read related documentation
- Ask the community
