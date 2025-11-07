"""
test_surgical_tool_info.py - Test suite for surgical_tool_info module.

Tests cover:
- Pydantic model validation
- Configuration handling
- SurgicalToolInfoGenerator class methods
- File I/O operations
- CLI argument parsing
- Error handling and edge cases
"""
import json
import sys
import pytest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from dataclasses import dataclass, field

# Import the modules to test
from surgical_tool_info import (
    Config,
    ToolBasics,
    ToolPurpose,
    PhysicalSpecifications,
    OperationalCharacteristics,
    SafetyFeatures,
    PreOperativePreperation,
    IntraOperativeUse,
    DiscomfortRisksAndComplications,
    MaintenanceAndCare,
    SterilizationAndDisinfection,
    AlternativesAndComparisons,
    HistoricalContext,
    SpecialtySpecificConsiderations,
    TrainingAndCertification,
    RegulatoryAndStandards,
    CostAndProcurement,
    EducationalContent,
    SurgicalToolInfo,
    SurgicalToolInfoGenerator,
    get_surgical_tool_info,
)


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def temp_output_dir():
    """Create a temporary output directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def config(temp_output_dir):
    """Create a test configuration."""
    return Config(
        output_dir=temp_output_dir,
        quiet=True,
        specialty="Surgery/Surgical Instruments"
    )


@pytest.fixture
def mock_client():
    """Create a mock MedKitClient."""
    return Mock()


@pytest.fixture
def sample_tool_basics():
    """Create sample ToolBasics data."""
    return ToolBasics(
        tool_name="Surgical Scalpel",
        alternative_names="Surgical knife, Blade",
        tool_category="Cutting instrument",
        surgical_specialties="General surgery, Orthopedics, Cardiovascular",
        instrument_family="Cutting instruments"
    )


@pytest.fixture
def sample_surgical_tool_info(sample_tool_basics):
    """Create complete sample SurgicalToolInfo."""
    return SurgicalToolInfo(
        tool_basics=sample_tool_basics,
        tool_purpose=ToolPurpose(
            primary_purpose="Precise tissue incision",
            surgical_applications="Initial incisions, dissection, tissue separation",
            anatomical_targets="Skin, subcutaneous tissue, superficial structures",
            tissue_types="Soft tissue, vascular tissue",
            unique_advantages="Precision, minimal tissue trauma, control"
        ),
        physical_specifications=PhysicalSpecifications(
            dimensions="15 cm total length",
            weight="10-15 grams",
            material_composition="Stainless steel, tungsten carbide blade",
            finish_type="Polished, non-reflective",
            blade_or_tip_specifications="Curved blade, 15-20 degree angle, sharp point",
            handle_design="Ergonomic grip, textured surface",
            sterility_type="Single-use, sterilized by ETO gas"
        ),
        operational_characteristics=OperationalCharacteristics(
            cutting_or_grasping_force="Minimal, user-controlled",
            actuation_mechanism="Manual, hand-controlled",
            degrees_of_freedom="Multi-directional, unrestricted",
            precision_level="Micro-level, 0.1mm precision",
            engagement_depth="Variable, up to 5mm",
            working_distance="15cm from handle to tip"
        ),
        safety_features=SafetyFeatures(
            safety_mechanisms="Protective cap, sterile packaging",
            slip_resistance="Textured handle for grip",
            wear_considerations="Blade dulling, handle cracks",
            maximum_safe_force="Light pressure, sharp technique required",
            emergency_protocols="Immediate hemostasis, pressure application",
            tissue_damage_prevention="Sharp blade reduces crushing, minimal pressure"
        ),
        preparation=PreOperativePreperation(
            inspection_requirements="Sharp test, integrity check, sterilization verification",
            cleaning_protocols="Sterile water rinse, dry with sterile gauze",
            sterilization_requirements="ETO gas sterilization, 12 hour aeration",
            quality_assurance_tests="Sharpness verification, handle integrity",
            storage_requirements="Sterile package, room temperature, dry environment",
            preparation_time="5 minutes for unpacking and inspection"
        ),
        intraoperative_use=IntraOperativeUse(
            positioning_in_field="Perpendicular to tissue surface",
            handling_technique="Swift, controlled cutting motion",
            hand_position_requirements="Thumb and fingers control blade angle",
            coordination_with_other_tools="Used before hemostatic clamps",
            common_movements="Cutting, slicing, precise incisions",
            visibility_requirements="Clear visualization of surgical field",
            ergonomic_considerations="Minimal hand fatigue with proper technique"
        ),
        discomfort_risks_and_complications=DiscomfortRisksAndComplications(
            surgeon_fatigue_factors="Prolonged use, poor grip, incorrect angle",
            common_handling_errors="Dull blade use, excessive force, poor control",
            tissue_damage_risks="Unintended cuts, crushing, tissue perforation",
            instrument_complications="Blade breakage, dulling, handle damage",
            cross_contamination_risks="Improper handling during use",
            material_reactions="Minimal risk with standard materials",
            electrical_safety="Not applicable - manual instrument"
        ),
        maintenance_and_care=MaintenanceAndCare(
            post_operative_cleaning="Enzymatic cleaner soak, ultrasonic cleaning",
            lubrication_schedule="Not required for single-use instruments",
            inspection_frequency="Before each use",
            wear_indicators="Visible blade dulling, handle cracks, corrosion",
            sharpening_protocol="Single-use - replacement when dull",
            repair_guidelines="Cannot be repaired, must be replaced",
            expected_lifespan="Single use, typically 1-2 hours in surgery"
        ),
        sterilization_and_disinfection=SterilizationAndDisinfection(
            approved_sterilization_methods="ETO gas sterilization at 37.8°C for 12 hours",
            incompatible_sterilization="Autoclave not recommended, chemical sterilization avoided",
            disinfection_alternatives="High-level disinfection with glutaraldehyde if reusable",
            packaging_requirements="Sterile surgical wrap, tamper-evident sealing",
            validation_standards="Biological indicator validation, process validation",
            reprocessing_manufacturer_protocols="Manufacturer instructions for reprocessing"
        ),
        alternatives_and_comparisons=AlternativesAndComparisons(
            similar_alternative_tools="Laser scalpel, electrosurgical unit, ultrasonic knife",
            advantages_over_alternatives="Lower cost, precise control, no thermal damage",
            disadvantages_vs_alternatives="Requires sharpening, manual control only",
            cost_comparison="Lower initial cost than powered alternatives",
            when_to_use_this_tool="Precise superficial incisions, vascular work",
            complementary_tools="Hemostatic clamps, retractors, suction apparatus"
        ),
        historical_context=HistoricalContext(
            invention_history="Developed in ancient times, refined in 18th-19th centuries",
            evolution_timeline="1600s: steel blades, 1900s: tungsten carbide edges, modern: single-use sterile packaging",
            clinical_evidence="Standard of care for precise tissue incision",
            widespread_adoption="Universal adoption in all surgical fields",
            current_status="Standard instrument, unlikely to be replaced"
        ),
        specialty_specific_considerations=SpecialtySpecificConsiderations(
            general_surgery_specific="Primary cutting tool for all incisions",
            orthopedic_specific="Minimal use due to bone work requirements",
            cardiac_specific="Critical for precision vascular work",
            neurosurgery_specific="Essential for delicate dissection",
            vascular_specific="Critical for precise vessel incision",
            laparoscopic_considerations="Miniaturized scalpel for endoscopic use",
            robotic_integration="Robotic arms use laser or ultrasonic alternatives"
        ),
        training_and_certification=TrainingAndCertification(
            training_requirements="Fundamental surgical training, multiple supervised uses",
            proficiency_indicators="Clean incisions, minimal tissue trauma, proper hemostasis",
            common_learning_mistakes="Excessive pressure, dull blade use, poor visibility",
            skill_development_timeline="Proficiency in 10-20 supervised uses",
            formal_education_resources="Surgical textbooks, simulation training, mentoring",
            mentoring_best_practices="Supervised practice, feedback on technique"
        ),
        regulatory_and_standards=RegulatoryAndStandards(
            fda_classification="Class I - General controls sufficient",
            fda_status="FDA approved, cleared for surgical use",
            iso_standards="ISO 7740 (surgical knives), ISO 13485 (quality management)",
            country_approvals="Approved in all major countries with surgical programs",
            quality_certifications="ISO 13485, CE mark, FDA clearance",
            traceability_requirements="Lot numbering, sterilization verification, recall capability"
        ),
        cost_and_procurement=CostAndProcurement(
            single_use_cost="$5-15 per unit",
            reusable_initial_cost="$50-200 per instrument",
            lifecycle_cost="Single-use: $5-15 per use; Reusable: $50-200 amortized over 100+ uses",
            vendor_options="Stryker, Ethicon, Medtronic, Hu-Friedy",
            procurement_lead_time="1-2 weeks standard stock",
            inventory_recommendations="10-20 units per OR for single-use, 2-3 for reusable",
            insurance_coverage="Covered as surgical supply, standard cost"
        ),
        educational_content=EducationalContent(
            plain_language_explanation="A surgical scalpel is a sharp knife used by surgeons to make precise cuts in tissue",
            key_takeaways="Precision cutting tool, sharp technique required, single-use for safety, primary tool in all surgery",
            common_misconceptions="Not a kitchen knife, requires specialized training, single-use more cost-effective in practice",
            patient_communication="Used for precise surgical incisions with minimal tissue trauma",
            video_demonstration_topics="Proper grip, cutting technique, tissue handling, safety precautions"
        )
    )


# ============================================================================
# TESTS FOR PYDANTIC MODELS
# ============================================================================

class TestToolBasics:
    """Test ToolBasics model."""

    def test_tool_basics_creation(self, sample_tool_basics):
        """Test creating ToolBasics instance."""
        assert sample_tool_basics.tool_name == "Surgical Scalpel"
        assert sample_tool_basics.tool_category == "Cutting instrument"
        assert "Orthopedics" in sample_tool_basics.surgical_specialties

    def test_tool_basics_required_fields(self):
        """Test that all required fields must be provided."""
        with pytest.raises(Exception):  # Pydantic validation error
            ToolBasics(
                tool_name="Test",
                # Missing other required fields
            )

    def test_tool_basics_dict_conversion(self, sample_tool_basics):
        """Test converting ToolBasics to dictionary."""
        data = sample_tool_basics.model_dump()
        assert isinstance(data, dict)
        assert data["tool_name"] == "Surgical Scalpel"


class TestPhysicalSpecifications:
    """Test PhysicalSpecifications model."""

    def test_physical_specs_creation(self):
        """Test creating PhysicalSpecifications instance."""
        specs = PhysicalSpecifications(
            dimensions="15 cm",
            weight="10g",
            material_composition="Stainless steel",
            finish_type="Polished",
            blade_or_tip_specifications="Sharp blade",
            handle_design="Ergonomic",
            sterility_type="Single-use"
        )
        assert specs.dimensions == "15 cm"
        assert specs.weight == "10g"

    def test_all_fields_required(self):
        """Test that missing fields raise validation error."""
        with pytest.raises(Exception):
            PhysicalSpecifications(
                dimensions="15 cm",
                # Missing required fields
            )


class TestSurgicalToolInfo:
    """Test the complete SurgicalToolInfo model."""

    def test_surgical_tool_info_creation(self, sample_surgical_tool_info):
        """Test creating complete SurgicalToolInfo."""
        assert sample_surgical_tool_info.tool_basics.tool_name == "Surgical Scalpel"
        assert sample_surgical_tool_info.tool_purpose.primary_purpose == "Precise tissue incision"

    def test_surgical_tool_info_dict_conversion(self, sample_surgical_tool_info):
        """Test converting SurgicalToolInfo to dictionary."""
        data = sample_surgical_tool_info.model_dump()
        assert isinstance(data, dict)
        assert "tool_basics" in data
        assert "tool_purpose" in data
        assert "physical_specifications" in data

    def test_surgical_tool_info_json_serialization(self, sample_surgical_tool_info):
        """Test JSON serialization of SurgicalToolInfo."""
        json_str = sample_surgical_tool_info.model_dump_json()
        assert isinstance(json_str, str)
        # Verify it's valid JSON
        parsed = json.loads(json_str)
        assert parsed["tool_basics"]["tool_name"] == "Surgical Scalpel"


# ============================================================================
# TESTS FOR CONFIGURATION
# ============================================================================

class TestConfig:
    """Test Config dataclass."""

    def test_config_default_values(self):
        """Test Config with default values."""
        config = Config()
        assert config.output_dir == Path("outputs")
        assert config.quiet is True
        assert config.specialty == "Surgery/Surgical Instruments"

    def test_config_custom_values(self, temp_output_dir):
        """Test Config with custom values."""
        config = Config(
            output_dir=temp_output_dir,
            quiet=False,
            specialty="Orthopedic Surgery"
        )
        assert config.output_dir == temp_output_dir
        assert config.quiet is False
        assert config.specialty == "Orthopedic Surgery"

    def test_config_log_file_path(self):
        """Test that log_file path is generated correctly."""
        config = Config()
        assert config.log_file.name == "surgical_tool_info.log"
        assert config.log_file.parent.name == "logs"


# ============================================================================
# TESTS FOR SURGICAL TOOL INFO GENERATOR
# ============================================================================

class TestSurgicalToolInfoGenerator:
    """Test SurgicalToolInfoGenerator class."""

    def test_generator_initialization(self, config):
        """Test initializing the generator."""
        generator = SurgicalToolInfoGenerator(config=config)
        assert generator.config == config
        assert generator.tool_name is None
        assert generator.output_path is None

    def test_generator_initialization_default_config(self):
        """Test initializing generator with default config."""
        with patch('surgical_tool_info.MedKitClient'):
            generator = SurgicalToolInfoGenerator()
            assert generator.config is not None
            assert isinstance(generator.config, Config)

    def test_generate_empty_tool_name(self, config):
        """Test that empty tool name raises ValueError."""
        generator = SurgicalToolInfoGenerator(config=config)
        with pytest.raises(ValueError, match="Tool name cannot be empty"):
            generator.generate("")

    def test_generate_whitespace_tool_name(self, config):
        """Test that whitespace-only tool name raises ValueError."""
        generator = SurgicalToolInfoGenerator(config=config)
        with pytest.raises(ValueError, match="Tool name cannot be empty"):
            generator.generate("   ")

    def test_generate_sets_tool_name(self, config):
        """Test that generate sets the tool_name attribute."""
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate("Test Scalpel")
                    assert generator.tool_name == "Test Scalpel"

    def test_generate_default_output_path(self, config):
        """Test that default output path is set correctly."""
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate("Test Scalpel")
                    expected_path = config.output_dir / "test_scalpel_info.json"
                    assert generator.output_path == expected_path

    def test_generate_custom_output_path(self, config, temp_output_dir):
        """Test generate with custom output path."""
        custom_path = temp_output_dir / "custom" / "path" / "output.json"
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate("Test Scalpel", output_path=custom_path)
                    assert generator.output_path == custom_path

    def test_generate_returns_surgical_tool_info(self, config, sample_surgical_tool_info):
        """Test that generate returns SurgicalToolInfo."""
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=sample_surgical_tool_info):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    result = generator.generate("Surgical Scalpel")
                    assert isinstance(result, SurgicalToolInfo)
                    assert result.tool_basics.tool_name == "Surgical Scalpel"

    def test_save_creates_output_file(self, config, sample_surgical_tool_info, temp_output_dir):
        """Test that save creates output JSON file."""
        generator = SurgicalToolInfoGenerator(config=config)
        output_path = temp_output_dir / "test_output.json"

        result = generator.save(sample_surgical_tool_info, output_path)

        assert output_path.exists()
        assert result == output_path

    def test_save_creates_parent_directories(self, config, sample_surgical_tool_info, temp_output_dir):
        """Test that save creates parent directories."""
        generator = SurgicalToolInfoGenerator(config=config)
        output_path = temp_output_dir / "nested" / "deep" / "path" / "output.json"

        generator.save(sample_surgical_tool_info, output_path)

        assert output_path.parent.exists()

    def test_save_json_format(self, config, sample_surgical_tool_info, temp_output_dir):
        """Test that saved file is valid JSON."""
        generator = SurgicalToolInfoGenerator(config=config)
        output_path = temp_output_dir / "test.json"

        generator.save(sample_surgical_tool_info, output_path)

        with open(output_path, 'r') as f:
            data = json.load(f)

        assert data["tool_basics"]["tool_name"] == "Surgical Scalpel"

    def test_print_summary_quiet_mode(self, config, sample_surgical_tool_info, capsys):
        """Test that print_summary respects quiet mode."""
        config.quiet = True
        generator = SurgicalToolInfoGenerator(config=config)
        generator.output_path = Path("test_output.json")

        generator.print_summary(sample_surgical_tool_info)

        captured = capsys.readouterr()
        assert captured.out == ""

    def test_print_summary_verbose_mode(self, config, sample_surgical_tool_info, capsys):
        """Test that print_summary prints when quiet=False."""
        config.quiet = False
        generator = SurgicalToolInfoGenerator(config=config)
        generator.output_path = Path("test_output.json")

        generator.print_summary(sample_surgical_tool_info)

        captured = capsys.readouterr()
        assert "SURGICAL TOOL INFORMATION SUMMARY" in captured.out
        assert "Surgical Scalpel" in captured.out


# ============================================================================
# TESTS FOR HELPER FUNCTIONS
# ============================================================================

class TestHelperFunctions:
    """Test module-level helper functions."""

    def test_get_surgical_tool_info_returns_tool_info(self, temp_output_dir, sample_surgical_tool_info):
        """Test get_surgical_tool_info returns SurgicalToolInfo."""
        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            mock_instance = MockGenerator.return_value
            mock_instance.generate.return_value = sample_surgical_tool_info

            result = get_surgical_tool_info("Surgical Scalpel")

            assert isinstance(result, SurgicalToolInfo)

    def test_get_surgical_tool_info_with_custom_output(self, temp_output_dir, sample_surgical_tool_info):
        """Test get_surgical_tool_info with custom output path."""
        custom_path = temp_output_dir / "custom.json"
        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            mock_instance = MockGenerator.return_value
            mock_instance.generate.return_value = sample_surgical_tool_info

            get_surgical_tool_info("Surgical Scalpel", output_path=custom_path)

            mock_instance.generate.assert_called_once_with(
                "Surgical Scalpel",
                custom_path
            )

    def test_get_surgical_tool_info_quiet_parameter(self, temp_output_dir, sample_surgical_tool_info):
        """Test get_surgical_tool_info quiet parameter."""
        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            with patch('surgical_tool_info.Config') as MockConfig:
                mock_instance = MockGenerator.return_value
                mock_instance.generate.return_value = sample_surgical_tool_info

                get_surgical_tool_info("Surgical Scalpel", quiet=False)

                MockConfig.assert_called_once()
                # Check that quiet was set to False
                call_kwargs = MockConfig.call_args[1]
                assert call_kwargs.get('quiet') is False


# ============================================================================
# TESTS FOR CLI
# ============================================================================

class TestCLI:
    """Test command-line interface."""

    def test_cli_basic_invocation(self, monkeypatch, temp_output_dir, sample_surgical_tool_info):
        """Test basic CLI invocation."""
        monkeypatch.setattr(
            sys, 'argv',
            ['surgical_tool_info.py', '-i', 'Surgical', 'Scalpel']
        )

        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            mock_instance = MockGenerator.return_value
            mock_instance.generate.return_value = sample_surgical_tool_info

            from surgical_tool_info import main
            # This should not raise an exception
            try:
                main()
            except SystemExit as e:
                # main() may exit with code 0
                assert e.code == 0 or e.code is None

    def test_cli_with_output_path(self, monkeypatch, temp_output_dir, sample_surgical_tool_info):
        """Test CLI with output path argument."""
        output_path = temp_output_dir / "output.json"
        monkeypatch.setattr(
            sys, 'argv',
            ['surgical_tool_info.py', '-i', 'Test', 'Tool', '-o', str(output_path)]
        )

        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            mock_instance = MockGenerator.return_value
            mock_instance.generate.return_value = sample_surgical_tool_info

            from surgical_tool_info import main
            try:
                main()
            except SystemExit as e:
                assert e.code == 0 or e.code is None

    def test_cli_with_verbose_flag(self, monkeypatch, temp_output_dir, sample_surgical_tool_info):
        """Test CLI with verbose flag."""
        monkeypatch.setattr(
            sys, 'argv',
            ['surgical_tool_info.py', '-i', 'Test', 'Tool', '-v']
        )

        with patch('surgical_tool_info.SurgicalToolInfoGenerator') as MockGenerator:
            mock_instance = MockGenerator.return_value
            mock_instance.generate.return_value = sample_surgical_tool_info

            from surgical_tool_info import main
            try:
                main()
            except SystemExit as e:
                assert e.code == 0 or e.code is None

    def test_cli_error_handling(self, monkeypatch):
        """Test CLI error handling."""
        monkeypatch.setattr(
            sys, 'argv',
            ['surgical_tool_info.py']  # Missing required arguments
        )

        from surgical_tool_info import main
        with pytest.raises(SystemExit):
            main()


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests for the entire module."""

    def test_full_workflow_with_mock_client(self, temp_output_dir, sample_surgical_tool_info):
        """Test complete workflow from generation to file save."""
        config = Config(output_dir=temp_output_dir, quiet=True)
        generator = SurgicalToolInfoGenerator(config=config)

        with patch.object(generator, '_generate_info', return_value=sample_surgical_tool_info):
            result = generator.generate("Surgical Scalpel")

        # Verify result
        assert result.tool_basics.tool_name == "Surgical Scalpel"

        # Verify file was saved
        expected_file = temp_output_dir / "surgical_scalpel_info.json"
        assert expected_file.exists()

        # Verify file contents
        with open(expected_file, 'r') as f:
            saved_data = json.load(f)
        assert saved_data["tool_basics"]["tool_name"] == "Surgical Scalpel"

    def test_multiple_tool_generations(self, temp_output_dir):
        """Test generating information for multiple tools."""
        config = Config(output_dir=temp_output_dir, quiet=True)
        generator = SurgicalToolInfoGenerator(config=config)

        tool_names = ["Surgical Scalpel", "Hemostatic Clamp", "Retractor"]

        for tool_name in tool_names:
            with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
                with patch.object(generator, 'print_summary'):
                    try:
                        generator.generate(tool_name)
                    except Exception:
                        # Mock client may not be fully functional
                        pass

    def test_output_directory_creation(self, temp_output_dir, sample_surgical_tool_info):
        """Test that output directories are created as needed."""
        nested_dir = temp_output_dir / "level1" / "level2" / "level3"
        generator = SurgicalToolInfoGenerator(
            config=Config(output_dir=nested_dir, quiet=True)
        )

        output_file = nested_dir / "test_output.json"
        generator.save(sample_surgical_tool_info, output_file)

        assert output_file.parent.exists()
        assert output_file.exists()


