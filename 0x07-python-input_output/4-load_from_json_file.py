#!/usr/bin/python3
# 4-load_from_json_file.py
# Laryssa Ribeiro
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
