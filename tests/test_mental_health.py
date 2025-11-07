"""
Tests for Mental Health Assessment Chat System.

Tests cover:
- Assessment schema validation
- Privacy and consent management
- Chat engine functionality
- Red flag detection
- Report generation
- Data retention policies
"""

import unittest
import json
import tempfile
from pathlib import Path
from datetime import datetime

from medkit.mental_health.mental_health_assessment import (
    PHQ9Assessment, GAD7Assessment, MoodSymptoms, AnxietySymptoms,
    CognitiveSymptoms, PhysicalSymptoms, TraumaSymptoms, PsychoticSymptoms,
    SubstanceUseIndicators, RiskAssessment, MentalHealthHistory,
    SocialFunctioning, MentalHealthCondition, TreatmentRecommendation,
    MentalHealthAssessment, ChatMessage, ChatSession, PrivacyConsent,
    AuditLog
)

from medkit.mental_health.mental_health_chat import MentalHealthChatEngine
from medkit.utils.privacy_compliance import PrivacyManager
from medkit.mental_health.mental_health_report import MentalHealthReportGenerator


# ==================== Assessment Schema Tests ====================

class TestPHQ9Assessment(unittest.TestCase):
    """Test PHQ-9 depression screening."""

    def test_phq9_minimal_depression(self):
        """Test PHQ-9 scoring for minimal depression."""
        phq9 = PHQ9Assessment(
            depressed_mood=0,
            sleep_disturbance=0,
            fatigue=0,
            appetite_change=0,
            guilt_shame=0,
            concentration=0,
            psychomotor=0,
            suicidal_ideation=0,
            functional_impairment=0
        )
        self.assertEqual(phq9.total_score, 0)
        self.assertEqual(phq9.severity, "minimal")

    def test_phq9_mild_depression(self):
        """Test PHQ-9 scoring for mild depression."""
        phq9 = PHQ9Assessment(
            depressed_mood=1,
            sleep_disturbance=1,
            fatigue=1,
            appetite_change=1,
            guilt_shame=1,
            concentration=0,
            psychomotor=0,
            suicidal_ideation=0,
            functional_impairment=0
        )
        self.assertEqual(phq9.total_score, 5)
        self.assertEqual(phq9.severity, "mild")

    def test_phq9_severe_depression(self):
        """Test PHQ-9 scoring for severe depression."""
        phq9 = PHQ9Assessment(
            depressed_mood=3,
            sleep_disturbance=3,
            fatigue=3,
            appetite_change=3,
            guilt_shame=3,
            concentration=3,
            psychomotor=3,
            suicidal_ideation=3,
            functional_impairment=3
        )
        self.assertEqual(phq9.total_score, 27)
        self.assertEqual(phq9.severity, "severe")

    def test_phq9_suicidal_ideation_detection(self):
        """Test suicidal ideation flag in PHQ-9."""
        phq9 = PHQ9Assessment(suicidal_ideation=3)
        self.assertEqual(phq9.suicidal_ideation, 3)
        self.assertGreaterEqual(phq9.total_score, 3)


class TestGAD7Assessment(unittest.TestCase):
    """Test GAD-7 anxiety screening."""

    def test_gad7_minimal_anxiety(self):
        """Test GAD-7 for minimal anxiety."""
        gad7 = GAD7Assessment(
            worry_frequency=0,
            worry_control=0,
            worry_concentration=0,
            irritability=0,
            restlessness=0,
            fatigue_anxiety=0,
            fear_catastrophe=0
        )
        self.assertEqual(gad7.total_score, 0)
        self.assertEqual(gad7.severity, "minimal")

    def test_gad7_moderate_anxiety(self):
        """Test GAD-7 for moderate anxiety."""
        gad7 = GAD7Assessment(
            worry_frequency=2,
            worry_control=2,
            worry_concentration=2,
            irritability=2,
            restlessness=1,
            fatigue_anxiety=1,
            fear_catastrophe=1
        )
        self.assertEqual(gad7.total_score, 11)
        self.assertEqual(gad7.severity, "moderate")


