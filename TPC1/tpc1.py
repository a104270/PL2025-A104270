
def on_off_sum(text):
    results = []
    current_sum = 0
    is_active = True
    current_number = ''

    i = 0
    while i < len(text):
        if i + 1 < len(text):
            rest_of_text = text[i:].lower()
            if rest_of_text.startswith('off'):
                if current_number and is_active:
                    current_sum += int(current_number)
                current_number = ''
                is_active = False
                i += 3
                continue
            elif rest_of_text.startswith('on'):
                if current_number and is_active:
                    current_sum += int(current_number)
                current_number = ''
                is_active = True
                i += 2
                continue

        if text[i].isdigit():
            current_number += text[i]
        else:
            if current_number and is_active:
                current_sum += int(current_number)
            current_number = ''

            if text[i] == '=':
                results.append(current_sum)

        i += 1

    if current_number and is_active:
        current_sum += int(current_number)
        results.append(current_sum)
    return results


def resultado_final(nome_ficheiro):

    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            conteudo = ficheiro.read()

            return on_off_sum(conteudo)
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{nome_ficheiro}' não encontrado.")
        return []
    except IOError:
        print(f"Erro ao ler o ficheiro '{nome_ficheiro}'.")
        return []


# Teste
ficheiro = input("Escreva o nome do ficheiro: ")
resultados = resultado_final("TPC1/" + ficheiro)
for i, resultado in enumerate(resultados, 1):
    print(f"{i}º= -> {resultado}")