"""
Proper unit tests for disease_info module.

Tests cover:
- Data model validation (Pydantic models)
- Model structure and required fields
- Optional fields handling
- Data serialization/deserialization
- Invalid data rejection
"""

import unittest
from typing import Optional, List
from pydantic import ValidationError

from medkit.medical.disease_info import (
    RiskFactors,
    DiagnosticCriteria,
    DiseaseIdentity,
    DiseaseBackground,
    DiseaseEpidemiology,
    DiseaseClinicalPresentation,
    DiseaseDiagnosis,
    DiseaseManagement,
    DiseaseResearch,
    DiseaseSpecialPopulations,
    DiseaseLivingWith,
    DiseaseInfo
)


# ==================== Risk Factors Tests ====================

class TestRiskFactors(unittest.TestCase):
    """Test RiskFactors data model."""

    def test_risk_factors_creation(self):
        """Test creating risk factors with valid data."""
        rf = RiskFactors(
            modifiable=["smoking", "high cholesterol"],
            non_modifiable=["age", "family history"],
            environmental=["air pollution", "occupational exposure"]
        )
        self.assertEqual(rf.modifiable, ["smoking", "high cholesterol"])
        self.assertEqual(rf.non_modifiable, ["age", "family history"])
        self.assertIn("air pollution", rf.environmental)

    def test_risk_factors_empty_lists(self):
        """Test risk factors with empty lists."""
        rf = RiskFactors(modifiable=[], non_modifiable=[], environmental=[])
        self.assertEqual(rf.modifiable, [])
        self.assertEqual(rf.non_modifiable, [])
        self.assertEqual(rf.environmental, [])

    def test_risk_factors_missing_fields(self):
        """Test risk factors with missing required fields."""
        with self.assertRaises(ValidationError):
            RiskFactors(modifiable=["smoking"], non_modifiable=["age"])


# ==================== Diagnostic Criteria Tests ====================

class TestDiagnosticCriteria(unittest.TestCase):
    """Test DiagnosticCriteria data model."""

    def test_diagnostic_criteria_creation(self):
        """Test creating diagnostic criteria."""
        dc = DiagnosticCriteria(
            symptoms=["Headache", "Chest pain"],
            physical_exam=["Elevated BP", "Heart murmur"],
            laboratory_tests=["BP reading", "EKG"],
            imaging_studies=["Chest X-ray", "Echocardiogram"]
        )
        self.assertEqual(len(dc.symptoms), 2)
        self.assertEqual(len(dc.physical_exam), 2)
        self.assertIn("Chest X-ray", dc.imaging_studies)

    def test_diagnostic_criteria_empty_arrays(self):
        """Test diagnostic criteria with empty arrays."""
        dc = DiagnosticCriteria(
            symptoms=[],
            physical_exam=[],
            laboratory_tests=[],
            imaging_studies=[]
        )
        self.assertEqual(len(dc.symptoms), 0)
        self.assertEqual(len(dc.physical_exam), 0)
        self.assertEqual(len(dc.laboratory_tests), 0)
        self.assertEqual(len(dc.imaging_studies), 0)


# ==================== Disease Identity Tests ====================

class TestDiseaseIdentity(unittest.TestCase):
    """Test DiseaseIdentity data model."""

    def test_disease_identity_creation(self):
        """Test creating disease identity."""
        di = DiseaseIdentity(
            name="Hypertension",
            synonyms=["High blood pressure", "HTN"],
            icd_10_code="I10"
        )
        self.assertEqual(di.name, "Hypertension")
        self.assertIn("HTN", di.synonyms)
        self.assertEqual(di.icd_10_code, "I10")

    def test_disease_identity_without_alternatives(self):
        """Test disease identity without alternative names."""
        di = DiseaseIdentity(
            name="Uncommon Disease",
            synonyms=[],
            icd_10_code="Z00.00"
        )
        self.assertEqual(len(di.synonyms), 0)

    def test_disease_identity_required_fields(self):
        """Test disease identity with missing required field."""
        with self.assertRaises(ValidationError):
            DiseaseIdentity(
                name="Test",
                synonyms=[]
            )


