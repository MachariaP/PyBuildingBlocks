#!/usr/bin/env python3

def read_file_with_encoding(filename):
    """
    Read a file wuth UTF-8 encoding and handle potential  decode errors.

    This function attempts to read a text file using UTF-8 encoding and handles
    any unicode decode errors that may occur during the reading process.

    Parameters:
        filename: (str): Name or path of the file to read.

    Returns:
        str or None: Contents of the file as a string if successful, None otherwise.

    Raises:
        UnicodeDecodeError: If the file cannot be decoded using UTF-8 encoding.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
        
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{filename}' using UTF-8 encoding.")
        return None
    

if __name__ == '__main__':
    file_path = 'sample.csv'
    file_content = read_file_with_encoding(file_path)
    if file_content:
        print(f'<== Reading file: {file_path} ==>', '\n')
        print(file_content)