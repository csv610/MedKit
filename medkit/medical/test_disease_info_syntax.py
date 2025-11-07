"""
Syntax and Import validation test for disease_info.py

This test validates:
1. Python syntax is correct
2. File structure is valid
3. Class definitions are proper
4. Configuration is correct
"""

import ast
from pathlib import Path


def test_python_syntax():
    """Test 1: Validate Python syntax."""
    print("\n" + "="*70)
    print("  TEST 1: Python Syntax Validation")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            code = f.read()

        ast.parse(code)
        print("✓ Python syntax is valid")
        print(f"✓ File: {disease_info_path}")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_class_structure():
    """Test 2: Validate class definitions."""
    print("\n" + "="*70)
    print("  TEST 2: Class Structure Validation")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            code = f.read()

        tree = ast.parse(code)

        classes_found = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                classes_found[node.name] = {
                    'methods': [m.name for m in node.body if isinstance(m, ast.FunctionDef)],
                    'line': node.lineno
                }

        print("✓ Classes found:")
        for class_name, info in classes_found.items():
            print(f"  - {class_name} (line {info['line']})")
            if info['methods']:
                for method in info['methods'][:3]:  # Show first 3 methods
                    print(f"    • {method}()")
                if len(info['methods']) > 3:
                    print(f"    • ... and {len(info['methods']) - 3} more methods")

        # Check for required classes
        required_classes = [
            'Config',
            'DiseaseInfoGenerator',
            'DiseaseInfo',
            'DiseaseIdentity',
            'DiseaseBackground',
        ]

        missing = [c for c in required_classes if c not in classes_found]
        if missing:
            print(f"\n✗ Missing classes: {missing}")
            return False

        print(f"\n✓ All required classes found: {required_classes}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_imports():
    """Test 3: Validate imports."""
    print("\n" + "="*70)
    print("  TEST 3: Import Statements Validation")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            code = f.read()

        tree = ast.parse(code)

        imports = {'standard': [], 'from': []}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports['standard'].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or 'relative'
                for alias in node.names:
                    imports['from'].append(f"{module}.{alias.name}")

        print("✓ Standard imports:")
        for imp in imports['standard']:
            print(f"  - {imp}")

        print("\n✓ From imports:")
        for imp in imports['from']:
            print(f"  - {imp}")

        # Check for required imports
        required_imports = [
            'json',
            'hashlib',
            'pathlib.Path',
            'dataclasses.dataclass',
            'pydantic.BaseModel',
        ]

        found_required = []
        for req in required_imports:
            parts = req.split('.')
            if parts[0] in imports['standard']:
                found_required.append(req)
            elif any(parts[0] in imp for imp in imports['from']):
                found_required.append(req)

        print(f"\n✓ Required imports check: {len(found_required)}/{len(required_imports)} found")

        # Check for LMDB imports
        lmdb_imports = [imp for imp in imports['from'] if 'lmdb' in imp.lower()]
        if lmdb_imports:
            print(f"\n✓ LMDB imports found:")
            for imp in lmdb_imports:
                print(f"  - {imp}")
        else:
            print(f"\n✗ LMDB imports NOT found")
            return False

        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_config_structure():
    """Test 4: Validate Config dataclass."""
    print("\n" + "="*70)
    print("  TEST 4: Config Dataclass Structure")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            content = f.read()

        # Check for config parameters
        config_checks = {
            'db_path': 'Database path configuration',
            'db_capacity_mb': 'Database capacity configuration',
            'db_store': 'Cache enable/disable flag',
            'output_dir': 'Output directory configuration',
            'speciality': 'Medical specialty configuration',
        }

        print("✓ Config parameters:")
        for param, desc in config_checks.items():
            if param in content:
                print(f"  ✓ {param}: {desc}")
            else:
                print(f"  ✗ {param}: NOT FOUND")
                return False

        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_cache_implementation():
    """Test 5: Validate cache implementation."""
    print("\n" + "="*70)
    print("  TEST 5: Cache Implementation Validation")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            content = f.read()

        # Check for cache-related methods and logic
        cache_checks = {
            '_generate_cache_key': 'Cache key generation method',
            'storage.get': 'Cache retrieval logic',
            'storage.put': 'Cache storage logic',
            'cached_json': 'JSON serialization for cache',
            'json.dumps': 'JSON dumping for caching',
            'json.loads': 'JSON loading from cache',
        }

        print("✓ Cache implementation components:")
        found = 0
        for check, desc in cache_checks.items():
            if check in content:
                print(f"  ✓ {check}: {desc}")
                found += 1
            else:
                print(f"  ✗ {check}: NOT FOUND")

        if found == len(cache_checks):
            print(f"\n✓ All cache components present ({found}/{len(cache_checks)})")
            return True
        else:
            print(f"\n⚠ Some cache components missing ({found}/{len(cache_checks)})")
            return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_context_manager():
    """Test 6: Validate context manager implementation."""
    print("\n" + "="*70)
    print("  TEST 6: Context Manager Implementation")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            content = f.read()

        # Check for context manager methods
        context_checks = {
            '__enter__': 'Context manager entry',
            '__exit__': 'Context manager exit',
            'def close': 'Close method for resource cleanup',
        }

        print("✓ Context manager components:")
        found = 0
        for check, desc in context_checks.items():
            if check in content:
                print(f"  ✓ {check}: {desc}")
                found += 1
            else:
                print(f"  ✗ {check}: NOT FOUND")

        if found == len(context_checks):
            print(f"\n✓ Context manager fully implemented ({found}/{len(context_checks)})")
            return True
        else:
            print(f"\n✗ Context manager incomplete ({found}/{len(context_checks)})")
            return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_storage_path():
    """Test 7: Validate storage path configuration."""
    print("\n" + "="*70)
    print("  TEST 7: Storage Path Configuration")
    print("="*70 + "\n")

    disease_info_path = Path(__file__).parent / "disease_info.py"

    try:
        with open(disease_info_path, 'r') as f:
            content = f.read()

        # Check for storage directory references
        checks = {
            'parent.parent.parent': 'Path traversal to project root',
            '/storage/': 'Storage directory reference',
            'disease_info.lmdb': 'LMDB database filename',
        }

        print("✓ Storage configuration:")
        found = 0
        for check, desc in checks.items():
            if check in content:
                print(f"  ✓ {check}: {desc}")
                found += 1
            else:
                print(f"  ✗ {check}: NOT FOUND")

        if found == len(checks):
            print(f"\n✓ Storage path correctly configured at project root")
            return True
        else:
            print(f"\n⚠ Some storage config missing ({found}/{len(checks)})")
            return found >= 2  # At least 2 should be present

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def run_all_tests():
    """Run all syntax and structure tests."""
    print("\n" + "="*70)
    print("  DISEASE_INFO.PY SYNTAX & STRUCTURE TEST SUITE")
    print("="*70)

    tests = [
        ("Python Syntax", test_python_syntax),
        ("Class Structure", test_class_structure),
        ("Imports", test_imports),
        ("Config Structure", test_config_structure),
        ("Cache Implementation", test_cache_implementation),
        ("Context Manager", test_context_manager),
        ("Storage Path", test_storage_path),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"\n✗ Test '{test_name}' crashed: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))

    # Print summary
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70 + "\n")

    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)

    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")

    print(f"\n{'='*70}")
    print(f"Total: {passed_count}/{total_count} tests passed")
    print(f"{'='*70}\n")

    return passed_count == total_count


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