# ==================== Disease Background Tests ====================

class TestDiseaseBackground(unittest.TestCase):
    """Test DiseaseBackground data model."""

    def test_disease_background_creation(self):
        """Test creating disease background."""
        db = DiseaseBackground(
            definition="Systemic arterial blood pressure > 140/90 mmHg",
            pathophysiology="Increased peripheral vascular resistance",
            etiology="Multifactorial: genetic and environmental factors"
        )
        self.assertIn("140/90", db.definition)
        self.assertIn("resistance", db.pathophysiology)

    def test_disease_background_long_text(self):
        """Test background with long descriptive text."""
        long_text = "A" * 500
        db = DiseaseBackground(
            definition=long_text,
            pathophysiology="Normal",
            etiology="Normal"
        )
        self.assertEqual(len(db.definition), 500)


# ==================== Disease Epidemiology Tests ====================

class TestDiseaseEpidemiology(unittest.TestCase):
    """Test DiseaseEpidemiology data model."""

    def test_epidemiology_creation(self):
        """Test creating epidemiology data."""
        risk_factors = RiskFactors(
            modifiable=["smoking", "diet"],
            non_modifiable=["age"],
            environmental=["pollution"]
        )
        de = DiseaseEpidemiology(
            prevalence="30% of adults",
            incidence="3 million new cases per year",
            risk_factors=risk_factors
        )
        self.assertIn("30%", de.prevalence)
        self.assertIn("smoking", de.risk_factors.modifiable)

    def test_epidemiology_regional_variation(self):
        """Test epidemiology with regional data."""
        risk_factors = RiskFactors(
            modifiable=[],
            non_modifiable=["age"],
            environmental=[]
        )
        de = DiseaseEpidemiology(
            prevalence="5-15% depending on region",
            incidence="Variable",
            risk_factors=risk_factors
        )
        self.assertIn("region", de.prevalence)


# ==================== Clinical Presentation Tests ====================

class TestDiseaseClinicalPresentation(unittest.TestCase):
    """Test DiseaseClinicalPresentation data model."""

    def test_clinical_presentation_creation(self):
        """Test creating clinical presentation."""
        dcp = DiseaseClinicalPresentation(
            symptoms=["Headache", "Chest discomfort"],
            signs=["Elevated BP", "Left ventricular hypertrophy"],
            natural_history="Progressive disorder with variable course"
        )
        self.assertEqual(len(dcp.symptoms), 2)
        self.assertIn("Elevated BP", dcp.signs)

    def test_clinical_presentation_empty_symptoms(self):
        """Test presentation with asymptomatic disease."""
        dcp = DiseaseClinicalPresentation(
            symptoms=[],
            signs=["Finding 1"],
            natural_history="Often asymptomatic initially"
        )
        self.assertEqual(len(dcp.symptoms), 0)


# ==================== Diagnosis Tests ====================

class TestDiseaseDiagnosis(unittest.TestCase):
    """Test DiseaseDiagnosis data model."""

    def test_diagnosis_creation(self):
        """Test creating diagnosis information."""
        dc = DiagnosticCriteria(
            symptoms=["Elevated BP"],
            physical_exam=["Increased BP reading"],
            laboratory_tests=["BP monitoring"],
            imaging_studies=[]
        )
        dd = DiseaseDiagnosis(
            diagnostic_criteria=dc,
            differential_diagnosis=["White coat effect", "Secondary hypertension"]
        )
        self.assertIsNotNone(dd.diagnostic_criteria)
        self.assertIn("White coat effect", dd.differential_diagnosis)


# ==================== Management Tests ====================

