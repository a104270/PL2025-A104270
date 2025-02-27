import re

def convert_markdown_to_html(markdown_text):

    # Converte headers (### primeiro para evitar conflitos com ## and #)
    lines = markdown_text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('### '):
            lines[i] = f"<h3>{line[4:]}</h3>"
        elif line.startswith('## '):
            lines[i] = f"<h2>{line[3:]}</h2>"
        elif line.startswith('# '):
            lines[i] = f"<h1>{line[2:]}</h1>"

    text = '\n'.join(lines)

    # Converte testo a negrito
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    # Converte texto em italico
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)

    # Converte imagens
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)

    # Converte links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    # Converte listas numeradas
    list_pattern = re.compile(r'(?:^\d+\. .*(?:\n|$))+', re.MULTILINE)

    def convert_list(match):
        items = match.group(0).strip().split('\n')
        html_items = [f"<li>{item[item.find('.') + 2:]}</li>" for item in items]
        return "<ol>\n" + "\n".join(html_items) + "\n</ol>"

    text = list_pattern.sub(convert_list, text)

    return text


# Exemplo para teste
test_markdown = """# Exemplo
Este é um exemplo em **bold** e outro em *italic*.

Lista Numerada:
1. First item
2. Second item
3. Third item


Link:
Check out the [página da UC](http://www.uc.pt)

Imagem:
Here's an image: ![imagem dum coelho](http://www.coelho.com)"""

print("Input Markdown:")
print("-" * 40)
print(test_markdown)
print("\nOutput HTML:")
print("-" * 40)
print(convert_markdown_to_html(test_markdown))

