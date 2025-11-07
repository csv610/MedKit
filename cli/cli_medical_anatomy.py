#!/usr/bin/env python
"""
CLI for medical anatomy information queries.

Usage:
    python cli/cli_medical_anatomy.py <body_part>

Example:
    python cli/cli_medical_anatomy.py heart
"""

import sys
import argparse
from medkit.medical.medical_anatomy import get_anatomy_info


def main():
    """Main CLI entry point for anatomy information."""
    parser = argparse.ArgumentParser(
        description='Get medical anatomy information about a body part'
    )
    parser.add_argument(
        'body_part',
        nargs='?',
        help='Name of the body part to look up'
    )
    parser.add_argument(
        '--functions',
        '-f',
        action='store_true',
        help='Show function information'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show detailed information'
    )

    args = parser.parse_args()

    if not args.body_part:
        parser.print_help()
        sys.exit(1)

    try:
        result = get_anatomy_info(args.body_part)
        if result:
            print(f"\nAnatomy Information: {args.body_part.title()}")
            print("=" * 50)
            print(result)
        else:
            print(f"No information found for: {args.body_part}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
