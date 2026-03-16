<<<<<<< HEAD
# Lexical Analyzer Suite - Team 05

**Institution**: Universidad Nacional Autónoma de México (UNAM)
**Faculty**: Facultad de Ingeniería
**Course**: Compilers (Semestre 2026-II)
**Submission Date**: March 15th, 2026

## 📌 Project Overview
This project presents a multi-level implementation of a Lexical Analyzer. It is designed as a modular Python package suite that allows users to compare three different approaches to lexical scanning, ranging from basic regular expression matching to a professional-grade engine using the **RPLY** library.

## 📂 Final Project Structure
The repository is organized into specific modules and packages, ensuring portability across different environments:

```text
05/
├── doc/                        # Documentation & Final Report
│   ├── 05-Compilers-Lexer.pdf  # Final compiled PDF
│   ├── Report.tex              # LaTeX source code
│   ├── UNAM_LOGO2.png          # Faculty logo
│   └── protocolo.bib           # Bibliography database
├── src/                        # Level 1: Simple Lexer
│   ├── __init__.py             # Package marker
│   ├── main.py                 # Level 1 entry point
│   ├── lector.py               # Manual scanning logic
│   └── lexertable.py           # Manual token definitions
├── src_recharged/              # Level 2: Enhanced Lexer
│   ├── __init__.py             # Package marker
│   ├── main2_0.py              # Level 2 entry point
│   ├── lector.py               # Optimized scanning logic
│   └── lexertable.py           # Formatted token definitions
├── src_rply/                   # Level 3: Professional Lexer
│   ├── __init__.py             # Package marker
│   ├── main3_0.py              # Level 3 entry point (RPLY)
│   └── LexerTable.py           # Optimized RPLY token table
├── executable.py               # Main Hub for version selection
├── hola.txt                    # Root-level test source file
└── README.md                   # This documentation
=======
# Lexer Implementation - Team 05

**University**: Universidad Nacional Autónoma de México (UNAM)  
**Faculty**: Facultad de Ingeniería  
**Course**: Compilers  
**Submission Date**: March 15th, 2026  

## 📌 Project Overview
This project consists of a Lexical Analyzer (Lexer) designed to scan and categorize tokens from source code strings or files. Following professional software engineering standards, the application is structured within the package `unam.fi.compilers.g5.05`.

## 🛠️ Technical Implementation
The lexer is built using the **RPLY** library in Python. This architectural choice was made to ensure:
* **Efficiency**: Regular expressions are compiled once upon instantiation, optimizing memory and processing speed.
* **Scalability**: The modular design separates the UI (`main.py`) from the lexical engine (`LexerTable.py`), facilitating future integration with a syntax parser.
* **Compliance**: This implementation strictly avoids the use of FLEX, meeting the core project requirements.

## 📋 Token Vocabulary (53 Total Tokens)
Our lexer recognizes 53 distinct patterns, far exceeding the minimum requirement of 40 tokens. These are categorized as follows:

* **Keywords (28)**: `print`, `printf`, `if`, `else`, `while`, `for`, `return`, `int`, `float`, `double`, `char`, `void`, `break`, `continue`, `main`, `bool`, `long`, `switch`, `case`, `default`, `do`, `static`, `struct`, `const`, `sizeof`, `typedef`, `unsigned`, `short`.
* **Operators (14)**: `=`, `+`, `-`, `*`, `/`, `<`, `>`, `!`, `==`, `!=`, `<=`, `>=`, `++`, `--`.
* **Punctuation (9)**: `(`, `)`, `{`, `}`, `[`, `]`, `;`, `,`, `.`.
* **Identifiers**: Supports variable names including the `$` character (e.g., `$a`).
* **Constants**: Handles numeric values and string literals.

## 📖 Theoretical Component: CFG & Left Factoring
As part of the theoretical requirements, we present a Context-Free Grammar (CFG) proposal for a variable declaration.

### Initial Grammar (Ambiguous)
The following grammar is ambiguous for top-down parsers due to a common prefix ($Type\ id$):
$$Decl \rightarrow Type\ id\ ;\ |\ Type\ id\ =\ Expr\ ;$$

### Improved Grammar (Left Factoring Applied)
By applying left factoring, we eliminate the common prefix to enhance parsing efficiency:
$$Decl \rightarrow Type\ id\ Decl'$$
$$Decl' \rightarrow ;\ |\ =\ Expr\ ;$$

## 🚀 Usage Instructions
1.  **Installation**: Ensure RPLY is installed via `pip install rply`.
2.  **Execution**: Run `python main.py`.
3.  **Modes**:
    * `terminal`: Enter code directly as a string.
    * `archive`: Provide the path to a `.txt` file (e.g., `hola.txt`).

## 📁 Project Structure
```text
unam.fi.compilers.g5.05/
├── doc/
│   └── 05-Compilers-Lexer.pdf  # Final PDF Report
├── src/
│   ├── main.py                 # Application Entry Point
│   └── LexerTable.py           # RPLY Token Definitions
├── README.md                   # Project Documentation
└── hola.txt                    # Test Case File
>>>>>>> 11bdbd03c2c6d361a5b5bdffe190c2773f62070d
