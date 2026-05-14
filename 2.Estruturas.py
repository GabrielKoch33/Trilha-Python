# ======================================================================
# LISTAS
# Use lista quando:

# - Você tem uma coleção ordenada de itens,
# - Geralmente do mesmo tipo, que:
# - Pode crescer, diminuir ou mudar.

# - Permite vários tipo;
# - mantém ordem;
# - permite repetição;
# - permite alteração, mutável;
# - acessa por índice;
# ======================================================================

numeros = [10, 20, 30]
nomes = ["Ana", "Carlos", "João"]
misturado = [1, "A", True, [12,"3"]]

# ======================================================================
# MÉTODOS:
# ======================================================================

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
# Use tupla quando:
# Você tem um grupo fixo de valores que pertencem juntos e cuja posição tem significado:

jogada = ("Alice", 30) 
coordenada = (10, 25)

# - mantém ordem
# - permite repetição
# - é imutável
# - boa para registros pequenos e fixos
# - Indexáveis
# - Úteis para dados fixos
# ======================================================================

numeros = (10, 20, 30)
nomes = ("Ana", "Carlos", "João")
misturado = (1, "A", True, (1,3))

# Permite desempacotamento, assim como listas, desde que 
# o numero de variaveis corresponda ao numero de indices da tupla
tuplinha = (1,2,3,4,5)

a,b,c,d,e = tuplinha 
(x,y,*z) = tuplinha 
x = a
y = b
z = [c,d,e]
# O * torna a variavel em lista, 
# permitindo que os valores faltantes sejam atribuidos e ninguem fique de fora

# A unica forma de incluir e remover valores de uma tupla é convertendo ela em uma lista e depois para tupla novamente
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
# Use set quando você quer valores únicos e não se importa com a ordem.
# - não mantém ordem confiável
# - não permite repetição
# - busca muito rápida
# - ótimo para remover duplicados
# - verificar existência rapidamente
# - comparar conjuntos
# - encontrar interseção/diferença
# ======================================================================

# Não possuem índice
# Não garantem ordem
# Não aceitam duplicados
# Ótimos para operações de conjunto
# Tipos mistos

# Remover duplicados
# Comparar listas
# Descobrir itens em comum

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
# - chave única
# - valor pode ser qualquer coisa
# - busca rápida por chave
# - ideal para cadastros, contadores, agrupamentos e registros
# - key:value
# ======================================================================

# Dentro de cada dicionário a chave deve ser unica

d = {
    "nome": "Gabriel",
    "idade": 25,
    "cidade": "SC"
}

# Acesso:
print(d["nome"]) # = Gabriel

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
# É uma forma compacta de criar listas a partir de um loop
# - Quando usar: quando se deseja criar uma lista a partir de outra
# - Quando não usar: quando um for exige muitos if, acumuladores e outras variaveis
# =================================================================================

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
# É uma forma compacta de criar dicionários a partir de um dicionário com valores percorridos de uma lista de forma compacta
# - Quando usar: quando se deseja criar uma lista a partir de outra
# - Quando não usar: quando um for exige muitos if, acumuladores e outras variaveis
# ==========================================================================================================================

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
