import json
import re
from collections import defaultdict
import ply.lex as lex

STOCK_FILE = "stock.json"
MOEDAS_VALIDAS = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

# Tokens definidos para a análise léxica
tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR', 'HELP', 'CODIGO', 'QUANTIDADE', 'PRECO')

# Definindo os padrões lexicais para os tokens
t_LISTAR = r'listar'
t_MOEDA = r'moeda\s+\d+[e|c]'
t_SELECIONAR = r'selecionar\s+\w+'
t_SAIR = r'sair'
t_HELP = r'help'
t_CODIGO = r'\w+'
t_QUANTIDADE = r'\d+'
t_PRECO = r'\d+'

# Ignorar espaços em branco
t_ignore = ' \t'

# Função para lidar com erros lexicais
def t_error(t):
    print("Comando inválido.")
    t.lexer.skip(1)

# Função para inicializar o lexer
def build_lexer():
    lexer = lex.lex()
    return lexer

def carregar_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

def listar_stock(stock):
    print("\n==================================================================")
    print("                         STOCK DISPONÍVEL                          ")
    print("==================================================================")
    print("| CÓDIGO |             CARRINHO             | QUANTIDADE | PREÇO |")
    print("------------------------------------------------------------------")
    for item in stock:
        print(f"| {item['cod']:<6} | {item['nome']:<32} | {item['quant']:^10} | {item['preco']:^5} |")
    print("==================================================================\n")

def processar_moedas(entrada):
    saldo = 0
    entrada = entrada.lower()
    moeda_re = re.findall(r"(\d+e|\d+c)", entrada, re.IGNORECASE)
    for moeda in moeda_re:
        if moeda.lower() in MOEDAS_VALIDAS:
            saldo += MOEDAS_VALIDAS[moeda.lower()]
    return saldo

def selecionar_produto(stock, saldo, entrada):
    match = re.search(r"(?i)SELECIONAR\s+(\w+)", entrada, re.IGNORECASE)
    if match:
        codigo = match.group(1).upper()
        for item in stock:
            if item["cod"] == codigo:
                preco = int(item["preco"] * 100)
                if saldo >= preco and item["quant"] > 0:
                    item["quant"] -= 1
                    saldo -= preco
                    print(f"Produto dispensado: \"{item['nome']}\"")
                else:
                    print(f"Saldo insuficiente!")
                    print(f"Saldo = {saldo}c | Pedido = {preco}c")
                return saldo
        print("Produto inexistente")
    return saldo


from collections import defaultdict


def calcular_troco(saldo):
    troco = defaultdict(int)

    # Lista de moedas ordenadas manualmente por valor em ordem decrescente
    moedas_ordenadas = [("2e", 200), ("1e", 100), ("50c", 50), ("20c", 20), ("10c", 10), ("5c", 5), ("2c", 2), ("1c", 1)]

    # Itera sobre as moedas ordenadas
    for moeda, valor in moedas_ordenadas:
        while saldo >= valor:
            troco[moeda] += 1
            saldo -= valor

    return troco

def mostrar_help():
    print("\n================================================================")
    print("                              AJUDA                              ")
    print("================================================================")
    print("  LISTAR                 - Mostra os produtos disponíveis")
    print("  MOEDA <moedas>        - Insere moedas (ex: MOEDA 1e, 50c, 10c)")
    print("  SELECIONAR <código>   - Escolhe um produto pelo código")
    print("  SAIR                  - Termina a operação e devolve o troco")
    print("  HELP                  - Mostra esta mensagem de ajuda")
    print("================================================================\n")

def main():
    stock = carregar_stock()
    print("Máquina ligada! Stock carregado e atualizado.")
    print("Olá! Estou disponível para atender o seu pedido.")
    saldo = 0

    lexer = build_lexer()

    while True:
        entrada = input("==> ")
        lexer.input(entrada.lower())

        comando_processado = False
        for tok in lexer:
            if tok.type == 'LISTAR':
                listar_stock(stock)
                comando_processado = True
            elif tok.type == 'MOEDA':
                saldo += processar_moedas(entrada)
                print(f"Saldo = {saldo}c")
                comando_processado = True
            elif tok.type == 'SELECIONAR':
                saldo = selecionar_produto(stock, saldo, entrada)
                comando_processado = True
            elif tok.type == 'SAIR':
                troco = calcular_troco(saldo)
                if troco:
                    print("Pode retirar o troco:", ", ".join([f"{v}x {k}" for k, v in troco.items()]))
                print("Até à próxima!")
                guardar_stock(stock)
                return
            elif tok.type == 'HELP':
                mostrar_help()
                comando_processado = True

        if not comando_processado:
            print("Comando inválido. Tente novamente.")

if __name__ == "__main__":
    main()
