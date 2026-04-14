#STRINGS EM PYTHON SÃO IMUTAVEIS;
#NENHUM METODO ALTERA DIRETAMENTE;
#ELES SEMPRE RETORNAM ALGO EM UMA NOVA VARIAVEL


frase = 'Curso em Vídeo Python'
len(frase) # = 21 caracteres

print(frase[9]) # = 'V'
print(frase[9:13]) # [9:N-1] 'Víde'
print(frase[9:21:2]) #'VdoPto' 
'''Você pode omitir o indice inicial 
ou final [:12] = escreve do começo até o 11.
[15:] = escreve da posição inicial até o fim
da string'''

frase.count('o',0,13)
'''Conta quantas vezes aparece a letra "o" 
da posição 0 a 12'''

frase.find('deo')
''' = 11; vai retornar a posição onde se
inicia a frase "deo"; caso não encontre ele 
retorna -1 '''

print('Curso' in frase)
# true | false

exemplo = 'Adoro mexer em Javascript'
print(exemplo)
exemplo.replace('Javascript','Python')
print(exemplo)

nova_frase = '   Aprenda Python  '
print(nova_frase.strip())# remove espaços indesejados
''' .rstrip() e lstrip() = right e left strip '''

teste1 = 'Curso em Vídeo Python'
teste_separado = teste1.split()
# [Curso] [em] [Vídeo] [Python]
# [01234] [01] [01234] [012345]
#    0      1     2       3
print(teste_separado)

teste1 = '-'.join(teste1)
print(teste1)

china = 'chines safado maluco   '
print(len(china)) #frase c/ os espaços no meio e fim
print(len(china.strip()))# frase s/ espaço no fim
print(len(china.replace(' ',''))) #frase sem espaços no meio
# se for para remover TODOS os espaços, o replace 
# faz o papel do strip
# replace já reajusta a frase automaticamente
# [i] = [i+1]

print(china.find('nes')) # = 3

new_china = china.split()
print(new_china[2][4])
#        2 = maluco 4 = 'c' 

num = int(input('escreva um numero de 1 a 9999 '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print(f'unidade = {u}\n dezena = {d}\n centena = {c}\n milhar = {m}')
