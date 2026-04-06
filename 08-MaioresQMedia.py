# Dada uma lista de números:
# Retorne quantos são maiores que a média
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
        print(lista[i])
        cont += 1