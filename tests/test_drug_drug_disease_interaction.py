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
            ImpactType.EFFICACY_REDUCTION,
            ImpactType.EFFICACY_ENHANCEMENT,
            ImpactType.INCREASED_TOXICITY,
            ImpactType.ALTERED_METABOLISM,
            ImpactType.CONTRAINDICATED,
            ImpactType.REQUIRES_MONITORING,
            ImpactType.REQUIRES_DOSE_ADJUSTMENT
        ]
        self.assertGreater(len(impacts), 3)


# ==================== Efficacy Impact Tests ====================

class TestEfficacyImpact(unittest.TestCase):
    """Test EfficacyImpact data model."""

    def test_efficacy_impact_creation(self):
        """Test creating efficacy impact."""
        ei = EfficacyImpact(
            has_impact=True,
            impact_description="Reduced effectiveness due to impaired drug metabolism",
            clinical_significance="Patient may require dose increase"
        )
        self.assertTrue(ei.has_impact)
        self.assertIn("metabolism", ei.impact_description.lower())

    def test_efficacy_impact_enhanced(self):
        """Test enhanced drug efficacy."""
        ei = EfficacyImpact(
            has_impact=True,
            impact_description="Enhanced effectiveness due to decreased drug clearance",
            clinical_significance="Risk of toxicity with standard dose"
        )
        self.assertTrue(ei.has_impact)
        self.assertIn("enhanced", ei.impact_description.lower())

    def test_efficacy_impact_none(self):
        """Test no efficacy impact."""
        ei = EfficacyImpact(
            has_impact=False,
            impact_description="No significant effect - Drug metabolism unaffected by condition",
            clinical_significance="Standard dosing appropriate"
        )
        self.assertFalse(ei.has_impact)


# ==================== Safety Impact Tests ====================

class TestSafetyImpact(unittest.TestCase):
    """Test SafetyImpact data model."""

    def test_safety_impact_increased_risk(self):
        """Test increased side effect risk."""
        si = SafetyImpact(
            has_impact=True,
            impact_description="Increased nephrotoxicity risk",
            increased_side_effects="Acute kidney injury, elevated creatinine",
            risk_level=InteractionSeverity.SIGNIFICANT
        )
        self.assertTrue(si.has_impact)
        self.assertIn("nephrotoxicity", si.impact_description.lower())
        self.assertEqual(si.risk_level, InteractionSeverity.SIGNIFICANT)

    def test_safety_impact_no_additional_risk(self):
        """Test no additional safety risk."""
        si = SafetyImpact(
            has_impact=False,
            impact_description="No additional risk identified",
            increased_side_effects=None
        )
        self.assertFalse(si.has_impact)

    def test_safety_impact_variable_risk(self):
        """Test variable risk based on condition severity."""
        si = SafetyImpact(
            has_impact=True,
            impact_description="Hyperkalemia risk increases with worsening renal function",
            increased_side_effects="Elevated potassium levels",
            risk_level=InteractionSeverity.MODERATE,
            monitoring_for_safety="eGFR, serum potassium, electrolytes"
        )
        self.assertTrue(si.has_impact)
        self.assertIn("eGFR", si.monitoring_for_safety)


# ==================== Dosage Adjustment Tests ====================

class TestDosageAdjustment(unittest.TestCase):
    """Test DosageAdjustment data model."""

    def test_dosage_adjustment_reduction(self):
        """Test dose reduction requirement."""
        da = DosageAdjustment(
            adjustment_needed=True,
            adjustment_type="dose reduction",
            specific_recommendations="Reduce dose by 50% due to impaired renal clearance",
            monitoring_parameters="Serum creatinine, serum levels weekly"
        )
        self.assertTrue(da.adjustment_needed)
        self.assertIn("50%", da.specific_recommendations)
        self.assertIn("renal", da.specific_recommendations.lower())

    def test_dosage_adjustment_no_change(self):
        """Test no dose adjustment needed."""
        da = DosageAdjustment(
            adjustment_needed=False,
            adjustment_type=None,
            specific_recommendations="Drug metabolism unaffected - routine monitoring only"
        )
        self.assertFalse(da.adjustment_needed)

    def test_dosage_adjustment_frequency_change(self):
        """Test frequency adjustment."""
        da = DosageAdjustment(
            adjustment_needed=True,
            adjustment_type="dosing interval change",
            specific_recommendations="Increase interval from Q6H to Q8H due to delayed clearance",
            monitoring_parameters="Monitor for drug accumulation, serum levels"
        )
        self.assertTrue(da.adjustment_needed)
        self.assertIn("Q8H", da.specific_recommendations)


