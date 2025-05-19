"""
This module provides a function and CLI for summing numbers.

Functions:
  - sum_numbers: Returns the sum of a list of numbers.

CLI:
  - Accepts numbers as command-line arguments and prints their sum.
"""

import argparse
import logging
from typing import List

__all__ = ["sum_numbers"]

def sum_numbers(numbers: List[float]) -> float:
    """
    Return the sum of a list of numbers.

    :param numbers: List of numbers to sum.
    :return: The sum of the numbers.
    """
    return sum(numbers)

def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Sum numbers from the command line.")
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="Numbers to sum."
    )
    return parser.parse_args()

def main() -> None:
    """
    Main entry point for the sum_numbers CLI application.
    """
    args = parse_args()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    result = sum_numbers(args.numbers)
    logger.info(f"Sum of {args.numbers} is {result}")

if __name__ == "__main__":
    main()
