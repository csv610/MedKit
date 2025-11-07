#!/usr/bin/env python
"""
CLI for disease information queries.

Usage:
    python cli/cli_disease_info.py <disease_name>

Example:
    python cli/cli_disease_info.py diabetes
"""

import sys
import argparse
from medkit.medical.disease_info import get_disease_info


def main():
    """Main CLI entry point for disease information."""
    parser = argparse.ArgumentParser(
        description='Get medical information about a disease'
    )
    parser.add_argument(
        'disease',
        nargs='?',
        help='Name of the disease to look up'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show detailed information'
    )

    args = parser.parse_args()

    if not args.disease:
        parser.print_help()
        sys.exit(1)

    try:
        result = get_disease_info(args.disease)
        if result:
            print(f"\nDisease Information: {args.disease.title()}")
            print("=" * 50)
            print(result)
        else:
            print(f"No information found for: {args.disease}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
