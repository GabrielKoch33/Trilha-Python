# while True:
#     text = input('Texto: ').title()
#     print()
#     print(text)
#     print()
while True:
    frase = input('frase: ')
    nova_frase = []

    # 1. Correção: split() separa a frase em palavras
    for palavra in frase.split():
        # 2. Correção: '==' para comparação, 'palavra' em vez de 'p'
        if len(palavra) == 1 or len(palavra) == 2 :
            # 3. Correção: 'paalavra' -> 'palavra'
            palavra = palavra.lower()
        else: 
            palavra = palavra.title()
        nova_frase.append(palavra)
    
    # Junta as palavras de volta em uma frase
    resultado = " ".join(nova_frase)
    print(resultado) # Saída: O rato roeu a roupa do rei a