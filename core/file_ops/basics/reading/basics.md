# Python File Reading Guide 📖

## Table of Contents
- [Basic File Reading Methods](#basic-file-reading-methods)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)
- [Practical Examples](#practical-examples)
- [Tips and Tricks](#tips-and-tricks)
- [Common Use Cases](#common-use-cases)
- [Quick Reference](#quick-reference)

## Basic File Reading Methods

### 1. Read Entire File (read0.py)
```python
# Returns the entire file content as a single string
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 2. Read Line by Line (read1.py)
```python
# Read one line at a time
with open('file.txt', 'r') as file:
    first_line = file.readline()    # Reads first line
    second_line = file.readline()   # Reads second line
    print(f"First line: {first_line.strip()}")
    print(f"Second line: {second_line.strip()}")
```

### 3. Read All Lines into List (read2.py)
```python
# Returns a list where each element is a line
with open('file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### 4. Iterate Over File (read3.py)
```python
# Most memory-efficient way to read large files
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

## Error Handling

### Basic Error Handling Template  (read4.py)
```python
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None
```

### Reading with Specific Encoding (read5.py)
```python
try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Could not decode the file with UTF-8 encoding")
```

## Best Practices

### 1. Always Use Context Managers
```python
# ✅ GOOD - Using context manager
with open('file.txt', 'r') as file:
    content = file.read()

# ❌ BAD - Manual file handling
file = open('file.txt', 'r')
content = file.read()
file.close()
```

### 2. Large File Handling
```python
# ✅ GOOD - Memory efficient
with open('large_file.txt', 'r') as file:
    for line in file:
        process_line(line)

# ❌ BAD - Loads entire file into memory
with open('large_file.txt', 'r') as file:
    content = file.read()
```

### 3. Path Handling
```python
from pathlib import Path

# Create path safely
file_path = Path('folder') / 'subfolder' / 'file.txt'

# Check if file exists
if file_path.exists():
    with open(file_path, 'r') as file:
        content = file.read()
```

## Practical Examples

### 1. File Analysis Tool
```python
def analyze_text_file(filename):
    """Analyze text file for basic statistics."""
    stats = {'lines': 0, 'words': 0, 'characters': 0}
    
    with open(filename, 'r') as file:
        for line in file:
            stats['lines'] += 1
            stats['words'] += len(line.split())
            stats['characters'] += len(line)
    
    return stats
```

### 2. Search in File
```python
def search_in_file(filename, search_term):
    """Search for a term in file and return matching lines."""
    matches = []
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if search_term in line:
                matches.append((line_num, line.strip()))
    return matches
```

## Tips and Tricks

### 1. File Position Management
```python
with open('file.txt', 'r') as file:
    position = file.tell()      # Get current position
    content = file.read(10)     # Read 10 characters
    file.seek(0)               # Go back to start
```

### 2. Reading Specific Portions
```python
with open('file.txt', 'r') as file:
    start = file.read(100)     # Read first 100 characters
    file.seek(file.tell() + 50) # Skip 50 characters
    middle = file.read(100)    # Read next 100 characters
```

### 3. Reading with Buffer Size
```python
with open('file.txt', 'r', buffering=4096) as file:
    content = file.read()
```

## Common Use Cases

### 1. Reading CSV-like Data
```python
def read_csv(filename, delimiter=','):
    data = []
    with open(filename, 'r') as file:
        headers = file.readline().strip().split(delimiter)
        for line in file:
            values = line.strip().split(delimiter)
            data.append(dict(zip(headers, values)))
    return data
```

### 2. Reading Configuration Files
```python
def read_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()
    return config
```

---

## Quick Reference

### File Modes
- `'r'` - Read (default)
- `'rb'` - Read binary
- `'r+'` - Read and write

### Common Methods
- `file.read()` - Read entire file
- `file.readline()` - Read single line
- `file.readlines()` - Read all lines into list
- `file.tell()` - Get current position
- `file.seek(0)` - Move to position

### Best Practices Checklist
- ✅ Always use `with` statement
- ✅ Include error handling
- ✅ Consider memory efficiency for large files
- ✅ Use appropriate encoding
- ✅ Handle paths properly using `pathlib`

---

> **Note**: This guide covers Python 3.x file reading operations. Some methods might work differently in Python 2.x.
