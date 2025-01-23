#!/usr/bin/env python3

"""
Description:
    Demonstrates the most memory-efficient way to read a CSV file.

This script implements a memory-efficient approach to read and process a CSV file:
    - Uses file object as an iterator.
    - Processes one line ata a time instead of loading entire file.
    - Ideal for large files where memory usage is a concern.
"""

with open('sample.csv', 'r') as file:
    print('<== Reading file line by line ==>', end='\n\n')
    for line in file:
        print(line.strip())