# MedKit CLI Tools

This directory contains command-line interfaces for querying MedKit medical information modules.

## Available CLI Tools

### Disease Information
```bash
python cli/cli_disease_info.py <disease_name> [--verbose]
```
Get comprehensive information about a disease.

**Example:**
```bash
python cli/cli_disease_info.py diabetes
python cli/cli_disease_info.py "heart disease" --verbose
```

### Medicine/Drug Information
```bash
python cli/cli_medicine_info.py <drug_name> [--interactions] [--verbose]
```
Get information about medications and drugs, including interaction data.

**Example:**
```bash
python cli/cli_medicine_info.py aspirin
python cli/cli_medicine_info.py ibuprofen --interactions
```

### Medical Anatomy
```bash
python cli/cli_medical_anatomy.py <body_part> [--functions] [--verbose]
```
Get anatomical information about body parts.

**Example:**
```bash
python cli/cli_medical_anatomy.py heart
python cli/cli_medical_anatomy.py brain --functions
```

## Setup

Install MedKit with development dependencies:
```bash
pip install -e ".[dev]"
```

Or install CLI requirements directly:
```bash
pip install -r requirements.txt
```

## Using from Command Line

After installation, you can run CLI scripts from any directory:

```bash
cd /path/to/medkit
python cli/cli_disease_info.py diabetes
```

Or make scripts executable:
```bash
chmod +x cli/cli_*.py
./cli/cli_disease_info.py diabetes
```

## Adding New CLI Tools

To add a new CLI tool:

1. Create a new file `cli/cli_<module_name>.py`
2. Import the relevant medkit function
3. Use argparse for argument handling
4. Add usage examples in this README

## Integration with Entry Points

These CLI tools are also accessible via the main package entry point:
```bash
pip install -e .
medkit --help
```