# ==================== Management Strategy Tests ====================

class TestManagementStrategy(unittest.TestCase):
    """Test ManagementStrategy data model."""

    def test_management_strategy_monitor(self):
        """Test monitoring strategy."""
        ms = ManagementStrategy(
            impact_types=[ImpactType.REQUIRES_MONITORING],
            clinical_recommendations="Check renal function weekly, Monitor drug levels, Adjust dose if needed",
            contraindication_status="Safe with monitoring"
        )
        self.assertIn(ImpactType.REQUIRES_MONITORING, ms.impact_types)
        self.assertIn("renal", ms.clinical_recommendations.lower())

    def test_management_strategy_avoid(self):
        """Test avoid strategy."""
        ms = ManagementStrategy(
            impact_types=[ImpactType.CONTRAINDICATED],
            clinical_recommendations="Use alternative drug, Document contraindication in chart, Inform patient",
            contraindication_status="Contraindicated"
        )
        self.assertIn(ImpactType.CONTRAINDICATED, ms.impact_types)
        self.assertEqual(ms.contraindication_status, "Contraindicated")

    def test_management_strategy_optimize(self):
        """Test optimization strategy."""
        ms = ManagementStrategy(
            impact_types=[ImpactType.REQUIRES_DOSE_ADJUSTMENT, ImpactType.REQUIRES_MONITORING],
            clinical_recommendations="Reduce dose, Increase monitoring frequency, Educate patient on side effects, Adjust based on therapeutic drug monitoring",
            contraindication_status="Safe with precautions"
        )
        self.assertGreater(len(ms.impact_types), 1)


# ==================== Interaction Details Tests ====================

class TestDrugDiseaseInteractionDetails(unittest.TestCase):
    """Test DrugDiseaseInteractionDetails model."""

    def setUp(self):
        """Set up test data."""
        self.details_data = {
            "medicine_name": "Metformin",
            "condition_name": "Chronic Kidney Disease",
            "overall_severity": InteractionSeverity.SIGNIFICANT,
            "mechanism_of_interaction": "Impaired renal clearance leads to drug accumulation",
            "efficacy_impact": EfficacyImpact(
                has_impact=True,
                impact_description="Reduced effectiveness due to impaired metabolism",
                clinical_significance="May need dose adjustment"
            ),
            "safety_impact": SafetyImpact(
                has_impact=True,
                impact_description="Increased toxicity risk",
                increased_side_effects="Lactic acidosis",
                risk_level=InteractionSeverity.MODERATE
            ),
            "dosage_adjustment": DosageAdjustment(
                adjustment_needed=True,
                adjustment_type="dose reduction",
                specific_recommendations="Reduce dose by 25-50% based on eGFR",
                monitoring_parameters="eGFR, serum creatinine"
            ),
            "management_strategy": ManagementStrategy(
                impact_types=[ImpactType.REQUIRES_DOSE_ADJUSTMENT, ImpactType.REQUIRES_MONITORING],
                clinical_recommendations="Monitor levels, Adjust dose based on renal function",
                contraindication_status="Safe with dose adjustment"
            ),
            "confidence_level": ConfidenceLevel.HIGH,
            "data_source_type": DataSourceType.CLINICAL_STUDIES
        }

    def test_interaction_details_creation(self):
        """Test creating interaction details."""
        details = DrugDiseaseInteractionDetails(**self.details_data)
        self.assertIsNotNone(details.efficacy_impact)
        self.assertIsNotNone(details.safety_impact)

    def test_interaction_details_serialization(self):
        """Test serialization."""
        details = DrugDiseaseInteractionDetails(**self.details_data)
        data_dict = details.model_dump()
        self.assertIn("efficacy_impact", data_dict)
        self.assertIn("safety_impact", data_dict)
        self.assertIn("medicine_name", data_dict)


# ==================== Patient Friendly Summary Tests ====================

class TestPatientFriendlySummary(unittest.TestCase):
    """Test PatientFriendlySummary model."""

    def test_patient_summary_creation(self):
        """Test creating patient-friendly summary."""
        pfs = PatientFriendlySummary(
            simple_explanation="Your kidney disease may affect how your body processes this medication",
            what_patient_should_do="Tell your doctor about your kidney disease",
            signs_of_problems="Unusual fatigue, Dark urine, Nausea",
            when_to_contact_doctor="If you feel more tired than usual",
            lifestyle_modifications="Stay hydrated, Maintain healthy diet"
        )
        self.assertIn("kidney disease", pfs.simple_explanation.lower())

    def test_patient_summary_empty_side_effects(self):
        """Test summary with minimal side effects."""
        pfs = PatientFriendlySummary(
            simple_explanation="This combination is generally safe",
            what_patient_should_do="No special precautions needed",
            signs_of_problems="Standard side effects only",
            when_to_contact_doctor="For routine adverse effects",
            lifestyle_modifications="No specific modifications required"
        )
        self.assertIn("generally safe", pfs.simple_explanation)


