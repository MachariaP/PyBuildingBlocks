#!/usr/bin/env python3

"""
Description:
    Reading all lines from a CSV file into a list.

This script:
    1. Opens a CSV file.
    2. Reads all lines at once into a list using readlines() method.
    3. Iterates over the list and prints each line.
    4. Removes whitespaces and newline characters using strip() method.
"""

# Open the file 'sample.csv' in read mode using context manager.
# 'with' ensures that the file is properly closed after we're done with it.
with open('sample.csv', 'r') as file:
    # Print header for clarity.
    print('<== Reading all lines of the file ==>', '\n')

    # readlines() reads all lines into a list.
    # Each element in the list is a single line from the file.
    lines = file.readlines()

    # Iterate through each line in the list.
    for line in lines:
        # strip() removes whitespaces and newline characters.
        # Print each cleaned line.
        print(line.strip())