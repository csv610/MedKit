#!/usr/bin/env python
"""
CLI for medical diagnostic devices and equipment information.

Usage:
    python cli/cli_medical_devices.py <device_name>
    python cli/cli_medical_devices.py <device_name> --output output.json
    python cli/cli_medical_devices.py <device_name> --verbose

Examples:
    python cli/cli_medical_devices.py MRI
    python cli/cli_medical_devices.py "CT scanner" --verbose
    python cli/cli_medical_devices.py ultrasound --output ultrasound_info.json
"""

import sys
import json
import argparse
from pathlib import Path
from medkit.diagnostics.medical_test_devices import get_device_info


def main():
    """Main CLI entry point for medical device information."""
    parser = argparse.ArgumentParser(
        description='Get detailed information about medical diagnostic devices'
    )
    parser.add_argument(
        'device',
        nargs='?',
        help='Name of the medical device (e.g., MRI, CT scanner, ultrasound, X-ray)'
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

    if not args.device:
        parser.print_help()
        sys.exit(1)

    try:
        # Get medical device information
        result = get_device_info(args.device)
        
        if result:
            print(f"\nMedical Device: {args.device.title()}")
            print("=" * 70)
            
            # Display device name
            if hasattr(result, 'device_name'):
                print(f"\nDevice Name: {result.device_name}")
            
            if hasattr(result, 'device_type'):
                print(f"Type: {result.device_type}")
            
            # Display overview
            if hasattr(result, 'overview'):
                print(f"\nOverview:")
                print(f"{result.overview}")
            
            # Display how it works
            if hasattr(result, 'how_it_works'):
                print(f"\nHow It Works:")
                print(f"{result.how_it_works}")
            
            # Display what it diagnoses
            if hasattr(result, 'what_it_diagnoses'):
                print(f"\nWhat It Diagnoses:")
                print(f"{result.what_it_diagnoses}")
            
            # Display procedure information
            if hasattr(result, 'procedure'):
                print(f"\nProcedure:")
                print(f"{result.procedure}")
            
            if hasattr(result, 'duration'):
                print(f"\nDuration: {result.duration}")
            
            if hasattr(result, 'preparation'):
                print(f"\nPreparation:")
                print(f"{result.preparation}")
            
            # Display comfort and discomfort
            if hasattr(result, 'comfort_and_discomfort'):
                print(f"\nComfort and Discomfort:")
                print(f"{result.comfort_and_discomfort}")
            
            # Display safety information
            if hasattr(result, 'safety'):
                print(f"\nSafety:")
                print(f"{result.safety}")
            
            # Display contraindications
            if hasattr(result, 'contraindications'):
                print(f"\nContraindications:")
                print(f"{result.contraindications}")
            
            # Display advantages
            if hasattr(result, 'advantages'):
                print(f"\nAdvantages:")
                print(f"{result.advantages}")
            
            # Display limitations
            if hasattr(result, 'limitations'):
                print(f"\nLimitations:")
                print(f"{result.limitations}")
            
            # Display cost
            if hasattr(result, 'cost'):
                print(f"\nTypical Cost: {result.cost}")
            
            # Display results timeline
            if hasattr(result, 'results_timeline'):
                print(f"\nResults Timeline: {result.results_timeline}")
            
            # Display special considerations
            if hasattr(result, 'special_considerations'):
                print(f"\nSpecial Considerations:")
                print(f"{result.special_considerations}")
            
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
                print(f"\n\n✓ Complete data saved to: {output_path}")
        
        else:
            print(f"No information found for device: {args.device}")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
