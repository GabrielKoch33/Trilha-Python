# =====================================================================
# 📋 Você recebe uma lista de registros de log de um servidor. 
# Cada linha tem o formato 'TIPO - log'. 
# Crie uma função que conta quantos logs são de cada tipo e lista as mensagens de erro.
# =====================================================================

logs = [
  "INFO - Servidor iniciado",
  "INFO - Usuário conectado",
  "ERRO - Falha na conexão",
  "INFO - Arquivo salvo",
  "ERRO - Timeout na requisição",
  "AVISO - Memória acima de 80%"
]
def separar_logs(logs): 
    logs_separados = []
    for log in logs: 
        partes = log.split(' - ')
        tipo = partes[0] 
        msg = partes[1]
        logs_separados.append((tipo,msg)) # Quando demos append((tipo,msg)) Estamos adicionando a lista uma tupla de ('tipo','mensagem')
    return logs_separados
 
def contar_logs(logs_separados):
    contagem = {
        "INFO": 0,
        "AVISO":0,
        "ERRO":0
    }
    for tipo, msg in logs_separados:
        if tipo == 'INFO':
            contagem["INFO"] += 1
        elif tipo == 'AVISO':
            contagem["AVISO"] += 1
        else:  
            contagem["ERRO"] += 1

    return contagem

def extrair_erros(logs_separados):
    textos_erros = []
    for tipo,msg in logs_separados:
        if tipo == 'ERRO':
            textos_erros.append(msg)
    return textos_erros

def analisar_logs(logs):
    logs_separados = separar_logs(logs)
    contagem = contar_logs(logs_separados)
    erros = extrair_erros(logs_separados)
    return {
        "contagem":contagem,
        "erros": erros
    }

logs_separados = separar_logs(logs) 
for item in logs_separados:
    print(item)
print()

log_analisados = analisar_logs(logs)
print(log_analisados)
print()



