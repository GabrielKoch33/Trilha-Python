

num = int(input('Escreva um numero qualquer: '))
suc = num+1
ant = num-1
print(f'O antecessor de {num} é {ant} e o sucessor de {num} é {suc}')

n = float(input('Escreva um numero qualquer: '))
dobro = num*2
triplo = num*3
raiz = num**(1/2)
print(f' O dobro, triplo e raíz quadrada de {n} é, respectivamente, {dobro},{triplo},{raiz}')

n1 = int(input('Escreva a nota 1: '))
n2 = int(input('Escreva a nota 2: '))
media =  (n1+n2)/2
print(f'A media de {n1} + {n2} = {media}')

tam = float(input('Digite o tamanho da peça em Metros '))
cm = tam*100
mm = tam*1000
print(f'{tam}m convertidos em cm: {cm}cm e em mm: {mm}mm')

a = int(input('Escreva um numero para exibir a tabuada: '))
i = 1
for i in range(1, 11):
    print(f'{a} X {i} = {a*i}')

dinheiro = float(input('Quanto dinheiro você possui? '))
dolar = float(3.27)
print(f'Você consegue adquirir com {dinheiro}, aproximadamente USD {dinheiro*dolar}(dólares)')

alt = float(input('Qual a altura da parede?'))
larg = float(input('Qual a largura da parede?'))
area = alt*larg
print(f'Serão necessários {area/2} baldes para pintar a parede de {area}m²')

preco = float(input('Preço produto'))
novopreco = preco-(preco*0.05)
print(f'Com o desconto de 5%, seu produto passou a valer: {novopreco}')

salario = float(input('Salário: '))
aumento = salario*1.15

print(f'O aumento de 15% ao seu salário equivale a R${aumento}')

c = float(input('Digite a temperatura em celsius:\n'))
f = (c*1.8)+32
print(f'{c} Celsius em Fahrenheit:{f}')

km = float(input('Quantos KM esse Fiat Uno alugado percorreu?\n'))
dias = int(input('Por quantos dias esse veículo ficou alugado'))
preco = (dias*60) + (km*0.15)
print(f'Valor {preco}')


