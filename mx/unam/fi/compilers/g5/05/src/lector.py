import re
from lexertable import token

def analizearchive(ruta):
    tokens = []
    position = 0
    with open(ruta,'r') as archivo:
        contenido = archivo.read().splitlines()            
    while position < len(contenido):
        palabra = contenido[i]
        palabraval = False

        for palabras, tokey in token:
            validar = re.compile(palabras)
            comparar = validar.match(palabra)

            if comparar:
                valor = match.group(0)
                if tokey:
                    tokens.append(tokey)
            
            position += len(valor)
            palabraval = True
            break
    
    if not palabraval:
        print(f"Error: Invalid symbol or symbol not found in the word: '{palabra[0]}'")
        break

    print(" ".join(tokens))
    print(f"Total of tokens: {len(tokens)}")

def analizeterminal(code):
    print(code)    

