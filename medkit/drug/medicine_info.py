"""
medicine_info.py - Comprehensive Medicine Information Generator

Generate comprehensive, evidence-based pharmaceutical documentation using structured
data models and the MedKit AI client with schema-aware prompting.

This module creates detailed medication information for patient education, clinical
reference, and medication counseling purposes.

QUICK START:
    from medicine_info import MedicineInfoGenerator, MedicineInfoConfig

    # Configure the analysis (settings only)
    config = MedicineInfoConfig(
        output_path=None,  # optional
        verbosity=False
    )

    # Create a generator and get the info
    med_info = MedicineInfoGenerator(config).generate(
        medicine="aspirin"
    )

    # Access different sections
    print(med_info.general_information.generic_name)
    print(med_info.general_information.brand_names)
    print(med_info.usage_and_administration.dosage_and_administration)

COMMON USES:
    1. Generate patient medication information sheets
    2. Create pharmacist counseling materials
    3. Provide clinical reference information
    4. Support medication selection decisions
    5. Generate medication safety information
    6. Create multilingual patient education materials

COVERAGE AREAS:
    - General information (names, strengths, forms)
    - Classification (therapeutic, pharmacological)
    - Uses and indications
    - Dosage and administration
    - Adverse effects and side effects
    - Drug interactions and contraindications
    - Precautions and warnings
    - Storage and handling
    - Special populations (pregnancy, elderly, pediatric)
"""

import sys
import json
import logging
from pathlib import Path
from dataclasses import dataclass, field
from pydantic import BaseModel, Field, validator
from typing import Optional

from medkit.core.medkit_client import MedKitClient
from medkit.utils.pydantic_prompt_generator import PromptStyle
from medkit.utils.logging_config import setup_logger
from medkit.utils.storage_config import StorageConfig

# Configure logging
logger = setup_logger(__name__)
logger.info("="*80)
logger.info("Medicine Info Module Initialized")
logger.info("="*80)

# ============================================================================
# CONFIGURATION
# ============================================================================

@dataclass
class MedicineInfoConfig(StorageConfig):
    """
    Configuration for generating medicine information.

    Inherits from StorageConfig for LMDB database settings:
    - db_path: Auto-generated path to medicine_info.lmdb
    - db_capacity_mb: Database capacity (default 500 MB)
    - db_store: Whether to cache results (default True)
    - db_overwrite: Whether to refresh cache (default False)
    """
    output_path: Optional[Path] = None
    output_dir: Path = field(default_factory=lambda: Path("outputs"))
    verbosity: bool = False  # If True, enable detailed debug logging
    prompt_style: PromptStyle = PromptStyle.DETAILED
    enable_cache: bool = True

    def __post_init__(self):
        """Set default db_path if not provided, then validate."""
        # Auto-generate db_path for this module if not set
        if self.db_path is None:
            self.db_path = str(
                Path(__file__).parent.parent / "storage" / "medicine_info.lmdb"
            )
        # Call parent validation
        super().__post_init__()


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class MedicineGeneralInformation(BaseModel):
    """Basic information about the medicine."""
    generic_name: str = Field(description="Generic name of the medicine")
    brand_names: str = Field(description="Brand names or trade names, comma-separated")
    active_ingredients: str = Field(description="Active pharmaceutical ingredients, comma-separated")
    common_strengths: str = Field(description="Available dosage strengths, comma-separated")
    forms_available: str = Field(description="Available pharmaceutical forms (tablet, capsule, liquid, injection, topical, etc.), comma-separated")


class TherapeuticClassification(BaseModel):
    """Classification of the medicine."""
    therapeutic_class: str = Field(description="Primary therapeutic class (e.g., Antivirals, Antihypertensives, Beta-blockers)")
    pharmacological_class: str = Field(description="Pharmacological class based on mechanism (e.g., ACE inhibitors, SSRIs, NSAIDs)")
    chemical_class: str = Field(description="Chemical classification based on structure (e.g., Benzimidazoles, Penicillins, Quinolones)")


class MedicineBackground(BaseModel):
    """Historical and mechanistic information."""
    mechanism_of_action: str = Field(description="How the medicine works at cellular/molecular level")
    history_of_medicine: str = Field(description="Historical development and approval of the medicine")


class Dosage(BaseModel):
    """Age-specific dosing recommendations."""
    pediatric_dosage: str = Field(description="Dosage for children/infants, often age or weight-based, comma-separated")
    adult_dosage: str = Field(description="Standard dosage for adult patients, comma-separated")
    geriatric_dosage: str = Field(description="Dosage for elderly patients, often requiring adjustments, comma-separated")


