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
- Processa o conteúdo linha a linha mantendo a integridade dos campos
- Gerencia estados através de variáveis de controlo:
  - `register`: Lista temporária para campos de uma linha
  - `current_field`: Buffer para construção do campo atual
  - `inside_field`: Controle de campo entre aspas
  - `data`: Estrutura final com todos os registros
- Implementa uma lógica robusta para:
  - Tratamento de campos entre aspas
  - Gerenciamento de quebras de linha dentro de campos
  - Processamento de delimitadores (ponto e vírgula)
  - Limpeza e normalização dos dados

#### 2. Função `interpretar_data(processed_lines)`
Função responsável pela análise dos dados processados:
- Extrai e valida o cabeçalho do arquivo
- Identifica índices das colunas necessárias
- Implementa três análises principais:
  - Lista de compositores únicos
  - Contagem de obras por período
  - Organização de títulos por período
- Inclui tratamento de erros para dados ausentes ou mal formatados

#### 3. Função `write_results(results)`
‘Interface’ de apresentação dos resultados:
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

   Estrutura dos dados:
   - ('Nome', 'id da obra')

   Barroco:
   - ('Ab Irato', 'O41')
   - ('Die Ideale, S.106', 'O58')
   - ('Fantasy No. 2', 'O170')
   - ('Hungarian Rhapsody No. 16', 'O146')
   - ('Hungarian Rhapsody No. 5', 'O44')
   - ('Hungarian Rhapsody No. 8', 'O159')
   - ('Impromptu Op.51', 'O66')
   - ('In the Steppes of Central Asia', 'O161')
   - ('Mazurkas, Op. 50', 'O48')
   - ('Military Band No. 1', 'O108')
   - ('Nocturne in C minor', 'O17')
   - ('Paganini Variations, Book I', 'O145')
   - (...)

   Contemporâneo:
   - ('Impromptu, Op. 36', 'O90')
   - ('Les cinq doigts', 'O35')
   - ('Polonaises, Op.40', 'O45')
   - ('Preludes Opus 51', 'O8')
   - ('Rhapsodies, Op. 79', 'O23')
   - ('Sonnerie de Ste-Geneviève du Mont-de-Paris', 'O26')
   - ('Études Op. 25', 'O137')
   - (...)
  
```

## Análise Técnica

### Áreas de Melhoria
1. Funcionalidades:
   - Melhorar o algoritmo de ordenação para considerar acentuação nas letras
        - Atualmente, a ordenação não leva em conta caracteres acentuados
        - Isso pode causar inconsistências na ordem alfabética em títulos com acentos
        - Implementar normalização Unicode antes da ordenação

## Conclusão

O Processador de Catálogo Musical demonstra uma implementação robusta
para análise de dados musicais em formato CSV. O programa lida efetivamente
com as complexidades de processamento de texto, mantendo a integridade dos
dados e produzindo análises úteis e bem organizadas.

A arquitetura do código, dividida em três funções principais com
responsabilidades bem definidas, facilita a manutenção e extensão do sistema.
O tratamento cuidadoso de casos especiais e a validação de dados garantem
a confiabilidade dos resultados gerados.

A solução atual serve como base sólida para futuras expansões,
como inclusão de análises mais complexas ou integração com sistemas
de gestão musical mais abrangentes.