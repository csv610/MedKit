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
├── utils/             # Caching, privacy, logging
└── vistools/          # Visualization tools
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
