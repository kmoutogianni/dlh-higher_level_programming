#!/usr/bin/python3
"""Module Input Output"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    python_list = load_from_json_file(filename)
except FileNotFoundError:
    python_list = []

python_list.extend(sys.argv[1:])

save_to_json_file(python_list, filename)
