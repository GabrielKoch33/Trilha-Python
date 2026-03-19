frase = 'Curso em Vídeo Python'
#        012345678901234567890   
print(frase[9])
#imprime apenas o nono indice ('V')
print(frase[9:14])
#imprime apenas os caracteres do indice 9 até o 13 (Vídeo)
print(frase[9:21:2])
#imprime a frase (Vídeo Python), porém, ignorando um caractere (ou pulando de dois em dois) (VdoPto)
print(frase[:5])
#Vai do indice 0 até o N-1
print(frase[9:])
#Incia no indice 15 (P) e vai até o final da string
print(frase[9::3])
#Começa no 9, vai até o final ignorando dois caracteres seguidos (pula de tres em tres)(Vphe)
#[inicio:fim:ignora caracteres]
#ANALISE

print('Video' in frase)
#TRUE or FALSE

len(frase) #lengh = conta a quantidade de caracteres

frase.count('o', 0,13) #o programa conta quantas vezes aparece a letra 'o' minuscula na frase = 3
#contando do indice 0 e indo até 13-1

frase.find('deo')
#isso vai retornar a POSIÇÃO 11, pois esse é o indice onde inicia a sequencia 'deo'
#caso retorne -1 significa que o find não achou a POSIÇÃO na string

frese = ('Sou usuário de Iphone')
android = frese.replace('Iphone','Android')
print(android)
#replace é usado para substitui a palavra escolhida (Iphone) pela palavra desejada (Android)

frase.upper() , frase.lower() #MAIUSCULA e minuscula

frase.capitalize #A string inteira fica em minuscula, exceto a primeira letra de toda a string

frase.title #Identifica palavras separadas e as primeiras letras de cada palavra ficam MAIUSCULA

frase.strip #remove espaços inuteis antes da frase e no final da frase '   OI   '

frase.rstrip() #remove apenas os espaços no lado direito
frase.lstrip() #remove apenas os espaços no lado esquerto

#DIVISÃO DE STRING

frase = 'Curso em Vídeo Python'
frase.split() #cada palavra é separa e recebe indice proprio, e cada mini-repartição tbm recebe indice
#'Curso em Video Python'
# 01234 01 01234 012345
#  1     2   3     4 

divido = frase.split()
print(divido[0][3])#O 0 mostra apenas o primeiro conjunto, e o 3 a terceira letra
