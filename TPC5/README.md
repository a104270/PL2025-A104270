# Relatório - Máquina de Venda Automática

**Data:** 7 de Março de 2025  

## Autor
- **Nome:** Joao Pedro Loureiro Pinto
- **Número:** 104270  
![Foto do Autor](../fotoCara.png)

# Descrição
> Programa desenvolvido em Python para simular uma máquina de venda automática.
> O sistema permite a inserção de moedas, seleção de produtos, listagem do ‘stock’ disponível, e cálculo de troco.
> O programa utiliza análise léxica para processar comandos do utilizador e interage com um ficheiro JSON para gerir o ‘stock’.

## Estrutura do Projeto

O projeto está organizado em dois ficheiros principais:

### 1. `tpc5.py`
- ‘Script’ Python que implementa a lógica da máquina de venda automática.
- Utiliza a biblioteca PLY para análise léxica dos comandos do utilizador.
- Interage com um ficheiro JSON (`stock.json`) para gerir o ‘stock’ de produtos.
- Contém funções para processar moedas, selecionar produtos, calcular troco, e listar o ‘stock’.

### 2. `stock.json`
- Ficheiro JSON que contém a lista de produtos disponíveis na máquina.
- Cada produto tem um código, nome, quantidade disponível, e preço.

### Funcionalidades
- **LISTAR:** Lista todos os produtos disponíveis no ‘stock’.
- **MOEDA:** Permite ao utilizador inserir moedas (ex: 1e, 50c, 10c).
- **SELECIONAR:** Seleciona um produto pelo código, verificando se há saldo suficiente e stock disponível.
- **SAIR:** Termina a operação e devolve o troco ao utilizador.
- **HELP:** Mostra uma mensagem de ajuda com os comandos disponíveis.
- **Processamento de Moedas:** Converte moedas inseridas em saldo (em cêntimos).
- **Cálculo de Troco:** Calcula o troco em moedas válidas (2e, 1e, 50c, etc.).
- **Atualização de ‘Stock’:** atualiza o ficheiro JSON após cada venda.

### Estrutura do Código (tpc5.py)

#### 1. Definição de ‘Tokens’
A classe `TokenType` define os tipos de ‘tokens’ suportados:
- Comandos: LISTAR, MOEDA, SELECIONAR, SAIR, HELP
- Elementos: CODIGO, QUANTIDADE, PRECO

#### 2. Regras de Reconhecimento de ‘Tokens’
Implementa funções específicas para cada tipo de token:
- `t_LISTAR`: Reconhece o comando "listar".
- `t_MOEDA`: Reconhece o comando "moeda" seguido de valores de moeda (ex: 1e, 50c).
- `t_SELECIONAR`: Reconhece o comando "selecionar" seguido de um código de produto.
- `t_SAIR`: Reconhece o comando "sair".
- `t_HELP`: Reconhece o comando "help".
- `t_CODIGO`: Reconhece códigos de produtos.
- `t_QUANTIDADE`: Reconhece quantidades numéricas.
- `t_PRECO`: Reconhece preços numéricos.
- `t_ignore`: Ignora espaços em branco.
- `t_error`: Trata caracteres não reconhecidos.

#### 3. Função `build_lexer()`
- Inicializa o lexer com o PLY.
- Configura o estado inicial para processar os comandos do utilizador.

#### 4. Função `carregar_stock()`
- Carrega o stock de produtos a partir do ficheiro JSON (`stock.json`).

#### 5. Função `guardar_stock(stock)`
- Guarda o ‘stock’ atualizado no ficheiro JSON.

#### 6. Função `listar_stock(stock)`
- Lista todos os produtos disponíveis no stock.

#### 7. Função `processar_moedas(entrada)`
- Processa as moedas inseridas pelo utilizador e converte-as em saldo.

#### 8. Função `selecionar_produto(stock, saldo, entrada)`
- Seleciona um produto pelo código, verificando se há saldo suficiente e stock disponível.
- Atualiza o stock e o saldo após a compra.

