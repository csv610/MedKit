# MedKit Codebase Coverage Report

**Generated**: November 8, 2024
**Total Tests**: 470
**Overall Coverage**: 40%
**Improvement**: +6% (from 34%)

## Coverage Summary

| Metric | Value |
|--------|-------|
| Total Statements | 8,824 |
| Covered Statements | 3,571 |
| Missing Statements | 5,253 |
| Coverage Percentage | 40% |
| Number of Test Files | 140 |
| Total Tests | 470 |

## Coverage by Module

### ✅ Excellent Coverage (>90%)

- `medkit/__init__.py` - **100%** (3/3)
- `medkit/core/__init__.py` - **100%** (3/3)
- `medkit/utils/__init__.py` - **100%** (3/3)
- `medkit/utils/logging_config.py` - **100%** (16/16)
- `medkit/drug/__init__.py` - **100%** (7/7)
- `medkit/diagnostics/__init__.py` - **100%** (3/3)
- `medkit/medical/__init__.py` - **100%** (17/17)
- `medkit/mental_health/models.py` - **100%** (39/39)
- `medkit/mental_health/mental_health_assessment.py` - **95%** (183/192)

### 🟢 Good Coverage (70-89%)

- `medkit/core/config.py` - **82%** (45/55)
- `medkit/medical/surgical_tool_info.py` - **75%** (153/205)
- `medkit/medical/prescription_analyzer.py` - **74%** (14/19)
- `medkit/diagnostics/medical_test_devices.py` - **73%** (160/218)
- `medkit/medical/medical_implant.py` - **73%** (150/205)
- `medkit/diagnostics/medical_test_info.py` - **72%** (155/214)
- `medkit/medical/herbal_info.py` - **70%** (120/172)
- `medkit/medical/medical_anatomy.py` - **68%** (112/164)
- `medkit/medical/medical_procedure_info.py` - **69%** (120/174)
- `medkit/medical/surgery_info.py` - **67%** (127/189)
- `medkit/medical/prescription_extractor.py` - **78%** (18/23)
- `medkit/medical/medical_topic.py` - **68%** (151/222)

### 🟡 Fair Coverage (40-69%)

| Module | Coverage | Covered/Total |
|--------|----------|---------------|
| `medkit/drug/medicine_info.py` | 51% | 111/218 |
| `medkit/medical/disease_info.py` | 50% | 88/175 |
| `medkit/medical/medical_speciality.py` | 50% | 52/105 |
| `medkit/medical/medical_term_extractor.py` | 50% | 69/138 |
| `medkit/mental_health/mental_health_report.py` | 48% | 48/101 |
| `medkit/medical/medical_decision_guide.py` | 48% | 50/104 |
| `medkit/medical/medical_dictionary.py` | 45% | 41/92 |
| `medkit/diagnostics/medical_tests_graph.py` | 44% | 45/102 |
| `medkit/mental_health/mental_health_chat.py` | 41% | 80/193 |
| `medkit/drug/similar_drugs.py` | 40% | 81/201 |
| `medkit/drug/drugs_comparison.py` | 39% | 106/271 |
| `medkit/medical/medical_faq.py` | 38% | 64/169 |
| `medkit/drug/drug_disease_interaction.py` | 38% | 106/277 |
| `medkit/mental_health/sane_interview.py` | 38% | 140/367 |
| `medkit/drug/drug_food_interaction.py` | 34% | 96/286 |
| `medkit/drug/drug_drug_interaction.py` | 33% | 75/229 |
| `medkit/medical/eval_physical_exam_questions.py` | 21% | 17/81 |
| `medkit/mental_health/sympton_detection_chat.py` | 22% | 72/323 |
| `medkit/mental_health/__init__.py` | 52% | 11/21 |

### 🔴 Low Coverage (<40%)

| Module | Coverage | Covered/Total |
|--------|----------|---------------|
| `medkit/core/gemini_client.py` | 28% | 50/176 |
| `medkit/medical/medical_physical_exams_questions.py` | 27% | 50/184 |
| `medkit/drug/rxnorm_client.py` | 32% | 18/57 |
| `medkit/core/medkit_client.py` | 14% | 12/85 |
| `medkit/utils/lmdb_storage.py` | 13% | 44/333 |
| `medkit/utils/pydantic_prompt_generator.py` | 10% | 33/328 |
| `medkit/drug/rx_med_info.py` | 27% | 25/93 |
| `medkit/drug/rxclass_examples.py` | 9% | 26/294 |
| `medkit/mental_health/llm_sane_interview.py` | 11% | 31/286 |
| `medkit/mental_health/mental_health_chat_app.py` | 12% | 22/176 |
| `medkit/refactoring_automation.py` | 16% | 21/135 |
| `medkit/update_question_ids.py` | 13% | 6/47 |
| `medkit/medical/synthetic_case_report.py` | 56% | 127/227 |
| `medkit/medical/patient_medical_history.py` | 6% | 9/147 |
| `medkit/medical/user_guide.py` | 9% | 19/217 |
| `medkit/medical/visualize_decision_guide.py` | 8% | 4/49 |
| `medkit/vistools/visualize_decision_guide.py` | 2% | 3/190 |

