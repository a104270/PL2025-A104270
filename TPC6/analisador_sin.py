import ply.yacc as yacc

from analisador_lex import tokens, lexer

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'), # Operadores listados mais abaixo sao processados antes
)
# Logo multiplicaçao e divisao sao processados antes das somas e subtraçoes


# Regra para expressões
def p_expression_plus(p):
    """expression : expression PLUS expression"""
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    """expression : expression MINUS expression"""
    p[0] = p[1] - p[3]

def p_expression_times(p):
    """expression : expression TIMES expression"""
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    """expression : expression DIVIDE expression"""
    p[0] = p[1] / p[3]

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

# Tratamento de erros sintáticos
def p_error(p):
    print("Erro de sintaxe!")

# Construir o parser
parser = yacc.yacc()