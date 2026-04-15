x = 10          # inteiro
y = 3.14        # float
nome = "Ana"    # string
ativo = True    # booleano

'+  soma'
'-  subtração'
'*  multiplicação'
'/  divisão'
'// divisão inteira'
'%  resto (mod)'
'** potência'

' =  recebe/atribuição'
' += ou  -= O nº recebe ele + i' '=' 'soma = soma + 1'
' == igual'
' != diferente'
' >  maior'
' <  menor'
' >= maior ou igual'
' <= menor ou igual'

'and'
'or'
'not'

nome = input("Digite seu nome: ") #input = readln
idade = int(input("Digite sua idade: ")) #int altera o tipo string pra inteiro
#primeiro lê o valor, depois converte o tipo
print("Olá", nome) #print = writeln
print(f"Idade: {idade}")#f{} é um recurso para concatenar de forma mais prática

idade = 18
if idade >= 18:
    print("Maior de idade")

if idade >= 18: #se isso for verdade então: maior
    print("Maior")
else: #senão, execute a próxima instrução sem quaisquer requisitos
    print("Menor")
    
nota = 7
if nota >= 9: 
    print("Excelente")
elif nota >= 7:
    print("Bom")
else:
    print("Reprovado")
#a diferença entre usar 2 IFs e 1 IF e 1 ELIF é que:
#Com 2 IFs ambas as condições vão ser testadas, independente se a primeira ja atende os requisitos
#Com If + Elif, caso a primeira já seja verdadeira, a segunda nem será testada

i = 1
while i <= 5: #enquanto essa condição for verdade, execute os passos a baixo:
    print(i)
    i += 1

for i in range(5):
    print(i)
   # 0,1,2,3,4
   #No python, indexações começam em 0 ao invés do 1.
   #Então lembre-se de sempre considerar o alcance(range) do loop n-1;

             #(inicio:fim:intervalo)
for i in range(1, 10, 2):
    print(i)
    #1,3,5,7,9
#Ou senão, defina o inicio e fim na função 'range()'
#range(inicio, fim, intervalo de numeros)

def soma(a, b):#programa lê a função e guarda para depois
    return a + b

resultado = soma(2, 3)#programa vê a chamada, entrega os numeros para função vista anteriormente
print(resultado)#exibe a operação realizada na função


num = [] #lista vazia
for i in range(10): #De 0 até o alcance N-1
    valor = int(input(f'Digite o {i+1} numero: '))
    num.append(valor)
print(num)  # escreve lista

for c in range (6, 0, -1):
    print(c)
#Para replicar um downto é necessário indicar o inicio (6), o fim(0), e o grau de descréscimo (-1)

    #Primeiro Lê, Depois converte, e dps recebe. Direita -> Esquerda
    #.append adiciona valores ao fim da lista/vetor

    #------------------------DICAS----------------------#
    #numeros tambem podem ser quebrados com indices: num = 4321;
    # num[0] = 4, num[1] 3, ...



