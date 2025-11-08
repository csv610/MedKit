"""
Proper unit tests for drug_disease_interaction module.

Tests cover:
- Interaction severity levels and enums
- Efficacy and safety impact models
- Dosage adjustment recommendations
- Management strategy validation
- Complete interaction result models
- Realistic drug-disease scenarios
"""

import unittest
from enum import Enum
from pydantic import ValidationError

from medkit.drug.drug_disease_interaction import (
    InteractionSeverity,
    ConfidenceLevel,
    DataSourceType,
    ImpactType,
    EfficacyImpact,
    SafetyImpact,
    DosageAdjustment,
    ManagementStrategy,
    DrugDiseaseInteractionDetails,
    PatientFriendlySummary,
    DataAvailabilityInfo,
    DrugDiseaseInteractionResult
)


# ==================== Enum Tests ====================

class TestInteractionSeverityEnum(unittest.TestCase):
    """Test InteractionSeverity enum."""

    def test_severity_values(self):
        """Test all severity levels exist."""
        severities = [
            InteractionSeverity.NONE,
            InteractionSeverity.MINOR,
            InteractionSeverity.MILD,
            InteractionSeverity.MODERATE,
            InteractionSeverity.SIGNIFICANT,
            InteractionSeverity.CONTRAINDICATED
        ]
        self.assertEqual(len(severities), 6)

    def test_severity_string_conversion(self):
        """Test severity can be converted to string."""
        severity = InteractionSeverity.MODERATE
        self.assertEqual(str(severity.value), "MODERATE")

    def test_severity_comparison(self):
        """Test severity values can be compared."""
        minor = InteractionSeverity.MINOR
        moderate = InteractionSeverity.MODERATE
        self.assertNotEqual(minor, moderate)


class TestConfidenceLevelEnum(unittest.TestCase):
    """Test ConfidenceLevel enum."""

    def test_confidence_levels(self):
        """Test confidence level options."""
        levels = [
            ConfidenceLevel.HIGH,
            ConfidenceLevel.MODERATE,
            ConfidenceLevel.LOW
        ]
        self.assertEqual(len(levels), 3)


class TestImpactTypeEnum(unittest.TestCase):
    """Test ImpactType enum."""

    def test_impact_types(self):
        """Test various impact types."""
        impacts = [
            ImpactType.EFFICACY,
            ImpactType.TOXICITY,
            ImpactType.METABOLISM,
            ImpactType.CLEARANCE,
            ImpactType.ABSORPTION
        ]
        self.assertGreater(len(impacts), 3)


# ==================== Efficacy Impact Tests ====================

class TestEfficacyImpact(unittest.TestCase):
    """Test EfficacyImpact data model."""

    def test_efficacy_impact_creation(self):
        """Test creating efficacy impact."""
        ei = EfficacyImpact(
            impact_type="Reduced effectiveness",
            mechanism="Impaired drug metabolism",
            clinical_significance="Patient may require dose increase"
        )
        self.assertEqual(ei.impact_type, "Reduced effectiveness")
        self.assertIn("metabolism", ei.mechanism.lower())

    def test_efficacy_impact_enhanced(self):
        """Test enhanced drug efficacy."""
        ei = EfficacyImpact(
            impact_type="Enhanced effectiveness",
            mechanism="Decreased drug clearance",
            clinical_significance="Risk of toxicity with standard dose"
        )
        self.assertIn("Enhanced", ei.impact_type)

    def test_efficacy_impact_none(self):
        """Test no efficacy impact."""
        ei = EfficacyImpact(
            impact_type="No significant effect",
            mechanism="Drug metabolism unaffected by condition",
            clinical_significance="Standard dosing appropriate"
        )
        self.assertIn("No", ei.impact_type)


# ==================== Safety Impact Tests ====================