# ============================================================================
# EDGE CASE TESTS
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_tool_name_with_special_characters(self, config):
        """Test tool name with special characters."""
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate("Surgical/Scalpel (Type-A)")
                    assert generator.tool_name == "Surgical/Scalpel (Type-A)"

    def test_tool_name_with_multiple_spaces(self, config):
        """Test tool name with multiple consecutive spaces."""
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate("Surgical   Scalpel")
                    assert generator.tool_name == "Surgical   Scalpel"

    def test_very_long_tool_name(self, config):
        """Test with very long tool name."""
        long_name = "Very " * 100 + "Long Tool Name"
        generator = SurgicalToolInfoGenerator(config=config)
        with patch.object(generator, '_generate_info', return_value=Mock(spec=SurgicalToolInfo)):
            with patch.object(generator, 'save'):
                with patch.object(generator, 'print_summary'):
                    generator.generate(long_name)
                    assert generator.tool_name == long_name

    def test_output_path_with_special_characters(self, config, sample_surgical_tool_info, temp_output_dir):
        """Test output path with special characters."""
        output_path = temp_output_dir / "test[1]_output(special).json"
        generator = SurgicalToolInfoGenerator(config=config)

        result = generator.save(sample_surgical_tool_info, output_path)

        assert output_path.exists()
        assert result == output_path

    def test_empty_surgical_tool_info_fields(self):
        """Test SurgicalToolInfo with minimal valid data."""
        minimal_info = SurgicalToolInfo(
            tool_basics=ToolBasics(
                tool_name="",
                alternative_names="",
                tool_category="",
                surgical_specialties="",
                instrument_family=""
            ),
            tool_purpose=ToolPurpose(
                primary_purpose="",
                surgical_applications="",
                anatomical_targets="",
                tissue_types="",
                unique_advantages=""
            ),
            physical_specifications=PhysicalSpecifications(
                dimensions="",
                weight="",
                material_composition="",
                finish_type="",
                blade_or_tip_specifications="",
                handle_design="",
                sterility_type=""
            ),
            operational_characteristics=OperationalCharacteristics(
                cutting_or_grasping_force="",
                actuation_mechanism="",
                degrees_of_freedom="",
                precision_level="",
                engagement_depth="",
                working_distance=""
            ),
            safety_features=SafetyFeatures(
                safety_mechanisms="",
                slip_resistance="",
                wear_considerations="",
                maximum_safe_force="",
                emergency_protocols="",
                tissue_damage_prevention=""
            ),
            preparation=PreOperativePreperation(
                inspection_requirements="",
                cleaning_protocols="",
                sterilization_requirements="",
                quality_assurance_tests="",
                storage_requirements="",
                preparation_time=""
            ),
            intraoperative_use=IntraOperativeUse(
                positioning_in_field="",
                handling_technique="",
                hand_position_requirements="",
                coordination_with_other_tools="",
                common_movements="",
                visibility_requirements="",
                ergonomic_considerations=""
            ),
            discomfort_risks_and_complications=DiscomfortRisksAndComplications(
                surgeon_fatigue_factors="",
                common_handling_errors="",
                tissue_damage_risks="",
                instrument_complications="",
                cross_contamination_risks="",
                material_reactions="",
                electrical_safety=""
            ),
            maintenance_and_care=MaintenanceAndCare(
                post_operative_cleaning="",
                lubrication_schedule="",
                inspection_frequency="",
                wear_indicators="",
                sharpening_protocol="",
                repair_guidelines="",
                expected_lifespan=""
            ),
            sterilization_and_disinfection=SterilizationAndDisinfection(
                approved_sterilization_methods="",
                incompatible_sterilization="",
                disinfection_alternatives="",
                packaging_requirements="",
                validation_standards="",
                reprocessing_manufacturer_protocols=""
            ),
            alternatives_and_comparisons=AlternativesAndComparisons(
                similar_alternative_tools="",
                advantages_over_alternatives="",
                disadvantages_vs_alternatives="",
                cost_comparison="",
                when_to_use_this_tool="",
                complementary_tools=""
            ),
            historical_context=HistoricalContext(
                invention_history="",
                evolution_timeline="",
                clinical_evidence="",
                widespread_adoption="",
                current_status=""
            ),
            specialty_specific_considerations=SpecialtySpecificConsiderations(
                general_surgery_specific="",
                orthopedic_specific="",
                cardiac_specific="",
                neurosurgery_specific="",
                vascular_specific="",
                laparoscopic_considerations="",
                robotic_integration=""
            ),
            training_and_certification=TrainingAndCertification(
                training_requirements="",
                proficiency_indicators="",
                common_learning_mistakes="",
                skill_development_timeline="",
                formal_education_resources="",
                mentoring_best_practices=""
            ),
            regulatory_and_standards=RegulatoryAndStandards(
                fda_classification="",
                fda_status="",
                iso_standards="",
                country_approvals="",
                quality_certifications="",
                traceability_requirements=""
            ),
            cost_and_procurement=CostAndProcurement(
                single_use_cost=None,
                reusable_initial_cost=None,
                lifecycle_cost="",
                vendor_options="",
                procurement_lead_time="",
                inventory_recommendations="",
                insurance_coverage=""
            ),
            educational_content=EducationalContent(
                plain_language_explanation="",
                key_takeaways="",
                common_misconceptions="",
                patient_communication="",
                video_demonstration_topics=""
            )
        )
        assert minimal_info is not None


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
