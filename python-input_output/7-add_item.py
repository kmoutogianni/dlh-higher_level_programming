#!/usr/bin/python3
"""Module Input Output"""
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    with open(filename, "r", encoding="utf-8") as f:
        python_list = json.load(f)
except FileNotFoundError:
    python_list = []

python_list.extend(sys.argv[1:])

save_to_json_file(python_list, filename)