class TestDiseaseManagement(unittest.TestCase):
    """Test DiseaseManagement data model."""

    def test_management_creation(self):
        """Test creating management information."""
        dm = DiseaseManagement(
            treatment_options=["Lifestyle modification", "ACE inhibitors"],
            prevention=["Reduce sodium intake", "Exercise"],
            prognosis="Good with treatment"
        )
        self.assertEqual(len(dm.treatment_options), 2)
        self.assertIn("Exercise", dm.prevention)

    def test_management_conservative_approach(self):
        """Test management with conservative treatment."""
        dm = DiseaseManagement(
            treatment_options=["Observation only"],
            prevention=["Lifestyle modifications"],
            prognosis="Variable with monitoring"
        )
        self.assertEqual(len(dm.treatment_options), 1)


# ==================== Research Tests ====================

class TestDiseaseResearch(unittest.TestCase):
    """Test DiseaseResearch data model."""

    def test_research_creation(self):
        """Test creating research information."""
        dr = DiseaseResearch(
            current_research="Gene therapy approaches and immunotherapy research",
            recent_advancements="New drug class approved 2023, improved management guidelines"
        )
        self.assertIn("Gene therapy", dr.current_research)

    def test_research_no_breakthroughs(self):
        """Test research with limited advancements."""
        dr = DiseaseResearch(
            current_research="Ongoing studies",
            recent_advancements="Limited recent breakthroughs"
        )
        self.assertIn("Limited", dr.recent_advancements)


# ==================== Special Populations Tests ====================

class TestDiseaseSpecialPopulations(unittest.TestCase):
    """Test DiseaseSpecialPopulations data model."""

    def test_special_populations_creation(self):
        """Test creating special populations data."""
        dsp = DiseaseSpecialPopulations(
            pediatric="Rare in children before age 12",
            geriatric="Common, often undertreated in older adults",
            pregnancy="Risk of pre-eclampsia during pregnancy"
        )
        self.assertIn("Rare", dsp.pediatric)
        self.assertIn("undertreated", dsp.geriatric)

    def test_special_populations_no_differences(self):
        """Test when there are no special considerations."""
        dsp = DiseaseSpecialPopulations(
            pediatric="No significant differences from adults",
            geriatric="No significant differences from adults",
            pregnancy="Generally safe during pregnancy"
        )
        self.assertIn("Generally safe", dsp.pregnancy)


# ==================== Living With Tests ====================

class TestDiseaseLivingWith(unittest.TestCase):
    """Test DiseaseLivingWith data model."""

    def test_living_with_creation(self):
        """Test creating living with information."""
        dlw = DiseaseLivingWith(
            quality_of_life="Usually good with treatment and lifestyle modification",
            support_resources=["Support groups", "Educational materials", "Online communities"]
        )
        self.assertIn("Support groups", dlw.support_resources)
        self.assertEqual(len(dlw.support_resources), 3)

    def test_living_with_no_support(self):
        """Test when disease has minimal support resources."""
        dlw = DiseaseLivingWith(
            quality_of_life="Excellent with proper management",
            support_resources=[]
        )
        self.assertEqual(len(dlw.support_resources), 0)


# ==================== Complete Disease Info Tests ====================

