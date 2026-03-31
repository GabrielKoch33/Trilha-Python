lista = []
nova = []
tam = int(input('Digite o Tamanho da lista: '))

#nova = list(set(lista)) <-- converte a lista em set (s/ duplicadas) e depois para lista denovo

for i in range(tam):
    lista.append(int(input(f'digite o {i+1}º valor: ')))

def nova_lista(listar, novo): #adiciona na lista 2 os valores únicos
    max = len(listar)
    for i in range(max):
        for j in range(max):
            if listar[i] != listar[j] and i != j:#i != j evita comparar posições iguais
                if listar[j] not in novo:
                    novo.append(listar[j])

    for k in range(len(novo)): #bubble sort
        for l in range(len(novo)-1):
            if novo[l] > novo[l+1]:
                aux = novo[l]
                novo[l] = novo[l+1]
                novo[l+1] = aux
    return novo


nova_lista(lista,nova)
print(nova)
#[3,2,2,3,1,4] = 2,1,4,3