#!/usr/bin/env python3
"""
Test runner script for mcup project using pytest.
"""
import sys
import pytest


def run_tests():
    """Discover and run all tests in the tests directory using pytest."""
    return pytest.main(["-v"])


if __name__ == "__main__":
    result = run_tests()
    sys.exit(result)
