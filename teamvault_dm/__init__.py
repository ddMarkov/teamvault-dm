"""Alias package so the sdist wheel matches the PyPI name."""
from importlib import import_module
import sys

# Re-export the real package under both names
_real = import_module("teamvault")
sys.modules[__name__] = _real      # makes `import teamvault_dm` work
