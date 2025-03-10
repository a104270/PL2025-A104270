import ply.lex as lex

# Definição dos tokens
class TokenType:
    COMMENT = 'COMMENT'
    SELECT = 'SELECT'
    WHERE = 'WHERE'
    LIMIT = 'LIMIT'
    OPEN_BRACE = 'OPEN_BRACE'
    CLOSE_BRACE = 'CLOSE_BRACE'
    VARIABLE = 'VARIABLE'
    PREFIX = 'PREFIX'
    STRING = 'STRING'
    DOT = 'DOT'
    NUMBER = 'NUMBER'
    IDENTIFIER = 'IDENTIFIER'
    WHITESPACE = 'WHITESPACE'
    ERROR = 'ERROR'

# Lista de nomes de tokens
tokens = [
    TokenType.COMMENT,
    TokenType.SELECT,
    TokenType.WHERE,
    TokenType.LIMIT,
    TokenType.OPEN_BRACE,
    TokenType.CLOSE_BRACE,
    TokenType.VARIABLE,
    TokenType.PREFIX,
    TokenType.STRING,
    TokenType.DOT,
    TokenType.NUMBER,
    TokenType.IDENTIFIER,
    TokenType.ERROR,
]

# Expressões regulares para tokens mais complexos
def t_COMMENT(t):
    r'\#.*'
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_PREFIX(t):
    r'[a-zA-Z0-9]+:[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_STRING(t):
    r'"[^"]*"(?:@[a-z]{2})?'
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Identificar SELECT, WHERE, LIMIT como palavras-chave
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.lower() == 'select':
        t.type = TokenType.SELECT
    elif t.value.lower() == 'where':
        t.type = TokenType.WHERE
    elif t.value.upper() == 'LIMIT':
        t.type = TokenType.LIMIT
    return t

# Definir tokens para caracteres especiais
def t_OPEN_BRACE(t):
    r'\{'
    return t

def t_CLOSE_BRACE(t):
    r'\}'
    return t

def t_DOT(t):
    r'\.'
    return t

# Tratamento de espaços em branco - não retorna token (ignora)
def t_WHITESPACE(t):
    r'[ \t\n\r]+'
    t.lexer.lineno += t.value.count('\n')

# Função de erro para caracteres não reconhecidos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir o lexer
def build_lexer():
    # Definir uma variável de estado para rastrear a linha atual
    lexer = lex.lex()
    lexer.lineno = 1
    return lexer

# Função para analisar a query
def analyze_query(query_text):
    lexer = build_lexer()
    lexer.input(query_text)

    # Imprime o cabeçalho
    print("\n{:<15} {:<40} {:<6} {:<6}".format("TIPO", "VALOR", "LINHA", "POS"))
    print("-----------------------------------------------------------------------")

    # Itera sobre os tokens e imprime cada um
    for token in lexer:
        tipo = token.type
        valor = token.value
        linha = token.lineno
        pos = token.lexpos
        print("{:<15} {:<40} {:<6} {:<6}".format(tipo, str(valor), linha, pos))

# Exemplo de uso
if __name__ == "__main__":
    example_query = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000"""

    print("Analise da query:")
    analyze_query(example_query)