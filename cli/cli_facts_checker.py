#!/usr/bin/env python
"""
CLI for medical facts checker - Verify medical claims and debunk myths.

Usage:
    python cli/cli_facts_checker.py <statement>
    python cli/cli_facts_checker.py <statement> --output output.json
    python cli/cli_facts_checker.py <statement> --verbose

Examples:
    python cli/cli_facts_checker.py "Vitamin C prevents common cold"
    python cli/cli_facts_checker.py "Coffee increases anxiety" --verbose
    python cli/cli_facts_checker.py "Eggs are bad for cholesterol" --output fact_check.json
"""

import sys
import json
import argparse
from pathlib import Path
from medkit.medical.medical_facts_checker import analyze_statement


def main():
    """Main CLI entry point for medical facts checker."""
    parser = argparse.ArgumentParser(
        description='Verify medical claims and fact-check health statements'
    )
    parser.add_argument(
        'statement',
        nargs='?',
        help='Medical statement or claim to verify'
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
        help='Show detailed analysis'
    )

    args = parser.parse_args()

    if not args.statement:
        parser.print_help()
        sys.exit(1)

    try:
        # Analyze the medical statement
        result = analyze_statement(args.statement, quiet=False)
        
        if result:
            print(f"\n{'=' * 70}")
            print(f"Medical Fact Check Analysis")
            print(f"{'=' * 70}")
            
            print(f"\nStatement: \"{args.statement}\"")
            
            # Display statement analysis
            if result.detailed_analysis:
                analysis = result.detailed_analysis
                
                print(f"\n--- CLASSIFICATION ---")
                if analysis.statement_analysis:
                    stmt = analysis.statement_analysis
                    print(f"Result: {stmt.classification.upper()}")
                    print(f"Confidence: {stmt.confidence_percentage}% ({stmt.confidence_level})")
                
                # Display explanation
                print(f"\n--- EXPLANATION ---")
                print(f"{analysis.explanation}")
                
                # Display context
                if analysis.context:
                    print(f"\n--- CONTEXT ---")
                    print(f"Subject Area: {analysis.context.subject_area}")
                    print(f"Key Terms: {analysis.context.key_terms}")
                    print(f"Scope Clarity: {analysis.context.scope_clarity}")
                
                # Display fact support or fiction indicators
                if stmt.classification.lower() == "fact":
                    if analysis.factual_support:
                        support = analysis.factual_support
                        print(f"\n--- FACTUAL SUPPORT ---")
                        print(f"Supporting Sources: {support.supporting_sources}")
                        print(f"Evidence Type: {support.evidence_type}")
                        print(f"Verification Method: {support.verification_method}")
                        print(f"Related Facts: {support.related_facts}")
                
                elif stmt.classification.lower() == "fiction":
                    if analysis.fiction_indicators:
                        fiction = analysis.fiction_indicators
                        print(f"\n--- FICTION INDICATORS ---")
                        print(f"Red Flags: {fiction.red_flags}")
                        print(f"Factual Errors: {fiction.factual_errors}")
                        print(f"Lack of Evidence: {fiction.lack_of_evidence}")
                        print(f"Fictional Elements: {fiction.fictional_elements}")
                
                # Display potential confusion/misconceptions
                print(f"\n--- COMMON MISCONCEPTIONS ---")
                print(f"{analysis.potential_confusion}")
                
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
                    print(f"\n\n✓ Complete analysis saved to: {output_path}")
            
            print(f"\n{'=' * 70}\n")
        
        else:
            print(f"Error: Could not analyze statement")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
