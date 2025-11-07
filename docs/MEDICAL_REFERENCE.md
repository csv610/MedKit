# Medical Reference Documentation

Comprehensive medical knowledge and reference materials covering disease information, medical anatomy, specialties, and related medical information.

## Table of Contents

1. [Disease Information](#disease-information)
2. [Medical Anatomy](#medical-anatomy)
3. [Medical Dictionary](#medical-dictionary)
4. [Medical Specialties](#medical-specialties)
5. [Surgical Procedures](#surgical-procedures)
6. [Medical Implants](#medical-implants)
7. [Herbal Medicine](#herbal-medicine)

---

## Disease Information

Get comprehensive information about diseases, conditions, and medical disorders.

### Features
- Disease definitions and descriptions
- Symptoms and clinical presentations
- Causes and risk factors
- Epidemiology and prevalence
- Treatment options and prognosis
- Complications and management strategies

### Usage

#### Programmatic
```python
from medkit.medical.disease_info import get_disease_info

# Get disease information
info = get_disease_info("diabetes mellitus")
print(f"Definition: {info.definition}")
print(f"Symptoms: {info.symptoms}")
print(f"Treatment: {info.treatment}")
```

#### Command-Line
```bash
python cli/cli_disease_info.py diabetes
python cli/cli_disease_info.py "heart disease" --verbose
```

### Available Information
- **Definition**: Clear, accurate medical definition
- **Symptoms**: Common and uncommon presentations
- **Causes**: Underlying etiology
- **Risk Factors**: Preventable and non-preventable factors
- **Diagnosis**: Diagnostic criteria and tests
- **Treatment**: Medical and surgical options
- **Prognosis**: Outcomes and complications
- **Prevention**: Evidence-based prevention strategies

### Examples

```python
# Diabetes
disease_info = get_disease_info("type 2 diabetes")

# Heart Disease
disease_info = get_disease_info("myocardial infarction")

# Infections
disease_info = get_disease_info("COVID-19")
```

---

## Medical Anatomy

Detailed anatomical structures, functions, and physiological processes.

### Features
- Organ system descriptions
- Anatomical structures and relationships
- Physiological functions
- Blood supply and innervation
- Common pathologies
- Clinical significance

### Usage

#### Programmatic
```python
from medkit.medical.medical_anatomy import get_anatomy_info

# Get anatomical information
anatomy = get_anatomy_info("heart")
print(anatomy.structure)
print(anatomy.function)
```

#### Command-Line
```bash
python cli/cli_medical_anatomy.py heart
python cli/cli_medical_anatomy.py brain --functions
```

### Body Systems Covered
- **Cardiovascular System**: Heart, blood vessels, circulation
- **Respiratory System**: Lungs, airways, gas exchange
- **Nervous System**: Brain, spinal cord, nerves
- **Musculoskeletal System**: Bones, muscles, joints
- **Gastrointestinal System**: Organs of digestion
- **Endocrine System**: Glands and hormones
- **Urinary System**: Kidneys and bladder
- **Reproductive System**: Male and female organs
- **Lymphatic System**: Immune organs and vessels
- **Integumentary System**: Skin and associated structures

### Examples

```python
# Cardiovascular anatomy
anatomy = get_anatomy_info("heart")
anatomy = get_anatomy_info("blood vessels")

# Nervous system
anatomy = get_anatomy_info("brain")
anatomy = get_anatomy_info("spinal cord")

# Musculoskeletal
anatomy = get_anatomy_info("knee joint")
```

---

## Medical Dictionary

Comprehensive medical terminology with definitions, synonyms, and explanations.

### Features
- Medical term definitions
- Alternative names and synonyms
- Etymology and origins
- Related terms and concepts
- Clinical usage examples

### Usage

#### Programmatic
```python
from medkit.medical.medical_dictionary import get_medical_definition

# Look up medical terms
definition = get_medical_definition("hypertension")
```

#### Command-Line
```bash
python cli/cli_medical_dictionary.py hypertension
python cli/cli_medical_dictionary.py "myocardial infarction" --verbose
```

### Coverage
- **Medical Conditions**: Disease names and syndromes
- **Procedures**: Surgical and diagnostic procedures
- **Anatomy**: Anatomical structures and terms
- **Pharmacology**: Drug names and classifications
- **Pathology**: Disease processes and mechanisms
- **Abbreviations**: Common medical abbreviations (MI, HTN, DM, etc.)

### Examples

```python
# Condition-related terms
definition = get_medical_definition("diabetes")
definition = get_medical_definition("hypertension")

# Procedure terms
definition = get_medical_definition("angioplasty")
definition = get_medical_definition("biopsy")

# Anatomical terms
definition = get_medical_definition("myocardium")
definition = get_medical_definition("ventricle")
```

---

## Medical Specialties

Information about medical disciplines, specialists, and their areas of focus.

### Features
- Specialty descriptions
- Specialist types and roles
- Common conditions treated
- Procedures and interventions
- Training and qualifications
- Sub-specialties

### Usage

#### Programmatic
```python
from medkit.medical.medical_speciality import get_speciality_info

# Get specialty information
specialty = get_speciality_info("cardiology")
```

#### Command-Line
```bash
python cli/cli_medical_speciality.py cardiology
python cli/cli_medical_speciality.py neurology --conditions
```

### Available Specialties
- **Cardiology**: Heart and cardiovascular system
- **Neurology**: Nervous system and brain
- **Orthopedics**: Bones, joints, and musculoskeletal system
- **Dermatology**: Skin conditions and dermatologic diseases
- **Oncology**: Cancer diagnosis and treatment
- **Gastroenterology**: Digestive system
- **Pulmonology**: Respiratory system and lungs
- **Psychiatry**: Mental health and behavior
- **Pediatrics**: Children's medicine
- **Obstetrics & Gynecology**: Pregnancy and women's health
- **Urology**: Urinary and reproductive systems
- **Otolaryngology**: Ears, nose, and throat
- **Ophthalmology**: Eyes and vision

### Examples

```python
# Major specialties
specialty = get_speciality_info("cardiology")
specialty = get_speciality_info("psychiatry")
specialty = get_speciality_info("oncology")

# Sub-specialties
specialty = get_speciality_info("interventional cardiology")
specialty = get_speciality_info("neuro-oncology")
```

---

## Surgical Procedures

Comprehensive information about surgical techniques, instruments, and procedures.

### Features
- Procedure indications
- Surgical technique descriptions
- Pre-operative preparation
- Surgical instruments used
- Post-operative care
- Complications and risks
- Recovery timeline

### Usage

#### Programmatic
```python
from medkit.medical.surgery_info import get_surgery_info

# Get surgical procedure information
surgery = get_surgery_info("coronary artery bypass")
print(surgery.indication)
print(surgery.technique)
```

#### Command-Line (Available via CLI)
```bash
# Currently available through Python API
python -c "from medkit.medical.surgery_info import get_surgery_info; print(get_surgery_info('bypass surgery'))"
```

### Common Procedures
- **Cardiovascular**: CABG, angioplasty, valve replacement
- **Orthopedic**: Joint replacement, arthroscopy, fusion
- **General**: Appendectomy, cholecystectomy, hernia repair
- **Neurosurgery**: Craniotomy, tumor resection
- **Vascular**: Aneurysm repair, bypass grafts
- **Thoracic**: Lung resection, pleurectomy
- **Urologic**: Prostatectomy, nephrectomy
- **Gynecologic**: Hysterectomy, cesarean section

### Examples

```python
# Cardiac surgeries
surgery = get_surgery_info("coronary artery bypass grafting")
surgery = get_surgery_info("valve replacement")

# Orthopedic surgeries
surgery = get_surgery_info("total knee replacement")
surgery = get_surgery_info("spinal fusion")

# General surgeries
surgery = get_surgery_info("appendectomy")
surgery = get_surgery_info("cholecystectomy")
```

---

## Medical Implants

Information about medical devices, implants, and prosthetics used in patient care.

### Features
- Implant descriptions and purposes
- Indications for use
- Materials and composition
- Installation/surgical procedure
- Maintenance and care
- Complications and considerations
- Longevity and replacement timeline

### Usage

#### Programmatic
```python
from medkit.medical.medical_implant import get_implant_info

# Get implant information
implant = get_implant_info("cardiac pacemaker")
print(implant.purpose)
print(implant.indications)
```

### Types of Implants
- **Cardiac**: Pacemakers, defibrillators, stents, artificial hearts
- **Orthopedic**: Joint replacements, plates, screws, rods
- **Neurological**: Deep brain stimulators, spinal cord stimulators
- **Ophthalmic**: Intraocular lenses, corneal implants
- **Otologic**: Cochlear implants, bone-conduction devices
- **Vascular**: Stents, grafts, filters
- **Dental**: Implants, bridges, dentures
- **Urologic**: Artificial sphincters, penile implants

### Examples

```python
# Cardiac implants
implant = get_implant_info("pacemaker")
implant = get_implant_info("coronary stent")

# Orthopedic implants
implant = get_implant_info("hip replacement")
implant = get_implant_info("knee replacement")

# Sensory implants
implant = get_implant_info("cochlear implant")
implant = get_implant_info("intraocular lens")
```

---

## Herbal Medicine

Evidence-based information about herbal remedies, traditional medicine, and botanical treatments.

### Features
- Herbal remedy descriptions
- Traditional and scientific uses
- Active compounds and mechanisms
- Dosage and administration
- Safety profile and contraindications
- Drug-herb interactions
- Efficacy evidence

### Usage

#### Programmatic
```python
from medkit.medical.herbal_info import get_herbal_information

# Get herbal medicine information
herb = get_herbal_information("turmeric")
print(herb.traditional_uses)
print(herb.safety)
```

#### Command-Line
```bash
python cli/cli_herbal_info.py turmeric
python cli/cli_herbal_info.py ginger --benefits --interactions
```

### Covered Herbs
- **Anti-inflammatory**: Turmeric, ginger, boswellia
- **Immune Support**: Echinacea, elderberry, astragalus
- **Digestive**: Peppermint, ginger, fennel
- **Sleep & Relaxation**: Valerian, chamomile, passionflower
- **Cardiovascular**: Hawthorn, garlic, ginkgo
- **Pain Relief**: Willow bark, capsaicin, feverfew
- **Respiratory**: Eucalyptus, thyme, licorice
- **Metabolic**: Green tea, cinnamon, fenugreek

### ⚠️ Important Safety Notes

**Before using herbal remedies:**
- Consult with healthcare provider
- Discuss with pharmacist about drug interactions
- Verify safe dosing
- Check contraindications
- Monitor for adverse effects

**Special precautions for:**
- Pregnancy and breastfeeding
- Children and elderly patients
- Immunocompromised individuals
- Patients on medications
- Those with allergies or sensitivities

### Examples

```python
# Anti-inflammatory herbs
herb = get_herbal_information("turmeric")
herb = get_herbal_information("ginger")

# Immune support
herb = get_herbal_information("echinacea")
herb = get_herbal_information("elderberry")

# Digestive aids
herb = get_herbal_information("peppermint")
herb = get_herbal_information("ginger")
```

---

## General Usage Notes

### Error Handling
All functions include error handling for invalid inputs:

```python
try:
    info = get_disease_info("unknown_disease_12345")
except ValueError as e:
    print(f"Error: {e}")
```

### Caching
Results are cached locally for better performance:

```python
from medkit.utils.lmdb_storage import get_cached_result

# Check cache first
cached = get_cached_result("disease:diabetes")
```

### Privacy
All functions respect privacy and HIPAA guidelines:

```python
from medkit.utils.privacy_compliance import anonymize_data

# Use when handling patient data
anonymized = anonymize_data(patient_info)
```

---

## Related Documentation

- [Drug Database Documentation](DRUG_DATABASE.md)
- [Diagnostic Tools Documentation](DIAGNOSTIC_TOOLS.md)
- [Mental Health Documentation](MENTAL_HEALTH.md)
- [CLI Tools Documentation](../cli/README.md)
- [API Reference](api/modules.rst)

---

## Disclaimer

This software is for **informational purposes only** and should not replace professional medical advice. Always consult with qualified healthcare providers for medical decisions, diagnoses, and treatment plans.