class TestSafetyImpact(unittest.TestCase):
    """Test SafetyImpact data model."""

    def test_safety_impact_increased_risk(self):
        """Test increased side effect risk."""
        si = SafetyImpact(
            risk_type="Increased nephrotoxicity",
            severity_if_occurs="Severe",
            estimated_incidence="20-30%"
        )
        self.assertIn("nephrotoxicity", si.risk_type.lower())
        self.assertEqual(si.severity_if_occurs, "Severe")

    def test_safety_impact_no_additional_risk(self):
        """Test no additional safety risk."""
        si = SafetyImpact(
            risk_type="No additional risk",
            severity_if_occurs="N/A",
            estimated_incidence="No increased risk"
        )
        self.assertIn("No", si.risk_type)

    def test_safety_impact_variable_risk(self):
        """Test variable risk based on condition severity."""
        si = SafetyImpact(
            risk_type="Hyperkalemia risk increases with worsening renal function",
            severity_if_occurs="Moderate to Severe",
            estimated_incidence="Depends on eGFR"
        )
        self.assertIn("eGFR", si.estimated_incidence)


# ==================== Dosage Adjustment Tests ====================

class TestDosageAdjustment(unittest.TestCase):
    """Test DosageAdjustment data model."""

    def test_dosage_adjustment_reduction(self):
        """Test dose reduction requirement."""
        da = DosageAdjustment(
            recommendation="Reduce dose by 50%",
            rationale="Impaired renal clearance",
            monitoring_requirement="Check serum levels weekly"
        )
        self.assertIn("50%", da.recommendation)
        self.assertIn("renal", da.rationale.lower())

    def test_dosage_adjustment_no_change(self):
        """Test no dose adjustment needed."""
        da = DosageAdjustment(
            recommendation="No adjustment needed",
            rationale="Drug metabolism unaffected",
            monitoring_requirement="Routine monitoring only"
        )
        self.assertIn("No", da.recommendation)

    def test_dosage_adjustment_frequency_change(self):
        """Test frequency adjustment."""
        da = DosageAdjustment(
            recommendation="Increase interval from Q6H to Q8H",
            rationale="Delayed clearance",
            monitoring_requirement="Monitor for accumulation"
        )
        self.assertIn("Q8H", da.recommendation)


# ==================== Management Strategy Tests ====================

class TestManagementStrategy(unittest.TestCase):
    """Test ManagementStrategy data model."""

    def test_management_strategy_monitor(self):
        """Test monitoring strategy."""
        ms = ManagementStrategy(
            strategy_type="Close monitoring",
            action_items=["Check renal function weekly", "Monitor drug levels"],
            frequency="Weekly for 4 weeks"
        )
        self.assertEqual(ms.strategy_type, "Close monitoring")
        self.assertEqual(len(ms.action_items), 2)

    def test_management_strategy_avoid(self):
        """Test avoid strategy."""
        ms = ManagementStrategy(
            strategy_type="Avoid combination",
            action_items=["Use alternative drug", "Document contraindication"],
            frequency="Not applicable"
        )
        self.assertIn("Avoid", ms.strategy_type)

    def test_management_strategy_optimize(self):
        """Test optimization strategy."""
        ms = ManagementStrategy(
            strategy_type="Optimize therapy",
            action_items=["Reduce dose", "Increase monitoring", "Educate patient"],
            frequency="As needed"
        )
        self.assertGreater(len(ms.action_items), 2)


# ==================== Interaction Details Tests ====================

class TestDrugDiseaseInteractionDetails(unittest.TestCase):
    """Test DrugDiseaseInteractionDetails model."""

    def setUp(self):
        """Set up test data."""
        self.details_data = {
            "efficacy_impact": EfficacyImpact(
                impact_type="Reduced effectiveness",
                mechanism="Impaired metabolism",
                clinical_significance="May need dose adjustment"
            ),
            "safety_impact": SafetyImpact(
                risk_type="Increased toxicity risk",
                severity_if_occurs="Moderate",
                estimated_incidence="10-20%"
            ),
            "dosage_adjustment": DosageAdjustment(
                recommendation="Reduce dose by 25-50%",
                rationale="Decreased clearance",
                monitoring_requirement="Weekly monitoring"
            ),
            "management_strategy": ManagementStrategy(
                strategy_type="Close monitoring",
                action_items=["Monitor levels", "Adjust dose"],
                frequency="Weekly"
            ),
            "monitoring_requirements": "Check renal function and drug levels",
            "clinical_considerations": "Consider alternative if possible"
        }

    def test_interaction_details_creation(self):
        """Test creating interaction details."""
        details = DrugDiseaseInteractionDetails(**self.details_data)
        self.assertIsNotNone(details.efficacy_impact)
        self.assertIsNotNone(details.safety_impact)

    def test_interaction_details_serialization(self):
        """Test serialization."""
        details = DrugDiseaseInteractionDetails(**self.details_data)
        data_dict = details.dict()
        self.assertIn("efficacy_impact", data_dict)
        self.assertIn("safety_impact", data_dict)


