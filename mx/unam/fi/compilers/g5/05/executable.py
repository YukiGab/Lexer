import src.main as simple_lexer
import src_recharged.main2_0 as recharged_lexer
import src_rply.main3_0 as rply_lexer

def main():
    while True:
        print("\n================================================")
        print("   UNAM FI - Compilers - Team #05")
        print("================================================")
        print("Welcome to the Lexical Analyzer Suite")
        print("1. Simple Lexer (Standard Output)")
        print("2. Enhanced Lexer (Formatted Output)")
        print("3. Professional Lexer (RPLY Implementation)")
        print("4. Exit")
        print("------------------------------------------------")
        
        selection = input("Which version would you like to use? (1-4): ").strip()
        
        try:
            if selection == "1":
                print("\n--- Running: src ---")
                simple_lexer.main()
            elif selection == "2":
                print("\n--- Running: src_recharged ---")
                recharged_lexer.main()
            elif selection == "3":
                print("\n--- Running: src_rply ---")
                rply_lexer.main()
            elif selection == "4":
                print("Exiting project suite... Goodbye!")
                break
            else:
                print("\n[!] Invalid selection. Please choose 1, 2, 3, or 4.")
        except Exception as e:
            print(f"\n[!] Execution Error: {e}")
            print("Please ensure all directories and files are correctly placed.")

if __name__ == "__main__":
    main()