#!/usr/bin/env python3
"""Test script to verify red flag detection works correctly."""

from medkit.mental_health.sympton_detection_chat import MedicalConsultation

def test_red_flag_detection():
    """Test red flag detection with various scenarios."""
    app = MedicalConsultation()

    # Test cases with expected results
    test_cases = [
        ("I have severe chest pain", True, "chest_pain"),
        ("I'm having trouble breathing", True, "respiratory_distress"),
        ("I had a stroke", True, "neurological"),
        ("I can't stop the bleeding", True, "severe_bleeding"),
        ("I feel dizzy and confused", True, "signs_of_shock"),
        ("I have a mild headache", False, None),
        ("I have a slight cough", False, None),
        ("sudden severe headache and weakness on my left side", True, "neurological"),
        ("chest pressure and shortness of breath", True, "chest_pain"),
        ("just a runny nose and mild fatigue", False, None),
    ]

    print("="*80)
    print("RED FLAG DETECTION TEST".center(80))
    print("="*80 + "\n")

    passed = 0
    failed = 0

    for test_input, expected_emergency, expected_category in test_cases:
        is_emergency, red_flags = app.detect_red_flags(test_input)

        status = "✓ PASS" if is_emergency == expected_emergency else "✗ FAIL"
        if is_emergency != expected_emergency:
            failed += 1
        else:
            passed += 1

        print(f"{status}")
        print(f"  Input: {test_input}")
        print(f"  Expected Emergency: {expected_emergency}, Got: {is_emergency}")
        print(f"  Red Flags Detected: {red_flags if red_flags else 'None'}")
        print()

    print("="*80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("="*80 + "\n")

    return failed == 0

if __name__ == "__main__":
    success = test_red_flag_detection()
    exit(0 if success else 1)
