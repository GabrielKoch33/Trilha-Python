# Quando não se usa from, deve se escrever no código math.sqrt (biblioteca.função)
# Quando se usa o from, pode se declara apenas a função escolhida


#============================================================================= 
# MACETES FUNÇÕES:
#=============================================================================

print ('-'*30) = '----------------------------'
#Você pode manipular quantas vezes algo vai ser escrito multiplicando a string

def contador (*num): # * é o sinal de desempacotar
	print(num) 
contador(2,3,8,9,4)
contador(6,8,9)
contador(1,2,0,4)
# É possível passar uma quantidade variada de parametros para uma função, usar o *variavel vai transformar variavel em uma TUPLA
# Podendo receber quantos valores quiser.
# isso ocorre pois numeros separados por vírgulas são interpretados como tuplas pelo python: 1,2,3 == (1,2,3)


# flush == True
# ao invés do python guardar os valores na memória para depois exibir, ele exibirá os valores imediatamente, limpando o buffer. 
# usar file.flush() permite gravar os dados da memoria no disco sem necessidade de fechar o arquivo

#=================================================================================
# Generator expression:
# formas compactas de gerar valores, realizam 'lazy evaluation', recebendo valores
# um por um ao invés de acessar a lista inteira em memória
# list comprehensio usa [], generator usa ()
#--usado com:
sum()
any()
#any verifica se pelo menos um elemento do iteravel é true, retorna false se todos forem falsos ou se o iteravel estiver vazio
# Em Python, 0, None, "" (string vazia) e [] (lista vazia) são considerados False.
all()
max()
min()
#=================================================================================

#com LC:
# cada item(r$xx) na lista de vendas é adicionada a outra lista (valores) que é criada na memória
valores = [item for item in 'vendas']
total = sum(valores) #ao final disso sum() percorre toda a lista e faz += dos valores

#com GE:
total = sum(item[1] for item in 'vendas')
#sum recebe os valores presentes em item[1] do valor atual em vendas, sem a necessidade de percorrer a lista inteira catando os valores,
#ao fim, total recebe o valor de sum()
#=============================================================================

import math
math.sqrt(16)         # 4.0
var = math.pi         # 3.14159...
math.ceil(3.2)        # 4
math.floor(3.9)       # 3
math.factorial(5)     # 120
math.log(100, 10)     # 2.0

import random
random.random()              # float entre 0.0 e 1.0
random.randint(1, 10)        # inteiro entre 1 e 10
random.choice(["a","b","c"]) # elemento aleatório
random.shuffle([1,2,3,4])    # embaralha in-place
random.sample(range(100),5)  # 5 únicos aleatórios

import statistics as st
dados = [2, 4, 4, 4, 5, 5, 7, 9]
st.mean(dados)      # 5.0 — média
st.median(dados)    # 4.5 — mediana
st.mode(dados)      # 4   — moda
st.stdev(dados)     # 2.0 — desvio padrão

len("Python")      # 6
len([1, 2, 3])     # 3
len({"a":1,"b":2}) # 2

list(range(5))        # [0,1,2,3,4]
list(range(2,8))      # [2,3,4,5,6,7] #2 = inicio 8 = fim, considere fim-1
list(range(0, 10, 2)) # [0,2,4,6,8] #2 pulando a cada 2

tuple([1,2,3])  # (1, 2, 3) #converte para tuple, o comando list também pode ser utilizado para conversão, assim como set()

set_ex = [1,2,2,3,3]  
set(set_ex)
#‘output’ = {1,2,3} (sem repetições)

abs(-5)    # 5
abs(-3.14) # 3.14
# Retorna valor absoluto (valor da distância até o 0(sempre um número positivo, independente se a entrada por + ou -))

round(3.7)      # 4
round(3.14159, 2) # 3.14; 2 = casas decimais
# Arredonda números

max(3, 1, 9, 2)     # 9
max([5, 8, 2])     # 8
max("banana")      # 'n'
# Maior valor

list(map(int, ["1","2","3"])) # [1,2,3]
list(map(str.upper, ["a","b"])) # ['A','B']
# map Aplica uma função a todos os elementos

sorted([3,1,4,1,5])         # [1,1,3,4,5]
sorted("python")           # ['h','n','o','p','t','y']
sorted([3,1,5,4], reverse=True) # [5,4,3,1]
# Retorna uma nova lista ordenada (em ordem crescente)

list(reversed([1,2,3]))  # [3,2,1]
list(reversed("abc"))    # ['c','b','a']
# Mesma função do reverse=True na funcão acima

name = input("Digite seu nome: ").lower()
# name já armazena em minúsculo/maiúsculo
# lower = gabrielkoch

texto = "Python"
novo = texto.upper()
# texto ainda é 'Python'
# novo é PYTHON

print("Python".upper())
# print = PYTHON

words = ["Python", "is", "awesome"]
sentence = " ".join(words) 
print(sentence)  # Output: 'Python is awesome'

string = "apple,banana,cherry".split(",") = ['apple', 'banana', 'cherry']
customstring = "one--two--three".split("--")= ['one', 'two', 'three']