class TestMentalHealthAssessment(unittest.TestCase):
    """Test complete mental health assessment."""

    def setUp(self):
        """Set up test assessment."""
        self.assessment_data = {
            "session_id": "test-session-123",
            "patient_name": "John Doe",
            "age": 35,
            "gender": "Male",
            "chief_complaint": "Feeling depressed and anxious",
            "complaint_duration": "3 months",
            "complaint_onset": "gradual",
            "phq9_assessment": {
                "depressed_mood": 2, "sleep_disturbance": 2, "fatigue": 2,
                "appetite_change": 1, "guilt_shame": 1, "concentration": 1,
                "psychomotor": 0, "suicidal_ideation": 0, "functional_impairment": 1
            },
            "gad7_assessment": {
                "worry_frequency": 2, "worry_control": 1, "worry_concentration": 2,
                "irritability": 1, "restlessness": 1, "fatigue_anxiety": 1,
                "fear_catastrophe": 1
            },
            "mood_symptoms": {"persistent_depressed_mood": True, "anhedonia": False, "worthlessness": False, "hopelessness": False, "emotional_numbness": False, "irritability_mood": False, "mood_cycling": False, "elevated_mood_episodes": False, "grandiosity": False},
            "anxiety_symptoms": {"generalized_worry": True, "panic_attacks": False, "specific_phobias": False, "social_anxiety": False, "agoraphobia": False, "physical_tension": False, "sleep_anxiety": False, "avoidance_behaviors": False, "obsessions": False, "compulsions": False},
            "cognitive_symptoms": {"poor_concentration": False, "indecisiveness": False, "memory_problems": False, "racing_thoughts": False, "slow_thinking": False, "negative_self_talk": False, "cognitive_rigidity": False},
            "physical_symptoms": {"sleep_disturbance": True, "appetite_change": False, "fatigue": False, "psychomotor_retardation": False, "psychomotor_agitation": False, "physical_pain": False, "gastrointestinal_symptoms": False},
            "trauma_symptoms": {"intrusive_memories": False, "nightmares": False, "hypervigilance": False, "emotional_numbness": False, "avoidance": False, "blame_self": False, "negative_beliefs": False},
            "psychotic_symptoms": {"hallucinations": False, "delusions": False, "disorganized_speech": False, "disorganized_behavior": False, "thought_insertion": False, "thought_broadcasting": False, "paranoia": False},
            "substance_use": {
                "substance_use_frequency": "none", "substances_used": [], "age_of_first_use": None,
                "substance_induced_symptoms": False, "tolerance_development": False,
                "withdrawal_symptoms": False, "failed_reduction_attempts": False
            },
            "mental_health_history": {
                "previous_diagnoses": [], "age_of_onset": None, "previous_treatment": [],
                "hospitalization_history": 0, "medication_trials": [], "current_medications": [],
                "family_mental_health_history": [], "trauma_history": [], "significant_life_events": []
            },
            "social_functioning": {
                "relationship_quality": "good", "social_support_system": "adequate",
                "employment_status": "employed", "occupational_functioning": "functioning",
                "family_relationships": "stable", "living_situation": "with family"
            },
            "risk_assessment": {
                "suicidal_ideation": False, "suicidal_ideation_frequency": None,
                "suicide_plan_method": None, "access_to_means": None,
                "previous_suicide_attempts": 0, "self_harm_behavior": False,
                "harm_to_others": False, "violence_history": False,
                "substance_abuse_severity": "none", "homelessness_risk": False,
                "overall_risk_level": "low", "crisis_resources_aware": False
            },
            "primary_diagnosis": {
                "condition_name": "Major Depressive Disorder", "diagnostic_code_dsm5": "F32.9",
                "diagnostic_code_icd11": "6M84", "condition_type": "mood",
                "severity": "moderate", "duration": "3 months",
                "diagnostic_criteria_met": [], "confidence_level": "high"
            },
            "secondary_diagnoses": [],
            "treatment_recommendations": {
                "psychotherapy_types": ["CBT"], "medication_class_considerations": ["SSRI"],
                "lifestyle_interventions": ["Exercise", "Sleep hygiene"],
                "referral_type": "Psychiatry", "urgency_of_care": "routine",
                "emergency_contact_needed": False
            },
            "clinical_summary": "Patient presents with depressive symptoms",
            "clinical_notes": "Appears stable at this time"
        }

    def test_assessment_creation(self):
        """Test creating a mental health assessment."""
        assessment = MentalHealthAssessment(**self.assessment_data)
        self.assertEqual(assessment.patient_name, "John Doe")
        self.assertEqual(assessment.age, 35)
        self.assertEqual(assessment.phq9_assessment.total_score, 10)

    def test_assessment_high_suicide_risk(self):
        """Test assessment with high suicide risk."""
        data = self.assessment_data.copy()
        data["risk_assessment"]["suicidal_ideation"] = True
        data["risk_assessment"]["suicide_plan_method"] = "medication"
        data["risk_assessment"]["overall_risk_level"] = "high"

        assessment = MentalHealthAssessment(**data)
        self.assertTrue(assessment.risk_assessment.suicidal_ideation)
        self.assertEqual(assessment.risk_assessment.overall_risk_level, "high")