## Coverage Improvements

### Recent Changes (Nov 8, 2024)

1. **Fixed 49 Failing Tests** (Commit 81ea602)
   - Fixed `test_drug_drug_disease_interaction.py` (30 tests)
   - Fixed `test_medical_disease_info.py` (19 tests)
   - Updated to Pydantic v2 API

2. **Added Zero-Coverage Module Tests** (Commit 9aa9a6f)
   - Created `test_zero_coverage_modules.py` with 20 tests
   - Improved coverage from 34% → 40%
   - Added 13 previously untested modules

### Modules with Improved Coverage

| Module | Previous | Current | Change |
|--------|----------|---------|--------|
| `drugs_comparison.py` | 0% | 39% | +39% |
| `medical_implant.py` | 0% | 73% | +73% |
| `exam_specifications.py` | 0% | 58% | +58% |
| `synthetic_case_report.py` | 0% | 56% | +56% |
| `rx_med_info.py` | 0% | 27% | +27% |
| `patient_medical_history.py` | 0% | 6% | +6% |
| `user_guide.py` | 0% | 9% | +9% |
| `refactoring_automation.py` | 0% | 16% | +16% |
| `update_question_ids.py` | 0% | 13% | +13% |
| `vistools/__init__.py` | 0% | 50% | +50% |
| `__main__.py` | 0% | 50% | +50% |
| `llm_sane_interview.py` | 0% | 11% | +11% |
| `mental_health_chat_app.py` | 0% | 12% | +12% |

## Test Statistics

| Category | Count |
|----------|-------|
| Total Test Files | 140 |
| Total Tests | 470 |
| Passing Tests | 470 |
| Failing Tests | 0 |
| Pass Rate | 100% |
| New Tests Added | 20 |

## Coverage Goals

### Short Term (Next 2-4 weeks)
- [ ] Increase core modules to >80% coverage
  - `medkit/core/medkit_client.py` (currently 14%)
  - `medkit/utils/lmdb_storage.py` (currently 13%)
  - `medkit/utils/pydantic_prompt_generator.py` (currently 10%)

- [ ] Improve critical drug interaction modules
  - `drug_disease_interaction.py` (currently 38%)
  - `drug_drug_interaction.py` (currently 33%)
  - `drug_food_interaction.py` (currently 34%)

### Medium Term (1-2 months)
- [ ] Improve mental health modules to >60%
  - `llm_sane_interview.py` (currently 11%)
  - `mental_health_chat_app.py` (currently 12%)
  - `sympton_detection_chat.py` (currently 22%)

- [ ] Improve visualization modules
  - `visualize_decision_guide.py` (currently 2-8%)
  - `user_guide.py` (currently 9%)

### Long Term (2-4 months)
- [ ] Reach 70% overall coverage
- [ ] Ensure all public APIs have >90% coverage
- [ ] Implement integration tests for complex workflows

## Test Coverage by Category

### Models & Data Structures
- `medkit/mental_health/models.py` - **100%** ✅
- Most Pydantic models have comprehensive validation tests

### API Clients
- `medkit/core/gemini_client.py` - **28%** 🔴
- `medkit/core/medkit_client.py` - **14%** 🔴
- Need: more integration tests, error handling tests

### Drug Information
- `medicine_info.py` - **51%** 🟡
- `drugs_comparison.py` - **39%** 🟡
- `drug_disease_interaction.py` - **38%** 🟡
- Need: more comprehensive feature testing

### Medical Information
- `medical_anatomy.py` - **68%** 🟢
- `medical_topic.py` - **68%** 🟢
- `surgery_info.py` - **67%** 🟢
- Good coverage, can still be improved

### Mental Health
- `mental_health_assessment.py` - **95%** ✅
- Other modules lag significantly behind
- Need: more comprehensive behavioral testing

### Storage & Utilities
- `lmdb_storage.py` - **13%** 🔴
- `pydantic_prompt_generator.py` - **10%** 🔴
- Need: more unit tests for edge cases

## Recommendations

1. **High Priority**
   - Write integration tests for API clients
   - Improve coverage of core storage utilities
   - Add comprehensive drug interaction tests

2. **Medium Priority**
   - Improve mental health module coverage
   - Add more validation tests
   - Test error handling paths

3. **Low Priority**
   - Visualization modules
   - Refactoring utilities
   - Legacy code (marked for refactoring)

## Tools & Configuration

- **Test Framework**: pytest (450 tests)
- **Coverage Tool**: pytest-cov
- **Python Version**: 3.14
- **Coverage Report**: HTML and terminal

## Running Coverage Analysis

```bash
# Run all tests with coverage
pytest tests/ --cov=medkit --cov-report=term-missing

# Generate HTML report
pytest tests/ --cov=medkit --cov-report=html

# View coverage for specific module
pytest tests/ --cov=medkit.drug --cov-report=term-missing
```

## References

- Test files: `tests/` directory (140 files)
- Source code: `medkit/` directory
- Recent commits: Fix failing tests, add comprehensive tests
