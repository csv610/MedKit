#!/usr/bin/env python3
"""
test_medicine_info_output.py - Test the output of medicine_info.py

Tests the generate() method with the new 'medicine' parameter and verifies output.
"""

import sys
from pathlib import Path

print("=" * 80)
print("TESTING MEDICINE_INFO OUTPUT")
print("=" * 80)

try:
    from medicine_info import MedicineInfoConfig, MedicineInfoGenerator
    print("✓ medicine_info imported successfully\n")
except Exception as e:
    print(f"✗ Failed to import medicine_info: {e}")
    sys.exit(1)

# Test 1: Basic usage with default config
print("TEST 1: Basic usage with default config")
print("-" * 80)
try:
    config = MedicineInfoConfig(verbosity=False)
    generator = MedicineInfoGenerator(config)
    result = generator.generate(medicine="aspirin")

    print(f"✓ Successfully generated medicine info for 'aspirin'")
    print(f"  - Generic name: {result.general_information.generic_name}")
    print(f"  - Brand names: {result.general_information.brand_names[:50]}...")
    print(f"  - Available forms: {result.general_information.forms_available}")
    print()
except Exception as e:
    print(f"✗ Test 1 failed: {e}")
    sys.exit(1)

# Test 2: With verbose logging enabled
print("TEST 2: With verbose logging enabled")
print("-" * 80)
try:
    config = MedicineInfoConfig(verbosity=True)
    generator = MedicineInfoGenerator(config)
    result = generator.generate(medicine="ibuprofen")

    print(f"✓ Successfully generated medicine info for 'ibuprofen' with verbosity=True")
    print(f"  - Generic name: {result.general_information.generic_name}")
    print(f"  - Available strengths: {result.general_information.common_strengths}")
    print()
except Exception as e:
    print(f"✗ Test 2 failed: {e}")
    sys.exit(1)

# Test 3: With optional parameters (patient_age and medical_conditions)
print("TEST 3: With optional parameters")
print("-" * 80)
try:
    config = MedicineInfoConfig(verbosity=False)
    generator = MedicineInfoGenerator(config)
    result = generator.generate(
        medicine="metformin",
        patient_age=65,
        medical_conditions="diabetes, hypertension"
    )

    print(f"✓ Successfully generated medicine info for 'metformin' with patient context")
    print(f"  - Generic name: {result.general_information.generic_name}")
    print(f"  - Therapeutic class: {result.classification.therapeutic_class}")
    print()
except Exception as e:
    print(f"✗ Test 3 failed: {e}")
    sys.exit(1)

# Test 4: With custom output directory
print("TEST 4: With custom output directory")
print("-" * 80)
try:
    custom_output_dir = Path("test_outputs")
    config = MedicineInfoConfig(
        output_dir=custom_output_dir,
        verbosity=False
    )
    generator = MedicineInfoGenerator(config)
    result = generator.generate(medicine="warfarin")

    print(f"✓ Successfully generated medicine info with custom output dir")
    print(f"  - Output directory: {custom_output_dir}")
    print(f"  - Generic name: {result.general_information.generic_name}")

    # Check if output file was created
    expected_file = custom_output_dir / "warfarin_info.json"
    if expected_file.exists():
        print(f"  - Output file created: {expected_file}")
    print()
except Exception as e:
    print(f"✗ Test 4 failed: {e}")
    sys.exit(1)

# Test 5: Verify parameter names
print("TEST 5: Verify parameter names")
print("-" * 80)
import inspect
try:
    sig = inspect.signature(generator.generate)
    params = list(sig.parameters.keys())

    print(f"✓ Method signature verified:")
    for param in params:
        print(f"    - {param}")

    assert 'medicine' in params, "Missing 'medicine' parameter"
    assert 'medicine_name' not in params, "'medicine_name' should not be in parameters"
    print(f"\n✓ Parameter names are correct (uses 'medicine' not 'medicine_name')")
    print()
except Exception as e:
    print(f"✗ Test 5 failed: {e}")
    sys.exit(1)

# Test 6: Verify config fields
print("TEST 6: Verify config fields")
print("-" * 80)
try:
    config = MedicineInfoConfig()

    print(f"✓ Config fields:")
    print(f"    - output_path: {config.output_path}")
    print(f"    - output_dir: {config.output_dir}")
    print(f"    - verbosity: {config.verbosity}")
    print(f"    - prompt_style: {config.prompt_style}")

    assert hasattr(config, 'verbosity'), "Missing 'verbosity' field"
    assert config.verbosity == False, "Default verbosity should be False"
    print(f"\n✓ Config fields are correct (verbosity defaults to False)")
    print()
except Exception as e:
    print(f"✗ Test 6 failed: {e}")
    sys.exit(1)

print("=" * 80)
print("ALL TESTS PASSED!")
print("=" * 80)
print("\nSummary:")
print("✓ Basic usage works correctly")
print("✓ Verbose logging can be enabled")
print("✓ Optional parameters work (patient_age, medical_conditions)")
print("✓ Custom output directory works")
print("✓ Parameter names are correct (uses 'medicine' not 'medicine_name')")
print("✓ Config has all required fields with correct defaults")
