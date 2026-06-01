#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize Python dictionary to XML file"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """deserialize an XML file to a Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    Pyth_dictionary = {}

    for child in root:
        print(child)
        key = child.tag
        value = child.text

        Pyth_dictionary[key] = value

    return Pyth_dictionary
