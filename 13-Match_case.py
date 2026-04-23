# ====================================
# Match/Case pode ser usado quando, a partir de um padrão de input esperado, retornamos um valor.
# Diferente do IF, ele não faz necessário uma condição True ou False
# ====================================

def verificar_status_http(status):
    match status:
        case 200:
            return "Requisicao bem-sucedida."
        case 404:
            return "Pagina nao encontrada."
        case 500:
            return "Erro interno do servidor."
        case _:
            return "Status desconhecido."


def saudacao_por_periodo(periodo):
    match periodo.lower():
        case "manha":
            return "Bom dia!"
        case "tarde":
            return "Boa tarde!"
        case "noite":
            return "Boa noite!"
        case _:
            return "Periodo invalido."


if __name__ == "__main__":
    print("Exemplos com match/case:\n")

    for codigo in [200, 404, 500, 302]:
        print(f"HTTP {codigo}: {verificar_status_http(codigo)}")

    print()

    for periodo in ["manha", "tarde", "noite", "madrugada"]:
        print(f"{periodo.title()}: {saudacao_por_periodo(periodo)}")
