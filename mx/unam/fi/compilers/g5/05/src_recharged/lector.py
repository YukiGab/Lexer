import re
from src_recharged.lexertable import token

def analizearchive(ruta):
    """
    Analiza un archivo y genera los tokens correspondientes
    
    Args:
        ruta (str): Ruta del archivo a analizar
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        print(f"\nAnalyzing file: {ruta}")
        print("-" * 40)
        return _analizar_contenido(contenido, "FILE")
        
    except FileNotFoundError:
        print(f"Error: File '{ruta}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def analizeterminal(code):
    """
    Analiza código ingresado por terminal y genera los tokens
    
    Args:
        code (str): Código a analizar
    """
    print("\nAnalyzing terminal input:")
    print("-" * 40)
    return _analizar_contenido(code, "TERMINAL")


def _analizar_contenido(contenido, fuente):
    """
    Función interna que realiza el análisis léxico
    
    Args:
        contenido (str): Contenido a analizar
        fuente (str): Fuente del contenido (FILE/TERMINAL)
    
    Returns:
        list: Lista de tokens encontrados
    """
    tokens = []
    posicion = 0
    longitud = len(contenido)
    linea = 1
    columna = 1
    
    print(f"\nInput code:")
    print(contenido)
    print("\nTokens found:")
    print("-" * 40)
    
    while posicion < longitud:
        encontrado = False
        
        # Saltar espacios en blanco pero contar líneas
        if contenido[posicion].isspace():
            if contenido[posicion] == '\n':
                linea += 1
                columna = 1
            else:
                columna += 1
            posicion += 1
            continue
        
        # Probar cada patrón de token
        for pattern, token_type in token:
            regex = re.compile(pattern)
            match = regex.match(contenido, posicion)
            
            if match:
                valor = match.group(0)
                
                # Solo agregar si no es None (ignorar espacios y comentarios)
                if token_type is not None:
                    tokens.append(token_type)
                    print(f"  {token_type:<12} | '{valor}' | line {linea}, col {columna}")
                
                # Actualizar posición y columna
                posicion += len(valor)
                columna += len(valor)
                encontrado = True
                break
        
        # Si no se encuentra ningún patrón válido
        if not encontrado:
            caracter = contenido[posicion]
            print(f"  ERROR{'':<8} | Lexical error: invalid character '{caracter}' at line {linea}, col {columna}")
            posicion += 1
            columna += 1
    
    # Mostrar resumen
    print("-" * 40)
    print(f"Total de tokens encontrados: {len(tokens)}")
    print(f"Fuente: {fuente}")
    
    # Mostrar lista compacta de tokens (formato requerido)
    print("\nOutput format (required):")
    print(" ".join(tokens))
    
    return tokens


def _test_ejemplo():
    """Función de prueba con el ejemplo del profesor"""
    ejemplo = 'printf("This is an example"); int a = 10;'
    print("\n" + "=" * 50)
    print("TESTING WITH PROFESSOR'S EXAMPLE")
    print("=" * 50)
    return _analizar_contenido(ejemplo, "TEST")