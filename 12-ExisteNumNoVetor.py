lista1 = [5,8,2,9,1]
achou = 0
posicao = 0

numero = int(input('digite um numero, vamos ver se ele está na lista!: '))

for i in range(len(lista1)):
    if numero == lista1[i]:
        posicao = i
        print(f'O valor está na posição {posicao}')

if numero not in lista1:
    achou -= 1
    print(achou)

# Peça um número ao usuário e:
# retorne a posição dele
# ou '-1' se não existir