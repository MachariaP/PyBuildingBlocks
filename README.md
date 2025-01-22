# PyBuildingBlocks 🧱

> A comprehensive collection of reusable Python components, algorithms, and utilities designed to accelerate development and learning.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

## ✨ Features

- 📚 **Data Structures**: Common data structure implementations
- 🔍 **Algorithms**: Classic algorithm implementations with explanations
- 🛠️ **Utilities**: Helpful tools for file operations, string manipulation, and more
- 📐 **Math**: Mathematical operations and utilities
- 🌐 **Web**: Web development tools and utilities

## 📁 Project Structure

```plaintext
PyBuildingBlocks/
├── algorithms/                  # Algorithm implementations
│   ├── searching/              # Search algorithms
│   │   ├── binary_search.py
│   │   └── linear_search.py
│   └── sorting/               # Sorting algorithms
│       ├── bubble_sort.py
│       └── quick_sort.py
├── data_structures/           # Data structure implementations
│   ├── linked_list.py
│   └── binary_tree.py
├── utils/                     # Utility functions
│   ├── file_ops/             # File operations
│   │   └── file_handler.py
│   └── string_ops/           # String operations
│       └── string_utils.py
├── math/                      # Mathematical operations
├── web/                      # Web-related utilities
├── tests/                    # Test files
├── docs/                     # Documentation
└── requirements.txt          # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MachariaP/PyBuildingBlocks.git
cd PyBuildingBlocks
```

2. **Create and activate a virtual environment:**
```bash
# Create virtual environment
python -m venv venv

# Windows activation
venv\Scripts\activate

# macOS/Linux activation
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Sorting Algorithms Example
```python
from algorithms.sorting.bubble_sort import bubble_sort

# Sort a list using bubble sort
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### File Operations Example
```python
from utils.file_ops.file_handler import read_file, write_file

# Write content to a file
write_file('example.txt', 'Hello, World!')

# Read content from a file
content = read_file('example.txt')
print(content)  # Output: Hello, World!
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run specific module tests
pytest tests/test_bubble_sort.py
```

## 📚 Documentation

Each module includes detailed documentation with:
- ✍️ Function/class descriptions
- 📝 Parameter explanations
- 💡 Usage examples
- ⚡ Time and space complexity (for algorithms)

> For detailed documentation, check the `docs/` directory or the docstrings in each module.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Steps to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Add more sorting algorithms
- [ ] Implement advanced data structures
- [ ] Add machine learning utilities
- [ ] Create comprehensive documentation website
- [ ] Add performance benchmarks

## ✨ Acknowledgments

- Thanks to all contributors who help improve this project
- Inspired by classic computer science concepts and modern Python practices

## 📧 Contact

Phinehas Macharia - [@_M_Phinehas](https://x.com/_M_Phinehas) - walburphinehas78@gmail.com

Project Link: [https://github.com/MachariaP/PyBuildingBlocks](https://github.com/MachariaP/PyBuildingBlocks)

---

<p align="center">Made with ❤️ by <a href="https://github.com/MachariaP">Phinehas Macharia</a></p>
