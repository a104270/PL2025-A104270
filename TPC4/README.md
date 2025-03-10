# Relatório - Análise de um Tokenizador

**Data:** 7 de Março de 2025  

## Autor
- **Nome:** Joao Pedro Loureiro Pinto
- **Número:** 104270  
-  ![Foto do Autor](../fotoCara.png)

# Descrição
> Programa desenvolvido em Python para analisar e tokenizar consultas.
> O sistema implementa um tokenizador (lexer) que identifica e classifica os
> diferentes elementos sintáticos de uma consulta, como palavras-chave,
> variáveis, prefixos, ‘strings’, números e símbolos especiais.

## Estrutura do Projeto

O projeto está organizado num único ficheiro principal:

### 1. `tpc4.py`
- ‘Script’ Python que implementa toda a lógica de tokenização
- Utiliza a biblioteca PLY para análise léxica
- Contém a definição dos tipos de ‘tokens’ e as suas regras de reconhecimento
- Inclui código de teste para demonstrar a funcionalidade

### Funcionalidades
- Reconhece palavras-chave (SELECT, WHERE, LIMIT)
- Identifica variáveis (começando com ?)
- Reconhece prefixos no formato namespace:termo
- Processa strings com suporte a tags de idioma (@en, @pt, etc.)
- Identifica símbolos especiais como chaves ({}) e pontos (.)
- Reconhece números e converte-os para inteiros
- Ignora espaços em branco, mantendo o controle correto de números de linha
- Detecta e reporta caracteres ilegais
- Exibe informações detalhadas sobre cada ‘token’, incluindo tipo, valor, linha e posição

### Estrutura do Código (tpc4.py)

#### 1. Definição de ‘Tokens’
A classe `TokenType` define os tipos de ‘tokens’ suportados:
- Palavras-chave: COMMENT, SELECT, WHERE, LIMIT
- Símbolos: OPEN_BRACE, CLOSE_BRACE, DOT
- Elementos: VARIABLE, PREFIX, STRING
- Elementos básicos: NUMBER, IDENTIFIER
- Controle de erros: ERROR

#### 2. Regras de Reconhecimento de ‘Tokens’
Implementa funções específicas para cada tipo de token:
- `t_COMMENT`: Reconhece comentários iniciados por #
- `t_VARIABLE`: Identifica variáveis SPARQL (começando com ?)
- `t_PREFIX`: Reconhece prefixos no formato namespace:termo
- `t_STRING`: Processa ‘strings’ com suporte a ‘tags’ de idioma
- `t_NUMBER`: Identifica e converte números para inteiros
- `t_IDENTIFIER`: Reconhece identificadores e determina se são palavras-chave
- `t_OPEN_BRACE`, `t_CLOSE_BRACE`, `t_DOT`: Reconhecem símbolos especiais
- `t_WHITESPACE`: Processa espaços em branco e mantém contagem de linhas
- `t_error`: Trata caracteres não reconhecidos

#### 3. Função `build_lexer()`
- Inicializa o lexer com o PLY
- Configura o estado inicial para rastrear as linhas

#### 4. Função `analyze_query(query_text)`
- Recebe o texto da consulta
- Inicializa o lexer e fornece o texto de entrada
- Itera sobre todos os tokens identificados
- Exibe informações detalhadas sobre cada ‘token’:
  - Tipo do token
  - Valor do token
  - Número da linha
  - Posição do caractere no texto de entrada

#### 5. Secção de Teste
Código para testar a funcionalidade do tokenizador:
- Define um exemplo de consulta SPARQL sobre obras de Chuck Berry
- Chama a função `analyze_query()` para processar a consulta
- Exibe o resultado da tokenização

### Regras de Processamento
1. Ordem de Reconhecimento:
   - Comentários e elementos complexos são processados primeiro
   - Identificadores são verificados para palavras-chave SPARQL
   - Espaços em branco são processados, mas não retornados como ‘tokens’

2. Expressões Regulares Utilizadas:
   - Comentários: `r'\#.*'`
   - Variáveis: `r'\?[a-zA-Z][a-zA-Z0-9_]*'`
   - Prefixos: `r'[a-zA-Z0-9]+:[a-zA-Z][a-zA-Z0-9]*'`
   - Strings: `r'"[^"]*"(?:@[a-z]{2})?'`
   - Números: `r'[0-9]+'`
   - Identificadores: `r'[a-zA-Z][a-zA-Z0-9_]*'`
   - Símbolos especiais: `r'\{'`, `r'\}'`, `r'\.'`
   - Espaços em branco: `r'[ \t\n\r]+'`

3. Tratamento Especial:
   - Números são convertidos de ‘string’ para inteiros
   - Identificadores são verificados para determinar se são palavras-chave
   - Espaços em branco são usados para rastrear números de linha, mas não retornados como ‘tokens’
   - Posições dos ‘tokens’ são rastreadas para referência na saída

## Exemplo de Dados

### Entrada
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
```

### Saída do Tokenizador
```
TIPO            VALOR                                    LINHA   POS   
-----------------------------------------------------------------------
COMMENT         # DBPedia: obras de Chuck Berry          1       0     
SELECT          select                                   2       31    
VARIABLE        ?nome                                    2       38    
VARIABLE        ?desc                                    2       44    
WHERE           where                                    2       50    
OPEN_BRACE      {                                        2       56    
VARIABLE        ?s                                       3       58    
IDENTIFIER      a                                        3       61    
PREFIX          dbo:MusicalArtist                        3       63    
DOT             .                                        3       80    
VARIABLE        ?s                                       4       82    
PREFIX          foaf:name                                4       85    
STRING          "Chuck Berry"@en                         4       95    
DOT             .                                        4       112   
VARIABLE        ?w                                       5       114   
PREFIX          dbo:artist                               5       117   
VARIABLE        ?s                                       5       128   
DOT             .                                        5       130   
VARIABLE        ?w                                       6       132   
PREFIX          foaf:name                                6       135   
VARIABLE        ?nome                                    6       145   
DOT             .                                        6       150   
VARIABLE        ?w                                       7       152   
PREFIX          dbo:abstract                             7       155   
VARIABLE        ?desc                                    7       168   
CLOSE_BRACE     }                                        8       174   
LIMIT           LIMIT                                    8       176   
NUMBER          1000                                     8       182   
```

## Análise Técnica

### Pontos Fortes
1. Utilização eficiente da biblioteca PLY para análise léxica
2. Expressões regulares bem definidas para cada tipo de ‘token’
3. Tratamento adequado de espaços em branco e números de linha
5. Informações detalhadas sobre cada ‘token’, incluindo posições

## Conclusão

O Tokenizador desenvolvido demonstra uma implementação eficiente e robusta
para análise léxica de consultas. O programa utiliza a biblioteca PLY de forma
eficaz para definir e reconhecer os diversos elementos sintáticos de uma consulta,
o que resulta num código bem estruturado e funcional.

A abordagem de definir funções específicas para cada tipo de ‘token’, combinada com
expressões regulares, permite um reconhecimento confiável dos elementos
da consulta. O tratamento adequado de espaços em branco e o rastreamento correto
de números de linha e posições dos ‘tokens’ agregam valor significativo para aplicações
de processamento e análise de consultas.

Embora o tokenizador atual implemente apenas um subconjunto dos elementos da
sintaxe, este serve como uma base sólida para expansões futuras. 
