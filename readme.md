# PDF Splitter

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black)](<https://buymeacoffee.com/jromero132> "Buy Me a Coffee - jromero132")
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](<https://python.org> "Go to Python homepage")
![Last commit](https://img.shields.io/github/last-commit/jromero132/pdf-splitter "Last commit")
---

PDF Splitter is a `Python` tool that takes a multi-page `PDF` file and splits it into individual `PDF` files, one for
each page of the original document.

## Features

- Split a multi-page `PDF` into individual single-page `PDFs`
- Maintain original page quality and formatting
- Simple command-line interface
- Fast and efficient processing

## Requirements

- `Python 3.6`
- `PyPDF2`

## Installation

To set up this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jromero132/pdf-splitter.git
   cd pdf-splitter
   pip install -r requirements.txt```

## Usage

To split a `PDF` file, use the following command:  
`python main.py path/to/your/file.pdf`

This will create the output directory if provided, otherwise it will use the current directory. Each page of the original
`PDF` will be saved as a separate PDF file in this new directory.

Example:  
`python main.py documents/my_large_document.pdf output_folder`

This will create a directory `output_folder` containing files like `page_1.pdf`, `page_2.pdf`, etc.

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the license file included in this repository.

### Happy Coding! 🚀
