# =====================================================================
# Exemplo While True para Loops Infinitos
# =====================================================================

while True: #Enquanto True for verdadeiro faça: (True sempre será verdadeiro, logo executa o código até ler um BREAK)
    
    resposta = input("Digite sair para encerrar: ")

    if resposta == "sair": #Se essa condição for atendida 
        break   # Então o programa é encerrado

    print("Você digitou:", resposta) # Se não for atendida, printa essa mensagem e volta ao início

    
print("Programa encerrado.") # Caso o IF for atendido, o programa sai do Loop While e exibe essa mensagem

# While funciona de forma que: enquanto a condição for verdadeira o laço se repete
# While True cria um loop infinito porque True é sempre verdade
# While False cria um loop que nunca vai ser executado, pois, False nunca será verdadeiro, logo o bloco do while false é ignorado


# =====================================================================
# Exercício 001: Crie um programa que leia vários números inteiros usando while.
# O programa deve parar apenas quando o usuário digitar 0. No final, mostre quantos
# números foram digitados, a soma total e a média entre eles, desconsiderando o 0.
# =====================================================================
contador = 0
media = 0
soma = 0
while True:
    num = int(input('DIGITE UM NUM, SE FOR 0 VC SAI: '))
    if num == 0:
        break
    else:
        contador += 1   
        soma += num
print(f'A quatidade de números inseridos: {contador}\nA soma total: {soma}\n A média {soma/contador}')

# =====================================================================
# Exercício 003: Crie um programa que leia nomes de produtos e seus preços usando
# while True. O cadastro deve parar quando o usuário responder "N" para continuar. No
# final, mostre o total gasto e quantos produtos custaram mais de R$1000.00.
# =====================================================================



# =====================================================================
# Exercício 010: Faça um programa que leia uma frase e conte, usando while, quantas
# vogais existem nela. Ignore diferenças entre letras maiúsculas e minúsculas.
# =====================================================================




# =====================================================================
# Exercício 014: Faça um programa que leia vários nomes e pesos, guardando os dados em
# uma lista composta. O cadastro deve continuar enquanto o usuário quiser. No final,
# mostre quantas pessoas foram cadastradas, a pessoa mais pesada e a pessoa mais leve.
# =====================================================================


# =====================================================================
# Exercício 015: Crie um programa que controle uma lista de tarefas. O usuário pode
# adicionar tarefa, marcar tarefa como concluída, listar tarefas pendentes, listar
# tarefas concluídas ou sair. Use while para manter o menu funcionando.
# =====================================================================

# =====================================================================
# Exercício 016: Validador de senha com tentativas limitadas
# Crie um programa que peça uma senha até ela ser considerada válida ou até
# o usuário errar 5 vezes.
#
# Critérios da senha:
# - mínimo 8 caracteres
# - pelo menos 1 número
# - pelo menos 1 letra maiúscula
# - pelo menos 1 caractere especial entre @, #, $, %, &, !
#
# Ao final, informe se o cadastro foi aceito ou bloqueado por excesso de
# tentativas.
#
# Obrigatório:
# [ ] usar while
# [ ] contar tentativas
# [ ] não aceitar senha inválida
# [ ] mostrar o motivo da invalidação
# =====================================================================

# =====================================================================
# Exercício 017: Caixa eletrônico com saque controlado
# O usuário começa com saldo de R$ 1000. O programa deve exibir um menu
# enquanto ele não escolher sair:
#
# 1 - Ver saldo
# 2 - Sacar
# 3 - Depositar
# 0 - Sair
#
# Regras:
# - não permitir saque maior que o saldo
# - não permitir valores negativos ou zero
# - contar quantas operações foram feitas
# - mostrar saldo final ao sair
#
# Obrigatório:
# [ ] while para o menu
# [ ] if/elif/else
# [ ] acumulador de operações
# [ ] validação de valor
# =====================================================================

# =====================================================================
# Exercício 018: Leitura de números até sentinela
# Peça números inteiros ao usuário até ele digitar -1.
#
# Ao final, mostre:
# - quantidade de números digitados, sem contar o -1
# - soma
# - média
# - maior número
# - menor número
# - quantidade de pares
# - quantidade de ímpares
#
# Regras:
# - se o primeiro número for -1, informe que nenhum número foi informado
# - não use max(), min() nem sum()
# =====================================================================

