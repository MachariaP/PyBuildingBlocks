#!/usr/bin/env python3
""" Reads the entire file content as a single string. """

with open('sample.csv', 'r') as file:
    content = file.read()
    print('<== The entire file content ==>','\n\n')
    print(content)