#!/usr/bin/env python3
"""
test_refactored_configs.py - Test script for refactored drug analysis modules.

Tests that all config classes only contain static settings and user parameters
are properly passed to method calls.
"""

import sys
from pathlib import Path

# Test imports
print("=" * 80)
print("TESTING IMPORTS")
print("=" * 80)

try:
    from drug_disease_interaction import DrugDiseaseInteractionConfig, DrugDiseaseInteraction
    print("✓ drug_disease_interaction imported successfully")
except Exception as e:
    print(f"✗ Failed to import drug_disease_interaction: {e}")
    sys.exit(1)

try:
    from similar_drugs import SimilarDrugsConfig, SimilarDrugs
    print("✓ similar_drugs imported successfully")
except Exception as e:
    print(f"✗ Failed to import similar_drugs: {e}")
    sys.exit(1)

try:
    from medicine_info import MedicineInfoConfig, MedicineInfoGenerator
    print("✓ medicine_info imported successfully")
except Exception as e:
    print(f"✗ Failed to import medicine_info: {e}")
    sys.exit(1)

try:
    from drugs_comparison import DrugsComparisonConfig, DrugsComparison
    print("✓ drugs_comparison imported successfully")
except Exception as e:
    print(f"✗ Failed to import drugs_comparison: {e}")
    sys.exit(1)

try:
    from drug_food_interaction import DrugFoodInteractionConfig, DrugFoodInteraction
    print("✓ drug_food_interaction imported successfully")
except Exception as e:
    print(f"✗ Failed to import drug_food_interaction: {e}")
    sys.exit(1)

try:
    from drug_drug_interaction import DrugDrugInteractionConfig, DrugDrugInteraction
    print("✓ drug_drug_interaction imported successfully")
except Exception as e:
    print(f"✗ Failed to import drug_drug_interaction: {e}")
    sys.exit(1)

# Test config instantiation
print("\n" + "=" * 80)
print("TESTING CONFIG INSTANTIATION")
print("=" * 80)

# Test DrugDiseaseInteractionConfig
try:
    config = DrugDiseaseInteractionConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ DrugDiseaseInteractionConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine_name'), "medicine_name should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ DrugDiseaseInteractionConfig test failed: {e}")
    sys.exit(1)

# Test SimilarDrugsConfig
try:
    config = SimilarDrugsConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ SimilarDrugsConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine_name'), "medicine_name should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ SimilarDrugsConfig test failed: {e}")
    sys.exit(1)

# Test MedicineInfoConfig
try:
    config = MedicineInfoConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ MedicineInfoConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine_name'), "medicine_name should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ MedicineInfoConfig test failed: {e}")
    sys.exit(1)

# Test DrugsComparisonConfig
try:
    config = DrugsComparisonConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ DrugsComparisonConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine1'), "medicine1 should not be in config"
    assert not hasattr(config, 'medicine2'), "medicine2 should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ DrugsComparisonConfig test failed: {e}")
    sys.exit(1)

# Test DrugFoodInteractionConfig
try:
    config = DrugFoodInteractionConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ DrugFoodInteractionConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine_name'), "medicine_name should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ DrugFoodInteractionConfig test failed: {e}")
    sys.exit(1)

# Test DrugDrugInteractionConfig
try:
    config = DrugDrugInteractionConfig(
        output_path=None,
        verbosity=False,
    )
    print("✓ DrugDrugInteractionConfig created successfully")
    assert hasattr(config, 'output_path'), "Missing output_path field"
    assert hasattr(config, 'verbosity'), "Missing verbosity field"
    assert hasattr(config, 'prompt_style'), "Missing prompt_style field"
    assert not hasattr(config, 'medicine1'), "medicine1 should not be in config"
    assert not hasattr(config, 'medicine2'), "medicine2 should not be in config"
    print("  - Config has correct fields only")
except Exception as e:
    print(f"✗ DrugDrugInteractionConfig test failed: {e}")
    sys.exit(1)

# Test analyzer instantiation with config
print("\n" + "=" * 80)
print("TESTING ANALYZER INSTANTIATION")
print("=" * 80)

# Test DrugDiseaseInteraction
try:
    config = DrugDiseaseInteractionConfig()
    analyzer = DrugDiseaseInteraction(config)
    print("✓ DrugDiseaseInteraction analyzer created successfully")
except Exception as e:
    print(f"✗ DrugDiseaseInteraction analyzer creation failed: {e}")
    sys.exit(1)

# Test SimilarDrugs
try:
    config = SimilarDrugsConfig()
    analyzer = SimilarDrugs(config)
    print("✓ SimilarDrugs analyzer created successfully")
except Exception as e:
    print(f"✗ SimilarDrugs analyzer creation failed: {e}")
    sys.exit(1)

# Test MedicineInfoGenerator
try:
    config = MedicineInfoConfig()
    generator = MedicineInfoGenerator(config)
    print("✓ MedicineInfoGenerator created successfully")
except Exception as e:
    print(f"✗ MedicineInfoGenerator creation failed: {e}")
    sys.exit(1)

# Test DrugsComparison
try:
    config = DrugsComparisonConfig()
    analyzer = DrugsComparison(config)
    print("✓ DrugsComparison analyzer created successfully")
except Exception as e:
    print(f"✗ DrugsComparison analyzer creation failed: {e}")
    sys.exit(1)

# Test DrugFoodInteraction
try:
    config = DrugFoodInteractionConfig()
    analyzer = DrugFoodInteraction(config)
    print("✓ DrugFoodInteraction analyzer created successfully")
except Exception as e:
    print(f"✗ DrugFoodInteraction analyzer creation failed: {e}")
    sys.exit(1)

