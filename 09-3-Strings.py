# 2) Contar vogais
def vogais(frasevogais):
    contadorvogal = 0
    for i in range(len(frasevogais)):
        if frasevogais[i].lower() in 'aeiou':
            contadorvogal += 1
    return contadorvogal

frasevogais = input('Escreva frase: ')
resultado = vogais(frasevogais)
print(resultado)


# 3) Palíndromo
def palindromo(frase):
    frase = frase.lower().replace(' ', '')
    frase_invertida = frase[::-1]
    return frase == frase_invertida

frase = input('Digite uma frase e veremos se é palíndromo: ')
print(palindromo(frase))


# 4) Substituição sem replace
def substituicao(frasevelha, oldpalavra, newpalavra):
    s = frasevelha.split()

    for i in range(len(s)):
        if s[i] == oldpalavra:
            s[i] = newpalavra

    frasenova = " ".join(s)
    return frasenova

frasevelha = input('Frase: ')
oldpalavra = input('Qual palavra da frase vai ser mudada?: ')
newpalavra = input('Qual vai ser a nova palavra?: ')
resultado1 = substituicao(frasevelha, oldpalavra, newpalavra)
print(resultado1)


# 5) Ler email
def ler_email(e):
    achou = -1
    for i in range(len(e)):
        if e[i] == '@':
            achou = i
            break

    if achou == -1:
        print('Email inválido')
    else:
        print(f'Usuário: {e[:achou]}')
        print(f'Domínio: {e[achou+1:]}')

e = input('Qual é seu email?: ')
ler_email(e)


# 6) Maior palavra
def qtd(frase):
    dividida = frase.split()

    if len(dividida) == 0:
        return ''

    maior = dividida[0]

    for i in range(len(dividida)):
        if len(dividida[i]) > len(maior):
            maior = dividida[i]

    return maior

frase = input('Digite uma frase: ')
resultado = qtd(frase)
print(resultado)


# 8) Inverter ordem das palavras
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


# 9) Formato título manual
def cap_nome(nome):
    newname = nome.split()
    resultadol = []

    for i in newname:
        novapalavra = i[0].upper() + i[1:].lower()
        resultadol.append(novapalavra)

    return " ".join(resultadol)

nome = input('Digite seu nome: ')
print(cap_nome(nome))


# 11) Validar senha
def validaSenha(senha):
    tem_numero = False
    tem_maiuscula = False
    tem_especial = False
    especiais = '@#$%&©®€°!*-_'

    if len(senha) < 8:
        print('A senha deve conter no mínimo 8 caracteres')
        return

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True
        if caractere in especiais:
            tem_especial = True

    if not tem_numero:
        print('A senha deve conter pelo menos 1 número')
    elif not tem_maiuscula:
        print('A senha deve conter pelo menos 1 letra maiúscula')
    elif not tem_especial:
        print('A senha deve conter pelo menos 1 caractere especial')
    else:
        print('Senha forte')

senha = input('Digite sua senha: ')
validaSenha(senha)


# CPF só números
def formata(cpf):
    novocpf = ''
    for caractere in cpf:
        if caractere.isdigit():
            novocpf += caractere
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12): ')
cpfnumerico = formata(cpf)
print(cpfnumerico)


# Ou com replace
def formatacao(cpf):
    novocpf = cpf.replace('.', '').replace('-', '')
    return novocpf

cpf = input('Digite seu CPF (modelo: 123.123.123-12): ')
cpfnumerico = formatacao(cpf)
print(cpfnumerico)
