def cheia (ponteiro):
    if ponteiro > 5:
        return True #Por padrão retorna true
    return False# Senão, falso

def incluir(fila,ponteiro):
    if cheia(ponteiro):
        return f'Fila Cheia, {ponteiro} Posições preenchidas'
        #O return serve para devolver um valor de dentro da função para quem a chamou, e também encerra a execução da função naquele ponto.
    else:
        fila[ponteiro] = input(f'informe um número')
        return fila,ponteiro + 1

def remover (fila,ponteiro):
    if ponteiro == 1:
        return 'Fila Vazia, nada a remover'
    else:
        for i in range(ponteiro - 2):
            fila[i] = fila[i+1]
        return fila, ponteiro - 1

def escrever (fila):
    for i in range(5):
        print(fila[i])

def checarproximo (fila):
     print(f'O Próximo a sair da fila é: {fila[0]}')

ponteiro = 0
opcao = 10
fila = [0,0,0,0,0]

while opcao != 0:
    print('---MENU---')
    print('0 - SAIR')
    print('1 - INCLUIR NUM')
    print('2 - REMOVER NUM')
    print('3 - ESCREVER FILA')
    print('4 - CONSULTAR 1o')
    print('5 - VAZIA OU CHEIA')

    op = int(input('Digite uma opção: '))
    if op == 0:
        break
    if op == 1:
        fila, ponteiro = incluir(fila,ponteiro)
    elif op == 2:
       fila, ponteiro =  remover (fila,ponteiro)
    elif op == 3:
        escrever(fila)
    elif op == 4:
        checarproximo(fila)
    elif op == 5:
        cheia(ponteiro)
        if ponteiro == 5:
            print('Fila Cheia')
        elif ponteiro == 1:
            print('Fila Vazia')
        else:
            print('Fila Com Espaços Livres')

#Remover não funciona
#Quebra se adicionar na fila cheia
