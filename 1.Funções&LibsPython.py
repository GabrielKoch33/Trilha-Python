# Quando não se usa from, deve se escrever no código math.sqrt (biblioteca.função)
# Quando se usa o from, pode se declara apenas a função escolhida

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