# =====================================================================
# Exercício 019: Jogo de adivinhação com dificuldade
# Crie um jogo em que o programa sorteia um número secreto.
#
# O usuário escolhe a dificuldade:
# 1 - Fácil: 10 tentativas, número de 1 a 50
# 2 - Médio: 7 tentativas, número de 1 a 100
# 3 - Difícil: 5 tentativas, número de 1 a 200
#
# A cada tentativa, informe se o chute foi maior ou menor que o número secreto.
#
# Obrigatório:
# [ ] usar random.randint()
# [ ] controlar tentativas com while
# [ ] validar chute fora do intervalo
# [ ] encerrar ao acertar ou ao acabar tentativas
# =====================================================================

# =====================================================================
# Exercício 020: Menu de lista de compras
# Crie um menu que manipula uma lista de compras:
#
# 1 - Adicionar item
# 2 - Remover item
# 3 - Listar itens
# 4 - Buscar item
# 5 - Limpar lista
# 0 - Sair
#
# Regras:
# - não adicionar item vazio
# - não adicionar item duplicado
# - ao remover, verificar se existe
# - ao listar, mostrar posição e nome do item
#
# Obrigatório:
# [ ] while para o menu
# [ ] lista
# [ ] in / not in
# [ ] validações
# =====================================================================

# =====================================================================
# Exercício 021: Sistema de notas com quantidade indefinida
# Peça o nome de alunos e suas notas até o usuário digitar fim no nome.
#
# Para cada aluno, peça 3 notas.
#
# Ao final, exiba:
# - nome do aluno
# - média
# - situação: aprovado, recuperação ou reprovado
#
# Critério:
# média >= 7       aprovado
# média >= 5       recuperação
# média < 5        reprovado
#
# Obrigatório:
# [ ] while para entrada indefinida
# [ ] lista de tuplas ou listas internas
# [ ] função para calcular média
# [ ] função para classificar situação
# =====================================================================

# =====================================================================
# Exercício 022: Simulador de login
# Você tem usuários válidos em duas listas paralelas:
#
# usuarios = ["ana", "joao", "maria"]
# senhas = ["1234", "abcd", "senha10"]
#
# Peça usuário e senha até o login ser válido ou até atingir 3 tentativas.
#
# Regras:
# - se usuário não existir, informar usuário inválido
# - se usuário existir mas senha estiver errada, informar senha inválida
# - se acertar, mostrar mensagem de boas-vindas
#
# Obrigatório:
# [ ] while com limite de tentativas
# [ ] busca manual na lista
# [ ] não usar dict
# =====================================================================

# =====================================================================
# Exercício 023: Compactador simples de caracteres
# Peça uma string e gere uma versão compactada contando caracteres repetidos
# consecutivos.
#
# Exemplo:
# Entrada: aaabbcaaaa
# Saída: a3b2c1a4
#
# Regras:
# - use while para percorrer a string
# - não use bibliotecas
# - cuidado com o último grupo de caracteres
#
# Esse é mais difícil. Ele treina índice, controle de repetição e estado anterior.
# =====================================================================

# =====================================================================
# Exercício 024: Verificador de CPF simplificado
# Peça um CPF no formato livre, podendo ter pontos e traço:
#
# 123.456.789-00
#
# Extraia apenas os números e valide:
# - deve ter exatamente 11 dígitos
# - não pode conter todos os números iguais, como 11111111111
#
# Não precisa implementar o cálculo oficial dos dígitos verificadores.
#
# Obrigatório:
# [ ] usar while para percorrer caracteres
# [ ] montar nova string só com dígitos
# [ ] validar tamanho
# [ ] validar repetição
# =====================================================================

