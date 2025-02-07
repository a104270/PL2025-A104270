# Relatório - Somador On/Off

## Descrição
> Programa desenvolvido em Python para processar 
> sequências de números com comandos de ativação/
desativação.

### Funcionalidades
- Soma sequências de dígitos em texto
- Processa comandos "On" e "Off" 
- Lê dados de arquivo .txt
- Apresenta resultados parciais e finais

### Estrutura do Código
1. `on_off_sum(text)`:
   - Processa texto caractere a caractere
   - Controla estado da soma (ativo/inativo)
   - Retorna lista de resultados

2. `resultado_final(nome_ficheiro)`:
   - Lê arquivo de entrada
   - Processa linha a linha
   - Trata erros de arquivo

### Regras de Processamento
- Soma inicia ativa automaticamente
- "Off" pausa a soma
- "On" retoma a soma
- "=" marca ponto de resultado parcial

## Testes

### Exemplo de Uso
```python
ficheiro = input("Escreva o nome do seu ficheiro: ")
resultados = resultado_final(ficheiro)
```
### Exemplo de formato de Entrada
> Escreva o nome do ficheiro: ficheiro.txt
```
123On45Off67On89=On
123Off300=On2025-07-23Off45On67=
12Off34On56=78=
```
### Resultados
```
1º= -> 257
2º= -> 380
3º= -> 2502
4º= -> 2570
5º= -> 2648
```