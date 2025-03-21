# Relatório - Analisador de Expressões Matemáticas

**Data:** 21 de Março de 2025  

## Autor
- **Nome:** Joao Pedro Loureiro Pinto
- **Número:** 104270  
![Foto do Autor](../fotoCara.png)

# Descrição
> Programa desenvolvido em Python para analisar e avaliar expressões matemáticas.
> O sistema utiliza análise léxica e sintática para processar expressões aritméticas inseridas pelo utilizador.
> O programa implementa um interpretador capaz de reconhecer operadores matemáticos básicos e calcular o resultado de expressões complexas.

## Estrutura do Projeto

O projeto está organizado em três ficheiros principais:

### 1. `analisador_lex.py`
- 'Script' Python que implementa a análise léxica das expressões matemáticas.
- Utiliza a biblioteca PLY para definir e reconhecer os ‘tokens’.
- Define os operadores matemáticos, números e parênteses como tokens válidos.

### 2. `analisador_sin.py`
- 'Script' Python que implementa a análise sintática das expressões.
- Utiliza a biblioteca PLY para definir as regras gramaticais.
- Implementa operações aritméticas básicas (soma, subtração, multiplicação, divisão).
- Define a precedência dos operadores matemáticos.

### 3. `test.py`
- Ficheiro de teste que utiliza o analisador para avaliar expressões matemáticas de exemplo.
- Demonstra o funcionamento do parser em diferentes tipos de expressões.

### Funcionalidades
- **Reconhecimento de Números:** Identifica números inteiros e decimais.
- **Operações Aritméticas:** Suporta adição, subtração, multiplicação e divisão.
- **Agrupamento com Parênteses:** Permite o uso de parênteses para alterar a precedência.
- **Precedência de Operadores:** Implementa a ordem correta de operações matemáticas.
- **Tratamento de Erros:** Identifica caracteres ilegais e erros de sintaxe.

### Estrutura do Código

#### 1. `analisador_lex.py`

##### 1.1 Definição de 'Tokens'
Define os tipos de tokens suportados:
- `NUMBER`: Números inteiros ou decimais
- `PLUS`: Operador de adição (+)
- `MINUS`: Operador de subtração (-)
- `TIMES`: Operador de multiplicação (*)
- `DIVIDE`: Operador de divisão (/)
- `LPAREN`: Parêntese esquerdo (()
- `RPAREN`: Parêntese direito ())

##### 1.2 Regras de Reconhecimento de 'Tokens'
Implementa expressões regulares para cada tipo de token:
- Operadores simples: `t_PLUS`, `t_MINUS`, `t_TIMES`, `t_DIVIDE`
- Parênteses: `t_LPAREN`, `t_RPAREN`
- Números: `t_NUMBER` (função que converte o valor para float)
- `t_ignore`: Ignora espaços em branco e tabulações
- `t_error`: Trata caracteres não reconhecidos

##### 1.3 Construção do Lexer
- Inicializa o analisador léxico com a função `lex.lex()`

#### 2. `analisador_sin.py`

##### 2.1 Definição de Precedência
Define a ordem de precedência dos operadores:
- Menor precedência: Adição e subtração (left-associative)
- Maior precedência: Multiplicação e divisão (left-associative)

##### 2.2 Regras Gramaticais
Implementa funções para cada regra gramatical:
- `p_expression_plus`: Regra para adição
- `p_expression_minus`: Regra para subtração
- `p_expression_times`: Regra para multiplicação
- `p_expression_divide`: Regra para divisão
- `p_expression_group`: Regra para expressões entre parênteses
- `p_expression_number`: Regra para números

##### 2.3 Tratamento de Erros
- `p_error`: Função para tratamento de erros sintáticos

##### 2.4 Construção do Parser
- Inicializa o analisador sintático com a função `yacc.yacc()`

#### 3. `test.py`

##### 3.1 Função de Teste
- Define a função `test_parser` que recebe uma expressão, utiliza o parser para avaliá-la e imprime o resultado

##### 3.2 Casos de Teste
Testa o analisador com diferentes expressões:
- Expressão com precedência mista: `"3 + 5 * (10 - 4)"`
- Expressão simples: `"2 * 3 + 4"`
- Expressão com parênteses: `"(2 + 3) * 4"`
- Expressão com divisão: `"10 / 2 - 3"`

### Regras de Processamento
1. **Ordem de Reconhecimento:**
   - ‘Tokens’ como números, operadores e parênteses são identificados pelo analisador léxico
   - O analisador sintático aplica as regras gramaticais conforme a precedência definida
   - Parênteses têm precedência sobre todos os operadores

2. **Expressões Regulares Utilizadas:**
   - Operadores: `r'\+'`, `r'-'`, `r'\*'`, `r'/'`
   - Parênteses: `r'\('`, `r'\)'`
   - Números: `r'\d+(\.\d+)?'`

3. **Tratamento Especial:**
   - Números são convertidos para o tipo float
   - Os operadores têm precedência definida (multiplicação/divisão > adição/subtração)
   - Espaços e tabulações são ignorados

## Exemplo de Dados

### Entrada #1
```
3 + 5 * (10 - 4)
```

### Saída do Programa #1
```
Resultado de '3 + 5 * (10 - 4)': 33.0
```

### Entrada #2
```
2 * 3 + 4
```
### Saída do Programa #2
```
Resultado de '2 * 3 + 4': 10.0
```

### Entrada #3
```
(2 + 3) * 4
```
### Saída do Programa #3
```
Resultado de '(2 + 3) * 4': 20.0
```

### Entrada #4
```
10 / 2 - 3
```
### Saída do Programa #4
```
Resultado de '10 / 2 - 3': 2.0
```

## Análise Técnica

### Pontos Fortes
1. Utilização eficiente da biblioteca PLY para análise léxica e sintática.
2. Implementação correta da precedência de operadores matemáticos.
3. Suporte para expressões complexas com parênteses.
5. Estrutura modular separando análise léxica e sintática.

## Conclusão

O programa desenvolvido demonstra uma implementação eficiente e robusta de um analisador de expressões matemáticas. 
A utilização da biblioteca PLY permite um processamento preciso e confiável das expressões, seguindo corretamente as 
regras de precedência matemática.

A separação entre o analisador léxico e o sintático segue boas práticas de desenvolvimento, 
permitindo uma manutenção mais fácil e possíveis extensões futuras. A capacidade de processar expressões complexas com 
parênteses e diferentes operadores torna o programa versátil para diversas aplicações matemáticas.

O sistema implementado serve como uma base sólida para o desenvolvimento de interpretadores mais complexos ou calculadoras programáveis. 
Embora atualmente suporte apenas operações aritméticas básicas, a estrutura modular facilita a adição de 
novas funcionalidades como operadores adicionais, funções matemáticas avançadas ou suporte para variáveis.