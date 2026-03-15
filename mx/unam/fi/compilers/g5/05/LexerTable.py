from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # 1. OPERADORES (Dobles primero)
        self.lexer.add('operator', r'==|!=|<=|>=|\+\+|\-\-|=|\+|-|\*|/|<|>|!')

        # 2. PALABRAS RESERVADAS (keyword)
        self.lexer.add('keyword', r'\b(print|printf|if|else|while|for|return|int|float|double|char|void|break|continue|main|bool|long|switch|case|default|do|static|struct|const|sizeof|typedef|unsigned|short)\b')

        # 3. IDENTIFICADORES (Soporta el caracter '$' como pide el PDF)
        self.lexer.add('identifier', r'[a-zA-Z_\$][a-zA-Z0-9_\$]*')

        # 4. CONSTANTES (Incluye tanto números como strings/literales)
        self.lexer.add('constant', r'\d+(\.\d+)?|".*?"')

        # 5. PUNTUACIÓN
        self.lexer.add('punctuation', r'\(|\)|\{|\}|\[|\]|;|,|\.')

        # 6. IGNORAR ESPACIOS
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()