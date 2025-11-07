Installation Guide
===================

System Requirements
-------------------

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for AI API access)

Basic Installation
-------------------

Install MedKit from PyPI:

.. code-block:: bash

   pip install medkit-client

Install all core dependencies:

.. code-block:: bash

   pip install medkit-client pydantic google-generativeai requests networkx

Development Installation
--------------------------

For development or contributing to MedKit:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/your-repo/medkit.git
   cd medkit

   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install development dependencies
   pip install -r requirements-dev.txt

Environment Configuration
---------------------------

API Keys
~~~~~~~~

MedKit requires a Gemini API key for AI-powered features:

1. Get your API key from `Google AI Studio <https://makersuite.google.com/app/apikey>`_
2. Set the environment variable:

.. code-block:: bash

   export GEMINI_API_KEY="your_api_key_here"

On Windows, use:

.. code-block:: cmd

   set GEMINI_API_KEY=your_api_key_here

Optional: Create a ``.env`` file in your project:

.. code-block:: bash

   GEMINI_API_KEY=your_api_key_here

Then load it in your application:

.. code-block:: python

   from dotenv import load_dotenv
   load_dotenv()

Verifying Installation
----------------------

Test your installation:

.. code-block:: python

   from src.rxnorm_client import RxNormClient

   with RxNormClient() as client:
       rxcui = client.get_identifier("aspirin")
       print(f"RxCUI for aspirin: {rxcui}")

Troubleshooting
---------------

Module Not Found
~~~~~~~~~~~~~~~~

If you get "ModuleNotFoundError", ensure:

1. The module is installed: ``pip list | grep medkit``
2. You're in the correct directory
3. The Python path includes the src directory

API Connection Issues
~~~~~~~~~~~~~~~~~~~~~

If you get connection errors:

1. Check your internet connection
2. Verify your API key is valid
3. Check rate limits on your API account

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

Install missing packages:

.. code-block:: bash

   pip install pydantic google-generativeai requests networkx matplotlib

Updating MedKit
----------------

To update to the latest version:

.. code-block:: bash

   pip install --upgrade medkit-client

Uninstalling
-----------

To remove MedKit:

.. code-block:: bash

   pip uninstall medkit-client