# =====================================================================
# Exercício 025: Controle de estoque sem dicionário
# Use duas listas paralelas:
#
# produtos = []
# quantidades = []
#
# Crie um menu:
# 1 - Cadastrar produto
# 2 - Entrada de estoque
# 3 - Saída de estoque
# 4 - Consultar produto
# 5 - Listar estoque
# 0 - Sair
#
# Regras:
# - não cadastrar produto duplicado
# - não permitir saída maior que o estoque
# - não permitir quantidade negativa
# - consultar produto pelo nome
#
# Obrigatório:
# [ ] while para menu
# [ ] listas paralelas
# [ ] busca por índice
# [ ] validação
#
# Esse exercício é importante porque depois vamos refazê-lo com dicionário.
# Aí você vai sentir por que dict é melhor.
# =====================================================================

# =====================================================================
# Exercício 026: Sequência de Fibonacci até limite
# Peça um número limite e gere a sequência de Fibonacci até que o próximo
# valor ultrapasse o limite.
#
# Exemplo:
# Limite: 30
# Saída: 0, 1, 1, 2, 3, 5, 8, 13, 21
#
# Obrigatório:
# [ ] usar while
# [ ] não usar lista pronta
# [ ] controlar os dois valores anteriores
# [ ] validar limite maior ou igual a 0
# =====================================================================

# =====================================================================
# Exercício 027: Analisador de frase interativo
# Crie um menu que recebe uma frase inicial e permite:
#
# 1 - Contar vogais
# 2 - Contar consoantes
# 3 - Contar palavras
# 4 - Mostrar frase invertida
# 5 - Trocar frase
# 0 - Sair
#
# Regras:
# - ignorar espaços na contagem de letras
# - tratar maiúsculas e minúsculas
# - se a frase estiver vazia, pedir nova frase
#
# Obrigatório:
# [ ] while para menu
# [ ] funções simples
# [ ] strings
# [ ] slicing ou loop manual para inverter
# =====================================================================

# =====================================================================
# Exercício 028: Remoção manual de todos os valores repetidos
# Peça uma lista de números ao usuário. Primeiro pergunte quantos números
# serão digitados.
#
# Depois peça um valor a remover.
#
# Remova todas as ocorrências desse valor sem usar remove().
#
# Exemplo:
# Lista: [2, 3, 2, 5, 2]
# Remover: 2
# Resultado: [3, 5]
#
# Obrigatório:
# [ ] usar while
# [ ] cuidado ao remover enquanto percorre
# [ ] pode usar pop()
# [ ] não pode usar remove()
#
# Dica conceitual: quando remove elementos enquanto percorre, o índice precisa
# ser controlado com cuidado.
# =====================================================================

# =====================================================================
# Exercício 029: Sistema de votação
# Crie um sistema de votação com candidatos fixos:
#
# 1 - Ana
# 2 - Bruno
# 3 - Carlos
# 4 - Voto nulo
# 0 - Encerrar votação
#
# Ao final, mostre:
# - total de votos
# - votos de cada candidato
# - votos nulos
# - percentual de cada candidato
# - vencedor
#
# Regras:
# - voto inválido não conta
# - se houver empate no maior número de votos, informar empate
# - se ninguém votar, informar votação vazia
#
# Obrigatório:
# [ ] while até digitar 0
# [ ] contadores
# [ ] cálculo percentual
# [ ] lógica de empate
# =====================================================================

# =====================================================================
# Exercício 030: Mini sistema bancário com histórico
# Crie um sistema bancário com menu:
#
# 1 - Depositar
# 2 - Sacar
# 3 - Ver saldo
# 4 - Ver extrato
# 0 - Sair
#
# Regras:
# - saldo inicial 0
# - depósito precisa ser positivo
# - saque precisa ser positivo
# - saque não pode ultrapassar saldo
# - cada operação válida deve ser salva no extrato
#
# O extrato deve ser uma lista de tuplas, por exemplo:
# [
#     ("depósito", 100.0),
#     ("saque", 40.0)
# ]
#
# Ao escolher "Ver extrato", mostre:
# DEPÓSITO: R$100.00
# SAQUE: R$40.00
# Saldo atual: R$60.00
#
# Obrigatório:
# [ ] while para menu
# [ ] lista de tuplas
# [ ] validação de valores
# [ ] controle de saldo
# [ ] relatório final
# =====================================================================
