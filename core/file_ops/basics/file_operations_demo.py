#!/usr/bin/env python3

"""
File Operations and Encodings Demo
A comprehensive demonstration of file handling concepts including:
- Different file modes
- Context managers
- Text encodings
- Error handling
"""

import os
import chardet
from typing import List, Optional


class FileHandler:
    """A class demonstrating robust file operations with different modes and encodings."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def write_with_encoding(self, content: str, encoding: str = 'utf-8') -> None:
        """
        Write content to file with specified encoding.
        Uses context manager for automatic resource cleanup.
        """
        try:
            with open(self.file_path, 'w', encoding=encoding) as file:
                file.write(content)
        except IOError as e:
            print(f"Error writing to file: {e}")
        except UnicodeEncodeError as e:
            print(f"Encoding error: {e}")
    
    def append_content(self, content: str) -> None:
        """Append content to existing file using append mode."""
        try:
            with open(self.file_path, 'a') as file:
                file.write(content + '\n')
        except IOError as e:
            print(f"Error appending to file: {e}")
    
    def read_with_encoding_detection(self) -> Optional[str]:
        """
        Read file content with automatic encoding detection.
        Returns None if reading fails.
        """
        try:
            # First, read the raw bytes to detect encoding
            with open(self.file_path, 'rb') as file:
                raw_data = file.read()
            
            # Detect the encoding
            result = chardet.detect(raw_data)
            detected_encoding = result['encoding']
            
            # Read the file with detected encoding
            with open(self.file_path, 'r', encoding=detected_encoding) as file:
                return file.read()
        except IOError as e:
            print(f"Error reading file: {e}")
            return None
    
    def read_in_chunks(self, chunk_size: int = 1024) -> List[str]:
        """
        Read file in chunks to handle large files efficiently.
        Returns list of chunks.
        """
        chunks = []
        try:
            with open(self.file_path, 'r') as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    chunks.append(chunk)
            return chunks
        except IOError as e:
            print(f"Error reading chunks: {e}")
            return []


def main():
    """Demonstrate various file operations."""
    # Create a handler instance
    handler = FileHandler('sample.txt')
    
    # 1. Write content with different encodings
    print("Writing content with UTF-8 encoding...")
    handler.write_with_encoding("Hello, 世界!\n", 'utf-8')
    
    # 2. Append additional content
    print("Appending content...")
    handler.append_content("This is an appended line.")
    handler.append_content("And another line.")
    
    # 3. Read and detect encoding
    print("\nReading content with encoding detection:")
    content = handler.read_with_encoding_detection()
    if content:
        print(f"Content: {content}")
    
    # 4. Demonstrate chunk reading
    print("\nReading in chunks:")
    chunks = handler.read_in_chunks(chunk_size=20)
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {chunk}")


if __name__ == "__main__":
    main()