class AdministrationGuidance(BaseModel):
    """Instructions for different forms of administration."""
    liquid_oral_suspension: Optional[str] = Field(description="Instructions for liquid forms: shaking, measuring, storage after opening")
    tablet_capsule: Optional[str] = Field(description="Instructions for solid forms: swallowing, crushing, timing with food")
    injectable: Optional[str] = Field(description="Instructions for injections: preparation, route, handling")
    topical: Optional[str] = Field(description="Instructions for topical application: technique, coverage, frequency")


class UsageAndAdministration(BaseModel):
    """Dosing and administration information."""
    patient_suitability: str = Field(description="Appropriate patient types and conditions for which this medicine is suitable")
    dosage_and_administration: str = Field(description="General dosing guidelines and administration frequency")
    age_specific_dosage: Dosage
    administration_guidance: AdministrationGuidance
    storage_instruction: str = Field(description="Storage requirements, temperature ranges, and shelf life")


class DrugInteractions(BaseModel):
    """Drug and substance interactions."""
    drug_interactions: str = Field(description="Clinically significant interactions with other medicines, comma-separated")
    supplement_interactions: str = Field(description="Interactions with herbal supplements and remedies, comma-separated")
    food_interactions: str = Field(description="Known interactions with specific foods or beverages, comma-separated")
    alcohol_interactions: str = Field(description="Effects of alcohol consumption with this medicine")


class SafetyInformation(BaseModel):
    """Safety, side effects, and warnings."""
    boxed_warning: Optional[str] = Field(description="FDA black box warning if applicable")
    common_side_effects: str = Field(description="Temporary side effects commonly experienced, comma-separated")
    serious_side_effects: str = Field(description="Rare but serious adverse effects requiring immediate medical attention, comma-separated")
    interactions: DrugInteractions
    contraindications: str = Field(description="Conditions or situations where medicine should not be used, comma-separated")
    precautions: str = Field(description="Special precautions and warnings for specific patient groups, comma-separated")


class SpecialInstructions(BaseModel):
    """Special situation guidance."""
    missing_dose: str = Field(description="What to do if a dose is missed")
    overdose: str = Field(description="Symptoms and management of overdose")
    expired_medicine: str = Field(description="Effects and risks of using expired medicine")


class SpecialPopulations(BaseModel):
    """Considerations for special populations."""
    pregnancy: str = Field(description="Safety and effects during pregnancy, including FDA pregnancy category")
    breastfeeding: str = Field(description="Transfer to breast milk and safety while breastfeeding")
    renal_impairment: Optional[str] = Field(description="Dosage adjustments needed for patients with kidney disease")
    hepatic_impairment: Optional[str] = Field(description="Dosage adjustments needed for patients with liver disease")


class Efficacy(BaseModel):
    """Effectiveness and clinical outcomes."""
    efficacy_rates: str = Field(description="Clinical effectiveness or success rates from studies")
    onset_of_action: str = Field(description="How long it takes for the medicine to start working")
    duration_of_effect: str = Field(description="How long the effects typically last")
    therapeutic_outcomes: str = Field(description="Expected health improvements and symptom relief, comma-separated")


class Alternatives(BaseModel):
    """Alternative treatment options."""
    alternative_medicines: str = Field(description="Other medicines used for similar conditions, comma-separated")
    non_pharmacological_options: str = Field(description="Non-medication treatment alternatives, comma-separated")
    advantages_over_alternatives: str = Field(description="Why this medicine may be preferred, comma-separated")
    better_alternatives: Optional[str] = Field(description="Superior or more effective replacement medicines with reasons why they are better, comma-separated")


class MedicineEducation(BaseModel):
    """Patient education content."""
    plain_language_explanation: str = Field(description="Simple explanation of what this medicine does")
    key_takeaways: str = Field(description="3-5 most important points about the medicine, comma-separated")
    common_misconceptions: str = Field(description="Common myths or misunderstandings about this medicine, comma-separated")


class CostAndAvailability(BaseModel):
    """Financial and availability information."""
    typical_cost_range: str = Field(description="General cost range without insurance")
    insurance_coverage: str = Field(description="How typically covered by insurance")
    availability: str = Field(description="Prescription status (OTC, Rx, controlled substance) and availability by region")
    generic_availability: str = Field(description="Whether generic versions are available and relative costs")
    patient_assistance_programs: str = Field(description="Manufacturer assistance programs or discounts available, comma-separated")
    ban_status: Optional[str] = Field(description="Countries or regions where the medicine is banned or restricted, if applicable")


