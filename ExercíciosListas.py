# =====================================================================
# Dada uma lista de números: Retorne quantos são maiores que a média
# =====================================================================
lista = []
tam = int(input('Digite o Tamanho da lista: '))
for i in range(tam):
    lista.append(int(input(f'digite o {i}º valor: ')))

sum = 0
for i in range(len(lista)):
    sum += lista[i]
media = sum / tam

print(f'A soma de todos os valores são {sum} e a média {media}')
cont = 0

for i in range(tam):
    if lista[i] > media:
        print(f'Valor acima da média: {lista[i]}')
        cont += 1
print(f'Existem {cont} Valores acima da média')

# =====================================================================
# Leia 10 números em uma lista e mostre: Vetor original & Vetor invertido (Sem Métodos)
# =====================================================================

num = []
for i in range(4):# = 0,1,2,3 = 4 espaços
    valor = int(input('Digite 4 Números: '))
    num.append(valor)

num_inv =[0,0,0,0]
c= 0
for i in range(3,-1,-1): # num = [{0}{1}{2}{3]}; -1 porque se fosse 0 ele iria apenas até o 1 (inicio,fim-1)
    num_inv[c] = num[i]
    c += 1

print(num)
print(num_inv)

# =====================================================================
# Dada a lista: lista2 = [1,2,3,4,5]: Peça um valor e remova todas as ocorrências dele manualmente (sem usar remove())
# =====================================================================

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

# =====================================================================
# Peça um número ao usuário e: Retorne a posição dele ou '-1' se não existir
# =====================================================================

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

# =====================================================================
# PLeia uma lista de números inteiros informada pelo usuário. 
# Em seguida, crie uma segunda lista contendo apenas os valores únicos da lista original, sem repetição.
# Ao final, ordene essa nova lista em ordem crescente e exiba o resultado.
# =====================================================================

lista = []
nova = []
tam = int(input('Digite o tamanho da lista: '))

for i in range(tam):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

def nova_lista(listar, novo):
    for i in range(len(listar)):
        if listar[i] not in novo:
            novo.append(listar[i])

    for k in range(len(novo)):  # bubble sort
        for l in range(len(novo) - 1):
            if novo[l] > novo[l + 1]:
                aux = novo[l]
                novo[l] = novo[l + 1]
                novo[l + 1] = aux

    return novo

nova_lista(lista, nova)
print(nova)
