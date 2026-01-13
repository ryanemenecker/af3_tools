"""
Unit and regression test for the af3_tools package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import af3_tools


def test_af3_tools_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "af3_tools" in sys.modules
