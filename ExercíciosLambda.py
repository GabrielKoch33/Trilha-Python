"""
=====================================================
EXERCÍCIOS - LIST COMPREHENSION E GENERATOR EXPRESSIONS
=====================================================

Regras:
- Não utilize respostas prontas.
- Prefira List Comprehension sempre que o exercício pedir.
- Nos exercícios sobre Generator Expression, evite converter para lista,
  exceto quando solicitado.
"""
lista = [1,25,4,30,5,68,7,87,9,11,22,23,45]

#List Comprehension usa: [ expressão for valor in lista ]
dobro = [x*2 for x in lista]
pares = [x for x in lista if x % 2 == 0] # filtra quais vão entrar
pares_impares = ["par" if x % 2 == 0 else "ímpar" for x in lista] #  classifica os valores de acordo com filtro
pares2impares3 = [ x*2 if x % 2 == 0 else x*3 for x in lista if x >= 30]
    # para cada elemento da lista, se x for maior ou igual a 30, veja se ele é par, se sim, dobre-o, senão, triplique-o

#Generator Expression usa: ( expressão for valor in lista) 
dobro = (x * 2 for x in lista)
maiores10 = (x for x in lista if x > 10)
pares_impares = ("Par" if x % 2 == 0 else "Ímpar" for x in lista)
    # semelhante a LC, porém, os resultados não vão direto para a memória, eles ficam armazenados em geradores que trabalham
    # com Lazy Evaluation, ou seja, só trazem os valores quando solicitados com next()

#Lambda usa: var = lambda arg : expressão
pares_impares = lambda x: "Par" if x % 2 == 0 else "Ímpar" 
grades = lambda x: ("A" if x >= 90 else "B" if x >= 70 else "C")

filtermaiores10 = filter(lambda x: x > 10, lista) #nesse caso filter (e map etc) armazem em um objeto gerador, semelhante a GENERATOR EXP.
print(pares_impares(10))
print(grades(10))

while True:
    continuar = input('continuar S/N: ')
    if continuar == 'S':
        print(next(filtermaiores10))
    else: 
        break

# =====================================================
# NÍVEL 1 - ENTENDENDO A SINTAXE
# =====================================================

# Exercício 1
# Dada a lista abaixo, gere outra lista contendo o dobro
# de todos os números.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobro = [n*2 for n in numeros]
       # ^       ^-- para cada valor na lista de numeros     
       # |-- retorne o valor * 2
print(dobro)
# Resultado esperado:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# -----------------------------------------------------

# Exercício 2
# Gere uma lista contendo apenas os números pares.
somente_pares = []
# Resultado esperado:
# [2, 4, 6, 8, 10]


# -----------------------------------------------------

# Exercício 3
# Gere uma lista contendo o quadrado apenas dos números
# ímpares.

# Resultado esperado:
# [1, 9, 25, 49, 81]


# -----------------------------------------------------

# Exercício 4
# Transforme todos os nomes para letras maiúsculas.

nomes = ["Ana", "Carlos", "Maria", "Pedro"]

# Resultado esperado:
# ["ANA", "CARLOS", "MARIA", "PEDRO"]


# =====================================================
# NÍVEL 2 - CONDIÇÕES
# =====================================================

# Exercício 5
# Transforme a lista abaixo em:
#
# ["positivo", "negativo", "positivo",
#  "negativo", "zero", "positivo"]

numeros = [4, -2, 8, -7, 0, 3]


# -----------------------------------------------------

# Exercício 6
# Retorne apenas as palavras com mais de quatro letras.

palavras = ["python", "java", "c", "javascript", "go"]


# -----------------------------------------------------

# Exercício 7
# Transforme todas as palavras em letras minúsculas.

linguagens = ["Python", "JAVA", "Sql", "Docker"]

# Resultado esperado:
# ["python", "java", "sql", "docker"]


# =====================================================
# NÍVEL 3 - DICIONÁRIOS
# =====================================================

produtos = {
    "mouse": 150,
    "teclado": 250,
    "monitor": 1200,
    "webcam": 400
}