# ==================== Privacy & Consent Tests ====================

class TestPrivacyConsent(unittest.TestCase):
    """Test privacy consent handling."""

    def test_privacy_consent_creation(self):
        """Test creating privacy consent record."""
        consent = PrivacyConsent(
            user_name="Test User",
            consent_version="1.0",
            terms_accepted=True,
            privacy_policy_accepted=True,
            data_retention_understood=True,
            hipaa_notice_acknowledged=True,
            data_sharing_consent=False
        )
        self.assertEqual(consent.user_name, "Test User")
        self.assertTrue(consent.terms_accepted)
        self.assertTrue(consent.hipaa_notice_acknowledged)

    def test_consent_all_fields(self):
        """Test all consent fields."""
        consent = PrivacyConsent(
            user_name="Jane Doe",
            consent_version="1.0",
            terms_accepted=True,
            privacy_policy_accepted=True,
            data_retention_understood=True,
            hipaa_notice_acknowledged=True,
            data_sharing_consent=True,
            research_consent=True
        )
        self.assertTrue(consent.research_consent)


class TestAuditLog(unittest.TestCase):
    """Test audit logging."""

    def test_audit_log_creation(self):
        """Test creating audit log entry."""
        log = AuditLog(
            session_id="session-123",
            action="data_access",
            user_role="patient"
        )
        self.assertEqual(log.session_id, "session-123")
        self.assertEqual(log.action, "data_access")
        self.assertEqual(log.user_role, "patient")

    def test_audit_log_with_details(self):
        """Test audit log with additional details."""
        log = AuditLog(
            session_id="session-456",
            action="session_created",
            user_role="system",
            details="New patient session for John Doe"
        )
        self.assertIsNotNone(log.details)


