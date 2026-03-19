import math

import math
from math import sqrt
from math import ceil, floor, pow

import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é = {math.ceil(raiz)}')

from math import sqrt
n = int(input('digite um numero: '))
ra = sqrt(n)
print(f'A raiz quadrada de {n} é = {ra}')

import random
num = random.randint(1,11)
print('aleatorio',num)

integer = float(input('Digite um numero REAL'))
print(f'A parte inteira de {integer} é ',int(integer))
# ou
import math
inteira = float(input('Digite numero real: '))
inteira = math.trunc(inteira)
print(f'A parte inteira desse número é: {inteira}')

co = float(input('Cateto oposto '))
ca = float(input('Cateto adjacente '))
hip  = (math.pow(co, 2)) + (math.pow(ca, 2))
hipo = math.sqrt(hip)
print(f'A hipotenusa = {hipo}')

ang = float(input('Digite angulo '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'Angulo {ang}, Seno {seno:.2f}, Cosseno {coss:.2f} e Tangente {tang:.2f}')

import random

a1 = input('Nome do primeiro aluno:')
a2 = input('Nome do segundo aluno:')
a3 = input('Nome do terceiro aluno:')

# sorteio = random.randint(1,3)
#sorteia um numero aletório de 1 a 3  (inteiros)

print(sorteio)
if sorteio == 1:
    print(f'O aluno escolhido para apagar o quadro é {a1}')

elif sorteio == 2:
    print(f'O aluno escolhido para apagar o quadro é {a2}')

elif sorteio == 3:
    print(f'O aluno escolhido para apagar o quadro é {a3}')

import random
aluno1 = input('Nome do primeiro aluno:')
aluno2 = input('Nome do segundo aluno:')
aluno3 = input('Nome do terceiro aluno:')
lista = [aluno1, aluno2, aluno3]
escolhido = random.choice(lista)#random.choice seleciona UM item aletório de uma lista/tupla/string
print(f'O aluno escolhido foi, {escolhido}')

#random.shuffle() <-- serve para embaralhar

v = math.pow(5,2)
print(v)

import random

random.randint(1,11) = 'sorteia inteiros de 1 a 11'

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list) = 'embaralha lista'
print(lista) = [3,2,5,1,4]


lista = [aluno1, aluno2, aluno3]
escolhido = random.choice(lista)
'escolhe um numero aleatório da lista/tupla/string'