# ==================== Complete Interaction Result Tests ====================

class TestDrugDiseaseInteractionResult(unittest.TestCase):
    """Test complete DrugDiseaseInteractionResult."""

    def setUp(self):
        """Set up test data."""
        self.result_data = {
            "interaction_details": DrugDiseaseInteractionDetails(
                medicine_name="Metformin",
                condition_name="Chronic Kidney Disease",
                overall_severity=InteractionSeverity.SIGNIFICANT,
                mechanism_of_interaction="Impaired renal clearance leads to drug accumulation",
                efficacy_impact=EfficacyImpact(
                    has_impact=True,
                    impact_description="Reduced effectiveness due to decreased clearance",
                    clinical_significance="May need to avoid"
                ),
                safety_impact=SafetyImpact(
                    has_impact=True,
                    impact_description="Lactic acidosis risk",
                    increased_side_effects="Lactic acidosis",
                    risk_level=InteractionSeverity.CONTRAINDICATED
                ),
                dosage_adjustment=DosageAdjustment(
                    adjustment_needed=True,
                    adjustment_type="contraindicated",
                    specific_recommendations="Contraindicated with eGFR <30 due to risk of lactic acidosis",
                    monitoring_parameters="eGFR, serum creatinine"
                ),
                management_strategy=ManagementStrategy(
                    impact_types=[ImpactType.CONTRAINDICATED],
                    clinical_recommendations="Switch to alternative antidiabetic, Use SGLT2i or GLP-1 agonist",
                    contraindication_status="Contraindicated with eGFR <30"
                ),
                confidence_level=ConfidenceLevel.HIGH,
                data_source_type=DataSourceType.CLINICAL_STUDIES,
                references="FDA guidance, Clinical studies on metformin nephrotoxicity"
            ),
            "technical_summary": "Metformin is contraindicated in chronic kidney disease with eGFR <30 due to risk of lactic acidosis",
            "patient_friendly_summary": PatientFriendlySummary(
                simple_explanation="Your kidney disease affects how your body processes metformin",
                what_patient_should_do="This medication may not be safe for you - ask your doctor about alternatives",
                signs_of_problems="Nausea, Unusual fatigue, Difficulty breathing, Muscle pain",
                when_to_contact_doctor="Immediately if you feel very tired, nauseous, or have difficulty breathing",
                lifestyle_modifications="Maintain hydration, Monitor kidney function regularly, Manage blood sugar with alternatives"
            ),
            "data_availability": DataAvailabilityInfo(
                data_available=True,
                reason=None
            )
        }

    def test_interaction_result_creation(self):
        """Test creating interaction result."""
        result = DrugDiseaseInteractionResult(**self.result_data)
        self.assertEqual(result.interaction_details.medicine_name, "Metformin")
        self.assertEqual(result.interaction_details.condition_name, "Chronic Kidney Disease")
        self.assertEqual(result.interaction_details.overall_severity, InteractionSeverity.SIGNIFICANT)

    def test_interaction_result_serialization(self):
        """Test serialization."""
        result = DrugDiseaseInteractionResult(**self.result_data)
        json_str = result.model_dump_json()
        self.assertIn("Metformin", json_str)
        self.assertIn("Kidney", json_str)

    def test_interaction_result_missing_field(self):
        """Test with missing required field."""
        incomplete = self.result_data.copy()
        del incomplete["technical_summary"]
        with self.assertRaises(ValidationError):
            DrugDiseaseInteractionResult(**incomplete)


# ==================== Realistic Scenario Tests ====================