# Exercício 8
# Gere uma lista contendo apenas os nomes dos produtos
# cujo preço seja maior que R$300.


# -----------------------------------------------------

# Exercício 9
# Gere uma lista contendo apenas os preços.

# Resultado esperado:
# [150, 250, 1200, 400]


# -----------------------------------------------------

# Exercício 10
# Gere uma lista contendo strings no formato:
#
# "mouse - R$150"
# "teclado - R$250"
# ...


# =====================================================
# NÍVEL 4 - COMPREENSÕES ANINHADAS
# =====================================================

# Exercício 11
# Gere todos os pares possíveis entre letras e números.

letras = ["A", "B", "C"]
numeros = [1, 2, 3]

# Resultado esperado:
#
# ('A',1)
# ('A',2)
# ('A',3)
# ('B',1)
# ...


# -----------------------------------------------------

# Exercício 12
# Crie uma matriz 5x5 preenchida com zeros.


# -----------------------------------------------------

# Exercício 13
# Crie uma matriz 4x4 onde cada posição seja:
#
# linha + coluna
#
# Resultado esperado:
#
# [
# [0,1,2,3],
# [1,2,3,4],
# [2,3,4,5],
# [3,4,5,6]
# ]


# =====================================================
# NÍVEL 5 - GENERATOR EXPRESSIONS
# =====================================================

# Exercício 14
# Crie um generator que produza os quadrados dos números
# de 1 até 100.
#
# Não transforme em lista.


# -----------------------------------------------------

# Exercício 15
# Consuma o generator anterior utilizando um for.


# -----------------------------------------------------

# Exercício 16
# Utilize um generator para calcular a soma dos quadrados
# de 1 até 100.
#
# Dica:
# sum(...)


# -----------------------------------------------------

# Exercício 17
# Crie um generator contendo apenas os números pares
# de 1 até 1000.
#
# Imprima apenas os 10 primeiros usando next().


# =====================================================
# NÍVEL 6 - COMPARAÇÕES
# =====================================================

# Exercício 18
# Faça duas implementações:
#
# 1) List Comprehension
# 2) Generator Expression
#
# Para gerar os quadrados dos números de 1 até 1.000.000.
#
# Depois compare:
#
# - type()
# - sys.getsizeof()
# - tempo de criação (opcional)


# -----------------------------------------------------

# Exercício 19
# Leia um arquivo texto.
#
# Crie um generator que produza apenas as linhas que
# contenham a palavra "erro".
#
# Não carregue todo o arquivo em memória.


# -----------------------------------------------------

# Exercício 20
# Considere:

clientes = [
    {"nome": "Ana", "idade": 20},
    {"nome": "Carlos", "idade": 15},
    {"nome": "Maria", "idade": 42},
    {"nome": "João", "idade": 18},
]

# Faça:
#
# a) Uma List Comprehension contendo apenas os nomes
#    dos maiores de idade.
#
# b) Um Generator Expression produzindo exatamente
#    o mesmo resultado.


# =====================================================
# DESAFIO FINAL
# =====================================================

transacoes = [
    {"tipo": "entrada", "valor": 1000},
    {"tipo": "saida", "valor": 300},
    {"tipo": "entrada", "valor": 500},
    {"tipo": "saida", "valor": 100},
    {"tipo": "entrada", "valor": 700},
]

"""
Sem utilizar laços for tradicionais (exceto para exibir resultados quando necessário):

1. Gere uma lista contendo apenas as entradas.

2. Gere uma lista contendo apenas as saídas.

3. Gere uma lista apenas com os valores das entradas.

4. Calcule o total de entradas utilizando um generator.

5. Calcule o total de saídas utilizando um generator.

6. Calcule o saldo final.

7. Gere uma lista de strings no formato:

ENTRADA: R$1000
SAÍDA: R$300
...

8. Bônus:
Ordene as transações por valor antes de gerar a lista
de strings utilizando sorted(key=lambda ...).
"""
