#!/usrr/bin/python3
"""defines a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create a python object fromn a JSON file"""
    with open(filename) as f:
        return json.load(f)