#### 9. Função `calcular_troco(saldo)`
- Calcula o troco em moedas válidas.

#### 10. Função `mostrar_help()`
- Mostra uma mensagem de ajuda com os comandos disponíveis.

#### 11. Função `main()`
- Função principal que controla o fluxo do programa.
- Processa os comandos do utilizador e interage com o stock.

### Regras de Processamento
1. **Ordem de Reconhecimento:**
   - Comandos como "listar", "moeda", "selecionar", "sair", e "help" são processados primeiro.
   - Espaços em branco são ignorados.
   - Caracteres não reconhecidos são tratados como erros.

2. **Expressões Regulares Utilizadas:**
   - Comandos: `r'listar'`, `r'moeda\s+\d+[e|c]'`, `r'selecionar\s+\w+'`, `r'sair'`, `r'help'`
   - Códigos de produtos: `r'\w+'`
   - Quantidades e preços: `r'\d+'`

3. **Tratamento Especial:**
   - Moedas são convertidas em saldo (em cêntimos).
   - O stock é atualizado após cada venda.
   - O troco é calculado em moedas válidas.

## Exemplo de Dados

### Entrada #1
```
==> MOEDA 1e, 50c
```

### Saída do Programa #1
```
Saldo = 150c
```

### Entrada #2
```
==> LISTAR
```
### Saída do Programa #2
```
==================================================================
                         STOCK DISPONÍVEL                          
==================================================================
| CÓDIGO |             CARRINHO             | QUANTIDADE | PREÇO |
------------------------------------------------------------------
| HW01   | Hot Wheels Mustang Shelby GT     |     2      |  2.5  |
| HW02   | Hot Wheels Ferrari F40           |     7      |  2.5  |
| HW03   | Hot Wheels Nissan Skyline R32    |     4      |  3.0  |
| HW04   | Hot Wheels McLaren P1            |     6      |  3.5  |
| HW05   | Hot Wheels Lamborghini Aventador |     3      |  3.8  |
| HW06   | Hot Wheels Bugatti Chiron        |     2      |  4.0  |
| HW07   | Hot Wheels Lexus LFA             |     8      |  3.2  |
| HW08   | Hot Wheels Porsche 918           |     5      |  3.6  |
| HW09   | Hot Wheels Toyota GR Yaris       |     6      |  2.9  |
| HW10   | Hot Wheels Ferrari LaFerrari     |     4      |  3.4  |
==================================================================
```

### Entrada #3
```
==> SELECIONAR HW01
```
### Saída do Programa #3
```
Produto dispensado: "Hot Wheels Mustang Shelby GT"
```

### Entrada #4
```
==> SAIR
```
### Saída do Programa #4
```
Pode retirar o troco: 1x 50c
Até à próxima!
```

## Análise Técnica

### Pontos Fortes
1. Utilização eficiente da biblioteca PLY para análise léxica.
2. Interação com ficheiro JSON para gerir o stock de produtos.
3. Tratamento adequado de moedas e cálculo de troco.
4. Interface simples e intuitiva para o utilizador.

## Conclusão

O programa desenvolvido demonstra uma implementação eficiente e robusta de uma máquina de venda automática. 
A utilização da biblioteca PLY permite um processamento rápido e confiável dos comandos do utilizador, 
enquanto a interação com o ficheiro JSON garante uma gestão eficaz do stock.

A abordagem de definir funções específicas para cada comando, combinada com expressões regulares bem definidas,
permite um reconhecimento confiável dos elementos de entrada. O tratamento adequado de moedas, stock, 
e troco agregam valor significativo para aplicações de venda automática.

Embora o programa atual implemente apenas um subconjunto de funcionalidades, 
este serve como uma base sólida para expansões futuras, como a adição de novos comandos ou 
a integração com sistemas de pagamento eletrónico.