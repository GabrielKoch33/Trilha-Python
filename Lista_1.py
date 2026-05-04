# =====================================================================
# Exercício 001: Simulador de fila de atendimento com prioridades.
# Crie um sistema que simula uma fila de atendimento em uma clínica.
# Cada paciente deve ser armazenado como uma tupla: (nome, idade, prioridade).
# A prioridade pode ser:
#   "NORMAL"
#   "PREFERENCIAL"
#   "URGENTE"
# =====================================================================
#
# Menu:
#
# 1 - Adicionar paciente
# 2 - Chamar próximo paciente
# 3 - Listar fila
# 4 - Buscar paciente pelo nome
# 5 - Cancelar atendimento de paciente
# 0 - Sair
#
# Regras:
#
# - Pacientes URGENTE devem ser chamados antes de todos.
# - Pacientes PREFERENCIAL devem ser chamados antes dos NORMAIS.
# - Dentro da mesma prioridade, respeite a ordem de chegada.
# - Não permita nome vazio.
# - Não permita idade menor ou igual a zero.
# - Ao chamar paciente, remova-o da fila.
# - Se a fila estiver vazia, informe corretamente.


# =====================================================================
# Exercício 002: Compactador e descompactador de texto simples.
# Crie um programa que compacte e descompacte textos simples.
# A compactação deve transformar repetições consecutivas em letra + quantidade.
# Exemplo:
#   Entrada: aaabbccccd
#   Saída: a3b2c4d1
# A descompactação deve fazer o inverso.
# Exemplo:
#   Entrada: a3b2c4d1
#   Saída: aaabbccccd
# =====================================================================
#
# Menu:
#
# 1 - Compactar texto
# 2 - Descompactar texto
# 0 - Sair
#
# Regras:
#
# - Use while para percorrer a string.
# - Não use bibliotecas.
# - Considere apenas letras seguidas de números de 1 dígito, por enquanto.
# - Valide texto vazio.
# - Na compactação, cuidado com o último bloco de caracteres.


# =====================================================================
# Exercício 003: Sistema de estoque com listas paralelas.
# Crie um sistema de estoque usando três listas paralelas.
# =====================================================================
#
# Estrutura obrigatória:
#
# produtos = []
# quantidades = []
# precos = []
#
# Menu:
#
# 1 - Cadastrar produto
# 2 - Entrada de estoque
# 3 - Saída de estoque
# 4 - Alterar preço
# 5 - Consultar produto
# 6 - Listar estoque completo
# 7 - Mostrar valor total em estoque
# 0 - Sair
#
# Regras:
#
# - Não permitir produto duplicado.
# - Não permitir quantidade negativa.
# - Não permitir preço menor ou igual a zero.
# - Saída de estoque não pode ultrapassar a quantidade disponível.
# - Consulta deve mostrar nome, quantidade, preço unitário e valor total daquele produto.
# - Valor total em estoque = soma de quantidade * preço de todos os produtos.


# =====================================================================
# Exercício 004: Analisador de transações financeiras sem dicionário.
# Crie funções para analisar transações financeiras.
# =====================================================================
#
# Estrutura obrigatória:
#
# transacoes = [
#     ("entrada", 1500.00),
#     ("saida", 300.00),
#     ("saida", 200.00),
#     ("entrada", 700.00),
#     ("saida", 2500.00)
# ]
#
# Regras:
#
# - O programa deve mostrar o total de entradas.
# - O programa deve mostrar o total de saídas.
# - O programa deve mostrar o saldo final.
# - O programa deve mostrar a maior entrada.
# - O programa deve mostrar a maior saída.
# - O programa deve mostrar em qual transação o saldo ficou negativo pela primeira vez.
# - O programa deve mostrar a lista de transações suspeitas.
# - Uma transação é suspeita quando a saída for maior que 1000.
# - Uma transação é suspeita quando a entrada for maior que 5000.
# - Não usar dicionário.
# - Use tuplas.
# - Use função para cada análise principal.
# - Não use sum(), max() ou min() nas partes principais.


