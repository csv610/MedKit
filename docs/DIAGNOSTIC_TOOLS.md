# Diagnostic Tools Documentation

Comprehensive diagnostic information, decision support, and clinical assessment tools.

## Table of Contents

1. [Medical Tests Information](#medical-tests-information)
2. [Diagnostic Devices](#diagnostic-devices)
3. [Physical Examinations](#physical-examinations)
4. [Medical Decision Guides](#medical-decision-guides)
5. [Symptom Detection](#symptom-detection)
6. [Test Relationships Graph](#test-relationships-graph)

---

## Medical Tests Information

Comprehensive information about diagnostic tests, lab work, and investigative procedures.

### Features
- Test descriptions and purposes
- Indications for testing
- Normal and abnormal values
- Sample collection methods
- Preparation requirements
- Result interpretation
- Clinical significance

### Usage

#### Programmatic
```python
from medkit.diagnostics.medical_test_info import get_test_info

# Get test information
test = get_test_info("complete blood count")
print(f"Purpose: {test.purpose}")
print(f"Normal Values: {test.normal_values}")
print(f"Collection: {test.collection_method}")
```

#### Command-Line (Available via Python API)
```bash
python -c "from medkit.diagnostics.medical_test_info import get_test_info; print(get_test_info('CBC'))"
```

### Common Laboratory Tests

#### Hematology (Blood Tests)
- **CBC (Complete Blood Count)**: RBC, WBC, platelets, hemoglobin
- **Coagulation Studies**: PT/INR, aPTT, platelets
- **Blood Smear**: Cell morphology examination
- **Reticulocyte Count**: Bone marrow function

#### Chemistry (Metabolic Tests)
- **Basic Metabolic Panel**: Electrolytes, glucose, kidney function
- **Comprehensive Metabolic Panel**: Includes liver function
- **Lipid Panel**: Cholesterol, triglycerides
- **Glucose Tests**: Fasting, random, HbA1c

#### Liver Function Tests
- **Bilirubin**: Liver function and hemolysis
- **Transaminases (ALT, AST)**: Liver damage
- **Alkaline Phosphatase**: Bone and liver disease
- **Albumin, Prothrombin Time**: Synthetic function

#### Renal Function Tests
- **Creatinine**: Kidney function marker
- **BUN (Blood Urea Nitrogen)**: Kidney function
- **Urine Electrolytes**: Kidney function assessment
- **Glomerular Filtration Rate (GFR)**: Kidney function estimate

#### Endocrine Tests
- **TSH, T3, T4**: Thyroid function
- **Fasting Glucose**: Diabetes screening
- **Insulin Levels**: Insulin resistance
- **Cortisol**: Adrenal function

#### Cardiac Markers
- **Troponin**: Myocardial infarction
- **BNP/NT-proBNP**: Heart failure
- **Myoglobin**: Muscle damage
- **CK-MB**: Cardiac injury

#### Microbiological Tests
- **Blood Culture**: Bacteremia/sepsis
- **Urinalysis & Culture**: UTI/kidney disease
- **Throat Culture**: Streptococcal infection
- **Stool Culture**: Enteric pathogens

#### Serological Tests
- **HIV Testing**: HIV infection
- **Hepatitis Serologies**: Hepatitis A/B/C
- **RPR/VDRL**: Syphilis screening
- **COVID-19 PCR/Antigen**: SARS-CoV-2 detection

### Examples

```python
# Common tests
test = get_test_info("complete blood count")
test = get_test_info("comprehensive metabolic panel")
test = get_test_info("lipid panel")

# Cardiac tests
test = get_test_info("troponin")
test = get_test_info("BNP")
test = get_test_info("EKG")

# Thyroid tests
test = get_test_info("TSH")
test = get_test_info("free T4")
```

---

## Diagnostic Devices

Information about medical equipment and devices used in diagnosis.

### Features
- Device descriptions
- Clinical applications
- Operation principles
- Advantages and limitations
- Safety considerations
- Maintenance requirements

### Usage

#### Programmatic
```python
from medkit.diagnostics.medical_test_devices import get_device_info

# Get device information
device = get_device_info("electrocardiograph")
print(f"Purpose: {device.purpose}")
print(f"Uses: {device.clinical_uses}")
```

### Common Diagnostic Devices

#### Cardiac Devices
- **Electrocardiograph (EKG/ECG)**: Records heart electrical activity
- **Echocardiogram**: Ultrasound of heart
- **Stress Test Equipment**: Exercise or pharmacologic stress testing
- **Holter Monitor**: 24-48 hour EKG recording
- **Cardiac Catheterization**: Invasive cardiac assessment

#### Imaging Devices
- **X-ray Equipment**: Radiographic imaging
- **CT Scanner**: Computed tomography
- **MRI Machine**: Magnetic resonance imaging
- **Ultrasound Machine**: Ultrasound imaging
- **PET Scanner**: Positron emission tomography
- **Nuclear Medicine Camera**: Radioisotope imaging

#### Respiratory Devices
- **Spirometer**: Pulmonary function testing
- **Pulse Oximeter**: Oxygen saturation monitoring
- **Capnograph**: CO2 measurement
- **Arterial Blood Gas Analyzer**: Blood gas analysis

#### Laboratory Analyzers
- **Hematology Analyzer**: Blood cell counts
- **Chemistry Analyzer**: Metabolic panel testing
- **Coagulation Analyzer**: Clotting studies
- **Blood Gas Analyzer**: pH, CO2, O2, electrolytes

#### Other Devices
- **Sphygmomanometer**: Blood pressure measurement
- **Thermometer**: Temperature measurement
- **Ophthalmoscope**: Eye examination
- **Otoscope**: Ear examination
- **Endoscope**: Internal visualization

### Examples

```python
# Cardiac devices
device = get_device_info("electrocardiograph")
device = get_device_info("echocardiography machine")

# Imaging devices
device = get_device_info("CT scanner")
device = get_device_info("MRI machine")

# Monitoring devices
device = get_device_info("pulse oximeter")
device = get_device_info("cardiac monitor")
```

---

## Physical Examinations

Comprehensive guides for physical examination techniques across body systems.

### Features
- Examination procedures
- Normal findings
- Abnormal findings (red flags)
- Patient positioning
- Equipment needed
- Documentation guidelines

### Usage

#### Programmatic
```python
from medkit.phyexams import exam_heart, exam_lungs, exam_neurological

# Get examination guides
cardiac_exam = exam_heart.get_cardiac_examination_guide()
lung_exam = exam_lungs.get_lung_examination_guide()
neuro_exam = exam_neurological.get_neurological_examination_guide()
```

#### CLI Tools
```bash
# Direct access through main package
python -m medkit exam --system cardiac
python -m medkit exam --system respiratory
python -m medkit exam --system neurological
```

### Physical Examination Systems (27+ Modules)

#### Cardiovascular
- Cardiac auscultation (heart sounds, murmurs)
- Pulse examination
- Venous pressure assessment
- Peripheral vascular examination
- Blood pressure measurement

#### Respiratory
- Inspection of chest
- Palpation and percussion
- Auscultation (breath sounds)
- Work of breathing assessment
- Cyanosis evaluation

#### Neurological
- Mental status assessment
- Cranial nerves (I-XII)
- Motor examination (strength, tone)
- Sensory examination
- Reflexes and cerebellar signs

#### Abdominal
- Inspection
- Auscultation
- Palpation (superficial, deep)
- Percussion
- Special maneuvers

#### Musculoskeletal
- Inspection and palpation
- Range of motion
- Muscle strength testing
- Special joint tests
- Gait assessment

#### HEENT (Head, Eyes, Ears, Nose, Throat)
- Head examination
- Eye examination (vision, pupils, extraocular movements)
- Ear examination
- Nose examination
- Throat examination

#### Skin, Hair, Nails
- Lesion description
- Distribution patterns
- Color and texture
- Hair and nail findings
- Special skin signs

#### Mental Health Screening
- Depression screening
- Anxiety assessment
- Suicidality assessment
- Cognitive function
- Substance abuse screening

### Examples

```python
# Cardiac examination
exam = exam_heart.get_cardiac_examination_guide()
print(exam.normal_findings)
print(exam.abnormal_findings)

# Respiratory examination
exam = exam_lungs.get_lung_examination_guide()
print(exam.technique)
print(exam.red_flags)

# Neurological examination
exam = exam_neurological.get_neurological_examination_guide()
print(exam.cranial_nerves)
print(exam.motor_testing)
```

---

## Medical Decision Guides

Evidence-based decision trees and diagnostic pathways.

### Features
- Diagnostic algorithms
- Differential diagnosis lists
- Decision logic
- Evidence-based recommendations
- Red flag identification
- Risk stratification

### Usage

#### Programmatic
```python
from medkit.medical.medical_decision_guide import get_decision_guide

# Get diagnostic decision tree
guide = get_decision_guide("chest pain")
print(f"Differential: {guide.differential_diagnosis}")
print(f"Red Flags: {guide.red_flags}")
```

#### Visualization
```python
from medkit.vistools.visualize_decision_guide import visualize_guide

# Visualize decision tree
guide = get_decision_guide("dyspnea")
visualize_guide(guide, output_file="dyspnea_algorithm.png")
```

### Common Decision Guides

#### Cardiovascular
- Chest pain evaluation
- Dyspnea (shortness of breath)
- Hypertension management
- Palpitations assessment
- Syncope (fainting) workup

#### Gastrointestinal
- Abdominal pain
- Diarrhea
- Constipation
- Nausea/vomiting
- GI bleeding

#### Respiratory
- Cough evaluation
- Dyspnea workup
- Hemoptysis
- Wheezing
- Asthma management

#### Neurological
- Headache evaluation
- Dizziness/vertigo
- Seizure workup
- Memory loss
- Tremor evaluation

#### Infectious Disease
- Fever workup
- UTI evaluation
- Respiratory infection management
- Meningitis assessment
- Sepsis evaluation

### Examples

```python
# Cardiovascular algorithms
guide = get_decision_guide("chest pain")
guide = get_decision_guide("acute coronary syndrome")

# Respiratory algorithms
guide = get_decision_guide("cough")
guide = get_decision_guide("dyspnea")

# Neurological algorithms
guide = get_decision_guide("headache")
guide = get_decision_guide("dizziness")
```

---

## Symptom Detection

AI-powered symptom analysis and differential diagnosis support.

### Features
- Symptom input and analysis
- Differential diagnosis generation
- Risk stratification
- Red flag identification
- Next step recommendations
- Educational information

### Usage

#### Programmatic
```python
from medkit.mental_health.sympton_detection_chat import SymptomDetectionChat

# Create symptom detector
detector = SymptomDetectionChat()

# Analyze symptoms
symptoms = ["fever", "cough", "shortness of breath"]
analysis = detector.analyze_symptoms(symptoms)
print(f"Top Diagnoses: {analysis.differential}")
print(f"Urgency: {analysis.urgency_level}")
```

#### Command-Line
```bash
python cli/cli_symptoms_checker.py --symptoms "fever,cough,fatigue"
python cli/cli_symptoms_checker.py --symptoms "chest pain" --urgent
```

### Symptom Analysis Features
- **Input Validation**: Ensure appropriate symptoms
- **Context Addition**: Duration, severity, associated symptoms
- **Red Flag Detection**: Emergency warning signs
- **Differential Generation**: Likely diagnoses
- **Recommendation**: Next steps and urgency

### Emergency Warning Signs
- Chest pain or pressure
- Difficulty breathing
- Loss of consciousness
- Severe bleeding
- Severe abdominal pain
- Stroke symptoms
- Severe allergic reaction
- Signs of sepsis

---

## Test Relationships Graph

Understand how tests relate to each other and diagnoses.

### Features
- Test networks and relationships
- Diagnosis-to-test mapping
- Test sequence recommendations
- Cost-effectiveness analysis
- Sensitivity/specificity data

### Usage

#### Programmatic
```python
from medkit.diagnostics.medical_tests_graph import get_test_relationships

# Get test relationships
relations = get_test_relationships("diabetes")
print(f"Initial Tests: {relations.initial_tests}")
print(f"Follow-up Tests: {relations.follow_up_tests}")
```

#### Visualization
```python
# Visualize test relationships
graph = get_test_relationships("hypertension")
graph.visualize(output_file="hypertension_tests.png")
```

### Test Sequences

#### Diabetes Workup
1. Fasting glucose or HbA1c (screening)
2. Oral glucose tolerance test (confirmation)
3. Metabolic panel (complications)
4. Urine albumin (kidney damage)
5. Lipid panel (cardiovascular risk)

#### Heart Disease Workup
1. EKG (initial assessment)
2. Troponin (acute MI)
3. Echocardiogram (cardiac structure/function)
4. Stress test (ischemia assessment)
5. Cardiac catheterization (intervention)

#### Infection Workup
1. CBC with differential
2. Blood cultures
3. Source-specific cultures
4. Procalcitonin or CRP
5. Imaging as indicated

---

## Best Practices

### Ordering Tests

1. **Clinical Indication First**
   - Always have clear clinical indication
   - Don't order "just to check"

2. **Know Test Characteristics**
   - Sensitivity and specificity
   - Positive/negative predictive value
   - Pre-test probability

3. **Follow Decision Pathways**
   - Use diagnostic algorithms
   - Sequence tests appropriately
   - Consider cost-effectiveness

4. **Interpret Results Appropriately**
   - Compare to normal ranges (which vary)
   - Consider clinical context
   - Avoid over-interpretation

5. **Follow Up Abnormal Results**
   - Confirm unexpected results
   - Pursue clinically significant findings
   - Communicate results to patient

---

## Related Documentation

- [Medical Reference Documentation](MEDICAL_REFERENCE.md)
- [Drug Database Documentation](DRUG_DATABASE.md)
- [Mental Health Documentation](MENTAL_HEALTH.md)
- [CLI Tools Documentation](../cli/README.md)
- [API Reference](api/modules.rst)

---

## Disclaimer

This software provides **informational and educational support** for diagnostic decision-making. It is not a substitute for:
- Clinical judgment of healthcare providers
- Professional medical evaluation
- Certified laboratory testing
- Comprehensive physical examination

Always consult with qualified healthcare providers for diagnosis and management decisions.
