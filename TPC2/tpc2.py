import re


def processar_ficheiro(lines):
    content = "".join(lines)

    # Primeiro precisamos reconstruir as linhas lógicas (campos que contêm quebras de linha)
    logical_lines = []
    current_line = ""
    in_quotes = False

    for char in content:
        if char == '"':
            in_quotes = not in_quotes

        current_line += char

        # Se estamos numa nova linha e não estamos dentro de aspas, temos uma linha lógica completa
        if char == '\n' and not in_quotes:
            if current_line.strip():
                logical_lines.append(current_line.strip())
            current_line = ""

    # Adiciona a última linha se houver
    if current_line.strip():
        logical_lines.append(current_line.strip())

    # Agora processamos cada linha lógica para extrair os campos
    data = []
    for line in logical_lines:
        if not line.strip():
            continue

        fields = []
        line_with_end = line + ";"  # Adiciona um ponto e vírgula ao final para facilitar o regex

        # Captura campos entre aspas ou até o próximo ponto e vírgula
        pattern = r'(?:^|;)\s*(?:"((?:[^"]|"")*)"|([^;\r\n]*))(?=;|$)'
        matches = re.finditer(pattern, line_with_end)

        for match in matches:
            # Pega o valor do grupo que foi capturado (com ou sem aspas)
            field = match.group(1) if match.group(1) is not None else match.group(2)

            # Trata aspas duplicadas dentro de campos com aspas (escape de aspas)
            if field is not None:
                field = field.replace('""', '"').strip()
                fields.append(field)

        if fields:
            data.append(fields)

    return data


def interpretar_data(processed_lines):
    if not processed_lines:
        raise ValueError("Erro: O ficheiro está vazio ou mal formatado.")

    header = processed_lines[0]
    try:
        id_idx = header.index("_id")
        title_idx = header.index("nome")
        period_idx = header.index("periodo")
        composer_idx = header.index("compositor")
    except ValueError:
        raise ValueError(f"Erro: Nome de coluna não encontrado. Colunas detectadas: {header}")

    composers = set()
    period_counter = {}
    period_titles = {}

    for line in processed_lines[1:]:
        if len(line) <= max(id_idx, title_idx, period_idx, composer_idx):
            continue

        id_value = line[id_idx].strip()
        title = line[title_idx].strip()
        period = line[period_idx].strip()
        composer = line[composer_idx].strip()

        if not title or not period or not composer:
            continue

        composers.add(composer)
        period_counter[period] = period_counter.get(period, 0) + 1
        period_titles.setdefault(period, []).append((title, id_value))

    return {
        'composers': sorted(composers),
        'period_counter': dict(sorted(period_counter.items())),
        'period_titles': {period: sorted(titles) for period, titles in sorted(period_titles.items())}
    }


def write_results(results):
    print("\n1. Lista ordenada de compositores:")
    for composer in results['composers']:
        print(f"   - {composer}")

    print("\n2. Distribuição de obras por período:")
    for period, count in results['period_counter'].items():
        print(f"   - {period}: {count} obras")

    print("\n3. Títulos das obras por período:")
    for period, titles in results['period_titles'].items():
        print(f"\n   {period}:")
        for title, id_value in titles:
            print(f"   - {title} ({id_value})")


if __name__ == "__main__":
    ficheiro = input("Escreva o nome do ficheiro: ").strip()
    try:
        with open(ficheiro, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = processar_ficheiro(lines)
        results = interpretar_data(processed_lines)
        write_results(results)
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O ficheiro '{ficheiro}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {str(e)}")