class TestRealisticDrugDiseaseInteractions(unittest.TestCase):
    """Test realistic drug-disease interactions."""

    def test_metformin_kidney_disease(self):
        """Test metformin with chronic kidney disease."""
        result = DrugDiseaseInteractionResult(
            interaction_details=DrugDiseaseInteractionDetails(
                medicine_name="Metformin",
                condition_name="Chronic Kidney Disease",
                overall_severity=InteractionSeverity.CONTRAINDICATED,
                mechanism_of_interaction="Decreased renal clearance leads to drug accumulation and lactic acidosis risk",
                efficacy_impact=EfficacyImpact(
                    has_impact=True,
                    impact_description="Reduced effectiveness due to decreased renal clearance",
                    clinical_significance="Drug accumulation risk"
                ),
                safety_impact=SafetyImpact(
                    has_impact=True,
                    impact_description="Lactic acidosis risk",
                    increased_side_effects="Lactic acidosis, metabolic complications",
                    risk_level=InteractionSeverity.CONTRAINDICATED
                ),
                dosage_adjustment=DosageAdjustment(
                    adjustment_needed=True,
                    adjustment_type="contraindicated",
                    specific_recommendations="Contraindicated with eGFR <30 due to high risk of lactic acidosis",
                    monitoring_parameters="eGFR, serum creatinine"
                ),
                management_strategy=ManagementStrategy(
                    impact_types=[ImpactType.CONTRAINDICATED],
                    clinical_recommendations="Use alternative antidiabetic, SGLT2i or GLP-1 agonist preferred",
                    contraindication_status="Contraindicated with eGFR <30"
                ),
                confidence_level=ConfidenceLevel.HIGH,
                data_source_type=DataSourceType.CLINICAL_STUDIES
            ),
            technical_summary="Metformin is contraindicated in chronic kidney disease with eGFR <30",
            patient_friendly_summary=PatientFriendlySummary(
                simple_explanation="Your weak kidneys cannot clear metformin safely",
                what_patient_should_do="You need a different diabetes medicine",
                signs_of_problems="Severe nausea, Difficulty breathing, Unusual fatigue",
                when_to_contact_doctor="Immediately if symptoms occur",
                lifestyle_modifications="Monitor kidney function regularly, Manage blood sugar with alternatives"
            ),
            data_availability=DataAvailabilityInfo(data_available=True)
        )

        self.assertEqual(result.interaction_details.overall_severity, InteractionSeverity.CONTRAINDICATED)
        self.assertIn(ImpactType.CONTRAINDICATED, result.interaction_details.management_strategy.impact_types)

    def test_nsaid_heart_failure(self):
        """Test NSAIDs with heart failure."""
        result = DrugDiseaseInteractionResult(
            interaction_details=DrugDiseaseInteractionDetails(
                medicine_name="Ibuprofen",
                condition_name="Heart Failure",
                overall_severity=InteractionSeverity.SIGNIFICANT,
                mechanism_of_interaction="Fluid retention and reduced renal perfusion worsen heart failure",
                efficacy_impact=EfficacyImpact(
                    has_impact=True,
                    impact_description="Counteracted by heart failure effects",
                    clinical_significance="Pain relief offset by worsening cardiac condition"
                ),
                safety_impact=SafetyImpact(
                    has_impact=True,
                    impact_description="Heart failure exacerbation risk",
                    increased_side_effects="Fluid retention, dyspnea, cardiac decompensation",
                    risk_level=InteractionSeverity.SIGNIFICANT
                ),
                dosage_adjustment=DosageAdjustment(
                    adjustment_needed=True,
                    adjustment_type="contraindicated",
                    specific_recommendations="Avoid completely - increased mortality risk",
                    monitoring_parameters="Fluid status, weight, dyspnea"
                ),
                management_strategy=ManagementStrategy(
                    impact_types=[ImpactType.CONTRAINDICATED],
                    clinical_recommendations="Use acetaminophen instead, Consider topical NSAIDs",
                    contraindication_status="Avoid NSAIDs completely"
                ),
                confidence_level=ConfidenceLevel.HIGH,
                data_source_type=DataSourceType.CLINICAL_STUDIES
            ),
            technical_summary="NSAIDs are contraindicated in heart failure due to increased mortality risk",
            patient_friendly_summary=PatientFriendlySummary(
                simple_explanation="NSAIDs can make your heart condition worse",
                what_patient_should_do="Avoid all pain medications except acetaminophen",
                signs_of_problems="Shortness of breath, Swelling, Weight gain",
                when_to_contact_doctor="If you have any difficulty breathing or swelling",
                lifestyle_modifications="Limit salt intake, Monitor weight daily, Rest when needed"
            ),
            data_availability=DataAvailabilityInfo(data_available=True)
        )

        self.assertEqual(result.interaction_details.overall_severity, InteractionSeverity.SIGNIFICANT)

    def test_acei_hyperkalemia(self):
        """Test ACE inhibitors with hyperkalemia."""
        result = DrugDiseaseInteractionResult(
            interaction_details=DrugDiseaseInteractionDetails(
                medicine_name="Lisinopril",
                condition_name="Hyperkalemia",
                overall_severity=InteractionSeverity.CONTRAINDICATED,
                mechanism_of_interaction="ACE inhibitor reduces aldosterone, worsening hyperkalemia and risk of cardiac arrhythmias",
                efficacy_impact=EfficacyImpact(
                    has_impact=False,
                    impact_description="ACE inhibitor still controls blood pressure",
                    clinical_significance="Benefit offset by severe safety risk"
                ),
                safety_impact=SafetyImpact(
                    has_impact=True,
                    impact_description="Severe hyperkalemia and life-threatening cardiac arrhythmias",
                    increased_side_effects="Ventricular fibrillation, cardiac arrest, severe hyperkalemia",
                    risk_level=InteractionSeverity.CONTRAINDICATED
                ),
                dosage_adjustment=DosageAdjustment(
                    adjustment_needed=True,
                    adjustment_type="contraindicated",
                    specific_recommendations="Absolutely contraindicated",
                    monitoring_parameters="Potassium level, ECG, cardiac monitoring"
                ),
                management_strategy=ManagementStrategy(
                    impact_types=[ImpactType.CONTRAINDICATED],
                    clinical_recommendations="Use alternative antihypertensive, Treat underlying hyperkalemia first",
                    contraindication_status="Contraindicated"
                ),
                confidence_level=ConfidenceLevel.HIGH,
                data_source_type=DataSourceType.CLINICAL_GUIDELINES
            ),
            technical_summary="ACE inhibitors are contraindicated in hyperkalemia due to life-threatening cardiac risk",
            patient_friendly_summary=PatientFriendlySummary(
                simple_explanation="This blood pressure medication can dangerously raise your potassium levels",
                what_patient_should_do="You need a different blood pressure medication",
                signs_of_problems="Heart palpitations, Weakness, Numbness, Shortness of breath",
                when_to_contact_doctor="Immediately if you feel palpitations or weakness",
                lifestyle_modifications="Limit potassium-rich foods, Avoid salt substitutes, Regular ECG monitoring"
            ),
            data_availability=DataAvailabilityInfo(data_available=True)
        )

        self.assertEqual(result.interaction_details.overall_severity, InteractionSeverity.CONTRAINDICATED)

    def test_statins_liver_disease(self):
        """Test statins with liver disease."""
        result = DrugDiseaseInteractionResult(
            interaction_details=DrugDiseaseInteractionDetails(
                medicine_name="Atorvastatin",
                condition_name="Cirrhosis",
                overall_severity=InteractionSeverity.SIGNIFICANT,
                mechanism_of_interaction="Impaired hepatic metabolism with cirrhosis increases drug accumulation and hepatotoxicity",
                efficacy_impact=EfficacyImpact(
                    has_impact=True,
                    impact_description="Reduced effectiveness due to impaired hepatic metabolism",
                    clinical_significance="May not achieve lipid targets safely"
                ),
                safety_impact=SafetyImpact(
                    has_impact=True,
                    impact_description="Hepatotoxicity and statin-induced myopathy risk",
                    increased_side_effects="Elevated liver enzymes, myopathy, hepatic decompensation",
                    risk_level=InteractionSeverity.MODERATE
                ),
                dosage_adjustment=DosageAdjustment(
                    adjustment_needed=True,
                    adjustment_type="dose reduction",
                    specific_recommendations="Start with low dose, increase cautiously based on liver function",
                    monitoring_parameters="LFTs at baseline, 3 months, then every 6 months"
                ),
                management_strategy=ManagementStrategy(
                    impact_types=[ImpactType.REQUIRES_DOSE_ADJUSTMENT, ImpactType.REQUIRES_MONITORING],
                    clinical_recommendations="Use lowest effective dose, Monitor liver function closely, Check CK if symptomatic, Consider alternatives",
                    contraindication_status="Safe with caution and close monitoring"
                ),
                confidence_level=ConfidenceLevel.MODERATE,
                data_source_type=DataSourceType.CLINICAL_STUDIES
            ),
            technical_summary="Statins require careful dosing and monitoring in cirrhosis due to hepatotoxicity risk",
            patient_friendly_summary=PatientFriendlySummary(
                simple_explanation="Your liver condition requires careful monitoring with this medication",
                what_patient_should_do="You may need blood tests more often to check your liver",
                signs_of_problems="Muscle pain, Yellowing of skin or eyes, Dark urine, Unusual fatigue",
                when_to_contact_doctor="If you have muscle pain, yellowing, or unusual fatigue",
                lifestyle_modifications="Avoid alcohol completely, Maintain low saturated fat diet, Monitor symptoms daily"
            ),
            data_availability=DataAvailabilityInfo(data_available=True)
        )

        self.assertGreaterEqual(
            result.interaction_details.overall_severity.value,
            InteractionSeverity.MODERATE.value
        )


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
