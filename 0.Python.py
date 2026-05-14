# ======================================================================
# LISTAS
# ======================================================================
'''
# Use lista quando:
 - Você tem uma coleção ordenada de itens,
 - Geralmente do mesmo tipo, que:
 - Pode crescer, diminuir ou mudar.
 - Permite vários tipo;
 - mantém ordem;
 - permite repetição;
 - permite alteração, mutável;
 - acessa por índice;
'''

numeros = [10, 20, 30]
nomes = ["Ana", "Carlos", "João"]
misturado = [1, "A", True, [12,"3"]]

# ------------------------------- metodos de lista ------------------------------------

nomes.append('Gabriel')  # Adiciona "Gabriel" ao fim da lista
nomes.insert(1,"Luiz")   # Adiciona "Luiz" na posição [1], os elementos a direita são movidos [i+1] 
nomes.remove(20)         # Remove a primeira ocorrência de um valor 20
nomes.pop()              # Remove o último valor da lista, ou pelo indice. Caso não exista o valor, gera erro.  
nomes.pop(2)             # Remove o INDICE 2, não o valor 2
nomes.sort()             # Organiza a lista em ordem crescente
nomes.sort(reverse=True) # Organiza a lista em ordem decrescente
nomes.reverse()          # Inverte a ordem atual da lista. [3,2,6] -> [6,2,3]
nomes.count("Ana")       # Conta quantas vezes o nome Ana aparece na lista
nomes.index("Carlos")    # Retorna o indice do valor fornecido

# ======================================================================
# TUPLA
# ======================================================================
'''
Use tupla quando:
- Você tem um grupo fixo de valores que pertencem juntos e cuja posição tem significado
- mantém ordem
- permite repetição
- é imutável
- boa para registros pequenos e fixos
- Indexáveis
- Úteis para dados fixos
'''
numeros = (10, 20, 30)
nomes = ("Ana", "Carlos", "João")
misturado = (1, "A", True, (1,3))

# ------------------------------- desempacotamento ------------------------------------

# o numero de variaveis deve ser igual ao numero de indices da tupla
tuplinha = (1,2,3,4,5)

a,b,c,d,e = tuplinha 
(x,y,*z) = tuplinha # O * torna a variavel em lista
'''
x = a
y = b
z = [c,d,e]
'''

# A unica forma de incluir e remover valores de uma tupla é convertendo ela em uma lista e depois para tupla novamente
# ou adicionar com concatenação
thistuple = ("apple", "banana", "cherry")
k = list(thistuple)
k.append("orange")
thistuple = tuple(k)

# Tuplas podem ser Concatenadas
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# ======================================================================
# SETS
# ======================================================================
'''
Use set quando você quer valores únicos e não se importa com a ordem.
- não permite repetição
- busca muito rápida
- ótimo para remover duplicados
- verificar existência rapidamente
- encontrar interseção/diferença
- Não possuem índice
- Não garantem ordem
- Não aceitam duplicados
- Ótimos para operações de conjunto
- Tipos mistos
'''
# ------------------------------- metodos de sets ------------------------------------

s = {1, 2, 3}
s.add(7) # Adiciona um valor
s.update([1,2,3]) # Adiciona VÁRIOS valores
s.remove(10) # Caso não exista, dá erro
s.discard(10) # Caso não exista, não dá erro
s.clear() # Esvazia o set

a = {1,3,5,2,6}
b = {3,2,5,6,8,10}

a.union(b) # A + B, sem repetição
a.intersection(b) # A = B, existe em ambos
a.difference(b) # A - B, exclusivo de A
a.symmetric_difference(b) # (A - B) + (B - A), exclusivo de cada um

# ======================================================================
# DICT
# ======================================================================
'''
- chave única
- valor pode ser qualquer coisa
- busca rápida por chave
- ideal para cadastros, contadores, agrupamentos e registros
- key:value
'''

d = {
    "nome": "Gabriel",
    "idade": 25,
    "cidade": "SC"
}
# Acesso:
print(d["nome"]) # = Gabriel

# ------------------------------- metodos de dict ------------------------------------

d.get("nome") # Pegar valor
d["idade"] = 30 # Atribuir/Substituir
d.keys()   # lista chaves
d.values() # lista valores
d.items()  # lista chaves + valore
d.pop("idade") # Remove valor
d.update({"cidade": "RJ"}) # Adicionar/criar key:value
d["sexo"] = "Masculino" # Pode-se criar e adicionar diretamente, sem função

# =================================================================================
# LIST COMPREHENSION
# =================================================================================
'''
- É uma forma compacta de criar listas a partir de um loop
- Quando usar: quando se deseja criar uma lista a partir de outra
- Quando não usar: quando um for exige muitos if, acumuladores e outras variaveis
'''

# Forma comum:
numeros = [1, 2, 3, 4, 5]

quadrados = []

for n in numeros:
    quadrados.append(n ** 2)

print(quadrados)

# Com list comprehension:
numeros = [1, 2, 3, 4, 5]

#nova_lista recebe [expressão sobre cada elemento de outra lista]
quadrados = [n ** 2 for n in numeros]

print(quadrados)
# Basicamente: 
# Crie uma lista 'quadrados',
# Onde cada elemento dela vai ser o resultado de percorrer outra lista potencializando seus valores **2

# Pode se usar com IF:
numeros = [1, 2, 3, 4, 5, 6]

# lista 'pares' recebe o valor atual da lista 'numeros' caso o valor seja par
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# resultado recebe os valores atuais de numeros, vezes 2, caso o valor atual seja menor 10 e for par
resultado = [x * 2 for x in numeros if x < 10 if x % 2 == 0]


