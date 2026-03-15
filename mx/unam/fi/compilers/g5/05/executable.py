import src.main
import src_recharged.main
#import src_rply.main

def main():
    while True:
        print("Welcome to the lexer analyzer")
        print("1. Simple lexer\n")
        print("2. Simple lexer, enhanced output\n")
        print("3. Simple lexer, rply version\n")
        print("4. Exit\n")
        selection = input("Which file would you like to use?\n")
        try:
            match selection:
                case "1":
                    src.main.main()
                case "2":
                    src_recharged.main.main()

                #case "3":
                 #   src_rply.main.main()

                case "4":
                    break
                case _:
                    print()
        except:
            print("Error: Invalid selection")
    

if __name__ == "__main__":
    main()