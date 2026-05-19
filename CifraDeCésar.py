
alfabeto = list("abcdefghijklmnopqrstuvwxyz") 
palavra = list(input('Digite uma palavra: ').strip().replace(' ','-')) #antes de transformar a frase em lista, eu tiro os espaços e substituo-os por '-'
# assim toda frase vai ser: 'hoje-e-um-belo-dia' ao invés de = [[hoje],[e],[um],[belo],[dia]]

for indice, letra in enumerate(palavra): # percorre toda a palavra que foi informada, de letra em letra
    for index, caractere in enumerate(alfabeto): # percorre todo o alfabeto
        if letra == '-': 
            break
        if letra == 'z': # se a letra da palavra for z, então recebe 'a'
            palavra[indice] = 'a'
            break
        elif letra == caractere: # se não for z, vai percorrer o alfabeto ate achar a letra igual
            palavra[indice] = alfabeto[index+1]
            break
    
palavra_criptografada = ''.join(palavra).replace('-',' ')#transforma a lista em string
print(palavra_criptografada)