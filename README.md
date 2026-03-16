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