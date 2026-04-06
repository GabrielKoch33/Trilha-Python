
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

# Dada a lista: lista2 = [1,2,3,4,5]
# Peça um valor e remova todas as ocorrências dele manualmente
# (sem usar remove())