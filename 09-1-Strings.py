# Peça ao usuário para digitar uma frase e exiba quantos caracteres ela tem, contando espaços
# frase = input("Digite uma frase: ")
# # exiba o total de caracteres

frase = input("Digite uma frase: ")
print(len(frase))

nome = input("Seu nome: ")
print(nome.lower())
print(nome.upper())
# exiba em maiúsculo e em minúsculo

frase = "   Python é incrível!   "
# exiba len() antes e depois do strip()
print(len(frase))
new = frase.strip()
print(len(new))

frase = input("Digite uma frase: ")
# 1. lista de palavras
# 2. quantidade de palavras
# 3. palavras unidas por '-'
lista = frase.split() #split separa as palavras em indices unicos
for i in lista: #range só se usa em numeros, em listas não
    print(i)

print(len(lista))
frasejoin = '-'.join(lista)
print(frasejoin)

#-----medio 
#7)
def limpar(texto):
    texto = texto.lower().strip()
    texto.replace(' ','')
    return

print(limpar("  Olá Mundo  "))  # 'olámundo'

#8)
#Dada a string 'Maria:25:São Paulo', separe os dados usando ':' como separador e exiba nome, idade e cidade em linhas separadas.
def formulada (dados):
    print(f'Nome: {dados[0]}')
    print(f'Idade: {dados[1]}')
    print(f'Cidade: {dados[2]}')
    
dados = "Maria:25:São Paulo"
formulada(dados.split)
# separe e exiba cada campo

#9)frase = input("Digite uma frase: ")
# 1. sem espaços
# 2. comprimento sem espaços
# 3. maiúsculo sem espaços
frase = input("Digite uma frase: ")
semEspacos = frase.replace(' ','')
print(semEspacos)
print(len(semEspacos))
print(semEspacos.lower()) 

# Faça uma função que receba uma frase e retorne quantas vogais existem nela.
def vogais(frasevogais):
    for i in range(len(frasevogais)):
        if frasevogais[i] == 'aeiou':
            contadorvogal += 1

    return contadorvogal
frasevogais = input('escreva frase: ')
resultado = vogais(frasevogais)

# na 3 eu gostaria de usar uma função nativa, existe?

# Faça uma função que receba uma frase e substitua todas as ocorrências de uma palavra por outra, sem usar replace().
def substituicao(frasevelha,oldpalavra, newpalavra):
    s = frasevelha.split() #s recebe a frase dividida em indices aaa[1] bbb[2]...
    for i in s: #percorre todos os indices buscando atender condições
        if i == oldpalavra:
            i = newpalavra
                            # Para o python uma lista ['a','b'] as ASPAS e VIRGULAS são meramente para LEITURA DO USUÁRIO
    frasenova = " ".join(s) # Logo, usar o " ".join(lista) apenas ligará os elementos com um ESPAÇO
    return frasenova

frasevelha = input(print('frase: ')) # fiofó[1] do[2] cachorro[3]
oldpalavra = input(print('qual palavra da frase vai ser mudada?: '))
newpalavra = input(print('qual vai ser a nova palavra?: '))
resultado1 = substituicao(frasevelha,oldpalavra, newpalavra)
print(resultado1)

# Crie uma função que receba um e-mail e retorne:
# usuário antes do @
# domínio depois do @

def ler_email(e):
    for i in range(len(e)):# len() e range() len() só é utilzado em strings e range em strings e numeros (10) == 0 a 9
        if e[i] == '@':
            achou = i
    print(f'Usuário: {e[:achou-1]}')    
    print(f'Domínio: {e[achou:]}')

e = print(input('Qual é seu email?: '))
ler_email(e)
