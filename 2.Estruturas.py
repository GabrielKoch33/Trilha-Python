# ======================================================================
# LISTAS
# ======================================================================

# Indexáveis
# Ordenadas
# Permite diferentes tipos
# Mutáveis

numeros = [10, 20, 30]
nomes = ["Ana", "Carlos", "João"]
misturado = [1, "A", True, [12,"3"]]

# ==========
# MÉTODOS:
# ==========

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
# SETS
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
# TUPLA
# ======================================================================

# Ordenadas
# Indexáveis
# Aceitam repetição
# Imutáveis
# Úteis para dados fixos

numeros = (10, 20, 30)
nomes = ("Ana", "Carlos", "João")
misturado = (1, "A", True, (1,3))

# ==========
# MÉTODOS: IGUAIS OS DA LISTA
# ==========

# Assim como a lista, pode ser acessada a ultima posição com [-1]
# [2:5] acessa tupla na posição 2 (incluida) até a 5-1

#Permite desempacotamento desde que o numero de variaveis corresponda ao numero de indices da tupla
tuplinha = (1,2,3,4,5)

a,b,c,d,e = tuplinha 
(x,y,*z) = tuplinha # O * Torna o variavel em lista, permitindo que os valores faltantes sejam atribuidos e ninguem fique de fora


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
# DICT
# ======================================================================

# Chave única
# Valor pode repetir
# Mutável
# Muito rápido para busca por chave

# USADO EM:
# JSON
# APIs
# cadastro
# configurações
# contadores
# registros


# "key":value
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