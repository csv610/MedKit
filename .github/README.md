# MedKit

A comprehensive medical knowledge system powered by Google's Gemini AI, providing programmatic access to authoritative medical information.

## What is MedKit?

MedKit gives developers and healthcare professionals instant access to medical knowledge through a Python API. Query disease information, drug interactions, diagnostic procedures, physical examination guides, and mental health assessments—all from a single integrated system.

## Key Features

**Medical Reference** — Disease information, anatomy, surgical procedures, implants, and herbal medicine

**Drug Database** — Medicine information, drug interactions, dosing, side effects, and alternatives

**Diagnostic Tools** — Medical tests, examination guides for 27+ body systems, symptom analysis, and clinical decision support

**Mental Health** — Psychological assessments, structured interviews, conversational support, and crisis resources

**Offline Access** — LMDB-based caching for offline data access and improved performance

## Quick Start

### Installation

```bash
pip install git+https://github.com/csv610/medkit.git
```

### Basic Usage

```python
from medkit.medical.disease_info import get_disease_info
from medkit.drug.medicine_info import get_medicine_info
from medkit.drug.drug_drug_interaction import get_drug_interaction

# Get disease information
disease = get_disease_info("diabetes")
print(disease.definition, disease.symptoms, disease.treatment)

# Get medicine information
medicine = get_medicine_info("aspirin")
print(medicine.dosage, medicine.side_effects)

# Check drug interactions
interaction = get_drug_interaction("aspirin", "ibuprofen")
print(interaction.severity, interaction.description)
```

### Command-Line Usage

```bash
python cli/cli_disease_info.py diabetes
python cli/cli_medicine_info.py aspirin
python cli/cli_medical_anatomy.py heart
```

See [cli/README.md](cli/README.md) for more examples.

## System Requirements

