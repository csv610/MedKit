# MedKit Testing Guide

## Overview

This document describes the proper testing approach for the MedKit project. The previous test suite was 91.8% dummy tests that provided zero validation. This guide provides the framework for creating real, meaningful tests.

## Current Status

### What Was Fixed
- ✅ Created proper unit tests for `disease_info` module (28 test cases, 100+ assertions)
- ✅ Created proper unit tests for `drug_drug_interaction` module (20+ test cases, 60+ assertions)
- ✅ Replaced 2 dummy test files with comprehensive test suites

### What Still Needs to be Done
- Replace 56 remaining dummy test files with proper tests
- Add tests for all 19 CLI tools
- Add mocking for Gemini API calls
- Add integration tests

## Test Structure

### Example: Proper Test vs. Dummy Test

**DUMMY TEST (Do NOT Write Like This):**
```python
import unittest

class TestSomething(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)  # MEANINGLESS!
```

**PROPER TEST (Write Like This):**
```python
import unittest
from pydantic import ValidationError
from medkit.medical.disease_info import DiseaseIdentity

class TestDiseaseIdentity(unittest.TestCase):
    """Test DiseaseIdentity data model."""

    def test_disease_identity_creation(self):
        """Test creating disease identity with valid data."""
        di = DiseaseIdentity(
            disease_name="Hypertension",
            alternative_names=["High blood pressure"],
            icd10_codes=["I10"],
            disease_category="Cardiovascular"
        )
        self.assertEqual(di.disease_name, "Hypertension")
        self.assertIn("I10", di.icd10_codes)

    def test_disease_identity_missing_required_field(self):
        """Test that missing required fields raise ValidationError."""
        with self.assertRaises(ValidationError):
            DiseaseIdentity(
                disease_name="Test",
                icd10_codes=["I10"]
                # Missing alternative_names and disease_category
            )
```

## Testing Patterns

### 1. Model Validation Tests

Test Pydantic models with valid and invalid data:

```python
class TestModelName(unittest.TestCase):

    def test_valid_creation(self):
        """Test creating model with valid data."""
        obj = Model(field1="value1", field2="value2")
        self.assertEqual(obj.field1, "value1")

    def test_missing_required_field(self):
        """Test that missing required fields raise ValidationError."""
        with self.assertRaises(ValidationError):
            Model(field1="value1")  # Missing field2

    def test_invalid_field_type(self):
        """Test that invalid field types are rejected."""
        with self.assertRaises(ValidationError):
            Model(field1=123, field2=[1, 2, 3])  # Wrong types
```

### 2. Data Serialization Tests

```python
class TestSerialization(unittest.TestCase):

    def test_dict_serialization(self):
        """Test converting model to dictionary."""
        obj = Model(field1="value")
        data = obj.dict()
        self.assertIn("field1", data)
        self.assertEqual(data["field1"], "value")

    def test_json_serialization(self):
        """Test converting model to JSON."""
        obj = Model(field1="value")
        json_str = obj.json()
        self.assertIn("value", json_str)
```

### 3. Realistic Scenario Tests

```python
class TestRealisticScenario(unittest.TestCase):
    """Test realistic use cases."""

    def test_hypertension_disease_model(self):
        """Test complete hypertension disease model."""
        disease = DiseaseInfo(
            identity=DiseaseIdentity(
                disease_name="Essential Hypertension",
                alternative_names=["Primary hypertension"],
                icd10_codes=["I10"],
                disease_category="Cardiovascular"
            ),
            # ... rest of model
        )

        # Verify key information is present
        self.assertEqual(disease.identity.disease_name, "Essential Hypertension")
        self.assertGreater(len(disease.management.medication_classes), 0)
        self.assertIn("Stroke", disease.living_with.complications)
```

### 4. Integration Tests

```python
class TestIntegration(unittest.TestCase):
    """Test system-wide functionality."""

    def test_multiple_interactions_workflow(self):
        """Test checking multiple drug interactions."""
        interactions = [
            create_interaction("Warfarin", "Aspirin", "High"),
            create_interaction("Metformin", "Alcohol", "Moderate"),
        ]

        high_severity = [i for i in interactions if i.severity == "High"]
        self.assertEqual(len(high_severity), 1)
```

## Test Naming Conventions

### Test File Names
- `test_medical_disease_info.py` - Test for `disease_info.py`
- `test_drug_drug_drug_interaction.py` - Test for `drug_drug_interaction.py`
- Pattern: `test_<module_path_with_underscores>.py`

### Test Class Names
- `TestDiseaseIdentity` - Test for `DiseaseIdentity` class
- `TestDiseaseInfoIntegration` - Integration tests
- Pattern: `Test<ClassName>` or `Test<Functionality>Integration`

### Test Method Names
```python
# Good test names
def test_disease_identity_creation(self):
def test_disease_identity_missing_required_field(self):
def test_hypertension_disease_model(self):

# Bad test names (avoid these)
def test_1(self):
def test_model(self):
def test_stuff(self):
```

## Priority Modules for Testing

