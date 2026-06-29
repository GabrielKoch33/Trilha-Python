import time
lista_de_processos = [('P1',5),('P2',1),('P3',7),('P4',3),('P5',4),('P6',10),('P7',2)]


print(f'Fila atual: {lista_de_processos}')


while lista_de_processos: #True enquanto houver elementos na lista, caso vazia, False
    processo = lista_de_processos[0]

    print(f'Processo: {processo[0]} | Tempo de execução: {processo[1]}s')

    for j in range(1,processo[1]+1): #timer 
        print(j, flush=True)
        time.sleep(1)

    lista_de_processos.pop(0)# remove o primeiro elemento e por consequẽncia ja move os demais para esquerda

print('Todos os processos concluídos!')
print(lista_de_processos)