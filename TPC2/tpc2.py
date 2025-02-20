def processar_ficheiro(lines):
    content = "".join(lines).strip()

    register = [] # Lista temporária para armazenar campos de uma linha
    current_field = "" # String para construir o campo atual
    inside_field = False # Indica se estamos num campo entre aspas
    data = [] # Lista para armazenar todos os registos

    for char in content:
        if char == ';':
            if inside_field:
                current_field += char # Se estiver entre aspas, inclui o ponto e vírgula no campo
            else:
                register.append(current_field.strip()) # Caso contrário, finaliza o campo atual
                current_field = ""
        elif char in ('\n', '\r'):
            if inside_field:
                current_field += ' '  # Se estiver entre aspas, converte quebra de linha em espaço
            else:
                if current_field:
                    register.append(current_field.strip()) # Finaliza campo atual
                    current_field = ""
                if register:
                    data.append(register)  # Finaliza o registo atual
                    register = []
        elif char == '"':
            inside_field = not inside_field # Alterna o estado de estar dentro/fora de aspas
        else:
            current_field += char # Adiciona o character ao campo atual

    # Para nao perder o último registo caso nao haja uma quebra de linha no final
    if current_field:
        register.append(current_field.strip())
    if register:
        data.append(register)

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

    composers = set() # Conjunto para armazenar compositores únicos
    period_counter = {} # Dicionário para contar obras por período
    period_titles = {} # Dicionário para armazenar títulos por período

    for line in processed_lines[1:]: # Itera sobre todas as linhas exceto o cabeçalho
        if len(line) <= max(id_idx, title_idx, period_idx, composer_idx): # Salta linhas que não têm todos os campos necessários
            continue

        id = line[id_idx].strip()
        title = line[title_idx].strip()
        period = line[period_idx].strip()
        composer = line[composer_idx].strip()

        if not title or not period or not composer:
            continue

        composers.add(composer)
        period_counter[period] = period_counter.get(period, 0) + 1
        period_titles.setdefault(period, []).append((title, id))

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
        for title in titles:
            print(f"   - {title}")


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
