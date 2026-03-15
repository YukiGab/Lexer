import re

# Lista de patrones y sus tipos de token correspondientes
token = [
    # ========== KEYWORDS (palabras reservadas) ==========
    (r'\bprint\b', 'keyword'),
    (r'\bprintf\b', 'keyword'),
    (r'\bint\b', 'keyword'),
    (r'\bfloat\b', 'keyword'),
    (r'\bdouble\b', 'keyword'),
    (r'\blong\b', 'keyword'),
    (r'\bshort\b', 'keyword'),
    (r'\bchar\b', 'keyword'),
    (r'\bvoid\b', 'keyword'),
    (r'\bbool\b', 'keyword'),
    (r'\bstring\b', 'keyword'),
    (r'\bif\b', 'keyword'),
    (r'\belse\b', 'keyword'),
    (r'\bwhile\b', 'keyword'),
    (r'\bfor\b', 'keyword'),
    (r'\bdo\b', 'keyword'),
    (r'\bswitch\b', 'keyword'),
    (r'\bcase\b', 'keyword'),
    (r'\bdefault\b', 'keyword'),
    (r'\bbreak\b', 'keyword'),
    (r'\bcontinue\b', 'keyword'),
    (r'\breturn\b', 'keyword'),
    (r'\btrue\b', 'constant'),
    (r'\bfalse\b', 'constant'),
    (r'\bNULL\b', 'constant'),
    (r'\bnullptr\b', 'constant'),
    
    # ========== CONSTANTS (literales) ==========
    (r'"[^"\\]*(\\.[^"\\]*)*"', 'constant'),
    (r"'[^'\\]*(\\.[^'\\]*)*'", 'constant'),
    
    # Números
    (r'\b0[xX][0-9a-fA-F]+\b', 'constant'),          # Hexadecimales
    (r'\b0[0-7]+\b', 'constant'),                    # Octales
    (r'\b\d+\.\d+([eE][+-]?\d+)?\b', 'constant'),    # Flotantes
    (r'\b\d+[uU]?[lL]?\b', 'constant'),              # Enteros
    
    # ========== IDENTIFIERS (identificadores) ==========
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'identifier'),
    
    # ========== OPERATORS (operadores) ==========
    # Operadores de 3 caracteres
    (r'>>=', 'operator'),
    (r'<<=', 'operator'),
    
    # Operadores de 2 caracteres
    (r'==', 'operator'),
    (r'!=', 'operator'),
    (r'<=', 'operator'),
    (r'>=', 'operator'),
    (r'&&', 'operator'),
    (r'\|\|', 'operator'),
    (r'\+\+', 'operator'),
    (r'--', 'operator'),
    (r'->', 'operator'),
    (r'>>', 'operator'),
    (r'<<', 'operator'),
    (r'\+=', 'operator'),
    (r'-=', 'operator'),
    (r'\*=', 'operator'),
    (r'/=', 'operator'),
    (r'%=', 'operator'),
    (r'&=', 'operator'),
    (r'\|=', 'operator'),
    (r'\^=', 'operator'),
    
    # Operadores de 1 caracter
    (r'=', 'operator'),
    (r'\+', 'operator'),
    (r'-', 'operator'),
    (r'\*', 'operator'),
    (r'/', 'operator'),
    (r'%', 'operator'),
    (r'<', 'operator'),
    (r'>', 'operator'),
    (r'!', 'operator'),
    (r'&', 'operator'),
    (r'\|', 'operator'),
    (r'\^', 'operator'),
    (r'~', 'operator'),
    (r'\?', 'operator'),
    
    # ========== PUNCTUATION ==========
    (r';', 'punctuation'),
    (r',', 'punctuation'),
    (r'\(', 'punctuation'),
    (r'\)', 'punctuation'),
    (r'\{', 'punctuation'),
    (r'\}', 'punctuation'),
    (r'\[', 'punctuation'),
    (r'\]', 'punctuation'),
    (r'\.', 'punctuation'),
    (r':', 'punctuation'),
    
    # ========== COMMENTS (comentarios - se ignoran) ==========
    (r'//.*', None),  # Comentarios de línea
    (r'/\*.*?\*/', None),  # Comentarios multilínea
    
    # ========== WHITESPACE (espacios en blanco - se ignoran) ==========
    (r'\s+', None),
]

# Total de tipos de tokens diferentes (excluyendo None)
TIPOS_TOKEN = len([t for t in token if t[1] is not None])

if __name__ == "__main__":
    print(f"Lexer Table loaded: {TIPOS_TOKEN} token types defined")
    print("Token types:", sorted(set(t[1] for t in token if t[1] is not None)))
