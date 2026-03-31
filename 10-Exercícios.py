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

'----------------------'

lista2 = [1,2,3,4,5]

escolhido = int(input('Escolha um numero a ser removido: '))
for i in range(len(lista2)):
    if escolhido == lista2[i]:
        for j in range(i,len(lista2)- 1):
            lista2[j] = lista2[j+1]
        lista2.pop()#remove o último valor da lista, evitando que haja valor duplicado
        break

print(f'{escolhido}REMOVIDO!')
print(lista2)

# Peça um valor e remova todas as ocorrências dele manualmente
# (sem usar remove())

# lista3 = [1,2,3,4,5]
# escolha = int(input('Escolha um numero a ser remover: '))
# lista3.remove(escolha)
# print(lista3)

'----------------------'
# encontre o tamanho da maior sequência crescente consecutiva

ordem =[1, 2, 2, 3, 4, 1, 2, 3] #7
# for i in range(1,len(ordem)):