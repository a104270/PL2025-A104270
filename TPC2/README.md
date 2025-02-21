# Relatório - Analise de um Dataset

**Data:** 19 de Fevereiro de 2025  

## Autor
- **Nome:** Joao Pedro Loureiro Pito
- **Número:** 104270  
 ![Foto do Autor](../fotoCara.png)

# Descrição
> Programa desenvolvido em Python para processar e analisar 
> um catálogo musical em formato CSV. O sistema implementa um processador
> que extrai informações sobre compositores, períodos musicais e obras, 
> organizando-as de forma estruturada.


## Estrutura do Projeto

O projeto está organizado em três ficheiros principais:

### 1. `obras.csv`
- Ficheiro de dados principal em formato CSV
- Contém o catálogo completo de obras musicais
- Estrutura de colunas:
  ```
  nome;desc;anoCriacao;periodo;compositor;duracao;_id
  ```
- Inclui dados com formatação complexa, incluindo campos com quebras de linha e aspas

### 2. `README.md`
- Documentação principal do projeto
- Contém instruções de utilização
- Descrição das funcionalidades
- Exemplos de uso
- Requisitos do sistema

### 3. `tpc2.py`
- Script Python principal que implementa toda a lógica do programa
- Contém as três funções principais:
  - `processar_ficheiro()`
  - `interpretar_data()`
  - `write_results()`
- Implementa o processamento e análise do catálogo musical
- Inclui tratamento de erros e validação de dados


### Funcionalidades
- Processa arquivos CSV com informações musicais
- Lida com campos que contêm caracteres especiais e quebras de linha
- Extrai e organiza dados sobre compositores, períodos e obras
- Gera relatórios estatísticos e listagens ordenadas
- Suporta processamento de dados com formatação complexa
- Mantém a integridade dos dados mesmo com campos contendo delimitadores

### Estrutura do Código (tpc2.py)

#### 1. Função `processar_ficheiro(lines)`
A função principal que implementa o parsing do CSV:
- Reconstrói as linhas lógicas do CSV considerando campos que contêm quebras de linha
- Implementa uma abordagem baseada em estados de processamento:
  - `current_line`: Buffer para construção da linha lógica atual
  - `in_quotes`: Controla se estamos dentro de um campo entre aspas
  - `logical_lines`: Lista de linhas lógicas completas
- Utiliza expressões regulares para extrair campos depois de reconstruir as linhas lógicas
- Processa cada linha lógica com a seguinte estratégia:
  - Adiciona um ponto e vírgula ao final para facilitar a captura via regex
  - Utiliza um padrão regex para capturar os campos:
    ```python
    pattern = r'(?:^|;)\s*(?:"((?:[^"]|"")*)"|([^;\r\n]*))(?=;|$)'
    ```
    - `(?:^|;)`: Começa no início da linha ou após um ponto e vírgula (não-capturante)
    - `\s*`: Ignora espaços em branco no início do campo
    - `(?:"((?:[^"]|"")*)"`: Captura campos entre aspas, permitindo aspas escapadas (`""`)
    - `|([^;\r\n]*)`: Alternativa para capturar campos sem aspas (até o próximo delimitador)
    - `(?=;|$)`: Lookahead positivo que verifica se o próximo caractere é ponto e vírgula ou fim da linha
  - Trata aspas duplicadas dentro de campos (escape de aspas)
  - Normaliza e limpa os campos capturados

#### 2. Função `interpretar_data(processed_lines)`
Função responsável pela análise dos dados processados:
- Extrai e valida o cabeçalho do arquivo
- Identifica índices das colunas necessárias usando `header.index()`
- Processa cada linha de dados para extrair:
  - Lista de compositores únicos (usando um conjunto `set`)
  - Contagem de obras por período (usando um dicionário contador)
  - Organização de títulos por período (usando dicionário de listas)
- Implementa validações para:
  - Verificação de índices válidos
  - Filtragem de linhas com campos vazios
  - Garantia de estrutura adequada dos dados
- Retorna um dicionário organizado com os três tipos de resultados

#### 3. Função `write_results(results)`
'Interface' de apresentação dos resultados:
- Formata e exibe os compositores em ordem alfabética
- Apresenta estatísticas de obras por período
- Lista os títulos organizados por período musical