# ==================== Patient Friendly Summary Tests ====================

class TestPatientFriendlySummary(unittest.TestCase):
    """Test PatientFriendlySummary model."""

    def test_patient_summary_creation(self):
        """Test creating patient-friendly summary."""
        pfs = PatientFriendlySummary(
            patient_friendly_explanation="Your kidney disease may affect how your body processes this medication",
            what_patient_should_know="Tell your doctor about your kidney disease",
            side_effects_to_watch_for=["Unusual fatigue", "Dark urine"],
            when_to_contact_doctor="If you feel more tired than usual"
        )
        self.assertIn("kidney disease", pfs.patient_friendly_explanation.lower())

    def test_patient_summary_empty_side_effects(self):
        """Test summary with minimal side effects."""
        pfs = PatientFriendlySummary(
            patient_friendly_explanation="This combination is generally safe",
            what_patient_should_know="No special precautions needed",
            side_effects_to_watch_for=[],
            when_to_contact_doctor="For routine adverse effects"
        )
        self.assertEqual(len(pfs.side_effects_to_watch_for), 0)


# ==================== Complete Interaction Result Tests ====================

class TestDrugDiseaseInteractionResult(unittest.TestCase):
    """Test complete DrugDiseaseInteractionResult."""

    def setUp(self):
        """Set up test data."""
        self.result_data = {
            "drug_name": "Metformin",
            "disease_name": "Chronic Kidney Disease",
            "interaction_severity": InteractionSeverity.SIGNIFICANT,
            "confidence_level": ConfidenceLevel.HIGH,
            "interaction_details": DrugDiseaseInteractionDetails(
                efficacy_impact=EfficacyImpact(
                    impact_type="Reduced effectiveness",
                    mechanism="Decreased clearance",
                    clinical_significance="May need to avoid"
                ),
                safety_impact=SafetyImpact(
                    risk_type="Lactic acidosis risk",
                    severity_if_occurs="Life-threatening",
                    estimated_incidence="0.3-1.3 per 1000 patient-years"
                ),
                dosage_adjustment=DosageAdjustment(
                    recommendation="Contraindicated with eGFR <30",
                    rationale="Risk of lactic acidosis",
                    monitoring_requirement="Check eGFR regularly"
                ),
                management_strategy=ManagementStrategy(
                    strategy_type="Avoid or use with extreme caution",
                    action_items=["Switch to alternative", "Monitor eGFR"],
                    frequency="Quarterly"
                ),
                monitoring_requirements="Monthly eGFR, lactic acid monitoring",
                clinical_considerations="Use GLP-1 agonist or SGLT2 inhibitor instead"
            ),
            "patient_friendly_summary": PatientFriendlySummary(
                patient_friendly_explanation="Your kidney disease affects how your body processes metformin",
                what_patient_should_know="This medication may not be safe for you",
                side_effects_to_watch_for=["Nausea", "Unusual fatigue"],
                when_to_contact_doctor="Immediately if you feel very tired or nauseous"
            )
        }

    def test_interaction_result_creation(self):
        """Test creating interaction result."""
        result = DrugDiseaseInteractionResult(**self.result_data)
        self.assertEqual(result.drug_name, "Metformin")
        self.assertEqual(result.disease_name, "Chronic Kidney Disease")
        self.assertEqual(result.interaction_severity, InteractionSeverity.SIGNIFICANT)

    def test_interaction_result_serialization(self):
        """Test serialization."""
        result = DrugDiseaseInteractionResult(**self.result_data)
        json_str = result.json()
        self.assertIn("Metformin", json_str)
        self.assertIn("Kidney", json_str)

    def test_interaction_result_missing_field(self):
        """Test with missing required field."""
        incomplete = self.result_data.copy()
        del incomplete["interaction_severity"]
        with self.assertRaises(ValidationError):
            DrugDiseaseInteractionResult(**incomplete)


# ==================== Realistic Scenario Tests ====================

