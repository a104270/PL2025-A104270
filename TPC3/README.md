# Relatório - Análise de um Conversor Markdown para HTML

**Data:** 27 de Fevereiro de 2025  

## Autor
- **Nome:** Joao Pedro Loureiro Pinto
- **Número:** 104270  
 ![Foto do Autor](../fotoCara.png)

# Descrição
> Programa desenvolvido em Python para converter texto em formato Markdown para HTML.
> O sistema implementa um conversor que transforma elementos de formatação Markdown
> como cabeçalhos, texto em negrito, itálico, links e imagens nas suas respetivas
> tags HTML equivalentes.

## Estrutura do Projeto

O projeto está organizado num único ficheiro principal:

### 1. `tpc3.py`
- Script Python que implementa toda a lógica de conversão
- Contém a função principal `convert_markdown_to_html()`
- Inclui código de teste para demonstrar a funcionalidade
- Utiliza expressões regulares para identificar e transformar elementos Markdown

### Funcionalidades
- Converte cabeçalhos Markdown (# h1, ## h2, ### h3) para tags HTML
- Transforma texto em negrito (**texto**) para tags `<b></b>`
- Converte texto em itálico (*texto*) para tags `<i></i>`
- Processa links Markdown para links HTML `<a href="url">texto</a>`
- Transforma imagens Markdown em imagens HTML `<img src="src" alt="alt"/>`
- Converte listas numeradas para listas ordenadas HTML `<ol><li>...</li></ol>`
- Preserva quebras de linha da estrutura do documento

### Estrutura do Código (tpc3.py)

#### 1. Função `convert_markdown_to_html(markdown_text)`
A função principal que implementa a conversão do Markdown para HTML:
- Divide o texto em linhas para processar elementos baseados em linha (cabeçalhos)
- Utiliza expressões regulares para identificar e substituir padrões Markdown
- Implementa uma abordagem sequencial de transformações:
  1. Processa cabeçalhos (h3, h2, h1) em ordem para evitar conflitos
  2. Substitui texto em negrito usando expressões regulares
  3. Converte texto em itálico
  4. Transforma imagens em tags HTML
  5. Processa links Markdown para âncoras HTML
  6. Converte listas numeradas para listas ordenadas HTML
- Utiliza expressões regulares avançadas para capturar e preservar a estrutura do documento

#### 2. Seção de Teste
Código para testar a funcionalidade do conversor:
- Define um exemplo de texto Markdown com vários elementos
- Exibe o texto Markdown original
- Chama a função `convert_markdown_to_html()` para processar o texto
- Imprime o resultado HTML para comparação

### Regras de Processamento
1. Ordem de Transformação:
   - Cabeçalhos h3 são processados primeiro para evitar conflitos com h2 e h1
   - Elementos em negrito e itálico são processados com expressões non-greedy (`.*?`)
   - Listas numeradas são identificadas e processadas em bloco

2. Expressões Regulares Utilizadas:
   - Negrito: `r'\*\*(.*?)\*\*'` → `<b>\1</b>`
   - Itálico: `r'\*(.*?)\*'` → `<i>\1</i>`
   - Imagens: `r'!\[(.*?)\]\((.*?)\)'` → `<img src="\2" alt="\1"/>`
   - Links: `r'\[(.*?)\]\((.*?)\)'` → `<a href="\2">\1</a>`
   - Listas: `r'(?:^\d+\. .*(?:\n|$))+'` → processado com função auxiliar

3. Tratamento Especial para Listas:
   - Utiliza uma expressão regular multiline para identificar blocos de listas
   - Implementa uma função auxiliar para converter cada item da lista
   - Extrai o conteúdo do item após o número e o ponto
   - Envolve os itens em tags `<li>` e o bloco completo em tags `<ol>`

## Exemplo de Dados

### Entrada Markdown
```markdown
# Exemplo
Este é um exemplo em **bold** e outro em *italic*.
Lista Numerada:
1. First item
2. Second item
3. Third item
Link:
Check out the [página da UC](http://www.uc.pt)
Imagem:
Here's an image: ![imagem dum coelho](http://www.coelho.com)
```

### Saída HTML
```html
<h1>Exemplo</h1>
Este é um exemplo em <b>bold</b> e outro em <i>italic</i>.
Lista Numerada:
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ol>
Link:
Check out the <a href="http://www.uc.pt">página da UC</a>
Imagem:
Here's an image: <img src="http://www.coelho.com" alt="imagem dum coelho"/>
```

## Análise Técnica

### Pontos Fortes
1. Utilização eficiente de expressões regulares para transformações de texto
2. Abordagem sequencial de transformações que evita conflitos entre padrões
3. Tratamento especial para listas numeradas, preservando a sua estrutura

## Conclusão

O Conversor Markdown para HTML demonstra uma implementação eficiente e direta
para transformar elementos básicos de formatação Markdown em HTML. O programa utiliza
expressões regulares de forma eficaz para identificar e substituir padrões, resultando
num código conciso e funcional.

A abordagem sequencial de transformações, especialmente a ordem de processamento
dos cabeçalhos, evita conflitos comuns em conversores de texto. O tratamento especial
para listas numeradas demonstra um bom entendimento dos desafios envolvidos na
conversão de estruturas de bloco.

Embora o conversor atual implemente apenas um subconjunto dos recursos do Markdown,
ele serve como uma base sólida para expansões futuras. A adição de suporte para
elementos como listas não ordenadas, blocos de código e tabelas seria um próximo passo
natural para tornar o conversor mais completo.

Para aplicações que requerem conversão Markdown mais robusta, seria recomendável
considerar o uso de bibliotecas Python especializadas. No entanto, para casos de uso
simples, esta implementação oferece uma solução leve e eficiente que demonstra
bom uso de expressões regulares para manipulação de texto.