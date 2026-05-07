# ==========================================================================================================================================
# 📋 Você trabalha num sistema de cadastro de usuários. Antes de salvar, o sistema precisa validar se os dados estão corretos.
# ==========================================================================================================================================

nome = "Ana S7474ilva"
email = "ana@email.com"
idade = 16
senha = "afg"


if type(nome) != str or nome.isnumeric() == True or nome.isalnum() == True:
    erroNome = 1
else:   
    erroNome = 0                             #   0      1    2    3
    # gabriel koch da silva
    for p in nome.strip().split():
        if len(p) == 1 or p.isalpha() == False or '|@\#$%/&*()' in p: 
            erroNome += 1 
            # REPLACE APENAS FUNCIONA EM STRING, NESSE CASO EU TORNEI NOVO NOME UMA LISTA COM STRINGS (1º e 2º nome)

email = email.strip()
if '@' not in email or '.com' not in email: # @ e .com existem?
    email_valido = False
else:
    if email[0] in '1234567890': #primeira posição é numero?
         email_valido = False
    else:
        for j in range(len(email)):
            if email[j].isalpha() and email[j] == email[j].upper():
                email_valido = False
                break
            else:
                email_valido = True

if idade < 18:
    idade_valida = False
else:
    idade_valida = True

if len(senha) < 6:
    senha_valida = False
else: 
    senha_valida = True
                    
     
acesso = 0 # >= 1 acesso negado
if erroNome == 0:
    print('Nome Válido')
else:
    print('Nome Inválido (NOME INVÁLIDO AOS PADRÕES DO SITE)')
    acesso += 1
if email_valido == True:
    print('Email Válido')
else:
    print('Email Inválido (EMAIL INEXISTÊNTE)')
    acesso += 1
if idade_valida == True:
    print('Idade Válida')
else:
    print('Idade Inválida (MENOR DE IDADE)')
    acesso += 1
if senha_valida == True:
    print('Senha Válida')
else:
    print('Senha Inválida (SENHA FRACA)')
    acesso += 1
if acesso >= 1:
    print('Cadastro REJEITADO')