# ==========================================================================================================================
# SET COMPREHENSION
# ==========================================================================================================================

# Normal:
nomes = ["Ana", "Bruno", "Ana", "Carlos", "Bruno"]

nomes_unicos = set() #nomes_unicos vai aceitar apenas valores distintos

for nome in nomes:
    nomes_unicos.add(nome)

print(nomes_unicos)

# com comprehension:
nomes = ["Ana", "Bruno", "Ana", "Carlos", "Bruno"]

nomes_unicos = {nome for nome in nomes}
# o set nomes_unicos, vai receber o nome de uma lista de nomes, caso ja exista, o set ignorará
print(nomes_unicos)

# ---
emails = [
    "ANA@EMAIL.COM",
    "bruno@email.com",
    "ana@email.com"
]

emails_normalizados = {email.lower() for email in emails}

print(emails_normalizados)

# ---

palavras = ["python", "sql", "dados", "ti", "engenharia"]

palavras_grandes = {palavra for palavra in palavras if len(palavra) > 3}

# ==========================================================================================================================
# DICT COMPREHENSION
# ==========================================================================================================================
'''
- É uma forma compacta de criar dicionários a partir de um dicionário com valores percorridos de uma lista de forma compacta
- Quando usar: quando se deseja criar uma lista a partir de outra
- Quando não usar: quando um for exige muitos if, acumuladores e outras variaveis
'''

# Com dict normal:
produtos = ["mouse", "teclado", "monitor"]
estoque = {}

for produto in produtos:
    estoque[produto] = 0

print(estoque)

# Com comprehension: 
produtos = ["mouse", "teclado", "monitor"]

estoque = {produto: 0 for produto in produtos}
# adicione em dicionário 'estoque' como chave o valor que seja o produto atual em 'produtos', e atribua a ela o valor 0 
print(estoque)

precos = {
    "mouse": 80.0,
    "teclado": 150.0,
    "monitor": 900.0
}

precos_com_desconto = {  produto: preco * 0.9 for produto, preco in precos.items()}
# dict precos_com_desc recebe como chave o produto atual do dicionario preocos e como valor, o preco * 0.9
# o .items() é para extrair tanto a chave e como o valor de precos
print(precos_com_desconto)

#=================================================================================
# Generator expression:
#=================================================================================
'''
 formas compactas de gerar valores, realizam 'lazy evaluation', recebendo valores
 um por um ao invés de acessar a lista inteira em memória
 list comprehensio usa [], generator usa ()
 Normalmente usado com:
'''
sum()
any()
all()
max()
min()

total_vendido = sum(item[1] for item in 'vendas') #soma de todos os campos de preços na tabela de vendas
tem_produto_caro = any(preco > 1000 for preco in 'precos') #retorna True caso algum produto, pelo menos um, tenha preco > 1000
todos_positivos = all(numero > 0 for numero in 'numeros') # retorna True se TODOS os numeros da lista forem positivos

# -------------- com list comprehension ----------------

valores = [item for item in 'vendas']
total = sum(valores) #ao final disso sum() percorre toda a lista e faz += dos valores

# -------------- com generator expression ----------------

total = sum(item[1] for item in 'vendas')
#sum recebe os valores presentes em item[1] do valor atual em vendas, sem a necessidade de percorrer a lista inteira catando os valores,
#ao fim, total recebe o valor de sum()

#============================================================================= 
# FUNÇÕES
#=============================================================================

# ----------------------------------------- docstrings -----------------------------------------
'''
primeira string depois do cabeçalho da função é chamada de docstring,
é uma string usada para especificar a funcionalidade da nossa função, e embora seja opcional, 
vos lembro que documentar é uma importante prática de programação, 
uma vez que possivelmente outras pessoas estarão lendo nosso código,
inclusive é importante até mesmo para você lembrar o que você fez!
'''

def contador (num): 
	'''
	isso é uma docstring, devemos usar elas para explicar oque a função faz
	'''
	print(num) 

contador(2)
contador(6)
contador(1)

''' para retornar a docstring: '''
print(contador.__doc__) 
help(contador) 

# ----------------------------------------- *args e *kwargs -----------------------------------------
'''
É possível passar uma quantidade variada de parametros para uma função, usar o *variavel vai transformar variavel em uma TUPLA
Podendo receber quantos valores quiser.
isso ocorre pois numeros separados por vírgulas são interpretados como tuplas pelo python: 1,2,3 == (1,2,3)
'''
# *args é usado para enviar uma variável que não tenha palavras-chave, veja um exemplo:
def soma(*args): # * é o sinal de empacotamento num = () 
    total = 0
    for num in args:
        total += num 
    return total

print(soma(2,3,4,6)) # 15
print(soma(2,3,4,6,5,5,5,1,2)) # 32
print(soma(2,3)) # 5

# **kwargs nos permite passarmos variáveis com palavras-chave como argumento, veja exemplos:

def pessoa(**kwargs): # basicamente um dicionário
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f'{nome} tem atualmente {idade} anos de idade')

pessoa(gabriel='33', rafael='47', daniel='22')
# {'gabriel': '33', 'rafael': '47', 'daniel': '22'}
# gabriel tem atualmente 33 anos de idade
# rafael tem atualmente 47 anos de idade
# daniel tem atualmente 22 anos de idade

#=============================================================================
# MÓDULOS E BIBLIOTECAS
#=============================================================================
'''
 Quando não se usa from, deve se escrever no código math.sqrt (biblioteca.função)
 Quando se usa o from, pode se declara apenas a função escolhida
'''

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
# printa de trás para frente

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