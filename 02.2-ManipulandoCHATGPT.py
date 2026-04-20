# Faça uma função que receba uma frase e retorne quantas vogais existem nela.
#2)
def vogais(frasevogais):
    contadorvogal = 0
    for i in range(len(frasevogais)):
        if frasevogais[i] in 'aeiou':
            contadorvogal += 1

    return contadorvogal

frasevogais = input('escreva frase: ')
resultado = vogais(frasevogais)

#3) Palindromos
def palindromo(frase, frase_invertida):
    if frase == frase_invertida:
        return True
    
frase = input('Digite uma frase e veremos se é palindromo')
frase_invertida = frase[::-1]
palindromo(frase,frase_invertida)


#4)
# Faça uma função que receba uma frase e substitua todas as ocorrências de uma palavra por outra, sem usar replace().
def substituicao(frasevelha,oldpalavra, newpalavra):
    s = frasevelha.split() #s recebe a frase dividida em indices aaa[1] bbb[2]...

    for i in range(len(s)): #percorre todos os indices buscando atender condições
        if s[i] == oldpalavra:
            s[i] = newpalavra
                            # Para o python uma lista ['a','b'] as ASPAS e VIRGULAS são meramente para LEITURA DO USUÁRIO
    frasenova = " ".join(s) # Logo, usar o " ".join(lista) apenas ligará os elementos com um ESPAÇO
    return frasenova

frasevelha = input('frase: ') # fiofó[1] do[2] cachorro[3]
oldpalavra = input('qual palavra da frase vai ser mudada?: ')
newpalavra = input('qual vai ser a nova palavra?: ')
resultado1 = substituicao(frasevelha,oldpalavra, newpalavra)
print(resultado1)

# Crie uma função que receba um e-mail e retorne:
# usuário antes do @
# domínio depois do @
#5)
def ler_email(e):
    achou = -1
    for i in range(len(e)):# len() e range() só é utilzado em strings; range em strings e numeros (10) == 0 a 9
        if e[i] == '@':
            achou = i
            break
    if achou == -1:
        print('Email inválido')
    else:
        print(f'Usuário: {e[:achou]}')
        print(f'Domínio: {e[achou+1:]}')

e = (input('Qual é seu email?: '))
ler_email(e)

#6)Faça uma função que receba uma frase e retorne a palavra com maior quantidade de letras.
def qtd(frase):
    dividida = frase.split()
    maior = dividida[0]

    for i in range(len(dividida)):
        if len(dividida[i]) > len(maior):
            maior = dividida[i]

    return maior

frase = input('Digite uma frase: ')
resultado = qtd(frase)
print(resultado)

#8)Faça uma função que receba uma frase e inverta apenas a ordem das palavras.
# Entrada:
# python é poderoso
# Saída:
# poderoso é python

def inverso(frase):
    d = frase.split()

    i = 0
    while i < len(d) // 2:
        aux = d[i]
        d[i] = d[len(d)-1-i]
        d[len(d)-1-i] = aux
        i += 1

    return " ".join(d)

frase = input('Digite a frase: ')
resultado = inverso(frase)
print(resultado)

#9)
# Crie uma função que receba uma string e converta para formato título manualmente.
# Entrada:
# joao da silva
# Saída:
# Joao Da Silva
                   
def cap_nome(nome):
    newname = nome.split()
    resultadol = []

    for i in newname:# new name = ana[1] maria[2] braga[3]
        novapalavra = i[0].upper() + i[1:].lower()
        # novapalavra = i[0].upper() = i percorre o nome + sobrenomes, [0] a primeira letra de cada virando maiuscula
        # + i[1:].lower() = Na palavra atual, da posição 1 em diante, mantenha minúcula
        resultadol.append(novapalavra)

    return " ".join(resultado) #Junta os elementos da lista com um espaço em branco

nome = input('Digite seu nome: ')
print(cap_nome(nome))

#11)
# Crie uma função que valide se uma senha atende:
# mínimo 8 caracteres
# pelo menos 1 número
# pelo menos 1 letra maiúscula
# pelo menos 1 caractere especial
import string
def novasenha(senha):
    senha_modificada = input('Altere sua senha: ')
    return senha_modificada


def validaSenha (senha):
    if len(senha) >= 8:    
        if senha.isalnum() == True:
            if string.ascii_uppercase in senha:
                if ['@','#', '$',' %', '&', '©', '®', '€', '°'] in senha:
                        print('Senha Forte! Bem vindo ao site :D ')
                        return 
                else:
                    print('A senha não pode conter Caracteres Especiais')
                    senha = novasenha(senha) 
                    validaSenha(senha)
                    return
            else:
                print('A senha deve conter letras Maiúsculas')
                senha = novasenha(senha) 
                validaSenha(senha)
                return
        else:
            print('A senha deve conter Números e Letras')
            senha = novasenha(senha) 
            validaSenha(senha)
            return
    else:
       print('A senha deve conter no Mínimo 8 Caracteres')
       senha = novasenha(senha) 
       validaSenha(senha)
       return

senha = input('Digite sua senha: ')
validaSenha(senha)

# 11)Faça uma função que receba CPF no formato texto e retorne apenas números.

# Entrada:
# 123.456.789-10

# Saída:
# 12345678910

def formata(cpf):
    novocpf = ''
    for caractere in cpf:
        if caractere.isdigit():
            novocpf += caractere
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12): ')
cpfnumerico = formata(cpf)
print(cpfnumerico)

#or

def formatacao(cpf):
    novocpf = cpf.replace('.', '').replace('-', '')
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12)')
formatacao(cpf) 
cpfnumerico = formatacao(cpf)