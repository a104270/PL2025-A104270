# Relatório - Somador On/Off

**Data:** 9 de Fevereiro de 2024  

## Autor
- **Nome:** Joao Pedro Loureiro Pito
- **Número:** 104270  
 ![Foto do Autor](../fotoCara.png)

## Descrição
> Programa desenvolvido em Python para processar sequências de números 
> com comandos de ativação/desativação. 
> O sistema implementa um somador inteligente que pode ser controlado 
> através de comandos "On" e "Off", permitindo somas parciais e totais 
> de sequências numéricas.


### Funcionalidades
- Soma sequências de dígitos em texto
- Processa comandos "On" e "Off" para controle da soma
- Lê dados de um ficheiro.txt
- Apresenta resultados parciais e finais
- Mantém estado entre comandos de igualdade
- Suporta processamento de múltiplas linhas

### Estrutura do Código

#### 1. Função `on_off_sum(text)`
A função principal que implementa a lógica do somador:
- Processa texto caractere a caractere usando um loop while controlado
- Mantém estado através de variáveis de controlo:
  - `results`: Lista para armazenar resultados parciais
  - `current_sum`: Acumulador da soma atual
  - `is_active`: Controle do estado ativo/inativo
  - `current_number`: Buffer para construção de números
- Implementa lógica robusta para:
  - Detecção de comandos On/Off
  - Construção de números dígito a dígito
  - Processamento de sinais de igualdade
  - Tratamento de casos limite

#### 2. Função `resultado_final(nome_ficheiro)`
Função de interface com o sistema de arquivos:
- Gerencia a leitura do arquivo de entrada
- Implementa tratamento de erros para:
  - Arquivo não encontrado
  - Problemas de I/O
- Integra com a função de processamento principal

### Regras de Processamento
1. Estado Inicial:
   - Soma começa ativa por padrão
   - Acumulador inicia em zero

2. Comandos de Controle:
   - "Off": Suspende a soma atual
   - "On": Retoma a soma do ponto atual
   - "=": Marca ponto de resultado parcial

3. Comportamento Especial:
   - Estado de ativação persiste entre sinais de igualdade
   - Soma continua acumulando após cada resultado parcial

## Exemplos de Uso

### Entrada de Dados
```text
123On45Off67On89=On
123Off300=On2025-07-23Off45On67=
12Off34On56=78=
```

### Saída Processada
```text
1º= -> 257
2º= -> 380
3º= -> 2502
4º= -> 2570
5º= -> 2648
```

## Análise Técnica

### Áreas de Melhoria
1. Performance:
   - Implementar buffer de leitura para arquivos grandes
   - Otimizar construção de ‘strings’ para números

## Conclusão

O Somador On/Off demonstra uma implementação robusta e flexível 
para processamento de sequências numéricas com controlo de estado. 
O programa consegue lidar efetivamente com diferentes cenários de entrada,
mantendo um controlo preciso sobre o estado da soma e produzindo resultados consistentes.

A arquitetura do código, dividida em duas funções principais com 
responsabilidades bem definidas, facilita a manutenção e extensão do sistema. 
O tratamento de erros implementado garante uma execução segura mesmo em condições adversas.

A solução atual serve como uma base sólida para futuras expansões, 
como suporte a operações mais complexas ou integração com outros 
sistemas de processamento de dados.