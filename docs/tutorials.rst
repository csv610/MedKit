Tutorials
=========

Learn MedKit through practical examples and walkthroughs.

Tutorial 1: Creating a Patient Medication Profile
--------------------------------------------------

In this tutorial, you'll create a comprehensive medication profile for a patient.

Step 1: Get Drug Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.rxnorm_client import RxNormClient
   from src.medicine_info import get_medicine_info

   # Get drug RxCUI
   with RxNormClient() as client:
       rxcui = client.get_identifier("metformin 500mg")
       print(f"RxCUI: {rxcui}")

Step 2: Analyze Drug-Disease Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.drug_disease_interaction import get_drug_disease_interaction

   # Patient has diabetes and kidney disease
   interaction = get_drug_disease_interaction(
       drug_name="metformin",
       disease_name="chronic kidney disease"
   )

   # Check for safety concerns
   if interaction.safety_impact.has_impact:
       print(f"⚠️ Safety concern: {interaction.safety_impact.impact_description}")

   # Check if dose adjustment needed
   if interaction.dosage_adjustments.adjustment_needed:
       print(f"📝 Dose adjustment: {interaction.dosage_adjustments.adjustment_type}")

Step 3: Generate Patient Education Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.disease_info import get_disease_info

   # Generate diabetes information
   diabetes_info = get_disease_info("diabetes type 2")

   # Create patient-friendly summary
   print("Disease Overview:")
   print(diabetes_info.background.definition)
   print("\nSymptoms:")
   for symptom in diabetes_info.clinical_presentation.symptoms:
       print(f"  - {symptom}")

Tutorial 2: Building a Medical Reference Tool
----------------------------------------------

Create a simple tool to look up medical information.

.. code-block:: python

   from src.medical_speciality import MedicalSpecialistDatabase
   from src.disease_info import get_disease_info

   def patient_advisor(symptoms, patient_age):
       """Suggest appropriate specialists based on symptoms."""

       # Load specialist database
       db = MedicalSpecialistDatabase(specialists=[...])

       # Find specialists for symptoms
       specialists = db.search_by_condition(symptoms)

       print(f"Specialists for {symptoms}:")
       for spec in specialists:
           print(f"  - {spec.specialty_name}: {spec.description}")

       # Generate disease information
       disease_info = get_disease_info(symptoms)
       print(f"\nAbout {disease_info.identity.disease_name}:")
       print(disease_info.background.definition)

   # Use the advisor
   patient_advisor("heart palpitations", 45)

Tutorial 3: Drug-Drug Interaction Checker
------------------------------------------

Check for interactions between multiple medications.

.. code-block:: python

   from src.drug_drug_interaction import get_drug_interaction

   medications = ["aspirin", "ibuprofen", "metformin"]

   # Check all pairs
   for i, drug1 in enumerate(medications):
       for drug2 in medications[i+1:]:
           interaction = get_drug_interaction(drug1, drug2)

           if interaction.severity != "NONE":
               print(f"⚠️ {drug1} + {drug2}")
               print(f"   Severity: {interaction.severity}")
               print(f"   Details: {interaction.interaction_details}")

Tutorial 4: Analyzing Prescription Images
------------------------------------------

Extract medicine information from prescription images.

.. code-block:: python

   from src.prescription_analyzer import analyze_prescription_image
   from pathlib import Path

   # Analyze prescription image
   image_path = Path("prescription.jpg")
   prescription_info = analyze_prescription_image(str(image_path))

   # Extract medicines
   for medicine in prescription_info.medicines:
       print(f"Medicine: {medicine.medicine_name}")
       print(f"  Dosage: {medicine.dosage_as_prescribed}")
       print(f"  Frequency: {medicine.frequency}")

       # Get detailed info for each medicine
       from src.medicine_info import get_medicine_info
       med_info = get_medicine_info(medicine.medicine_name)
       print(f"  Uses: {med_info.uses.primary_uses}")

Tutorial 5: Mental Health Support
----------------------------------

Use MedKit for mental health assessment and support.

.. code-block:: python

   from src.mental_health_assessment import MentalHealthAssessment
   from src.mental_health_chat import MentalHealthChat

   # Start assessment
   assessment = MentalHealthAssessment()
   results = assessment.assess("depression")

   print(f"Assessment Results:")
   print(f"  Severity: {results.severity_level}")
   print(f"  Risk Level: {results.risk_level}")

   # Get chat support
   chat = MentalHealthChat()
   response = chat.get_response("I feel anxious")
   print(f"Support: {response}")

Best Practices
--------------

1. **Always validate inputs** - Check drug names and disease names before use
2. **Handle API errors** - Wrap API calls in try-except blocks
3. **Cache results** - Store API responses to avoid redundant calls
4. **Respect privacy** - Never log sensitive patient information
5. **Verify outputs** - Always verify AI-generated medical information with authoritative sources

Resources
---------

- :doc:`API Reference </api/modules>`
- :doc:`Quick Start </quick_start>`
- GitHub Issues and Discussions
