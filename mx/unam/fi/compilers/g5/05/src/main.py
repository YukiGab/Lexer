import lector
def main():
    while True:
        seleccion = input("Select how you will enter your code (archive/terminal): ").strip().lower()
        match seleccion:
            case "archive":
                try:
                    ruta = input("Enter your file path:\n")
                    lector.analizearchive(ruta)
                except:
                    print("Erron, invalid location")
                
                break
            case "terminal":
                code = input("Enter your code:\n")
                lector.analizeterminal(code)
                break
            case "exit":
                exit()
            case _:
                print("Error: Invalid option. Please try again.\n")


if __name__ == "__main__":
    print("Welcome to Lexer from Team 5")
    main()