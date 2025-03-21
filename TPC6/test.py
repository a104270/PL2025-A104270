# Função para testar o parser
from TPC6.analisador_sin import parser


def test_parser(expression):
    result = parser.parse(expression)
    print(f"Resultado de '{expression}': {result}")

# Testes
test_parser("3 + 5 * (10 - 4)")
test_parser("2 * 3 + 4")
test_parser("(2 + 3) * 4")
test_parser("10 / 2 - 3")

while s := input('test ==> '):
   result = parser.parse(s)
   print(result)