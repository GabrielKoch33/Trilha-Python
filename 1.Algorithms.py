# ==============================================================================================================
# Inserction Sort:
# - Forma de ordenar arrays
# - A comparação ocorre entre j e i-=n (posição atual e seus antecessores a fim de encontrar a posição adequada)
# - Pequenos conjuntos de dados, como exige muitas comparações pode ser muito custoso
# ==============================================================================================================
array = [5, 2, 4, 6, 1, 3]

for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = key

print(array)
# ==============================================================================================================
# Bubble Sort:
# - Forma de ordenar arrays
# - A comparação ocorre entre j e j+1 (posição atual e sua sucessora)
# - Pequenos conjuntos de dados, como exige muitas comparações pode ser muito custoso
# ==============================================================================================================

bubble_sort = [4,1,7,99,8,11,6,87,2,34,23,76]

for k in range(len(bubble_sort)):
    numTRocas = 0
    for l in range(len(bubble_sort)- k - 1): 
        if bubble_sort[l] > bubble_sort[l+1]:
            bubble_sort[l], bubble_sort[l+1] = bubble_sort[l+1], bubble_sort[l]
            numTRocas += 1
    if numTRocas == 0:
            break
    
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

array = [6, 12, 17, 23, 38, 45, 77, 84, 90]

num = int(input('Digite o número para achar: '))

first = 0
last = len(array) - 1
# achou = False

while first <= last: # or achou = False

    mid = (first + last) // 2

    if array[mid] == num:
        print(f'O número {num} estava na posição {mid}')
        # achou = True
        break

    elif num > array[mid]:
        first = mid + 1

    else: # num < array[mid]
        last = mid - 1

else: # é possivel usar Else em for e while loops, o else acontecerá quando o loop for encerrado naturalmente 
    print(f'O número {num} não foi encontrado')


'''
O else executa quando o laço termina normalmente.
O else não executa se o laço for interrompido por um break.
'''

#1) Metade do vetor OG
#2) Metade//2

