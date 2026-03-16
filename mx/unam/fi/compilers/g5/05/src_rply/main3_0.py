from src_rply.LexerTable import Lexer

# --- FUNCIONES DEL MOTOR LÉXICO ---
def procesar_codigo(codigo, lexer):
    try:
        tokens = lexer.lex(codigo)
        lista_nombres = []

        for token in tokens:
            # RPLY extrae el nombre en minúsculas (ej. 'keyword', 'identifier')
            lista_nombres.append(token.gettokentype())

        # Imprime exactamente en el formato que pide el PDF
        print(" ".join(lista_nombres))
        print(f"Total of tokens: {len(lista_nombres)}")

    except Exception as e:
        print("Error: Invalid symbol found in code")


def analizearchive(ruta, lexer):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
        procesar_codigo(codigo, lexer)
    except FileNotFoundError:
        print(f"Error, file not found in {ruta}")


def analizeterminal(code, lexer):
    procesar_codigo(code, lexer)


# --- MENÚ PRINCIPAL DEL EQUIPO 5 ---
def main():
    # Instanciamos el autómata de RPLY una sola vez al inicio
    mi_lexer = Lexer().get_lexer()

    while True:
        seleccion = input("Select how you will enter your code (archive/terminal): ").strip().lower()
        match seleccion:
            case "archive":
                try:
                    ruta = input("Enter your file path:\n")
                    analizearchive(ruta, mi_lexer)
                except:
                    print("Error, invalid location")
                break
            case "terminal":
                code = input("Enter your code:\n")
                analizeterminal(code, mi_lexer)
                break
            case "exit":
                break
            case _:
                print("Error: Invalid option. Please try again.\n")


if __name__ == "__main__":
    print("Welcome to Lexer from Team 5")
    main()