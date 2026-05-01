brasil = []
estado1 = {"uf":'São Paulo','sigla':'SP'}
estado2 = {"uf":'Rio de Janeiro','sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]["uf"])#'Rio de Janeiro'
print(brasil[0]["sigla"])

estado = {}
pais = []
for i in range(0,3):
    estado['uf'] = str(input('uf: '))
    estado['população'] = int(input('pop: '))
    pais.append(estado.copy())
print(pais)
for p in pais:
    for v in p.values():
        print(v)
    print()