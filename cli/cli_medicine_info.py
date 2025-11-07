#!/usr/bin/env python
"""
CLI for medicine/drug information queries.

Usage:
    python cli/cli_medicine_info.py <drug_name>

Example:
    python cli/cli_medicine_info.py aspirin
"""

import sys
import argparse
from medkit.drug.medicine_info import get_medicine_info


def main():
    """Main CLI entry point for medicine information."""
    parser = argparse.ArgumentParser(
        description='Get medical information about a medicine/drug'
    )
    parser.add_argument(
        'drug',
        nargs='?',
        help='Name of the drug/medicine to look up'
    )
    parser.add_argument(
        '--interactions',
        '-i',
        action='store_true',
        help='Show drug interactions'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show detailed information'
    )

    args = parser.parse_args()

    if not args.drug:
        parser.print_help()
        sys.exit(1)

    try:
        result = get_medicine_info(args.drug)
        if result:
            print(f"\nMedicine Information: {args.drug.title()}")
            print("=" * 50)
            print(result)
        else:
            print(f"No information found for: {args.drug}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