class TestPrivacyManager(unittest.TestCase):
    """Test privacy and HIPAA compliance manager."""

    def setUp(self):
        """Set up temporary directory for tests."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.manager = PrivacyManager()

    def tearDown(self):
        """Clean up temporary directory."""
        self.temp_dir.cleanup()

    def test_session_id_generation(self):
        """Test session ID generation."""
        session_id_1 = self.manager.generate_session_id()
        session_id_2 = self.manager.generate_session_id()

        self.assertNotEqual(session_id_1, session_id_2)
        self.assertGreater(len(session_id_1), 20)

    def test_create_session(self):
        """Test creating a chat session."""
        session = self.manager.create_session("Test Patient", 40, "Female")
        self.assertEqual(session.patient_name, "Test Patient")
        self.assertEqual(session.age, 40)
        self.assertEqual(session.gender, "Female")

    def test_save_and_load_session(self):
        """Test saving and loading sessions."""
        # Create session
        session = self.manager.create_session("John Doe", 35, "Male")
        session_id = session.session_id

        # Save session
        saved_path = self.manager.save_session(session)
        self.assertTrue(saved_path.exists())

        # Load session
        loaded = self.manager.load_session(session_id)
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.patient_name, "John Doe")

    def test_mask_pii(self):
        """Test PII masking for logs."""
        text = "Contact patient at test@example.com or 555-123-4567"
        masked = self.manager.mask_pii(text)

        self.assertNotIn("test@example.com", masked)
        self.assertNotIn("555-123-4567", masked)
        self.assertIn("[EMAIL]", masked)
        self.assertIn("[PHONE]", masked)

    def test_cleanup_expired_data(self):
        """Test data retention cleanup."""
        # Create test sessions
        session1 = self.manager.create_session("Patient 1", 30, "M")
        self.manager.save_session(session1)

        # Run cleanup
        result = self.manager.cleanup_expired_data()
        self.assertIsInstance(result, dict)
        self.assertIn('sessions', result)


# ==================== Chat Engine Tests ====================

class TestMentalHealthChatEngine(unittest.TestCase):
    """Test chat engine functionality."""

    def setUp(self):
        """Set up chat engine."""
        self.engine = MentalHealthChatEngine()

    def test_initialize_session(self):
        """Test session initialization."""
        session = self.engine.initialize_session(
            "Jane Doe", 28, "Female", "Feeling anxious and overwhelmed"
        )
        self.assertEqual(session.patient_name, "Jane Doe")
        self.assertEqual(session.age, 28)
        self.assertEqual(session.session_status, "active")

    def test_red_flag_detection_suicidal(self):
        """Test detection of suicidal ideation red flag."""
        has_flags, flags, severity = self.engine.detect_red_flags(
            "I've been thinking about ending my life"
        )
        self.assertTrue(has_flags)
        self.assertIn("suicidal_ideation", flags)
        self.assertEqual(severity, "emergency")

    def test_red_flag_detection_self_harm(self):
        """Test detection of self-harm red flag."""
        has_flags, flags, severity = self.engine.detect_red_flags(
            "I've been cutting myself on my arms"
        )
        self.assertTrue(has_flags)
        self.assertIn("self_harm", flags)
        self.assertEqual(severity, "emergency")

    def test_red_flag_detection_psychotic(self):
        """Test detection of psychotic symptoms."""
        has_flags, flags, severity = self.engine.detect_red_flags(
            "I keep hearing voices that only I can hear"
        )
        self.assertTrue(has_flags)
        self.assertIn("psychotic_symptoms", flags)
        self.assertEqual(severity, "urgent")

    def test_red_flag_detection_false_negative(self):
        """Test normal conversation without red flags."""
        has_flags, flags, severity = self.engine.detect_red_flags(
            "I've been feeling a bit tired lately and having trouble sleeping"
        )
        self.assertFalse(has_flags)
        self.assertEqual(len(flags), 0)

    def test_get_session_info(self):
        """Test retrieving session information."""
        self.engine.initialize_session("Patient", 25, "M", "Anxiety")
        info = self.engine.get_session_info()

        self.assertEqual(info['patient_name'], "Patient")
        self.assertEqual(info['age'], 25)
        self.assertEqual(info['status'], "active")


# ==================== Report Generation Tests ====================

class TestMentalHealthReportGenerator(unittest.TestCase):
    """Test report generation."""

    def setUp(self):
        """Set up report generator with test assessment."""
        self.generator = MentalHealthReportGenerator()

        self.assessment_data = {
            "session_id": "test-123",
            "patient_name": "Test Patient",
            "age": 30,
            "gender": "Female",
            "chief_complaint": "Depression and anxiety",
            "complaint_duration": "2 months",
            "complaint_onset": "gradual",
            "phq9_assessment": {"depressed_mood": 2, "sleep_disturbance": 2,
                              "fatigue": 1, "appetite_change": 0, "guilt_shame": 0,
                              "concentration": 0, "psychomotor": 0,
                              "suicidal_ideation": 0, "functional_impairment": 0},
            "gad7_assessment": {"worry_frequency": 2, "worry_control": 1,
                              "worry_concentration": 1, "irritability": 0,
                              "restlessness": 0, "fatigue_anxiety": 0,
                              "fear_catastrophe": 0},
            "mood_symptoms": {"persistent_depressed_mood": True, "anhedonia": False, "worthlessness": False, "hopelessness": False, "emotional_numbness": False, "irritability_mood": False, "mood_cycling": False, "elevated_mood_episodes": False, "grandiosity": False},
            "anxiety_symptoms": {"generalized_worry": True, "panic_attacks": False, "specific_phobias": False, "social_anxiety": False, "agoraphobia": False, "physical_tension": False, "sleep_anxiety": False, "avoidance_behaviors": False, "obsessions": False, "compulsions": False},
            "cognitive_symptoms": {"poor_concentration": False, "indecisiveness": False, "memory_problems": False, "racing_thoughts": False, "slow_thinking": False, "negative_self_talk": False, "cognitive_rigidity": False},
            "physical_symptoms": {"sleep_disturbance": True, "appetite_change": False, "fatigue": False, "psychomotor_retardation": False, "psychomotor_agitation": False, "physical_pain": False, "gastrointestinal_symptoms": False},
            "trauma_symptoms": {"intrusive_memories": False, "nightmares": False, "hypervigilance": False, "emotional_numbness": False, "avoidance": False, "blame_self": False, "negative_beliefs": False},
            "psychotic_symptoms": {"hallucinations": False, "delusions": False, "disorganized_speech": False, "disorganized_behavior": False, "thought_insertion": False, "thought_broadcasting": False, "paranoia": False},
            "substance_use": {
                "substance_use_frequency": "none", "substances_used": [], "age_of_first_use": None,
                "substance_induced_symptoms": False, "tolerance_development": False,
                "withdrawal_symptoms": False, "failed_reduction_attempts": False
            },
            "mental_health_history": {
                "previous_diagnoses": [], "age_of_onset": None, "previous_treatment": [],
                "hospitalization_history": 0, "medication_trials": [], "current_medications": [],
                "family_mental_health_history": [], "trauma_history": [], "significant_life_events": []
            },
            "social_functioning": {
                "relationship_quality": "good", "social_support_system": "adequate",
                "employment_status": "employed", "occupational_functioning": "functioning",
                "family_relationships": "stable", "living_situation": "with family"
            },
            "risk_assessment": {
                "suicidal_ideation": False, "suicidal_ideation_frequency": None,
                "suicide_plan_method": None, "access_to_means": None,
                "previous_suicide_attempts": 0, "self_harm_behavior": False,
                "harm_to_others": False, "violence_history": False,
                "substance_abuse_severity": "none", "homelessness_risk": False,
                "overall_risk_level": "low", "crisis_resources_aware": False
            },
            "primary_diagnosis": {
                "condition_name": "Major Depressive Disorder", "diagnostic_code_dsm5": "F32.9",
                "diagnostic_code_icd11": "6M84", "condition_type": "mood",
                "severity": "mild", "duration": "2 months",
                "diagnostic_criteria_met": [], "confidence_level": "moderate"
            },
            "secondary_diagnoses": [],
            "treatment_recommendations": {
                "psychotherapy_types": ["CBT"], "medication_class_considerations": ["SSRI"],
                "lifestyle_interventions": ["Exercise"], "referral_type": "Psychology",
                "urgency_of_care": "routine", "emergency_contact_needed": False
            },
            "clinical_summary": "Patient with depressive symptoms",
            "clinical_notes": "Stable presentation"
        }

    def test_clinical_report_generation(self):
        """Test generating clinical report."""
        assessment = MentalHealthAssessment(**self.assessment_data)
        report = self.generator.generate_clinical_report(assessment)

        self.assertIn("MENTAL HEALTH CLINICAL ASSESSMENT REPORT", report)
        self.assertIn("Test Patient", report)
        self.assertIn("PHQ-9", report)
        self.assertIn("GAD-7", report)

    def test_patient_summary_generation(self):
        """Test generating patient-friendly summary."""
        assessment = MentalHealthAssessment(**self.assessment_data)
        summary = self.generator.generate_patient_summary(assessment)

        self.assertIn("MENTAL HEALTH ASSESSMENT SUMMARY", summary)
        self.assertIn("Depression Screening Score", summary)
        self.assertIn("HELPFUL RESOURCES", summary)

    def test_report_contains_diagnosis(self):
        """Test that report includes diagnosis information."""
        assessment = MentalHealthAssessment(**self.assessment_data)
        report = self.generator.generate_clinical_report(assessment)

        self.assertIn("Major Depressive Disorder", report)
        self.assertIn("F32.9", report)  # DSM-5 code

    def test_report_contains_recommendations(self):
        """Test that report includes treatment recommendations."""
        assessment = MentalHealthAssessment(**self.assessment_data)
        report = self.generator.generate_clinical_report(assessment)

        self.assertIn("TREATMENT RECOMMENDATIONS", report)
        self.assertIn("Psychotherapy", report)


# ==================== Integration Tests ====================

class TestMentalHealthSystemIntegration(unittest.TestCase):
    """Integration tests for complete mental health system."""

    def setUp(self):
        """Set up system components."""
        self.engine = MentalHealthChatEngine()
        self.privacy_manager = PrivacyManager()
        self.report_generator = MentalHealthReportGenerator()

    def test_full_workflow(self):
        """Test complete assessment workflow."""
        # 1. Create session
        session = self.privacy_manager.create_session("John Doe", 35, "Male")
        self.assertIsNotNone(session.session_id)

        # 2. Initialize chat
        self.engine.initialize_session("John Doe", 35, "Male", "Feeling depressed")
        self.assertIsNotNone(self.engine.session)

        # 3. Save session
        self.privacy_manager.save_session(session)
        saved_path = self.engine.save_session()
        self.assertTrue(saved_path.exists())

        # 4. Resume session
        loaded_engine = MentalHealthChatEngine()
        loaded_session = loaded_engine.resume_session(session.session_id)
        self.assertIsNotNone(loaded_session)
        self.assertEqual(loaded_session.patient_name, "John Doe")

    def test_emergency_protocol(self):
        """Test emergency handling workflow."""
        self.engine.initialize_session("Test", 30, "M", "Crisis support")

        has_flags, flags, severity = self.engine.detect_red_flags(
            "I want to kill myself right now"
        )

        self.assertTrue(has_flags)
        self.assertEqual(severity, "emergency")

        response = self.engine.handle_emergency(flags)
        self.assertIn("988", response)
        self.assertIn("emergency", response.lower())


# ==================== Main Test Runner ====================

if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