class TestDiseaseInfo(unittest.TestCase):
    """Test complete DiseaseInfo model."""

    def setUp(self):
        """Set up test data."""
        risk_factors = RiskFactors(
            modifiable=["smoking", "diet"],
            non_modifiable=["age"],
            environmental=["stress"]
        )
        dc = DiagnosticCriteria(
            symptoms=["Headache", "Chest discomfort"],
            physical_exam=["Elevated BP"],
            laboratory_tests=["BP reading"],
            imaging_studies=[]
        )
        self.disease_data = {
            "identity": DiseaseIdentity(
                name="Hypertension",
                synonyms=["High blood pressure"],
                icd_10_code="I10"
            ),
            "background": DiseaseBackground(
                definition="BP > 140/90",
                pathophysiology="Increased peripheral vascular resistance",
                etiology="Multifactorial"
            ),
            "epidemiology": DiseaseEpidemiology(
                prevalence="30%",
                incidence="3M/year",
                risk_factors=risk_factors
            ),
            "clinical_presentation": DiseaseClinicalPresentation(
                symptoms=["Headache"],
                signs=["Elevated BP"],
                natural_history="Progressive if untreated"
            ),
            "diagnosis": DiseaseDiagnosis(
                diagnostic_criteria=dc,
                differential_diagnosis=["White coat effect"]
            ),
            "management": DiseaseManagement(
                treatment_options=["Medication", "Lifestyle modification"],
                prevention=["Reduce sodium", "Exercise"],
                prognosis="Good with treatment"
            ),
            "research": DiseaseResearch(
                current_research="Gene therapy approaches",
                recent_advancements="Improved management guidelines"
            ),
            "special_populations": DiseaseSpecialPopulations(
                pediatric="Rare in children",
                geriatric="Common in elderly",
                pregnancy="Can cause complications"
            ),
            "living_with": DiseaseLivingWith(
                quality_of_life="Good with treatment",
                support_resources=["Support groups"]
            )
        }

    def test_disease_info_creation(self):
        """Test creating complete disease info."""
        di = DiseaseInfo(**self.disease_data)
        self.assertEqual(di.identity.name, "Hypertension")
        self.assertEqual(di.epidemiology.prevalence, "30%")

    def test_disease_info_serialization(self):
        """Test disease info can be serialized to dict."""
        di = DiseaseInfo(**self.disease_data)
        data_dict = di.model_dump()
        self.assertIn("identity", data_dict)
        self.assertIn("background", data_dict)
        self.assertEqual(data_dict["identity"]["name"], "Hypertension")

    def test_disease_info_json_serialization(self):
        """Test disease info can be serialized to JSON."""
        di = DiseaseInfo(**self.disease_data)
        json_str = di.model_dump_json()
        self.assertIn("Hypertension", json_str)

    def test_disease_info_missing_required_field(self):
        """Test disease info with missing required field."""
        risk_factors = RiskFactors(
            modifiable=[],
            non_modifiable=["age"],
            environmental=[]
        )
        incomplete_data = {
            "identity": DiseaseIdentity(
                name="Test",
                synonyms=[],
                icd_10_code="Z00"
            ),
            "background": DiseaseBackground(
                definition="Test",
                pathophysiology="Test",
                etiology="Test"
            )
        }
        with self.assertRaises(ValidationError):
            DiseaseInfo(**incomplete_data)


# ==================== Integration Tests ====================