class TestRealisticDrugDiseaseInteractions(unittest.TestCase):
    """Test realistic drug-disease interactions."""

    def test_metformin_kidney_disease(self):
        """Test metformin with chronic kidney disease."""
        result = DrugDiseaseInteractionResult(
            drug_name="Metformin",
            disease_name="Chronic Kidney Disease",
            interaction_severity=InteractionSeverity.CONTRAINDICATED,
            confidence_level=ConfidenceLevel.HIGH,
            interaction_details=DrugDiseaseInteractionDetails(
                efficacy_impact=EfficacyImpact(
                    impact_type="Reduced effectiveness",
                    mechanism="Decreased renal clearance",
                    clinical_significance="Drug accumulation risk"
                ),
                safety_impact=SafetyImpact(
                    risk_type="Lactic acidosis",
                    severity_if_occurs="Life-threatening",
                    estimated_incidence="Increased with eGFR <30"
                ),
                dosage_adjustment=DosageAdjustment(
                    recommendation="Contraindicated with eGFR <30",
                    rationale="High risk of lactic acidosis",
                    monitoring_requirement="Regular eGFR monitoring"
                ),
                management_strategy=ManagementStrategy(
                    strategy_type="Avoid",
                    action_items=["Use alternative antidiabetic", "SGLT2i or GLP-1 agonist"],
                    frequency="N/A"
                ),
                monitoring_requirements="eGFR at baseline and regularly",
                clinical_considerations="Risk increases as kidney function declines"
            ),
            patient_friendly_summary=PatientFriendlySummary(
                patient_friendly_explanation="Your weak kidneys cannot clear metformin safely",
                what_patient_should_know="You need a different diabetes medicine",
                side_effects_to_watch_for=["Severe nausea", "Difficulty breathing"],
                when_to_contact_doctor="Immediately if symptoms occur"
            )
        )

        self.assertEqual(result.interaction_severity, InteractionSeverity.CONTRAINDICATED)
        self.assertIn("Avoid", result.interaction_details.management_strategy.strategy_type)

    def test_nsaid_heart_failure(self):
        """Test NSAIDs with heart failure."""
        result = DrugDiseaseInteractionResult(
            drug_name="Ibuprofen",
            disease_name="Heart Failure",
            interaction_severity=InteractionSeverity.SIGNIFICANT,
            confidence_level=ConfidenceLevel.HIGH,
            interaction_details=DrugDiseaseInteractionDetails(
                efficacy_impact=EfficacyImpact(
                    impact_type="Counteracted by heart failure",
                    mechanism="Fluid retention worsens heart failure",
                    clinical_significance="Exacerbation risk"
                ),
                safety_impact=SafetyImpact(
                    risk_type="Heart failure exacerbation",
                    severity_if_occurs="Severe",
                    estimated_incidence="20-30% increased risk"
                ),
                dosage_adjustment=DosageAdjustment(
                    recommendation="Avoid completely",
                    rationale="Increased mortality risk",
                    monitoring_requirement="N/A"
                ),
                management_strategy=ManagementStrategy(
                    strategy_type="Avoid NSAIDs",
                    action_items=["Use acetaminophen", "Consider topical agents"],
                    frequency="N/A"
                ),
                monitoring_requirements="Monitor for fluid retention and dyspnea",
                clinical_considerations="Even short-term use increases risk"
            ),
            patient_friendly_summary=PatientFriendlySummary(
                patient_friendly_explanation="NSAIDs can make your heart condition worse",
                what_patient_should_know="Avoid all pain medications except acetaminophen",
                side_effects_to_watch_for=["Shortness of breath", "Swelling"],
                when_to_contact_doctor="If you have any difficulty breathing"
            )
        )

        self.assertEqual(result.interaction_severity, InteractionSeverity.SIGNIFICANT)

    def test_acei_hyperkalemia(self):
        """Test ACE inhibitors with hyperkalemia."""
        result = DrugDiseaseInteractionResult(
            drug_name="Lisinopril",
            disease_name="Hyperkalemia",
            interaction_severity=InteractionSeverity.CONTRAINDICATED,
            confidence_level=ConfidenceLevel.HIGH,
            interaction_details=DrugDiseaseInteractionDetails(
                efficacy_impact=EfficacyImpact(
                    impact_type="No efficacy impact",
                    mechanism="ACE inhibitor still controls blood pressure",
                    clinical_significance="Benefit offset by safety risk"
                ),
                safety_impact=SafetyImpact(
                    risk_type="Severe hyperkalemia and cardiac arrhythmias",
                    severity_if_occurs="Life-threatening",
                    estimated_incidence="High risk of cardiac events"
                ),
                dosage_adjustment=DosageAdjustment(
                    recommendation="Contraindicated",
                    rationale="ACE inhibitor worsens hyperkalemia",
                    monitoring_requirement="K+ monitoring mandatory"
                ),
                management_strategy=ManagementStrategy(
                    strategy_type="Avoid",
                    action_items=["Use alternative antihypertensive", "Treat hyperkalemia first"],
                    frequency="N/A"
                ),
                monitoring_requirements="K+ and ECG monitoring",
                clinical_considerations="Treat underlying hyperkalemia before use"
            ),
            patient_friendly_summary=PatientFriendlySummary(
                patient_friendly_explanation="ACE inhibitors can dangerously raise your potassium levels",
                what_patient_should_know="You need a different blood pressure medication",
                side_effects_to_watch_for=["Heart palpitations", "Weakness"],
                when_to_contact_doctor="Immediately if you feel palpitations"
            )
        )

        self.assertEqual(result.interaction_severity, InteractionSeverity.CONTRAINDICATED)

    def test_statins_liver_disease(self):
        """Test statins with liver disease."""
        result = DrugDiseaseInteractionResult(
            drug_name="Atorvastatin",
            disease_name="Cirrhosis",
            interaction_severity=InteractionSeverity.SIGNIFICANT,
            confidence_level=ConfidenceLevel.MODERATE,
            interaction_details=DrugDiseaseInteractionDetails(
                efficacy_impact=EfficacyImpact(
                    impact_type="Reduced effectiveness",
                    mechanism="Impaired hepatic metabolism",
                    clinical_significance="May not achieve lipid targets"
                ),
                safety_impact=SafetyImpact(
                    risk_type="Hepatotoxicity and statin-induced myopathy",
                    severity_if_occurs="Moderate to Severe",
                    estimated_incidence="Elevated liver enzyme risk"
                ),
                dosage_adjustment=DosageAdjustment(
                    recommendation="Reduce dose; start with low dose",
                    rationale="Decreased hepatic clearance",
                    monitoring_requirement="LFTs at baseline, 3 months, then yearly"
                ),
                management_strategy=ManagementStrategy(
                    strategy_type="Use with caution",
                    action_items=["Start low dose", "Monitor liver function", "Check CK if symptomatic"],
                    frequency="Quarterly LFTs"
                ),
                monitoring_requirements="Liver function tests and CK",
                clinical_considerations="Consider alternative lipid-lowering agent"
            ),
            patient_friendly_summary=PatientFriendlySummary(
                patient_friendly_explanation="Your liver condition requires careful monitoring with this medication",
                what_patient_should_know="You may need blood tests more often",
                side_effects_to_watch_for=["Muscle pain", "Yellowing of skin"],
                when_to_contact_doctor="If you have muscle pain or yellowing"
            )
        )

        self.assertGreaterEqual(result.interaction_severity.value, InteractionSeverity.MODERATE.value)