### Regras de Processamento
1. Estrutura do CSV:
   - Campos delimitados por ponto e vírgula
   - Suporte a campos com aspas duplas
   - Tratamento de quebras de linha em campos descritivos

2. Validação de Dados:
   - Verificação de campos obrigatórios
   - Tratamento de campos vazios
   - Normalização de espaços e caracteres especiais

3. Organização dos Resultados:
   - Ordenação alfabética de compositores
   - Agrupamento por períodos musicais
   - Contabilização de obras por período

## Exemplo de Dados

### Estrutura do CSV
```text
nome;desc;anoCriacao;periodo;compositor;duracao;_id
```

### Campos Principais
- `nome`: Título da obra
- `periodo`: Período musical (ex: Barroco, Clássico)
- `compositor`: Nome do compositor
- `_id`: Identificador único da obra


## Exemplos de Output

O programa gera três tipos principais de relatórios:

### 1. Lista ordenada de compositores
```
1. Lista ordenada de compositores:
   - Alessandro Stradella
   - Antonio Maria Abbatini
   - Bach, Johann Christoph
   - Bach, Johann Michael
   - Bach, Wilhelm Friedemann
   - Balbastre, Claude
   - Baldassare Galuppi
   (...)
```

### 2. Distribuição de obras por período
```
2. Distribuição de obras por período:
   - Barroco: 26 obras
   - Clássico: 15 obras
   - Contemporâneo: 7 obras
   - Medieval: 48 obras
   - Renascimento: 41 obras
   - Romântico: 19 obras
   - Século XX: 18 obras
```

### 3. Títulos das obras por período
```
3. Títulos das obras por período:

   Barroco:
   - Ab Irato (O41)
   - Die Ideale, S.106 (O58)
   - Fantasy No. 2 (O170)
   - Hungarian Rhapsody No. 16 (O146)
   - Hungarian Rhapsody No. 5 (O44)
   - Hungarian Rhapsody No. 8 (O159)
   - Impromptu Op.51 (O66)
   - In the Steppes of Central Asia (O161)
   - Mazurkas, Op. 50 (O48)
   - Military Band No. 1 (O108)
   - Nocturne in C minor (O17)
   - Paganini Variations, Book I (O145)
   - (...)

   Contemporâneo:
   - Impromptu, Op. 36 (O90)
   - Les cinq doigts (O35)
   - Polonaises, Op.40 (O45)
   - Preludes Opus 51 (O8)
   - Rhapsodies, Op. 79 (O23)
   - Sonnerie de Ste-Geneviève du Mont-de-Paris (O26)
   - Études Op. 25 (O137)
   - (...)
  
```

## Análise Técnica

### Áreas de Melhoria
1. Funcionalidades:
   - Melhorar o algoritmo de ordenação para considerar acentuação nas letras
        - Atualmente, a ordenação não leva em conta caracteres acentuados
        - Isso pode causar inconsistências na ordem alfabética em títulos com acentos
        - Implementar normalização Unicode antes da ordenação
   - Considerar a utilização de bibliotecas como `csv` ou `pandas` para maior eficiência
        - A implementação atual usa expressões regulares, que podem ser complexas de manter
        - Bibliotecas padrão oferecem soluções mais robustas para casos especiais

## Conclusão

O Processador de Catálogo Musical demonstra uma implementação robusta
para análise de dados musicais em formato CSV. O programa lida efetivamente
com as complexidades de processamento de texto, mantendo a integridade dos
dados e produzindo análises úteis e bem organizadas.

A arquitetura do código, dividida em três funções principais com
responsabilidades bem definidas, facilita a manutenção e extensão do sistema.
O tratamento cuidadoso de casos especiais, especialmente a reconstrução de linhas lógicas
com campos contendo quebras de linha, garante a precisão do processamento. O uso
de expressões regulares para a extração de campos proporciona uma solução elegante
para lidar com a complexidade da estrutura do CSV.

A solução atual serve como base sólida para futuras expansões,
como inclusão de análises mais complexas ou integração com sistemas
de gestão musical mais abrangentes.