class MedicineEvidence(BaseModel):
    """Evidence-based information."""
    evidence_level: str = Field(description="Quality of evidence supporting this medicine (high, moderate, low)")
    clinical_studies: str = Field(description="Summary of major clinical trials and research findings")
    fda_approval_status: str = Field(description="FDA approval status and indication approved")
    approval_dates: Optional[str] = Field(description="FDA and other regulatory approval dates (e.g., FDA approval date, EMA approval date, WHO approval date), comma-separated")


class MedicineResearch(BaseModel):
    """Current research and innovations."""
    recent_advancements: str = Field(description="Recent developments in formulation or delivery, comma-separated")
    ongoing_research: str = Field(description="Current clinical trials or research areas, comma-separated")
    future_developments: str = Field(description="Potential future improvements or new formulations, comma-separated")


class MedicineInfoResult(BaseModel):
    """
    Comprehensive pharmaceutical medicine information.

    Organized as a collection of BaseModel sections, each representing
    a distinct aspect of medicine documentation.
    """
    # Core identification
    general_information: MedicineGeneralInformation

    # Classification and background
    classification: TherapeuticClassification
    background: MedicineBackground

    # Usage and administration
    usage_and_administration: UsageAndAdministration

    # Safety and interactions
    safety: SafetyInformation
    special_instructions: SpecialInstructions

    # Specific populations
    special_populations: SpecialPopulations

    # Efficacy and alternatives
    efficacy: Efficacy
    alternatives: Alternatives

    # Patient communication
    education: MedicineEducation

    # Financial and availability
    cost_and_availability: CostAndAvailability

    # Evidence-based information
    evidence: MedicineEvidence

    # Research and innovation
    research: MedicineResearch


# ============================================================================
# MEDICINE INFO GENERATOR
# ============================================================================