class TestDiseaseInfoIntegration(unittest.TestCase):
    """Integration tests for disease information system."""

    def test_hypertension_disease_model(self):
        """Test a realistic hypertension model."""
        risk_factors = RiskFactors(
            modifiable=["smoking", "alcohol", "salt intake", "obesity", "stress"],
            non_modifiable=["age", "family history", "race"],
            environmental=["air pollution", "socioeconomic status"]
        )
        dc = DiagnosticCriteria(
            symptoms=["Often asymptomatic", "Headache", "Dizziness"],
            physical_exam=["Elevated BP on 2+ occasions", "Left ventricular hypertrophy"],
            laboratory_tests=["Blood pressure readings", "Serum creatinine", "Potassium"],
            imaging_studies=["Echocardiogram"]
        )
        hypertension = DiseaseInfo(
            identity=DiseaseIdentity(
                name="Essential Hypertension",
                synonyms=["Primary hypertension", "High blood pressure"],
                icd_10_code="I10"
            ),
            background=DiseaseBackground(
                definition="Systemic arterial blood pressure ≥140/90 mmHg on ≥2 occasions",
                pathophysiology="Increased peripheral vascular resistance with expanded intravascular volume",
                etiology="Multifactorial: 95% have unknown etiology (primary HTN)"
            ),
            epidemiology=DiseaseEpidemiology(
                prevalence="30-45% of adults in developed countries",
                incidence="3-4 million new cases annually in USA",
                risk_factors=risk_factors
            ),
            clinical_presentation=DiseaseClinicalPresentation(
                symptoms=["Often asymptomatic", "Headache", "Dizziness", "Chest discomfort"],
                signs=["Elevated systolic and/or diastolic BP", "Left ventricular hypertrophy"],
                natural_history="Often asymptomatic in early stages to severe with complications"
            ),
            diagnosis=DiseaseDiagnosis(
                diagnostic_criteria=dc,
                differential_diagnosis=[
                    "White coat hypertension",
                    "Secondary hypertension",
                    "Masked hypertension"
                ]
            ),
            management=DiseaseManagement(
                treatment_options=[
                    "Lifestyle modification alone",
                    "Pharmacological therapy",
                    "Combined approach"
                ],
                prevention=[
                    "DASH diet (sodium <2.3g/day)",
                    "Regular aerobic exercise (150 min/week)",
                    "Weight loss if overweight",
                    "Limit alcohol",
                    "Stress reduction"
                ],
                prognosis="Excellent with medication adherence and lifestyle changes"
            ),
            research=DiseaseResearch(
                current_research="Novel antihypertensive agents, gene therapy approaches",
                recent_advancements="SGLT2 inhibitors showing benefit in HTN with CKD, Renal denervation techniques"
            ),
            special_populations=DiseaseSpecialPopulations(
                pediatric="Rare; secondary causes must be ruled out",
                geriatric="Very common; often undertreated; target BP 130-139/70-79",
                pregnancy="High risk for pre-eclampsia; specific medication restrictions"
            ),
            living_with=DiseaseLivingWith(
                quality_of_life="Generally excellent with treatment adherence",
                support_resources=["American Heart Association", "Patient education programs", "Online support groups"]
            )
        )

        # Verify the model structure
        self.assertEqual(hypertension.identity.name, "Essential Hypertension")
        self.assertEqual(hypertension.identity.icd_10_code, "I10")
        self.assertGreater(len(hypertension.management.prevention), 3)
        self.assertGreater(len(hypertension.living_with.support_resources), 2)

    def test_disease_model_completeness(self):
        """Test that disease model captures all necessary information."""
        risk_factors = RiskFactors(
            modifiable=["factor1"],
            non_modifiable=["factor2"],
            environmental=["factor3"]
        )
        dc = DiagnosticCriteria(
            symptoms=["symp"],
            physical_exam=["exam"],
            laboratory_tests=["test"],
            imaging_studies=["imaging"]
        )
        di = DiseaseInfo(
            identity=DiseaseIdentity(
                name="Test",
                synonyms=[],
                icd_10_code="Z00"
            ),
            background=DiseaseBackground(
                definition="def",
                pathophysiology="path",
                etiology="etio"
            ),
            epidemiology=DiseaseEpidemiology(
                prevalence="prev",
                incidence="inc",
                risk_factors=risk_factors
            ),
            clinical_presentation=DiseaseClinicalPresentation(
                symptoms=["symp"],
                signs=["sign"],
                natural_history="history"
            ),
            diagnosis=DiseaseDiagnosis(
                diagnostic_criteria=dc,
                differential_diagnosis=["diff"]
            ),
            management=DiseaseManagement(
                treatment_options=["treat"],
                prevention=["prev"],
                prognosis="prog"
            ),
            research=DiseaseResearch(
                current_research="curr",
                recent_advancements="adv"
            ),
            special_populations=DiseaseSpecialPopulations(
                pediatric="ped",
                geriatric="ger",
                pregnancy="preg"
            ),
            living_with=DiseaseLivingWith(
                quality_of_life="qol",
                support_resources=["support"]
            )
        )

        # Verify all main sections are present
        self.assertIsNotNone(di.identity)
        self.assertIsNotNone(di.background)
        self.assertIsNotNone(di.epidemiology)
        self.assertIsNotNone(di.clinical_presentation)
        self.assertIsNotNone(di.diagnosis)
        self.assertIsNotNone(di.management)
        self.assertIsNotNone(di.research)
        self.assertIsNotNone(di.special_populations)
        self.assertIsNotNone(di.living_with)


if __name__ == "__main__":
    unittest.main(verbosity=2)