### High Priority (Most Used)
1. `disease_info.py` - ✅ DONE
2. `drug_drug_interaction.py` - ✅ DONE
3. `drug_disease_interaction.py` - Core drug interactions
4. `drug_food_interaction.py` - Core drug interactions
5. `medical_topic.py` - Core medical documentation
6. `medical_physical_exams_questions.py` - Medical assessment
7. `medical_term_extractor.py` - NLP functionality

### Medium Priority
8. `medical_test_info.py` - Test information
9. `medical_test_devices.py` - Device information
10. `surgery_info.py` - Surgical procedures
11. `surgical_tool_info.py` - Surgical tools
12. All CLI tools (19 total)

### Lower Priority (Specialized)
- `herbal_info.py`
- `medical_anatomy.py`
- `medical_dictionary.py`
- `medical_facts_checker.py`

## Mocking Strategy

For modules that call the Gemini API, use mocking:

```python
from unittest.mock import patch, MagicMock
from medkit.medical.disease_info import DiseaseInfoGenerator

class TestDiseaseInfoGenerator(unittest.TestCase):

    @patch('medkit.medical.disease_info.MedKitClient')
    def test_generate_calls_api(self, mock_client):
        """Test that generator calls Gemini API."""
        mock_client.return_value.generate.return_value = {
            "identity": {...},
            "background": {...}
        }

        generator = DiseaseInfoGenerator()
        result = generator.generate("diabetes")

        # Verify API was called
        mock_client.return_value.generate.assert_called_once()
        self.assertIsNotNone(result)
```

## Running Tests

### Run All Tests
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### Run Specific Test File
```bash
python3 -m unittest tests.test_medical_disease_info -v
```

### Run Specific Test Class
```bash
python3 -m unittest tests.test_medical_disease_info.TestDiseaseIdentity -v
```

### Run Specific Test Method
```bash
python3 -m unittest tests.test_medical_disease_info.TestDiseaseIdentity.test_disease_identity_creation -v
```

### With Coverage
```bash
python3 -m coverage run -m unittest discover -s tests -p "test_*.py"
python3 -m coverage report -m
```

## Test Metrics

### Current Status
- **Total test files:** 61
- **Proper test files:** 2 (3.3%)
- **Dummy test files:** 59 (96.7%)
- **Total assertions in proper tests:** 100+

### Target Goals
- **Proper test files:** 35+ (by end of implementation)
- **Dummy test files:** 0 (replace all)
- **Average assertions per test class:** 5-10
- **Code coverage:** >80% for core modules

## Example: Complete Test File

See `tests/test_medical_disease_info.py` for a complete example with:
- 14+ test classes
- 40+ test methods
- 100+ assertions
- Realistic medical data
- Integration tests
- Proper documentation

## Best Practices

### DO:
✅ Test both valid and invalid inputs
✅ Use descriptive test names with docstrings
✅ Test boundary conditions and edge cases
✅ Test error handling and exceptions
✅ Use setUp() for common test data
✅ Test serialization/deserialization
✅ Test model validation (Pydantic models)
✅ Group related tests in classes
✅ Run tests frequently during development

### DON'T:
❌ Write `self.assertEqual(True, True)` dummy tests
❌ Test implementation details, test behavior
❌ Make tests dependent on external services
❌ Use hardcoded paths in tests
❌ Create massive test methods (keep under 20 lines)
❌ Skip error cases
❌ Leave tests in "pending" state
❌ Test multiple concerns in one test

## Template for New Tests

```python
"""
Proper unit tests for [MODULE_NAME].

Tests cover:
- [What is being tested]
- [What is being validated]
- [Special scenarios]
"""

import unittest
from pydantic import ValidationError
from medkit.[PATH].module_name import Class1, Class2

# ==================== Class1 Tests ====================

class TestClass1(unittest.TestCase):
    """Test Class1 data model."""

    def test_class1_creation(self):
        """Test creating Class1 with valid data."""
        obj = Class1(field1="value1", field2="value2")
        self.assertEqual(obj.field1, "value1")

    def test_class1_missing_field(self):
        """Test Class1 with missing required field."""
        with self.assertRaises(ValidationError):
            Class1(field1="value1")

    def test_class1_serialization(self):
        """Test Class1 serialization."""
        obj = Class1(field1="value1", field2="value2")
        data = obj.dict()
        self.assertIn("field1", data)

# ==================== Integration Tests ====================

class TestIntegration(unittest.TestCase):
    """Integration tests for module."""

    def test_realistic_scenario(self):
        """Test realistic use case."""
        obj1 = Class1(...)
        obj2 = Class2(...)
        # Test interaction between objects
        self.assertTrue(...)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Maintenance

### Keep Tests Updated
- Update tests when API changes
- Update tests when models change
- Keep tests in sync with code
- Review and refactor tests regularly

### Monitor Test Health
- Run tests regularly (on every commit)
- Track coverage trends
- Fix failing tests immediately
- Remove obsolete tests

## Resources

- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Pydantic testing docs](https://docs.pydantic.dev/latest/)
- [unittest.mock documentation](https://docs.python.org/3/library/unittest.mock.html)

## Questions?

Refer to these proper test examples:
- `tests/test_medical_disease_info.py` - Comprehensive example
- `tests/test_drug_drug_drug_interaction.py` - Interaction testing
- `tests/test_mental_health.py` - Existing comprehensive example