class MedicineInfoGenerator:
    """Generates comprehensive medicine information based on provided configuration."""

    def __init__(self, config: MedicineInfoConfig):
        self.config = config

        # Load model name from ModuleConfig
        model_name = "gemini-1.5-flash"  # Default model for this module

        self.client = MedKitClient(model_name=model_name)
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

        # Apply verbosity to logger
        if self.config.verbosity:
            logger.setLevel("DEBUG")
        else:
            logger.setLevel("INFO")

        logger.info(f"Initialized MedicineInfoGenerator")
        if self.config.verbosity:
            logger.debug(f"Config: {self.config}")

    def generate(
        self,
        medicine: str,
        patient_age: Optional[int] = None,
        medical_conditions: Optional[str] = None,
    ) -> MedicineInfoResult:
        """
        Generates comprehensive medicine information.

        Args:
            medicine: Name of the medicine
            patient_age: Patient's age in years (optional)
            medical_conditions: Patient's medical conditions (optional, comma-separated)

        Returns:
            MedicineInfoResult: Validated medicine information object
        """
        # Validate inputs
        if not medicine or not str(medicine).strip():
            raise ValueError("Medicine name cannot be empty")
        if patient_age is not None and (patient_age < 0 or patient_age > 150):
            raise ValueError("Age must be between 0 and 150 years")

        logger.info("-" * 80)
        logger.info(f"Starting medicine information generation")
        logger.info(f"Medicine Name: {medicine}")
        logger.info(f"Prompt Style: {self.config.prompt_style.value if hasattr(self.config.prompt_style, 'value') else self.config.prompt_style}")

        # Determine output path
        output_path = self.config.output_path
        if output_path is None:
            output_path = self.config.output_dir / f"{medicine.lower().replace(' ', '_')}_info.json"
        else:
            output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output path: {output_path}")

        # Build context
        context_parts = [f"Generating information for {medicine}"]
        if patient_age is not None:
            context_parts.append(f"Patient age: {patient_age} years")
            logger.info(f"Patient age provided: {patient_age}")
        if medical_conditions:
            context_parts.append(f"Patient conditions: {medical_conditions}")
            logger.info(f"Patient conditions provided: {medical_conditions}")

        context = ". ".join(context_parts) + "."
        logger.debug(f"Context: {context}")

        # Generate medicine information
        logger.info("Calling MedKitClient.generate_text()...")
        try:
            prompt = f"Generate comprehensive information for the medicine: {medicine}. {context}"
            logger.debug(f"Prompt: {prompt}")

            result = self.client.generate_text(
                prompt=prompt,
                schema=MedicineInfoResult,
            )

            logger.info(f"✓ Successfully generated medicine information")
            logger.info(f"Generic name: {result.general_information.generic_name}")
            logger.info(f"Brand names: {result.general_information.brand_names}")
            logger.info(f"Available forms: {result.general_information.forms_available}")
            logger.info("-" * 80)
            return result
        except Exception as e:
            logger.error(f"✗ Error generating medicine information: {e}")
            logger.exception("Full exception details:")
            logger.info("-" * 80)
            raise

    def save(self, medicine_info: MedicineInfoResult, output_path: str):
        """
        Saves the medicine information to a JSON file.

        Args:
            medicine_info: The MedicineInfoResult object to save
            output_path: Path where the JSON file should be saved
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Saving medicine information to: {output_file}")

        try:
            with open(output_file, "w") as f:
                json.dump(medicine_info.model_dump(), f, indent=2)
            file_size = output_file.stat().st_size
            logger.info(f"✓ Successfully saved medicine information")
            logger.info(f"File: {output_file}")
            logger.info(f"File size: {file_size} bytes")
        except Exception as e:
            logger.error(f"✗ Error saving medicine information: {e}")
            logger.exception("Full exception details:")
            raise


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_medicine_info(
    medicine: str,
    config: MedicineInfoConfig,
    patient_age: Optional[int] = None,
    medical_conditions: Optional[str] = None,
) -> Optional[MedicineInfoResult]:
    """
    Get comprehensive medicine information.

    This is a convenience function that instantiates and runs the
    MedicineInfoGenerator.

    Args:
        medicine: Name of the medicine
        config: Configuration object for the generation
        patient_age: Patient's age in years (optional)
        medical_conditions: Patient's medical conditions (optional)

    Returns:
        MedicineInfoResult: The result of the generation, or None if it fails
    """
    try:
        generator = MedicineInfoGenerator(config)
        return generator.generate(
            medicine=medicine,
            patient_age=patient_age,
            medical_conditions=medical_conditions,
        )
    except Exception as e:
        logger.error(f"Failed to generate medicine information: {e}")
        return None


# ============================================================================
# CLI INTERFACE
# ============================================================================

import argparse

import hashlib
from medkit.utils.lmdb_storage import LMDBStorage, LMDBConfig


def main():
    """
    CLI entry point for generating medicine information.
    """
    logger.info("="*80)
    logger.info("MEDICINE INFO CLI - Starting")
    logger.info("="*80)

    parser = argparse.ArgumentParser(
        description="Generate comprehensive medicine information.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python medicine_info.py -m aspirin
  python medicine_info.py -m "ibuprofen" -o output.json -v
  python medicine_info.py -m "metformin" -a 65 --conditions "diabetes, hypertension"
        """
    )
    parser.add_argument(
        "-m", "--medicine",
        required=True,
        help="The name of the medicine to generate information for."
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to save the output JSON file."
    )
    parser.add_argument(
        "-a", "--age",
        type=int,
        help="Patient age for context-specific information."
    )
    parser.add_argument(
        "-c", "--conditions",
        help="Comma-separated list of patient medical conditions."
    )
    parser.add_argument(
        "-d", "--output-dir",
        default="outputs",
        help="Directory for output files (default: outputs)."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose/debug logging output."
    )

    args = parser.parse_args()

    # Create configuration
    config = MedicineInfoConfig(
        output_path=Path(args.output) if args.output else None,
        output_dir=Path(args.output_dir),
        verbosity=args.verbose
    )

    logger.info(f"CLI Arguments:")
    logger.info(f"  Medicine: {args.medicine}")
    logger.info(f"  Age: {args.age if args.age else 'Not specified'}")
    logger.info(f"  Conditions: {args.conditions if args.conditions else 'None'}")
    logger.info(f"  Output Dir: {args.output_dir}")
    logger.info(f"  Output File: {args.output if args.output else 'Default'}")
    logger.info(f"  Verbose: {args.verbose}")

    # Generate medicine information
    try:
        generator = MedicineInfoGenerator(config)
        medicine_info = generator.generate(
            medicine=args.medicine,
            patient_age=args.age,
            medical_conditions=args.conditions,
        )

        if medicine_info is None:
            logger.error("✗ Failed to generate medicine information.")
            sys.exit(1)

        # Save if output path is specified
        if args.output:
            generator.save(medicine_info, args.output)
        else:
            # Save to default location
            default_path = config.output_dir / f"{args.medicine.lower().replace(' ', '_')}_info.json"
            generator.save(medicine_info, str(default_path))

        logger.info("="*80)
        logger.info("✓ Medicine information generation completed successfully")
        logger.info("="*80)
    except Exception as e:
        logger.error("="*80)
        logger.error(f"✗ Medicine information generation failed: {e}")
        logger.exception("Full exception details:")
        logger.error("="*80)
        sys.exit(1)


if __name__ == "__main__":
    main()
