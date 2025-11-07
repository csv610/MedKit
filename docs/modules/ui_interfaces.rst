User Interface Modules
======================

Streamlit UI
------------

Interactive web interface using Streamlit for MedKit applications.

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install streamlit

Usage
~~~~~

.. code-block:: bash

   streamlit run streamlit_ui.py

Features
~~~~~~~~

- Interactive medical search
- Disease information lookup
- Drug interaction checker
- Mental health assessment
- Real-time results

Gradio UI
---------

Simple web interface using Gradio.

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install gradio

Usage
~~~~~

.. code-block:: bash

   python gradio_ui.py

Features
~~~~~~~~

- Prescription image analysis
- Medicine information lookup
- Quick disease reference
- Simple form-based interface

CLI Tools
---------

Command-line interfaces for MedKit modules.

Examples
~~~~~~~~

.. code-block:: bash

   # Look up drug in RxNorm
   python rxnorm_client.py aspirin

   # Generate disease information
   python disease_info.py --disease diabetes

   # Check drug interactions
   python drug_disease_interaction.py --drug metformin --disease diabetes

Choosing an Interface
---------------------

- **Streamlit**: Best for interactive dashboards and complex workflows
- **Gradio**: Best for simple single-task applications
- **CLI**: Best for scripting and automation
- **Python API**: Best for integration into other applications
