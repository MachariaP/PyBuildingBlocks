#!/usr/bin/env python3
""" Reads one line at a time. """

with open('sample.csv', 'r') as file:
    first_line = file.readline() # Reads the first line
    second_line = file.readline() # Reads the second line
    print('<== Reading line by line ==>','\n')
    print(f'First line: {first_line.strip()}')
    print(f'Second line: {second_line.strip()}')