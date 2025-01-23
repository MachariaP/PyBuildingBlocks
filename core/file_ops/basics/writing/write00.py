#!/usr/bin/env python3

"""
Writing multiple lines to a file.
"""

lines = [
    'First line.',
    'Second line.',
    'Third line.'
    'Fourth line.'
]

with open('sample2.txt', 'w') as file:
    print('Writing to file...', '\n')
    for line in lines:
        file.write(line + '\n')
        print(line)