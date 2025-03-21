import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Expressões regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Expressão regular para números (inteiros ou decimais)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)  # Converte para float
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()