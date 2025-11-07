#!/usr/bin/env python
"""
CLI for comprehensive medical topic documentation generation.

Usage:
    python cli/cli_medical_topic.py <topic_name>
    python cli/cli_medical_topic.py <topic_name> --output output.json
    python cli/cli_medical_topic.py <topic_name> --verbose

Examples:
    python cli/cli_medical_topic.py diabetes
    python cli/cli_medical_topic.py "heart disease" --verbose
    python cli/cli_medical_topic.py asthma --output asthma_info.json
"""

import sys
import json
import argparse
from pathlib import Path
from medkit.medical.medical_topic import get_topic_info


def main():
    """Main CLI entry point for medical topic information."""
    parser = argparse.ArgumentParser(
        description='Generate comprehensive medical topic documentation with FAQs'
    )
    parser.add_argument(
        'topic',
        nargs='?',
        help='Name of the medical topic to document'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (JSON format)'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show detailed information'
    )

    args = parser.parse_args()

    if not args.topic:
        parser.print_help()
        sys.exit(1)

    try:
        # Generate comprehensive topic information
        result = get_topic_info(args.topic, verbose=args.verbose)
        
        if result:
            print(f"\nMedical Topic: {args.topic.title()}")
            print("=" * 70)
            
            # Display overview
            if result.overview:
                print(f"\nTopic: {result.overview.topic_name}")
                print(f"Category: {result.overview.topic_category}")
                print(f"Specialties: {result.overview.medical_specialties}")
                print(f"Prevalence: {result.overview.prevalence}")
            
            # Display definition
            if result.definition:
                print(f"\n--- DEFINITION ---")
                print(f"Simple Explanation:\n{result.definition.plain_language_explanation}")
                print(f"\nMedical Definition:\n{result.definition.medical_definition}")
            
            # Display epidemiology
            if result.epidemiology:
                print(f"\n--- EPIDEMIOLOGY ---")
                print(f"Incidence: {result.epidemiology.incidence}")
                print(f"Demographics: {result.epidemiology.demographics}")
            
            # Display etiology
            if result.etiology:
                print(f"\n--- ETIOLOGY (CAUSES) ---")
                print(f"Primary Causes: {result.etiology.primary_causes}")
                print(f"Risk Factors: {result.etiology.risk_factors}")
            
            # Display clinical presentation
            if result.clinical_presentation:
                print(f"\n--- CLINICAL PRESENTATION ---")
                print(f"Symptoms: {result.clinical_presentation.symptoms}")
                print(f"Onset: {result.clinical_presentation.onset_pattern}")
            
            # Display diagnosis
            if result.diagnosis:
                print(f"\n--- DIAGNOSIS ---")
                print(f"Tests: {result.diagnosis.diagnostic_tests}")
                print(f"Criteria: {result.diagnosis.diagnostic_criteria}")
            
            # Display treatment
            if result.treatment:
                print(f"\n--- TREATMENT ---")
                print(f"First-line: {result.treatment.first_line_treatment}")
                print(f"Medications: {result.treatment.medications}")
            
            # Display prognosis
            if result.prognosis:
                print(f"\n--- PROGNOSIS ---")
                print(f"Outcomes: {result.prognosis.expected_outcomes}")
                print(f"Timeline: {result.prognosis.treatment_timeline}")
            
            # Display prevention
            if result.prevention:
                print(f"\n--- PREVENTION ---")
                print(f"Primary Prevention: {result.prevention.primary_prevention}")
                print(f"Screening: {result.prevention.screening_recommendations}")
            
            # Display education
            if result.education:
                print(f"\n--- PATIENT EDUCATION ---")
                if result.education.patient_faq:
                    print("\nFrequently Asked Questions:")
                    faq = result.education.patient_faq
                    for i, question in enumerate(faq.questions, 1):
                        print(f"\nQ{i}: {question.question}")
                        print(f"A: {question.answer}")
            
            # Save to file if requested
            if args.output:
                output_path = Path(args.output)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Convert to dict for JSON serialization
                result_dict = result.dict()
                with open(output_path, 'w') as f:
                    json.dump(result_dict, f, indent=2)
                print(f"\n\n✓ Complete data saved to: {output_path}")
        
        else:
            print(f"No information found for: {args.topic}")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
