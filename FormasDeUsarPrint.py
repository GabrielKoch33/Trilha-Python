print('O rato \nroeu a roupa \ndo rei de Roma') #o \n serve para quebrar linhas

print('Quer fazer assim: você tenta responder as 20 questões?', end=' ')
#end=' ' serve para dar espaço e continuar o print de baixo
print('Posso corrigir por partes se preferir (tipo 1–10 e depois 11–20). Como prefere?')

nome = input('digite seu nome ')
print('prazer {:20}!'.format(nome))
print('prazer {:>20}!'.format(nome))
print('prazer {:^20}!'.format(nome))
#O valor de nome ocupou 20 espaços de texto: GABRIEL       !
#Usando {:>20} o nome ocupa 20 espaços, porem está alinhado a direita:        GABRIEL!
#Utilizando {:^20} o nome ocupa um total de 20 espaços, porem centralizando o nome:      GABRIEL    .