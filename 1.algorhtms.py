# ==============================================================================================================
# Bubble Sort:
# - Forna de ordenar arrays
# - A comparação ocorre entre j e j+1 (posição atual e sua sucessora)
# - Pequenos conjuntos de dados, como exige muitas comparações pod ser muito custoso
# ==============================================================================================================
bubble_sort = [4,1,7,99,8,11,6,87,2,34,23,76]

for k in range(len(bubble_sort)):
    for l in range(len(bubble_sort)- k - 1): 
        if bubble_sort[l] > bubble_sort[l+1]:
            bubble_sort[l], bubble_sort[l+1] = bubble_sort[l+1], bubble_sort[l]
print(f'Com Bubble Sort{bubble_sort}')

# 1) len()-i -1 # impede que façamos a comparação com os valores  já ordenados no fim da lista

# ==============================================================================================================
# Selection Sort:
# - Mais rápido que um bubble sort, pois faz menos trocas devido a divisão que ele faz no selection_sortor
# - A cada incrementação de 'i', o 'j' deixar de percorrer os i's anteriores, pois eles já foram ordenados
# ==============================================================================================================

selection_sort = [7,3,5,0,2,1,11,4,2,8,9,23]
busca_binaria = []

for i in range(len(selection_sort)):
    posi_menor = i # 1) 
    for j in range(i+1,len(selection_sort)): #2)
        if selection_sort[j] < selection_sort[posi_menor]: 
            posi_menor = j #3)
    selection_sort[i], selection_sort[posi_menor] = selection_sort[posi_menor], selection_sort[i] 

print(f'Com Selection Sort{selection_sort}')
busca_binaria = selection_sort[:]       


# 1) Definimos que a posição do menor elemento é sempre a atual
# 2) i+1 impede que comparemos elementos já ordenados do selection_sortor     
# 3) Caso encontremos um menor, definimos a posição desse novo elemento como o menor
# 4) Ao fim da busca pela posição/valor do menor elemento, atribuimos na posição atual de 'i' o valor da posição do menor elemento de encontrado em 'j' 

# ==============================================================================================================
# Merge Sort:
# - Mais rápido que outros Sorts pois dessa forma ordenamos em pequenas partes que no final se juntam
# - Marge e Binary seguem principios semelhantes 
# - "Dividir para conquistar"
# ==============================================================================================================  




# ==============================================================================================================
# Binary Search:
# - Mais rápido que uma busca linear, na qual percorremos um vetor , posição por posição, até encontrar um elemento
# - A diferença entre Binary e Linear Search é que a busca binária é exclusiva para vetores já ORDENADOS
# - "Dividir para conquistar"
# - A busca ocorre com base na grandeza do seu valor em relação ao valor central
# ==============================================================================================================  

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 23] # LEN = 12

middle = (len(array))//2 #1)
num = int(input('Qual valor deseja encontrar?'))

if array[middle] == num:
    print(f'O seu valor: {array[middle]} está no meio, na posição {middle}')
elif num > array[middle]:
    while middle != 1:
        for i in range(array[middle+1],array[-1]):
            middle = len(array[middle+1],array[-1])//2 #2)
            pass

elif num < array[middle]:
    while middle != 1:
        for i in range(array[0],array[middle]):
            pass

#1) Metade do vetor OG
#2) Metade//2

