Quick Start Guide
=================

Welcome to MedKit! This guide will help you get started with the most common use cases.

Package Organization
--------------------

MedKit is organized into specialized packages for different domains:

.. code-block:: text

   from src.core              # AI client and core functionality
   from src.drug              # Drug interactions and medicine information
   from src.medical           # Medical reference information (diseases, anatomy, etc.)
   from src.mental_health     # Mental health assessment tools
   from src.tests_diagnostics # Medical tests and diagnostics
   from src.utilities         # Helper utilities (privacy, validation, etc.)
   from src.visualization     # Data visualization tools
   from src.ui                # Web interfaces (Streamlit, Gradio)

Installation
------------

.. code-block:: bash

   pip install medkit-client pydantic google-generativeai

Basic Usage
-----------

Medical Specialties
~~~~~~~~~~~~~~~~~~~

Find the right specialist for a patient condition:

.. code-block:: python

   from src.medical import MedicalSpecialistDatabase

   # Load database
   db = MedicalSpecialistDatabase(specialists=[...])

   # Find specialists for a condition
   specialists = db.search_by_condition("heart disease")
   for specialist in specialists:
       print(f"{specialist.specialty_name}: {specialist.description}")

   # Get all surgical specialties
   surgeons = db.get_surgical_specialists()

   # List all categories
   categories = db.get_all_categories()

Disease Information
~~~~~~~~~~~~~~~~~~~

Generate comprehensive disease information:

.. code-block:: python

   from src.medical import get_disease_info

   # Generate disease information
   disease_info = get_disease_info("diabetes")

   # Access different sections
   symptoms = disease_info.clinical_presentation.symptoms
   treatments = disease_info.management.treatment_options
   risk_factors = disease_info.risk_and_causes.risk_factors

   # Save to file
   disease_info = get_disease_info("hypertension", output_path="hypertension.json")

Drug Information
~~~~~~~~~~~~~~~~

Look up drugs in the RxNorm database:

.. code-block:: python

   from src.drug import RxNormClient

   with RxNormClient() as client:
       # Get drug identifier
       rxcui = client.get_identifier("aspirin")
       print(f"RxCUI: {rxcui}")

       # Get drug properties
       props = client.get_properties(rxcui)
       print(f"Drug name: {props['properties']['name']}")

       # Validate drug name
       if client.check_valid_drug("metformin"):
           print("Drug is valid")

Drug-Disease Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~

Check how diseases affect medications:

.. code-block:: python

   from src.drug import get_drug_disease_interaction

   # Analyze interaction
   interaction = get_drug_disease_interaction(
       drug_name="metformin",
       disease_name="kidney disease"
   )

   # Check safety impact
   if interaction.safety_impact.has_impact:
       print(f"Safety risk: {interaction.safety_impact.risk_level}")

   # Check if dose adjustment needed
   if interaction.dosage_adjustments.adjustment_needed:
       print(f"Adjustment type: {interaction.dosage_adjustments.adjustment_type}")

Common Patterns
---------------

Using the MedKit Client
~~~~~~~~~~~~~~~~~~~~~~

Most modules use the MedKitClient for AI-powered analysis:

.. code-block:: python

   from src.core import MedKitClient

   client = MedKitClient()
   result = client.generate_text(
       prompt="What are the symptoms of pneumonia?",
       schema=YourDataModel,
       sys_prompt="You are a medical expert..."
   )

Working with Pydantic Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MedKit uses Pydantic for data validation:

.. code-block:: python

   from pydantic import BaseModel, Field

   class MedicineInfo(BaseModel):
       name: str = Field(..., description="Medicine name")
       dosage: str = Field(..., description="Dosage information")

   # Validate and parse
   medicine = MedicineInfo(name="Aspirin", dosage="500mg")

Next Steps
----------

- Read the :doc:`API Reference </api/modules>` for detailed module documentation
- Check :doc:`Module Categories </modules/medical_reference>` for specific use cases
- Explore the :doc:`Development Guide </development_setup>` to contribute

Troubleshooting
---------------

Import Errors
~~~~~~~~~~~~~

If you get import errors, make sure dependencies are installed:

.. code-block:: bash

   pip install --upgrade medkit-client pydantic google-generativeai

API Key Configuration
~~~~~~~~~~~~~~~~~~~~~

Most modules require the GEMINI_API_KEY environment variable:

.. code-block:: bash

   export GEMINI_API_KEY="your_api_key_here"

Need Help?
----------

- Check the API documentation for the specific module you're using
- Review example code in the tutorials
- Open an issue on GitHub