# Test DrugDrugInteraction
try:
    config = DrugDrugInteractionConfig()
    analyzer = DrugDrugInteraction(config)
    print("✓ DrugDrugInteraction analyzer created successfully")
except Exception as e:
    print(f"✗ DrugDrugInteraction analyzer creation failed: {e}")
    sys.exit(1)

# Test method signatures
print("\n" + "=" * 80)
print("TESTING METHOD SIGNATURES")
print("=" * 80)

import inspect

# Check DrugDiseaseInteraction.analyze signature
try:
    config = DrugDiseaseInteractionConfig()
    analyzer = DrugDiseaseInteraction(config)
    sig = inspect.signature(analyzer.analyze)
    params = list(sig.parameters.keys())
    assert 'medicine_name' in params, "medicine_name should be in analyze() signature"
    assert 'condition_name' in params, "condition_name should be in analyze() signature"
    print("✓ DrugDiseaseInteraction.analyze() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ DrugDiseaseInteraction.analyze() signature test failed: {e}")
    sys.exit(1)

# Check SimilarDrugs.find signature
try:
    config = SimilarDrugsConfig()
    analyzer = SimilarDrugs(config)
    sig = inspect.signature(analyzer.find)
    params = list(sig.parameters.keys())
    assert 'medicine_name' in params, "medicine_name should be in find() signature"
    print("✓ SimilarDrugs.find() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ SimilarDrugs.find() signature test failed: {e}")
    sys.exit(1)

# Check MedicineInfoGenerator.generate signature
try:
    config = MedicineInfoConfig()
    generator = MedicineInfoGenerator(config)
    sig = inspect.signature(generator.generate)
    params = list(sig.parameters.keys())
    assert 'medicine_name' in params, "medicine_name should be in generate() signature"
    print("✓ MedicineInfoGenerator.generate() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ MedicineInfoGenerator.generate() signature test failed: {e}")
    sys.exit(1)

# Check DrugsComparison.compare signature
try:
    config = DrugsComparisonConfig()
    analyzer = DrugsComparison(config)
    sig = inspect.signature(analyzer.compare)
    params = list(sig.parameters.keys())
    assert 'medicine1' in params, "medicine1 should be in compare() signature"
    assert 'medicine2' in params, "medicine2 should be in compare() signature"
    print("✓ DrugsComparison.compare() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ DrugsComparison.compare() signature test failed: {e}")
    sys.exit(1)

# Check DrugFoodInteraction.analyze signature
try:
    config = DrugFoodInteractionConfig()
    analyzer = DrugFoodInteraction(config)
    sig = inspect.signature(analyzer.analyze)
    params = list(sig.parameters.keys())
    assert 'medicine_name' in params, "medicine_name should be in analyze() signature"
    print("✓ DrugFoodInteraction.analyze() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ DrugFoodInteraction.analyze() signature test failed: {e}")
    sys.exit(1)

# Check DrugDrugInteraction.analyze signature
try:
    config = DrugDrugInteractionConfig()
    analyzer = DrugDrugInteraction(config)
    sig = inspect.signature(analyzer.analyze)
    params = list(sig.parameters.keys())
    assert 'medicine1' in params, "medicine1 should be in analyze() signature"
    assert 'medicine2' in params, "medicine2 should be in analyze() signature"
    print("✓ DrugDrugInteraction.analyze() has correct parameters")
    print(f"  - Parameters: {params}")
except Exception as e:
    print(f"✗ DrugDrugInteraction.analyze() signature test failed: {e}")
    sys.exit(1)

# Test input validation
print("\n" + "=" * 80)
print("TESTING INPUT VALIDATION")
print("=" * 80)

# Test empty medicine_name validation
try:
    config = DrugDiseaseInteractionConfig()
    analyzer = DrugDiseaseInteraction(config)
    try:
        analyzer.analyze(medicine_name="", condition_name="diabetes")
        print("✗ Should have raised ValueError for empty medicine_name")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ DrugDiseaseInteraction validates empty medicine_name: {e}")
except Exception as e:
    print(f"✗ DrugDiseaseInteraction validation test failed: {e}")
    sys.exit(1)

# Test age validation
try:
    config = SimilarDrugsConfig()
    analyzer = SimilarDrugs(config)
    try:
        analyzer.find(medicine_name="aspirin", patient_age=200)
        print("✗ Should have raised ValueError for invalid age")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ SimilarDrugs validates age range: {e}")
except Exception as e:
    print(f"✗ SimilarDrugs age validation test failed: {e}")
    sys.exit(1)

# Test age validation in MedicineInfoGenerator
try:
    config = MedicineInfoConfig()
    generator = MedicineInfoGenerator(config)
    try:
        generator.generate(medicine_name="aspirin", patient_age=-5)
        print("✗ Should have raised ValueError for negative age")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ MedicineInfoGenerator validates age: {e}")
except Exception as e:
    print(f"✗ MedicineInfoGenerator validation test failed: {e}")
    sys.exit(1)

# Test medicine validation in DrugsComparison
try:
    config = DrugsComparisonConfig()
    analyzer = DrugsComparison(config)
    try:
        analyzer.compare(medicine1="aspirin", medicine2="")
        print("✗ Should have raised ValueError for empty medicine2")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ DrugsComparison validates empty medicine names: {e}")
except Exception as e:
    print(f"✗ DrugsComparison validation test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 80)
print("ALL TESTS PASSED!")
print("=" * 80)
print("\nSummary:")
print("✓ All imports successful")
print("✓ All configs instantiate correctly with only static fields")
print("✓ All analyzers instantiate with config objects")
print("✓ All methods have correct parameter signatures")
print("✓ All input validations work correctly")
print("\nRefactoring successful - configs only contain static behavior!")
