# Drug Database Documentation

Comprehensive pharmaceutical information including medicine details, drug interactions, dosing, and safety information.

## Table of Contents

1. [Medicine Information](#medicine-information)
2. [Drug-Drug Interactions](#drug-drug-interactions)
3. [Drug-Disease Interactions](#drug-disease-interactions)
4. [Drug-Food Interactions](#drug-food-interactions)
5. [Similar Drugs & Alternatives](#similar-drugs--alternatives)
6. [Drug Comparison](#drug-comparison)
7. [RxNorm Integration](#rxnorm-integration)

---

## Medicine Information

Get comprehensive information about medications, drugs, and pharmaceuticals.

### Features
- Drug names (brand and generic)
- Dosage forms and strengths
- Indications and uses
- Dosing recommendations
- Side effects and adverse reactions
- Contraindications and warnings
- Drug interactions summary
- Pharmacokinetics and mechanism

### Usage

#### Programmatic
```python
from medkit.drug.medicine_info import get_medicine_info

# Get medicine information
info = get_medicine_info("aspirin")
print(f"Generic Name: {info.generic_name}")
print(f"Brand Names: {info.brand_names}")
print(f"Dosage: {info.dosage}")
print(f"Indications: {info.indications}")
print(f"Side Effects: {info.side_effects}")
```

#### Command-Line
```bash
python cli/cli_medicine_info.py aspirin
python cli/cli_medicine_info.py ibuprofen --interactions
python cli/cli_medicine_info.py "metformin" --verbose
```

### Available Information

#### Basic Information
- **Generic Name**: International nonproprietary name (INN)
- **Brand Names**: Proprietary/trade names
- **Drug Class**: Therapeutic category
- **Manufacturer**: Original manufacturer

#### Clinical Information
- **Indications**: What the drug treats
- **Dosage Forms**: Tablets, capsules, injections, etc.
- **Strengths**: Available doses
- **Dosing**: Typical dosing schedules
- **Administration**: How to take the medication

#### Safety Information
- **Side Effects**: Common and serious adverse reactions
- **Contraindications**: When NOT to use
- **Warnings**: Important safety considerations
- **Precautions**: Special populations (pregnancy, elderly, etc.)
- **Allergic Reactions**: Known allergens

#### Pharmacological Information
- **Mechanism**: How the drug works
- **Absorption**: How it enters the body
- **Distribution**: Where it goes in the body
- **Metabolism**: How the body processes it
- **Elimination**: How it leaves the body
- **Half-life**: Duration of action

### Examples

```python
# Pain relievers
info = get_medicine_info("aspirin")
info = get_medicine_info("ibuprofen")
info = get_medicine_info("acetaminophen")

# Cardiovascular medications
info = get_medicine_info("lisinopril")
info = get_medicine_info("metoprolol")
info = get_medicine_info("atorvastatin")

# Antibiotics
info = get_medicine_info("amoxicillin")
info = get_medicine_info("azithromycin")

# Diabetes medications
info = get_medicine_info("metformin")
info = get_medicine_info("insulin")
```

---

## Drug-Drug Interactions

Check for interactions between two or more medications.

### Features
- Interaction identification
- Severity levels (mild, moderate, severe)
- Mechanism of interaction
- Clinical significance
- Management recommendations
- Monitoring parameters

### Usage

#### Programmatic
```python
from medkit.drug.drug_drug_interaction import get_drug_interaction

# Check interaction between two drugs
interaction = get_drug_interaction("warfarin", "aspirin")
print(f"Severity: {interaction.severity}")
print(f"Mechanism: {interaction.mechanism}")
print(f"Management: {interaction.management}")
```

#### Command-Line
```bash
python cli/cli_drug_interaction.py aspirin ibuprofen
python cli/cli_drug_interaction.py warfarin aspirin --severity
python cli/cli_drug_interaction.py metformin alcohol --verbose
```

### Severity Levels

- **Mild**: No clinical significance, monitor if needed
- **Moderate**: May require dose adjustment or monitoring
- **Severe**: Contraindicated or requires significant caution

### Common Drug Interactions

#### Anticoagulants (Blood Thinners)
- Warfarin + NSAIDs = Increased bleeding risk
- Warfarin + Aspirin = Increased bleeding risk
- Aspirin + Clopidogrel = Increased bleeding risk

#### Cardiovascular Drugs
- ACE inhibitors + NSAIDs = Kidney problems
- Beta-blockers + Calcium channel blockers = Bradycardia
- Statins + Macrolide antibiotics = Muscle problems

#### Diabetes Medications
- Metformin + Contrast dye = Kidney problems
- Sulfonylureas + NSAIDs = Hypoglycemia
- Insulin + Beta-blockers = Masked hypoglycemia

#### CNS Depressants
- Alcohol + Opioids = Respiratory depression
- Alcohol + Benzodiazepines = CNS depression
- Alcohol + Sedatives = Enhanced sedation

### Examples

```python
# Anticoagulation interactions
interaction = get_drug_interaction("warfarin", "aspirin")
interaction = get_drug_interaction("warfarin", "ibuprofen")

# Cardiovascular interactions
interaction = get_drug_interaction("lisinopril", "ibuprofen")
interaction = get_drug_interaction("metoprolol", "diltiazem")

# Common OTC interactions
interaction = get_drug_interaction("acetaminophen", "alcohol")
interaction = get_drug_interaction("ibuprofen", "aspirin")
```

---

## Drug-Disease Interactions

Check for interactions between medications and medical conditions.

### Features
- Condition-drug contraindications
- Safety considerations for specific diseases
- Alternative medication recommendations
- Monitoring requirements
- Dosage adjustments needed

### Usage

#### Programmatic
```python
from medkit.drug.drug_disease_interaction import get_drug_disease_interaction

# Check drug safety in disease
interaction = get_drug_disease_interaction("ibuprofen", "kidney disease")
print(f"Safety: {interaction.safety_rating}")
print(f"Recommendation: {interaction.recommendation}")
```

### Common Drug-Disease Interactions

#### Renal Disease
- Avoid NSAIDs (damage kidneys)
- Avoid ACE inhibitors (in advanced stages)
- Adjust doses of renally-cleared drugs

#### Hepatic Disease
- Avoid acetaminophen (liver damage)
- Avoid statins (liver toxicity)
- Adjust doses of hepatically-metabolized drugs

#### Cardiac Conditions
- Avoid NSAIDs (fluid retention, hypertension)
- Avoid decongestants (increase BP)
- Avoid some antiarrhythmics (proarrhythmic)

#### Pregnancy
- Avoid ACE inhibitors
- Avoid NSAIDs (especially 3rd trimester)
- Avoid tetracyclines
- Use prenatal-safe alternatives

### Examples

```python
# Renal disease considerations
interaction = get_drug_disease_interaction("ibuprofen", "chronic kidney disease")
interaction = get_drug_disease_interaction("lisinopril", "end-stage renal disease")

# Hepatic disease considerations
interaction = get_drug_disease_interaction("acetaminophen", "hepatitis")
interaction = get_drug_disease_interaction("atorvastatin", "cirrhosis")

# Cardiac considerations
interaction = get_drug_disease_interaction("ibuprofen", "heart failure")
interaction = get_drug_disease_interaction("decongestant", "hypertension")
```

---

## Drug-Food Interactions

Information about interactions between medications and food.

### Features
- Food components that interact with drugs
- Absorption effects
- Efficacy impacts
- Safety considerations
- Dietary recommendations

### Usage

#### Programmatic
```python
from medkit.drug.drug_food_interaction import get_drug_food_interaction

# Check drug-food interaction
interaction = get_drug_food_interaction("warfarin", "vitamin K")
print(f"Effect: {interaction.effect}")
print(f"Recommendation: {interaction.dietary_advice}")
```

#### Command-Line (Available via Python API)
```bash
python -c "from medkit.drug.drug_food_interaction import get_drug_food_interaction; print(get_drug_food_interaction('metformin', 'alcohol'))"
```

### Common Drug-Food Interactions

#### Warfarin (Blood Thinner)
- Vitamin K decreases effectiveness
- Cranberry juice increases bleeding risk
- Alcohol increases bleeding risk
- Consistent vitamin K intake important

#### Certain Antibiotics
- Tetracyclines + Calcium/Iron = Reduced absorption
- Fluoroquinolones + Dairy = Reduced absorption

#### Statins
- Grapefruit juice increases side effects
- High-fat meals increase absorption (good for some)

#### Thyroid Medications
- Calcium/Iron/Fiber decrease absorption
- Take on empty stomach
- Consistent timing important

### Examples

```python
# Anticoagulation
interaction = get_drug_food_interaction("warfarin", "vitamin K")
interaction = get_drug_food_interaction("warfarin", "cranberry")

# Antibiotic absorption
interaction = get_drug_food_interaction("tetracycline", "calcium")
interaction = get_drug_food_interaction("fluoroquinolone", "dairy")

# Statin interactions
interaction = get_drug_food_interaction("simvastatin", "grapefruit juice")
```

---

## Similar Drugs & Alternatives

Find alternative medications and similar drugs.

### Features
- Similar drug recommendations
- Alternative therapeutic options
- Indication-based alternatives
- Cost and availability comparison
- Efficacy and safety profiles

### Usage

#### Programmatic
```python
from medkit.drug.similar_drugs import get_similar_drugs

# Find alternative medications
alternatives = get_similar_drugs("aspirin", indication="pain relief")
for alt in alternatives:
    print(f"{alt.name}: {alt.indication}")
```

### Examples

```python
# Pain relief alternatives
similar = get_similar_drugs("aspirin")  # ibuprofen, acetaminophen, naproxen
similar = get_similar_drugs("ibuprofen")  # naproxen, meloxicam, celecoxib

# Hypertension alternatives
similar = get_similar_drugs("lisinopril")  # ramipril, enalapril, losartan
similar = get_similar_drugs("metoprolol")  # atenolol, carvedilol, propranolol

# Diabetes alternatives
similar = get_similar_drugs("metformin")  # glyburide, pioglitazone, glipizide
```

---

## Drug Comparison

Compare multiple medications side-by-side.

### Features
- Efficacy comparison
- Side effect profiles
- Cost comparison
- Dosing schedules
- Convenience factors
- Safety profiles

### Usage

#### Programmatic
```python
from medkit.drug.drugs_comparison import compare_drugs

# Compare medications
comparison = compare_drugs(["aspirin", "ibuprofen", "acetaminophen"])
print(comparison.efficacy_table)
print(comparison.side_effects_comparison)
```

### Examples

```python
# Pain relievers
comparison = compare_drugs(["aspirin", "ibuprofen", "acetaminophen"])

# ACE inhibitors for hypertension
comparison = compare_drugs(["lisinopril", "enalapril", "ramipril"])

# Statins for cholesterol
comparison = compare_drugs(["atorvastatin", "simvastatin", "rosuvastatin"])
```

---

## RxNorm Integration

Access RxNorm database for standardized drug information and identifiers.

### Features
- RxNorm concept IDs and terms
- Drug normalization
- Ingredient information
- Strength standardization
- Dose form information

### Usage

#### Programmatic
```python
from medkit.drug.rxnorm_client import RxNormClient

# Initialize client
rxnorm = RxNormClient()

# Get RxNorm information
results = rxnorm.search("aspirin")
for result in results:
    print(f"RxCUI: {result.rxcui}, Name: {result.name}")
```

### RxNorm Benefits
- **Standardization**: Consistent drug naming
- **Integration**: Works with EHR systems
- **Accuracy**: Official FDA/NLM standards
- **Interoperability**: Industry standard identifiers

---

## Best Practices

### Before Taking Any Medication

1. **Check Interactions**
   ```python
   # Check all interactions
   interaction = get_drug_interaction(drug1, drug2)
   ```

2. **Verify Dosing**
   ```python
   # Get correct dosing
   info = get_medicine_info(drug)
   print(info.dosing)
   ```

3. **Check Contraindications**
   ```python
   # Check for disease interactions
   interaction = get_drug_disease_interaction(drug, condition)
   ```

4. **Consult Healthcare Provider**
   - Always verify with doctor or pharmacist
   - Don't self-diagnose or self-treat

### Database Limitations
- Not a substitute for professional advice
- Always consult pharmacist or doctor
- Information may not be 100% current
- Verify with official sources

---

## Related Documentation

- [Medical Reference Documentation](MEDICAL_REFERENCE.md)
- [Diagnostic Tools Documentation](DIAGNOSTIC_TOOLS.md)
- [Mental Health Documentation](MENTAL_HEALTH.md)
- [CLI Tools Documentation](../cli/README.md)
- [API Reference](api/modules.rst)

---

## Disclaimer

This software is for **informational purposes only**. Always consult with qualified healthcare providers, pharmacists, and refer to official pharmaceutical resources for medication decisions. Never start, stop, or change medications without professional medical guidance.
