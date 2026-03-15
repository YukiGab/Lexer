import re
from lexertable import token

def analizearchive(ruta):
    tokens = []
    position = 0
    try:
        with open(ruta,'r') as archivo:
            contenido = archivo.read().splitlines()     


        for linea in contenido:
            position = 0

            while position < len(contenido):
                
                palabra = contenido[posicion]
                posicion += 1
                palabraval = False

                for palabras, tokens in token:
                    validar = re.compile(palabras)
                    comparar = validar.match(palabra)

                    if comparar:
                        valor = comparar.group(0)
                        if tokens:
                            tokens.append(tokens)
                    
                    position += len(valor)
                    palabraval = True

                    break
        
                if not palabraval:
                    print(f"Error: Invalid symbol at '{linea[position]}'")
                    return

        print(" ".join(tokens))
        print(f"Total of tokens: {len(tokens)}")
    except FileNotFoundError:
        print(f"Error, file not found in {ruta}")

def analizeterminal(code):
    tokens =[]
    coded = code.splitlines() 
    for linea in coded:
            position = 0



            while position < len(coded):
                if linea[position].isspace():
                    position += 1
                    continue

                palabra = coded[position]
                palabraval = False

                for palabras, tokens in token:
                    validar = re.compile(palabras)
                    comparar = validar.match(palabra)

                    if comparar:
                        valor = comparar.group(0)
                        if tokens:
                            tokens.append(tokens)
                    
                        position += len(valor)
                        palabraval = True

                    break
        
            if not palabraval:
                print(f"Error: Invalid symbol at '{linea[position]}'")
                return

    print(" ".join(tokens))
    print(f"Total of tokens: {len(tokens)}")