# ==================== Integration Tests ====================

class TestDrugDiseaseInteractionIntegration(unittest.TestCase):
    """Integration tests for drug-disease interaction system."""

    def test_patient_multiple_comorbidities(self):
        """Test patient with multiple interacting conditions."""
        # Metformin with both kidney disease and heart failure
        conditions_interactions = [
            ("Metformin", "Chronic Kidney Disease", InteractionSeverity.SIGNIFICANT),
            ("Metformin", "Heart Failure", InteractionSeverity.MODERATE),
        ]

        critical_interactions = [
            (drug, disease) for drug, disease, severity
            in conditions_interactions
            if severity in [InteractionSeverity.SIGNIFICANT, InteractionSeverity.CONTRAINDICATED]
        ]

        self.assertEqual(len(critical_interactions), 1)

    def test_interaction_severity_hierarchy(self):
        """Test severity level comparison."""
        severities = [
            InteractionSeverity.NONE,
            InteractionSeverity.MINOR,
            InteractionSeverity.MILD,
            InteractionSeverity.MODERATE,
            InteractionSeverity.SIGNIFICANT,
            InteractionSeverity.CONTRAINDICATED
        ]

        # Higher index = more severe
        for i in range(len(severities) - 1):
            self.assertNotEqual(severities[i], severities[i + 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