# =====================================================================
# Exercício 005: Validador de comandos de terminal simplificado.
# Crie um programa que simula comandos básicos digitados pelo usuário.
# Esse exercício já começa a parecer ferramenta real de automação.
# =====================================================================
#
# Estrutura obrigatória:
#
# Comandos válidos:
# add nome_do_arquivo
# remove nome_do_arquivo
# list
# clear
# exit
#
# Exemplo de uso:
#
# > add dados.csv
# Arquivo adicionado.
#
# > add logs.txt
# Arquivo adicionado.
#
# > list
# 1 - dados.csv
# 2 - logs.txt
#
# > remove dados.csv
# Arquivo removido.
#
# > exit
# Encerrando.
#
# Regras:
#
# - Armazene os arquivos em uma lista.
# - Não permita arquivo duplicado.
# - Não permita remover arquivo inexistente.
# - O comando list mostra todos os arquivos.
# - O comando clear limpa a lista.
# - O comando exit encerra o programa.
# - Qualquer comando fora do padrão deve ser rejeitado.


# =====================================================================
# Exercício 006: Detector de duplicidade e conflito em cadastros.
# Crie um sistema de cadastro simples.
# Variação mais difícil: detectar CPFs com todos os dígitos iguais, como 11111111111.
# =====================================================================
#
# Estrutura obrigatória:
#
# emails = []
# cpfs = []
#
# Menu:
#
# 1 - Cadastrar pessoa
# 2 - Verificar e-mails duplicados
# 3 - Verificar CPFs duplicados
# 4 - Listar cadastros
# 0 - Sair
#
# Regras:
#
# - O CPF deve ter 11 dígitos após remover pontos e traço.
# - O e-mail deve conter @ e ponto após o @.
# - Não bloqueie duplicados no cadastro.
# - As opções 2 e 3 devem detectar duplicidades depois.
# - Mostre quais e-mails ou CPFs aparecem repetidos.
# - Faça a detecção sem usar dicionários.


# =====================================================================
# Exercício 007: Interpretador de expressões matemáticas simples.
# Crie um programa que recebe expressões no formato: numero operador numero.
# Este é muito bom para sair de exercício acadêmico comum.
# =====================================================================
#
# Estrutura obrigatória:
#
# Exemplos:
# 10 + 5
# 20 - 3
# 4 * 8
# 9 / 3
# 10 // 3
# 10 % 3
# 2 ** 5
#
# Menu:
#
# 1 - Calcular expressão
# 2 - Ver histórico
# 3 - Limpar histórico
# 0 - Sair
#
# Regras:
#
# - Use split() para separar a expressão.
# - Valide se existem exatamente 3 partes.
# - Valide se os números são válidos.
# - Não permita divisão por zero.
# - Salve no histórico uma tupla: (expressao, resultado).
# - Não use eval().


# =====================================================================
# Exercício 008: Gerenciador de tarefas com estados.
# Crie um sistema de tarefas usando lista de tuplas: (titulo, status).
# Status possíveis:
#   "PENDENTE"
#   "EM_ANDAMENTO"
#   "CONCLUIDA"
# Esse exercício conversa bem com sistemas reais.
# =====================================================================
#
# Menu:
#
# 1 - Criar tarefa
# 2 - Alterar status
# 3 - Listar todas
# 4 - Listar por status
# 5 - Remover tarefa
# 6 - Mostrar resumo
# 0 - Sair
#
# Regras:
#
# - Não permitir título vazio.
# - Não permitir tarefa duplicada.
# - Para alterar status, buscar pelo título.
# - Como tupla é imutável, você precisará substituir a tupla inteira na lista.
# - O resumo deve mostrar quantidade de tarefas por status.


