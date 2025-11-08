#!/usr/bin/env python
"""
CLI for medical term extraction from text.

Usage:
    python cli/cli_term_extractor.py <text>
    python cli/cli_term_extractor.py --file <file.txt>
    python cli/cli_term_extractor.py <text> --output output.json
    python cli/cli_term_extractor.py <text> --verbose

Examples:
    python cli/cli_term_extractor.py "Patient has diabetes and hypertension"
    python cli/cli_term_extractor.py "History of myocardial infarction treated with aspirin" --verbose
    python cli/cli_term_extractor.py --file clinical_notes.txt --output extracted_terms.json
"""

import sys
import json
import argparse
from pathlib import Path
from medkit.medical.medical_term_extractor import extract_medical_terms


def main():
    """Main CLI entry point for medical term extraction."""
    parser = argparse.ArgumentParser(
        description='Extract and categorize medical terms from text'
    )
    parser.add_argument(
        'text',
        nargs='?',
        help='Medical text to extract terms from'
    )
    parser.add_argument(
        '--file',
        '-f',
        help='Read text from file instead of command line'
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
        help='Show detailed extraction information'
    )

    args = parser.parse_args()

    # Get text from either command line or file
    if args.file:
        try:
            with open(args.file, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        parser.print_help()
        sys.exit(1)

    try:
        # Extract medical terms
        result = extract_medical_terms(text)
        
        if result:
            print(f"\n{'=' * 70}")
            print(f"Medical Term Extraction Results")
            print(f"{'=' * 70}")
            
            print(f"\nInput Text:")
            print(f"{text[:200]}{'...' if len(text) > 200 else ''}")
            
            # Display diseases
            if hasattr(result, 'diseases') and result.diseases:
                print(f"\n--- DISEASES ({len(result.diseases)}) ---")
                for disease in result.diseases:
                    if hasattr(disease, 'name'):
                        print(f"• {disease.name}")
                        if hasattr(disease, 'context') and args.verbose:
                            print(f"  Context: {disease.context}")
            
            # Display medicines
            if hasattr(result, 'medicines') and result.medicines:
                print(f"\n--- MEDICINES/DRUGS ({len(result.medicines)}) ---")
                for medicine in result.medicines:
                    if hasattr(medicine, 'name'):
                        print(f"• {medicine.name}")
                        if hasattr(medicine, 'context') and args.verbose:
                            print(f"  Context: {medicine.context}")
            
            # Display symptoms
            if hasattr(result, 'symptoms') and result.symptoms:
                print(f"\n--- SYMPTOMS/SIGNS ({len(result.symptoms)}) ---")
                for symptom in result.symptoms:
                    if hasattr(symptom, 'name'):
                        print(f"• {symptom.name}")
                        if hasattr(symptom, 'context') and args.verbose:
                            print(f"  Context: {symptom.context}")
            
            # Display treatments
            if hasattr(result, 'treatments') and result.treatments:
                print(f"\n--- TREATMENTS/THERAPIES ({len(result.treatments)}) ---")
                for treatment in result.treatments:
                    if hasattr(treatment, 'name'):
                        print(f"• {treatment.name}")
                        if hasattr(treatment, 'context') and args.verbose:
                            print(f"  Context: {treatment.context}")
            
            # Display procedures
            if hasattr(result, 'procedures') and result.procedures:
                print(f"\n--- PROCEDURES/TESTS ({len(result.procedures)}) ---")
                for procedure in result.procedures:
                    if hasattr(procedure, 'name'):
                        print(f"• {procedure.name}")
                        if hasattr(procedure, 'context') and args.verbose:
                            print(f"  Context: {procedure.context}")
            
            # Display anatomical terms
            if hasattr(result, 'anatomical_terms') and result.anatomical_terms:
                print(f"\n--- ANATOMICAL TERMS ({len(result.anatomical_terms)}) ---")
                for term in result.anatomical_terms:
                    if hasattr(term, 'name'):
                        print(f"• {term.name}")
                        if hasattr(term, 'context') and args.verbose:
                            print(f"  Context: {term.context}")
            
            # Display side effects
            if hasattr(result, 'side_effects') and result.side_effects:
                print(f"\n--- SIDE EFFECTS/ADVERSE REACTIONS ({len(result.side_effects)}) ---")
                for effect in result.side_effects:
                    if hasattr(effect, 'name'):
                        print(f"• {effect.name}")
                        if hasattr(effect, 'context') and args.verbose:
                            print(f"  Context: {effect.context}")
            
            # Display relationships
            if hasattr(result, 'relationships') and result.relationships:
                print(f"\n--- RELATIONSHIPS ({len(result.relationships)}) ---")
                for rel in result.relationships:
                    if hasattr(rel, 'source') and hasattr(rel, 'target') and hasattr(rel, 'relation_type'):
                        print(f"• {rel.source} → [{rel.relation_type}] → {rel.target}")
            
            # Display summary statistics
            print(f"\n--- SUMMARY ---")
            total_terms = 0
            if hasattr(result, 'diseases'):
                total_terms += len(result.diseases) if result.diseases else 0
            if hasattr(result, 'medicines'):
                total_terms += len(result.medicines) if result.medicines else 0
            if hasattr(result, 'symptoms'):
                total_terms += len(result.symptoms) if result.symptoms else 0
            if hasattr(result, 'treatments'):
                total_terms += len(result.treatments) if result.treatments else 0
            if hasattr(result, 'procedures'):
                total_terms += len(result.procedures) if result.procedures else 0
            if hasattr(result, 'anatomical_terms'):
                total_terms += len(result.anatomical_terms) if result.anatomical_terms else 0
            if hasattr(result, 'side_effects'):
                total_terms += len(result.side_effects) if result.side_effects else 0
            
            print(f"Total Medical Terms Extracted: {total_terms}")
            
            # Save to file if requested
            if args.output:
                output_path = Path(args.output)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Convert to dict for JSON serialization
                if hasattr(result, 'dict'):
                    result_dict = result.dict()
                else:
                    result_dict = vars(result)
                
                with open(output_path, 'w') as f:
                    json.dump(result_dict, f, indent=2)
                print(f"\n✓ Complete extraction saved to: {output_path}")
            
            print(f"\n{'=' * 70}\n")
        
        else:
            print(f"Error: Could not extract medical terms from text")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
