#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    """reads from CSV filename and writes the JSON data to data.json"""
    try:
        with open(filename, "r", encoding="utf-8") as input_csv_file:
            input_data = csv.DictReader(input_csv_file)  # DictReader obj/rows
            data = list(input_data)

        with open("data.json", "w", encoding="utf-8") as output_json_file:
            json.dump(data, output_json_file)

        return True

    except Exception:
        return False
