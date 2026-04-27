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


# =====================================================================
# Exercício 002: Faça um programa que peça uma senha ao usuário. Enquanto a senha
# digitada for diferente de "python123", o programa deve mostrar uma mensagem de erro
# e pedir novamente. Quando acertar, mostre uma mensagem de acesso permitido.
# =====================================================================


# =====================================================================
# Exercício 003: Crie um programa que leia nomes de produtos e seus preços usando
# while True. O cadastro deve parar quando o usuário responder "N" para continuar. No
# final, mostre o total gasto e quantos produtos custaram mais de R$1000.00.
# =====================================================================


# =====================================================================
# Exercício 004: Faça um programa que leia vários números inteiros e guarde-os em uma
# lista. A leitura deve parar quando o usuário digitar 999. No final, mostre a lista,
# o maior valor, o menor valor e a posição de cada um deles.
# =====================================================================


# =====================================================================
# Exercício 005: Crie um menu com as opções somar, subtrair, multiplicar, dividir e
# sair. O programa deve ler dois números e repetir o menu usando while até que o usuário
# escolha sair. Valide a divisão por zero.
# =====================================================================


# =====================================================================
# Exercício 006: Faça um programa que simule um caixa simples. O usuário começa com um
# saldo inicial informado pelo teclado e pode escolher entre depositar, sacar, consultar
# saldo ou sair. Use while para manter o menu ativo e impeça saques maiores que o saldo.
# =====================================================================


# =====================================================================
# Exercício 007: Crie um jogo em que o computador pense em um número de 1 a 50 e o
# usuário tente adivinhar. A cada tentativa, informe se o palpite foi maior ou menor que
# o número sorteado. No final, mostre quantas tentativas foram necessárias.
# =====================================================================


# =====================================================================
# Exercício 008: Faça um programa que leia a idade de várias pessoas usando while.
# O programa deve parar quando a idade digitada for negativa. No final, mostre quantas
# pessoas são maiores de idade, quantas são menores e a média das idades válidas.
# =====================================================================


# =====================================================================
# Exercício 009: Crie um programa que leia vários valores e separe-os em duas listas:
# uma com números pares e outra com números ímpares. A leitura deve continuar enquanto
# o usuário quiser. No final, mostre as duas listas em ordem crescente.
# =====================================================================


# =====================================================================
# Exercício 010: Faça um programa que leia uma frase e conte, usando while, quantas
# vogais existem nela. Ignore diferenças entre letras maiúsculas e minúsculas.
# =====================================================================


# =====================================================================
# Exercício 011: Crie um programa que leia notas de vários alunos. Para cada aluno,
# leia o nome e duas notas, calcule a média e guarde tudo em uma lista composta. O
# cadastro deve continuar enquanto o usuário quiser. No final, mostre nome e média.
# =====================================================================


# =====================================================================
# Exercício 012: Faça um programa que leia uma sequência de números e só aceite valores
# entre 1 e 10. Caso o usuário digite um valor fora desse intervalo, peça novamente.
# O programa deve parar quando forem cadastrados 5 valores válidos.
# =====================================================================


# =====================================================================
# Exercício 013: Crie um programa que simule uma votação. Enquanto o usuário não
# digitar 0, ele deve votar em um candidato usando os números 1, 2 ou 3. No final,
# mostre a quantidade de votos de cada candidato, votos inválidos e o vencedor.
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