- Python 3.8+
- Google Gemini API key (get from https://ai.google.dev/)
- 512MB RAM minimum (1GB recommended)
- 500MB+ disk space for caching
- Internet connection for initial use (caching enables offline access)

## Configuration

Set your API key:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or configure programmatically:

```python
from medkit.core.config import MedKitConfig

config = MedKitConfig(
    api_key="your-api-key",
    model="gemini-2.5-flash",
    temperature=0.3,
    db_store=True,
    db_path="~/.medkit/cache",
    verbosity="info"
)
```

## Project Structure

```
medkit/
├── core/              # Configuration and API client
├── medical/           # Disease, anatomy, specialties, procedures
├── drug/              # Medicine info, interactions, comparisons
├── diagnostics/       # Medical tests and diagnostic devices
├── mental_health/     # Assessments, chat, interviews
├── phyexams/          # Physical examination guides (27+ systems)
├── medgraphs/         # Knowledge graph relationships
├── utils/             # Caching, privacy, logging
├── vistools/          # Visualization tools
└── cli/               # Command-line interfaces
```

## Component Overview

### Core Module (`medkit/core/`)

Foundation layer providing API clients and configuration management.

**Key Components:**
- **`medkit_client.py`** - Extended Gemini client optimized for medical content with schema-aware prompt generation, automatic retry logic, and multimodal support
- **`gemini_client.py`** - Base client for Google Gemini API with structured output support and session management
- **`config.py`** - Centralized configuration for MedKit, logging, and HIPAA-aligned privacy settings

**Usage:**
```python
from medkit.core.config import MedKitConfig

config = MedKitConfig(
    api_key="your-api-key",
    model="gemini-2.5-flash",
    temperature=0.3,
    db_store=True
)
```

### Medical Module (`medkit/medical/`)

Comprehensive medical reference information with 22+ sub-modules covering diseases, anatomy, procedures, and clinical tools.

**Sub-modules by Category:**

**Disease & Condition Information:**
- `disease_info.py` - Complete disease documentation (epidemiology, clinical presentation, diagnosis, management)
- `medical_topic.py` - Medical topics with auto-generated FAQs and patient education
- `medical_facts_checker.py` - Fact vs. fiction analysis with confidence scoring
- `medical_dictionary.py` - Medical term definitions and clinical context

**Anatomical & Procedural:**
- `medical_anatomy.py` - Detailed anatomical documentation (12+ sections including imaging)
- `medical_procedure_info.py` - Non-surgical procedures (indications, preparation, recovery)
- `surgery_info.py` - Comprehensive surgical procedure documentation (14+ sections)
- `surgical_tool_info.py` - Medical and surgical instrument information
- `medical_implant.py` - Medical implant specifications and alternatives

**Clinical Tools:**
- `medical_speciality.py` - Medical specialty database and lookup
- `herbal_info.py` - Herbal remedy documentation (14+ areas)
- `medical_decision_guide.py` - AI-generated clinical decision trees for symptom assessment
- `prescription_extractor.py` - Extract prescription data from images
- `patient_medical_history.py` - Patient health record management
- `synthetic_case_report.py` - Educational case generation

**Usage:**
```python
from medkit.medical.disease_info import get_disease_info
from medkit.medical.medical_anatomy import get_anatomy_info
from medkit.medical.surgery_info import get_surgery_info

# Get comprehensive disease information
disease = get_disease_info("diabetes")
print(disease.definition, disease.symptoms, disease.treatment)

# Get anatomical information
anatomy = get_anatomy_info("heart")
print(anatomy.gross_morphology, anatomy.clinical_significance)

# Get surgical procedure information
surgery = get_surgery_info("appendectomy")
print(surgery.indications, surgery.operative_steps)
```

### Drug Module (`medkit/drug/`)

Pharmaceutical database with drug interactions, comparisons, and RxNorm integration.

**Sub-modules:**
- `medicine_info.py` - Comprehensive drug documentation (classification, dosage, adverse effects, contraindications)
- `drug_drug_interaction.py` - Drug-drug interaction analysis with severity levels (MINOR to CONTRAINDICATED)
- `drug_food_interaction.py` - Medication-food interaction analysis with clinical guidance
- `drug_disease_interaction.py` - Drug-disease (comorbidity) interaction analysis
- `drugs_comparison.py` - Side-by-side medication comparison
- `similar_drugs.py` - Find therapeutic alternatives and substitutes
- `rxnorm_client.py` - RxNorm API integration for drug standardization
- `rxclass_examples.py` - Drug classification examples and related drugs

**Usage:**
```python
from medkit.drug.medicine_info import get_medicine_info
from medkit.drug.drug_drug_interaction import get_drug_interaction
from medkit.drug.drug_food_interaction import get_food_interaction

# Get medicine information
medicine = get_medicine_info("metformin")
print(medicine.dosage, medicine.side_effects)

# Check drug interactions
interaction = get_drug_interaction("aspirin", "ibuprofen")
print(interaction.severity, interaction.clinical_effects)

# Check food interactions
food_int = get_food_interaction("warfarin", "leafy greens")
print(food_int.severity, food_int.guidance)
```

### Diagnostics Module (`medkit/diagnostics/`)

Medical tests, diagnostic devices, and clinical decision support.

**Sub-modules:**
- `medical_test_info.py` - Comprehensive test documentation (indications, preparation, results interpretation, cost)
- `medical_test_devices.py` - Diagnostic device information and specifications
- `medical_tests_graph.py` - Knowledge graph mapping test relationships and clinical ordering logic

**Usage:**
```python
from medkit.diagnostics.medical_test_info import get_medical_test_info

test = get_medical_test_info("complete blood count")
print(test.purpose, test.normal_values, test.interpretation)
```

### Mental Health Module (`medkit/mental_health/`)

Mental health assessments, structured interviews, and conversational support with HIPAA compliance and crisis detection.

**Sub-modules:**
- `mental_health_assessment.py` - PHQ-9 and GAD-7 screening, risk assessment, DSM-5 diagnostic models
- `sane_interview.py` - Sexual Assault Nurse Examiner (SANE) trauma-informed interview system
- `llm_sane_interview.py` - AI-assisted SANE interview with adaptive questioning
- `mental_health_chat.py` - Conversational assessment engine with real-time red flag detection
- `sympton_detection_chat.py` - Symptom analysis chatbot
- `mental_health_chat_app.py` - Full-featured mental health chat application
- `mental_health_report.py` - Assessment report generation
- `models.py` - HIPAA-compliant session management and audit logging

**Features:**
- PHQ-9/GAD-7 screening scales with severity classification
- Suicidal ideation and self-harm detection
- Session persistence and privacy compliance
- Audit logging of all access and modifications
- Emergency crisis resource information

**Usage:**
```python
from medkit.mental_health.mental_health_chat import MentalHealthChat

chat = MentalHealthChat()
response = chat.assess("I've been feeling sad for weeks")
print(response.assessment, response.crisis_resources)
```

### Physical Exams Module (`medkit/phyexams/`)

Comprehensive physical examination guides covering 27+ body systems with structured assessment protocols.

**Examination Categories:**

**Cardiovascular & Respiratory:**
- `exam_heart.py` - Cardiac examination (vitals, auscultation, peripheral findings)
- `exam_lungs_chest.py` - Pulmonary examination (breath sounds, adventitious sounds)
- `exam_blood_vessels.py` - Vascular examination (pulses, arterial assessment)

**Head & Neck:**
- `exam_ears_nose_throat.py` - ENT examination
- `exam_head_and_neck.py` - Head/neck examination with cranial nerve testing
- `exam_lymphatic_system.py` - Lymph node examination

**Abdominal & Genital:**
- `exam_breast_axillae.py` - Breast and axillary examination
- `exam_female_genitalia.py` - Female genital examination
- `exam_male_genitalia.py` - Male genital examination
- `exam_anal_rectum_prostate.py` - Rectal and prostatic examination

**Musculoskeletal & Neurological:**
- `exam_musculoskeletal.py` - General musculoskeletal assessment
- `exam_musculoskeletal_core.py` - Core stability evaluation
- `exam_neurology_system.py` - Comprehensive neurological exam (cranial nerves, motor/sensory, reflexes)

**Cognitive & Mental Status:**
- `exam_memory_ability.py` - Memory and cognitive assessment
- `exam_abstract_reasoning.py` - Abstract reasoning evaluation
- `exam_attention_span.py` - Attention and concentration
- `exam_arithmetic_calculation.py` - Arithmetic ability
- `exam_writing_ability.py` - Writing assessment
- `exam_judgement.py` - Executive function evaluation

**Nutritional & Dermatological:**
- `exam_nutrition_growth.py` - Nutrition and growth measurement
- `exam_skin_hair_nails.py` - Dermatological examination
- `exam_depression_screening.py` - Depression screening
- `exam_emotional_stability.py` - Emotional stability evaluation

**Key Features:**
- LLM-generated assessments with confidence scoring
- Follow-up question generation
- Triage urgency levels (normal, monitor, urgent, emergency)
- Multimodal support (text, images, videos)

**Usage:**
```python
from medkit.phyexams.exam_heart import get_cardiac_exam

exam = get_cardiac_exam(patient_data)
print(exam.findings, exam.assessment, exam.urgency_level)
```

### Medical Graphs Module (`medkit/medgraphs/`)

Knowledge graphs representing relationships between medical concepts.

**Graph Types:**
- `disease_graph.py` - Disease-symptom-cause relationships
- `anatomy_graph.py` - Anatomical structure relationships
- `medicine_graph.py` - Drug relationships
- `pathophysiology_graph.py` - Disease mechanism relationships
- `genetic_graph.py` - Hereditary relationships
- `procedure_graph.py` - Procedural relationships
- `surgery_graph.py` - Surgical approach graphs
- `sympton_graph.py` - Symptom manifestation relationships

**Features:**
- NetworkX-based graph structures
- Visual export (DOT, Mermaid formats)
- Query and traversal capabilities
- Relationship mapping between medical concepts

**Usage:**
```python
from medkit.medgraphs.disease_graph import DiseaseGraph

graph = DiseaseGraph()
symptoms = graph.get_symptoms("hypertension")
complications = graph.get_complications("diabetes")
```

### Utils Module (`medkit/utils/`)

Infrastructure and cross-cutting concerns.

**Key Components:**
- `lmdb_storage.py` - LMDB key-value storage with automatic compression
- `pydantic_prompt_generator.py` - Schema-aware prompt generation (DETAILED, CONCISE, TECHNICAL styles)
- `privacy_compliance.py` - HIPAA compliance manager with audit logging
- `logging_config.py` - Centralized logging configuration
- `storage_config.py` - Configuration management with per-module database paths

**Usage:**
```python
from medkit.utils.privacy_compliance import PrivacyManager

privacy = PrivacyManager()
session = privacy.create_session("user_id")
privacy.log_access("user_id", "disease_info", "diabetes")
```

### Visualization Module (`medkit/vistools/`)

Visual representation of medical data.

**Components:**
- `visualize_decision_guide.py` - Render clinical decision trees as DOT/Mermaid diagrams

**Usage:**
```python
from medkit.vistools.visualize_decision_guide import visualize_decision_tree

diagram = visualize_decision_tree(decision_tree_json)
print(diagram)  # Mermaid or Graphviz format
```

### CLI Module (`cli/`)

Command-line interfaces for all major functionality.

**20 CLI Scripts:**
- `cli_disease_info.py` - Disease lookup
- `cli_medicine_info.py` - Medicine information
- `cli_drug_interaction.py` - Drug interactions
- `cli_medical_anatomy.py` - Anatomical information
- `cli_surgery_info.py` - Surgery procedures
- `cli_medical_test.py` - Medical tests
- `cli_mental_health.py` - Mental health assessments
- `cli_physical_exams.py` - Physical examination guides
- And more... see [cli/README.md](cli/README.md)

**Usage:**
```bash
python cli/cli_disease_info.py diabetes
python cli/cli_medicine_info.py aspirin --verbose
python cli/cli_drug_interaction.py aspirin ibuprofen
python cli/cli_physical_exams.py heart
```

## Documentation

| Section | Location |
|---------|----------|
| Medical Reference | [docs/medical_ai/](docs/medical_ai/) |
| Drug Database | [docs/drug_ai/](docs/drug_ai/) |
| Diagnostic Tools | [docs/diagnostic_ai/](docs/diagnostic_ai/) |
| Mental Health | [docs/psychology_ai/](docs/psychology_ai/) |
| CLI Tools | [cli/README.md](cli/README.md) |
| Full Docs | https://medkit.readthedocs.io |

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=medkit

# Using make
make test
make test-cov
make test-parallel
```

## Development

### Setup

```bash
git clone https://github.com/csv610/medkit.git
cd medkit
pip install -e ".[dev]"
```

### Common Tasks

```bash
make lint              # Code quality checks
make format            # Format code
make typecheck         # Type checking
make security          # Security scan
make docs              # Build documentation
make ready             # Full CI checks
```

## Important Disclaimers

**Medical Disclaimer:** This tool is for informational purposes only and should not replace professional medical advice. Always consult qualified healthcare professionals.

**Accuracy:** Medical information evolves constantly. Verify all information with current medical literature before use.

**Privacy:** Users are responsible for HIPAA compliance and data protection. MedKit provides privacy-aware features but does not guarantee compliance.

**Emergency:** For medical emergencies, contact emergency services immediately. Do not use this tool for emergency diagnosis.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Citation

```bibtex
@software{medkit2024,
  title={MedKit: Medical Information and Reference System},
  author={Your Name},
  year={2024},
  url={https://github.com/csv610/medkit}
}
```

## Support

- **Documentation:** https://medkit.readthedocs.io
- **Issues:** https://github.com/csv610/medkit/issues
- **Discussions:** https://github.com/csv610/medkit/discussions

## Acknowledgments

- Google Gemini AI (https://ai.google.dev/)
- RxNorm API (https://www.nlm.nih.gov/research/umls/rxnorm/)
- Pydantic, LMDB, NetworkX, Matplotlib, Sphinx

---

**Last Updated:** December 2024

For the latest information, visit: https://github.com/csv610/medkit
