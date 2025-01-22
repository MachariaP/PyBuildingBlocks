#!/usr/bin/env python3

"""
Demonstrates safe file reading with error handling.
"""

def safe_read_file(filename):
    """
    Safely read and print contents of a file with error handling.

    Parameters:
        filename: str: Name of the file to read.

    Returns:
        None
    """
    try:

        with open(filename, 'r') as file:
            print(f'<== Reading file: {filename} ==>', '\n')
            for line in file:
                print(line.strip())
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except PermissionError:
        print(f"Error: Permission denied to access file '{filename}'.")

    except Exception as e:
        print(f"Error: {e}")

    return None


if __name__ == '__main__':
    file_path = 'sample.csv'
    safe_read_file(file_path)