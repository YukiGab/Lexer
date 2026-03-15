import sys
import os
from lector import analizearchive, analizeterminal

def main():
    """Función principal del lexer"""
    print("=" * 50)
    print("Welcome to Lexer from Team 5")
    print("UNAM FI Compilers - Group 5")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Read from file (archive)")
        print("2. Read from terminal")
        print("3. Exit")
        
        seleccion = input("\nSelect how you will enter your code (archive/terminal/exit): ").strip().lower()
        
        match seleccion:
            case "archive" | "1":
                ruta = input("Enter your file path:\n").strip()
                if os.path.exists(ruta):
                    analizearchive(ruta)
                else:
                    print(f"Error: File '{ruta}' not found.")
                break
                
            case "terminal" | "2":
                print("Enter your code (end with Ctrl+D on empty line or type 'END' on new line):")
                lines = []
                try:
                    while True:
                        line = input()
                        if line == "END":
                            break
                        lines.append(line)
                except EOFError:
                    pass
                
                code = "\n".join(lines)
                if code.strip():
                    analizeterminal(code)
                else:
                    print("Error: No code entered.")
                break
                
            case "exit" | "3":
                print("Goodbye!")
                sys.exit(0)
                
            case _:
                print("Error: Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()