# =====================================================================
# Exercício 009: Simulador de processamento em lote.
# Crie um sistema que simula o processamento de arquivos pendentes.
# Esse exercício é diretamente alinhado com Engenharia de Dados.
# =====================================================================
#
# Estrutura obrigatória:
#
# arquivos = [
#     "clientes.csv",
#     "vendas.csv",
#     "produtos.txt",
#     "logs.csv",
#     "backup.zip",
#     "eventos.csv"
# ]
#
# Relatório esperado:
#
# Arquivos processados:
# - clientes.csv
# - vendas.csv
# - logs.csv
# - eventos.csv
#
# Arquivos rejeitados:
# - produtos.txt
# - backup.zip
#
# Total processados: 4
# Total rejeitados: 2
#
# Regras:
#
# - Só arquivos .csv devem ser processados.
# - Arquivos com outra extensão devem ser rejeitados.
# - Cada arquivo processado deve ir para uma lista de processados.
# - Cada arquivo rejeitado deve ir para uma lista de rejeitados.
# - O processamento deve ocorrer um arquivo por vez, usando while.
# - Ao final, mostre relatório.
# - O relatório deve mostrar os arquivos processados.
# - O relatório deve mostrar os arquivos rejeitados.
# - O relatório deve mostrar o total de processados.
# - O relatório deve mostrar o total de rejeitados.


# =====================================================================
# Exercício 010: Mini validador de dataset tabular.
# Crie um programa que analisa uma tabela e gera um relatório de qualidade.
# =====================================================================
#
# Estrutura obrigatória:
#
# dados = [
#     ["id", "nome", "idade", "cidade"],
#     ["1", "Ana", "23", "Curitiba"],
#     ["2", "Bruno", "", "São Paulo"],
#     ["3", "", "31", "Rio de Janeiro"],
#     ["4", "Carlos", "abc", "Belo Horizonte"],
#     ["5", "Daniela", "29", ""]
# ]
#
# Formato dos erros:
#
# (numero_linha, nome_coluna, descricao_erro)
#
# Exemplo:
#
# (2, "idade", "campo vazio")
# (3, "nome", "campo vazio")
# (4, "idade", "valor não numérico")
#
# Regras:
#
# - A primeira linha é o cabeçalho.
# - As demais linhas são registros.
# - Verifique campos vazios.
# - Verifique se idade é numérica.
# - Conte quantas linhas válidas existem.
# - Conte quantas linhas inválidas existem.
# - Guarde os erros em uma lista de tuplas.
# - O formato dos erros deve ser: (numero_linha, nome_coluna, descricao_erro).

# =====================================================================
# Exercício 011: Você recebeu um arquivo CSV exportado de um sistema legado.
# Os dados estão sujos: espaços sobrando, campos em maiúsculo, separador inconsistente.
# Escreva uma função que:
# recebe uma lista de linhas brutas e retorna uma lista de dicionários limpos.

#saída esperada:
# [
#   {"id": "1", "nome": "Ana Silva",    "salario": 4500.0},
#   {"id": "2", "nome": "Carlos Souza", "salario": 3200.0},
#   {"id": "3", "nome": "Maria Lima",   "salario": 5100.5}
# ]
# =====================================================================
csv = [
    "ID ; NOME ; SALÁRIO ",
    "1;  Ana Silva ;4500.0",
    "2; CARLOS SOUZA;  3200",
    "3; maria lima ;5100.50"
]

# =====================================================================
# Exercício 012: Você está construindo um mecanismo de busca simples.
# Dado um conjunto de documentos, construa um índice invertido:
# para cada palavra, quais documentos a contêm.

# Saída esperada:
    # {
    #   "python": ["doc1", "doc3"],
    #   "é":      ["doc1", "doc2"],
    #   "rápido": ["doc1"],
    #   ...
    # }
# =====================================================================

docs = {
    "doc1": "python é rápido e simples",
    "doc2": "java é verboso mas robusto",
    "doc3": "python tem muitas bibliotecas"
}

# =====================================================================
# Exercício 013: Antes de inserir registros num banco, 
# você precisa validar se cada campo tem o tipo correto
# e se os campos obrigatórios estão presentes. 
# Escreva uma função que recebe um registro 
# e um esquema e retorna uma lista de erros encontrados.
    # saída esperada:
    # [
    # "Campo 'idade': esperado int, recebido str",
    # "Campo 'ativo': ausente"
    # ]
# =====================================================================

esquema = {
    "nome": str,
    "idade": int,
    "salario": float,
    "ativo": bool
}
registro = {"nome": "Ana", "idade": "vinte", "salario": 3000.0}