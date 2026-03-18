'''Leia 10 números em uma lista e mostre:
Vetor original
Vetor invertido'''

num = []
for i in range(4):# = 0,1,2,3 = 4 espaços
    valor = int(input('Digite 4 Números: '))
    num.append(valor)

num_inv =[0,0,0,0]
c= 0
for i in range(3,-1,-1):# = 3,2,1,0 ( caso o 'fim' fosse 0, iria ser 3,2,1
    num_inv[c] = num[i]
    c += 1

print(num)
print(num_inv)