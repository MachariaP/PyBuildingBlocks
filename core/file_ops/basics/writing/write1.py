#!/usr/bin/env python3

"""
Demonstrating different ways to write to a file.
"""
# 1. Write Mode ('w') - Overwrites existing file or creates new file

with open('example.txt', 'w')as file:
    file.write('This DELETES the existing content and writes new!.\n')

# 2. Append Mode ('a') - Appends to existing file or creates new file
with open('example.txt', 'a') as file:
    file.write('This appends to the existing content.\n')

# 3. Exclusive Creation ('x') - Creates new file. Fails if file exists
try:
    with open('example.txt', 'x') as file:
        file.write('This will fail if the file exists.\n')
except FileExistsError:
    print('File already exists. Cannot create new file.')