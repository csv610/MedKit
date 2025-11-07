# Documentation Priorities - Remaining 43 Modules

## High Priority (Most Used) - 15 modules

These modules are frequently used and require comprehensive documentation:

### Drug & Medicine Related (6)
- [ ] drug_food_interaction - Food-drug interaction analysis
- [ ] similar_drugs - Drug similarity and comparison
- [ ] medicine_info - Comprehensive medicine information
- [ ] drugs_comparison - Compare multiple drugs
- [ ] rx_med_info - RxNorm medicine information
- [ ] rxclass_examples - RxClass drug classification examples

### Medical Diagnostic (4)
- [ ] medical_test_info - Medical test reference information
- [ ] medical_tests_graph - Knowledge graph of medical tests
- [ ] medical_procedure_info - Medical procedures reference
- [ ] herbal_info - Herbal medicine information

### Support & Analysis (5)
- [ ] privacy_compliance - HIPAA and privacy utilities
- [ ] medical_dictionary - Medical terminology dictionary
- [ ] medical_facts_checker - Verify medical information accuracy
- [ ] prescription_analyzer - Already partially done - complete it
- [ ] mental_health_assessment - Mental health evaluation

## Medium Priority (Important) - 15 modules

### Mental Health (5)
- [ ] mental_health_chat - Mental health chatbot
- [ ] mental_health_chat_app - Mental health chat application
- [ ] mental_health_report - Mental health assessment reports
- [ ] sympton_detection_chat - Symptom detection conversation
- [ ] sane_interview - Structured assessment interview

### Medical Reference (6)
- [ ] medical_anatomy - Human anatomy reference
- [ ] medical_topic - Medical topics and conditions
- [ ] medical_faq - Frequently asked medical questions
- [ ] medical_term_extractor - Extract medical terms
- [ ] patient_medical_history - Patient history management
- [ ] surgical_tool_info - Surgical instrument reference

### Medical Exams (2)
- [ ] eval_physical_exam_questions - Physical exam evaluation
- [ ] exam_specifications - Exam specifications
- [ ] medical_physical_exams_questions - Physical exam questions (if separate)

### Support/Integration (2)
- [ ] medkit_client - Main MedKit AI client
- [ ] pydantic_prompt_generator - Pydantic schema to prompt generator

## Low Priority (Support/Utility) - 13 modules

### UI & Interfaces (2)
- [ ] streamlit_ui - Streamlit web interface
- [ ] gradio_ui - Gradio web interface

### Surgery & Medical Devices (3)
- [ ] surgery_info - Surgery information and procedures
- [ ] surgical_tool_info - Surgical tools reference
- [ ] medical_test_devices - Medical testing devices

### Advanced Features (5)
- [ ] llm_sane_interview - LLM-based structured interview
- [ ] synthetic_case_report - Generate synthetic medical cases
- [ ] refactoring_automation - Code refactoring automation
- [ ] visualize_decision_guide - Visualize decision guides
- [ ] medical_decision_guide - Medical decision support

### Medical Classification (2)
- [ ] exam_specifications - Specifications for exams
- [ ] update_question_ids - Update question identifiers

### Integration (1)
- [ ] prescription_extractor - Extract from prescriptions

## Documentation Template

For each module, include:

1. **Module Docstring** (500 chars minimum)
   - Brief description
   - QUICK START section with code example
   - COMMON USES section (3-5 items)
   - KEY CONCEPTS if applicable

2. **Class/Function Docstrings**
   - Description
   - Args with types
   - Returns with type
   - Raises (if applicable)
   - Examples

3. **Create `.rst` file** in `docs/api/`

4. **Update** `docs/api/modules.rst`

## Completion Status

- ✅ Documented: disease_info, medical_speciality, rxnorm_client, drug_disease_interaction, drug_drug_interaction (5)
- ⏳ In Progress: Additional modules
- ⏹️ Remaining: 38 modules

## Quick Documentation Script

Create docstrings following this pattern:

```python
"""
module_name - Brief description

Longer description explaining the module's purpose and value.

QUICK START:
    from module_name import SomeClass
    
    obj = SomeClass()
    result = obj.method()

COMMON USES:
    1. First common use case
    2. Second common use case
    3. Third common use case
"""
```

## Notes

- Priority 1 modules should be documented first
- Each module should take 15-30 minutes to document fully
- Estimate: 10-15 hours to document all 43 modules
- Can be parallelized by category
