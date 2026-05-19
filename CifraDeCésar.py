alfabeto = list("abcdefghijklmnopqrstuvwxyz1234567890") 

palavra = list(input('Digite uma palavra: ').strip().replace(' ','-').lower()) 
#antes de transformar a frase em lista, eu tiro os espaços e substituo-os por '-'
# assim toda frase vai ser: 'hoje-e-um-belo-dia' ao invés de = [[hoje],[e],[um],[belo],[dia]]

chave = int(input('digite o valor que será deslocado: ')) # fazer amanhã <--

for indice, letra in enumerate(palavra): # percorre cada letra da palavra informada
    for index, caractere in enumerate(alfabeto): # percorre todo o alfabeto
        if letra == '-': 
            break
        elif letra == 'z': # se a letra da palavra for z, então recebe 'a'
            palavra[indice] = 'a'
            break
        elif letra == '0':
            palavra[indice] = '1'
            break
        elif letra == caractere: # se for qualquer outra letra ou número, vai percorrer o alfabeto ate achar a letra igual
            palavra[indice] = alfabeto[index+1]
            break
    
palavra_criptografada = ''.join(palavra).replace('-',' ')#transforma a lista em string
print(palavra_criptografada)
