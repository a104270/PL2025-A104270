
def on_off_sum(text):
    """
    Explicação do código:

    Função on_off_sum(text):
    - Recebe um texto como entrada para processar
    - Utiliza variáveis de controle:
      * results: lista para armazenar as somas parciais
      * current_sum: guarda o valor da soma atual
      * is_active: controla se a soma está ativa ou suspensa
      * current_number: armazena o número sendo construído dígito a dígito

    Lógica de processamento:
    1. Percorre o texto caractere por caractere
    2. Identifica comandos "On" e "Off"
       - "Off" interrompe a soma atual
       - "On" retoma a soma
    3. Constrói numeros dígito por dígito
    4. Adiciona números à soma quando está ativo
    5. Quando encontra "=", adiciona a soma atual à lista de resultados
    6. Continua a acumular a soma entre os sinais de "="
    """

    results = []
    current_sum = 0
    is_active = True
    current_number = ''

    i = 0
    while i < len(text):
        # Check for On/Off commands
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

        # Process current character
        if text[i].isdigit():
            current_number += text[i]
        else:
            # Add number to sum if we have one and is active
            if current_number and is_active:
                current_sum += int(current_number)
            current_number = ''

            # Check for equals sign
            if text[i] == '=':
                results.append(current_sum)

        i += 1

    # Handle any remaining number
    if current_number and is_active:
        current_sum += int(current_number)
        results.append(current_sum)
    return results


def resultado_final(nome_ficheiro):

    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            # Lê o conteúdo do ficheiro
            conteudo = ficheiro.read()

            # Processa o conteúdo
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