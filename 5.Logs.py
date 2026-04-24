# =====================================================================
# 📋 Você recebe uma lista de registros de log de um servidor. 
# Cada linha tem o formato 'TIPO - mensagem'. 
# Crie uma função que conta quantos logs são de cada tipo e lista as mensagens de erro.
# =====================================================================

def typelogs(logs):
    cInfo = 0
    cErro = 0
    cAviso = 0
    logs_tratados = []
    erros = []

    for i in range(len(logs)):
        logs_tratados.append(logs[i].split(' - '))# logs_tratados = [['INFO','xxxxxx']['AVISO','yyyyyyyy'][...]]
    
    for j in range(len(logs_tratados)):
        tipo = logs_tratados[j][0]      # 'INFO', 'ERRO' ou 'AVISO'
        mensagem = logs_tratados[j][1]  # texto depois do ' - '

        if tipo == 'INFO':
            cInfo += 1
        elif tipo == 'AVISO':
            cAviso += 1
        else:
            cErro += 1
            erros.append(mensagem)

    print(f'INFO: {cInfo}')
    print(f'AVISO: {cAviso}')
    print(f'ERRO: {cErro}')
    print('\nMensagens de erro:')
    for erro in erros:
        print(f'- {erro}')

logs = [
  "INFO - Servidor iniciado",
  "INFO - Usuário conectado",
  "ERRO - Falha na conexão",
  "INFO - Arquivo salvo",
  "ERRO - Timeout na requisição",
  "AVISO - Memória acima de 80%"
]

typelogs(logs)

# =====================================================================
# Refatoração com foco em:
# - Evitar print() dentro da função principal
# - Uso de dicionários com foco em escalar o código
# - Usar: for item in lista:  print(item)
# - def analisar_logs(logs: list[str]) -> dict: (Escrever funções que retornem valores ao invés de prints internos)
# =====================================================================

