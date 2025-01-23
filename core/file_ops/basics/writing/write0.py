#!/usr/bin/env python3

"""
Basic file writing demonstration.

This script demonstrates the fundamental way to write context to a file in python
using the 'write' method and context manager ('with' statement).

Key concepts demonstrated:
- Writing to a file in write mode
- Using context manager for safe file handling
- Writing multiple lines to a file
- Using newline characters
"""

# Method 1: Simple writing
# 'w' mode creates a new file or overwrites existing file
with open('sample.txt', 'w') as file:
    file.write('Hello, world! This is my first file.\n')
    file.write('This file was created using Python.\n')