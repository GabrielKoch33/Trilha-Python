# =====================================================================
# Exercício 001: Cadastro simples de pessoa.
# Crie um dicionário representando uma pessoa.
    # Regras:
    # - Exiba o nome.
    # - Altere a idade.
    # - Adicione a chave "email".
    # - Remova a chave "cidade".
    # - Exiba o dicionário final.
# =====================================================================

pessoa = {
     "nome": "Ana",
     "idade": 25,
     "cidade": "Curitiba"
}

print(pessoa['nome'])
pessoa['idade'] = 26
print(pessoa['idade'])
pessoa['email']  = 'gabriel123@gmail.com'
print(pessoa['email'])
del pessoa['cidade']
print(pessoa)

# =====================================================================
# Exercício 002: Consulta segura com get().
# Crie um dicionário de produto e peça ao usuário o nome de uma chave.
    # Regras:
    # - Se a chave existir, mostre o valor.
    # - Se não existir, mostre "Chave não encontrada".
    # - Use get().

# =====================================================================

produto = {
     "nome": "Teclado",
     "preco": 150.0,
     "estoque": 10
}
print(produto)

while True:
    chave = str(input('Digite a chave que deseje acessar dentre as opções acima: '))
    if chave not in produto:
        print(produto.get(chave,'Chave Não Encontrada'))
    else:
        print(produto.get(chave))
    op = str(input('Deseja Sair?: (escreva sair)'))
    if op.upper() == 'SAIR':
        break
print()

# .get() é uma forma 'segura' de retornar um valor de um dicionário. Caso o valor não exista, ao invés dele crashar o programa 
# como o dict['nomeproduto'] faz, o get() retorna uma mensagem padrão: get('nomeproduto','mensagem de retorno negativo'), ou caso não definida, None.

# =====================================================================
# Exercício 003: Percorrendo chaves, valores e itens.
# Crie um dicionário de aluno e exiba chaves, valores e itens separadamente.
    # Regras:
    # - Exiba todas as chaves.
    # - Exiba todos os valores.
    # - Exiba chave e valor juntos.
    # - Use nomeprodutos().
    # - Use QtdPrecos().
    # - Use items().
# =====================================================================
aluno = {
     "nome": "Carlos",
     "curso": "TI",
     "semestre": 2,
     "ativo": True
}
print(aluno.nomeprodutos())
print()
print(aluno.QtdPrecos())
print()
print(aluno.items())
print()

# =====================================================================
# Exercício 004: Contador de letras.
# Peça uma palavra ao usuário e conte quantas vezes cada letra aparece.
# Exemplo:
#   Entrada: banana
#   Saída:
#   b: 1
#   a: 3    
#   n: 2
# Regras:
    # - Use um dicionário vazio.
    # - Cada letra deve ser uma chave.
    # - A quantidade deve ser o valor.
    # - Ignore espaços, se houver.
# =====================================================================#
palavra = str(input('Digite uma palavra para o usuário exibir a quantidade de cada letra: ')).replace(' ','')

dicionario = {

}

for letra in palavra:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1
print(dicionario)

# =====================================================================
# Exercício 005: Contador de palavras.
# Peça uma frase e conte quantas vezes cada palavra aparece.
# Exemplo:
#   Entrada: 
    #   python é bom python é forte
#   Saída:
    #   python: 2
    #   é: 2
    #   bom: 1
    #   forte: 1

    # Regras:
    # - Use split().
    # - Transforme tudo para minúsculo.
    # - Use dicionário como contador.
# =====================================================================
frase = str(input('Digite uma frase: ')).split()
PalavrasDistintas = {

}
for palavra in frase:
    if palavra not in PalavrasDistintas:
        PalavrasDistintas[palavra] = 1
    else:
        PalavrasDistintas[palavra] += 1 

print(PalavrasDistintas)
print()

# =====================================================================
# Exercício 006: Estoque simples.
# Crie um dicionário em que a chave é o nome do produto e o valor é a
# quantidade em estoque.

# Regras:
    # - Não adicionar produto duplicado.
    # - Não atualizar produto inexistente.
    # - Não remover produto inexistente.
    # - Quantidade não pode ser negativa.
# =====================================================================
estoque = {
     "mouse": 10,
     "teclado": 5,
     "monitor": 2
}
def emEstoque(estoque, prod):
    if prod in estoque:
        return True
        
def consultar(estoque):
     (listar(estoque))
     prod = str(input('Procure um produto em nosso estoque: '))
     IsInEstoque = estoque.get(prod,'Produto não disponível')
     return IsInEstoque

def adicionar(estoque):
    prod = str(input('Digite um produto para adicionar ao estoque: '))
    if emEstoque(estoque, prod):
        return 'Produto Já Está em Estoque, não é possível adicionar'
    else:
        valor = int(input('Qual o valor desse produto?: '))
        estoque[prod] = valor
        return f'{prod} Adicionado!'

def atualizar(estoque):
    (listar(estoque))
    prod = str(input('Digite o nome do produto que será atualizado: '))
    if emEstoque(estoque, prod):
        chaveouvalor = str(input('Deseja atualizar o nome ou o valor?: ')).upper()

        if chaveouvalor == 'NOME':
            update_prod = str(input('Digite o produto vai substituir: ')) 
            estoque[update_prod] = estoque.pop(prod) #Atribui o valor de prod ao update_prod e após isso remove o prod com pop()
            return estoque[update_prod]

        elif chaveouvalor == 'VALOR':
            valor = float(input(f'Digite a quantidade que {prod} que receberá: '))
            estoque[prod] = valor
            return estoque[prod]
        else:
            return 'Opção Inválida'
    else:
        return 'Produto Inexistênte em Estoque, Impossível atualizar'

def remover(estoque) :
    (listar(estoque))

    prod = str(input('Digite o produto que deseja remover de estoque: '))
    if emEstoque(estoque, prod):
        del estoque[prod]
        return estoque
    else:
        return 'Produto Inexistênte em Estoque, Impossível Remover'

def listar(estoque):
    print(estoque)
# ============================================
print(listar(estoque))
while True:
    print('1 - Consultar produto')
    print('2 - Adicionar produto')
    print('3 - Atualizar quantidade')
    print('4 - Remover produto')
    print('5 - Listar estoque')
    print('0 - Sair')
    op = int(input('O que deseja fazer? '))
    if op == 1:
        r1 = consultar(estoque)
        print(f'Preço: {r1}')
    elif op == 2:
        r1 = adicionar(estoque)
        print(r1)
    elif op == 3:
        r1 = atualizar(estoque)
        print(r1)
    elif op == 4: 
        r1 = remover(estoque)       
        print(r1)
    elif op == 5:
        r1 = listar(estoque)
        print(r1)
    elif op == 0:
        break
# =====================================================================
# Exercício 007: Estoque com preço e quantidade.
# Agora o estoque deve ser mais realista. 
# Crie funções ou um menu para manipular produtos, preços e quantidades.
    # Regras:
    # - Consultar produto.
    # - Atualizar quantidade.
    # - Atualizar preço.
    # - Calcular valor total de um produto.
    # - Calcular valor total do estoque.
# =====================================================================

estoque = {
     "mouse": {"quantidade": 10, "preco": 80.0},
     "teclado": {"quantidade": 5, "preco": 150.0},
     "monitor": {"quantidade": 2, "preco": 900.0}
}

def emEstoque(estoque, prod):
    return prod in estoque #true ou false/none
        
def consultar(estoque):
     (listar(estoque))
     prod = str(input('Procure um produto em nosso estoque: '))
     IsInEstoque = estoque.get(prod,'Produto não disponível')
     return IsInEstoque

def adicionar(estoque):
    prod = str(input('Digite um produto para adicionar ao estoque: '))
    if emEstoque(estoque, prod):
        return 'Produto Já Está em Estoque, não é possível adicionar'
    else:
        valor = float(input('Qual o valor desse produto?: '))
        estoque[prod]['preco'] = valor
        qtd = int(input('Qual a quantidade desse produto?: '))
        estoque[prod]['quantidade'] = qtd
        return f'{prod} Adicionado!'

def atualizarQuantidade(estoque):
    (listar(estoque))
    prod = str(input('Digite o nome do produto que será atualizado: '))
    if emEstoque(estoque, prod):
        qtd = int(input(f'Digite a quantidade que {prod} que receberá: '))
        estoque[prod]['quantidade'] = qtd
        return estoque[prod]['quantidade']
    else:
        return 'Produto Inexistênte em Estoque, Impossível atualizar'
    
def atualizarPreco(estoque):
    (listar(estoque))
    prod = str(input('Digite o nome do produto que será atualizado: '))
    if emEstoque(estoque, prod):
        valor = float(input(f'Digite o valor que {prod} que receberá: '))
        estoque[prod]['preco'] = valor
        return estoque[prod]['preco']
    else:
        return 'Produto Inexistênte em Estoque, Impossível atualizar'

def remover(estoque) :
    (listar(estoque))

    prod = str(input('Digite o produto que deseja remover de estoque: '))
    if emEstoque(estoque, prod):
        del estoque[prod]
        return estoque
    else:
        return 'Produto Inexistênte em Estoque, Impossível Remover'

def listar(estoque):
    for i in estoque.items():
        print(i)

def CalTotProduto(estoque):
    (listar(estoque))
    prod = str(input('Procure um produto em nosso estoque: '))
    if emEstoque(estoque, prod):
        return(f'O valor total de {prod} em nosso estoque é de: {(estoque[prod]['quantidade'])*(estoque[prod]['preco'])}')    
    else:
        return 'Imposível calcular valor de produto que não existe'
    
def CalTotEstoque(estoque):
    soma = 0
    for QtdPreco in estoque.values(): #{"quantidade": 10, "preco": 80.0},
        m = 1
        for valor in QtdPreco.values(): # 10 e 80.0
            m = m*valor
        soma += m
    return soma      
# ============================================
listar(estoque)
while True:
    print('1 - Consultar produto')
    print('2 - Adicionar produto')
    print('3 - Atualizar quantidade')
    print('4 - Atualizar preço')
    print('5 - Remover produto')
    print('6 - Listar estoque')
    print('7 - Qtd x Valor do Produto')
    print('8 - Valor Total do Estoque')
    print('0 - Sair')
    op = int(input('O que deseja fazer? '))
    if op == 1:
        r1 = consultar(estoque)
        print(f'Preço: {r1}')
    elif op == 2:
        r1 = adicionar(estoque)
        print(r1)
    elif op == 3:
        r1 = atualizarQuantidade(estoque)
        print(r1)
    elif op == 4:
        r1 = atualizarPreco(estoque)
        print(r1)
    elif op == 5: 
        r1 = remover(estoque)       
        print(r1)
    elif op == 6:
        r1 = listar(estoque)
        print(r1)
    elif op == 7:
        r1 = CalTotProduto(estoque)
        print(r1)
    elif op == 8:
        r1 = CalTotEstoque(estoque)
        print(f'O valor total do estoque é: {r1}')
    elif op == 0:
        break

# =====================================================================
# Exercício 008: Cadastro de alunos com notas.
# Crie um dicionário em que a chave é o nome do aluno e o valor é uma lista de notas.
# Regras:
    
    # - Exiba a média de cada aluno.
    # - Exiba a situação de cada aluno.
    # - Média >= 7: aprovado.
    # - Média >= 5: recuperação.
    # - Média < 5: reprovado.

# =====================================================================
alunos = {
     "Ana": [8.0, 7.5, 9.0],
     "Bruno": [5.0, 6.5, 6.0],
     "Carlos": [3.0, 4.0, 5.0]
}
def definemedia(media):
    if media >= 7: 
         return 'aprovado' 
    elif media >= 5:
         return 'em exame'        
    else:
        return 'reprovado' 
        
for k,v in alunos.items():
    soma = 0
    for nota in v:
        soma += nota
    media = soma/len(v)
    print(f'-{k}:\n  -Média: {media:.2f}\n  -Status: {definemedia(media)}')
    # {valor:.nf} :.nf define n casas após o . (float)

# Versão mais prática:
'''for k, v in alunos.items():
    media = sum(v) / len(v) ---- A cada chamada de função o os valores utilizados são substituidos, não ficam guardados
    print(f'{k}:\n-Média: {media}\n-Status: {definemedia(media)}')'''
    

# =====================================================================
# Exercício 009: Agenda de contatos.
# Crie uma agenda em que a chave é o nome da pessoa e o valor é outro dicionário com telefone e email.

# Regras:
    # - Não permitir contato duplicado.
    # - Validar se o contato existe antes de alterar/remover.
    # - Buscar deve mostrar telefone e email.
    # - Email não pode repetir, Telefone Pode
# =====================================================================

# Quando usamos return x,y o python entende como tupla, logo é necessário desempacotar
agenda = {
     "Ana": {
         "telefone": "9999-1111",
         "email": "ana@email.com"
     }
}

def existeNome(agenda,nomePessoa):
    if nomePessoa in agenda:
        return True
    
def existeEmail(agenda,emailPessoa):
    achou = False
    for dados in agenda.values():
        if dados['email'] == emailPessoa:
            achou = True
    return achou # se achou for false é porque não há email duplicado, se for true é porque há duplicidade

def addContato(agenda):
    while True:
        nomePessoa = str(input('Digite o nome da pessoa que deseja cadastrar: ')).title()
        if existeNome(agenda, nomePessoa) == True:
            print('Pessoa já existênte, cadastre outro nome')
            resp = input('Ainda deseja continuar? Sim ou Não?')
            if resp[0].upper() == 'N':
                break
        else:
            while True:
                emailPessoa = str(input('Digite o email da pessoa que deseja cadastrar: ')).replace(' ','').lower()
                if existeEmail(agenda,emailPessoa) == True:
                    print('Email já existênte, cadastre outro')
                else:
                    numCelular = str(input('Digite o número da pessoa que deseja cadastrar: '))
                    agenda[nomePessoa] = {
                        'telefone': numCelular,
                        'email': emailPessoa
                    }
                    break #O return é quem faz a interrupção de funções, break apenas interrompe o loop
            break #O break não sai de condicionais, apenas loops While e For que ele está inserido
    return f'{nomePessoa} Adicionada!'

def BuscarContato(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        return agenda[nomePessoa]
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
        # return não escreve nada em tela, apenas entrega valor a função. BuscarContato(agenda) = 'Essa pessoa não...'

def AttTelefone(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        novoTelefone = str(input(f'Digite o novo telefone de {nomePessoa}: '))
        agenda[nomePessoa]['telefone'] = novoTelefone
        return f'Telefone atualizado para {novoTelefone}!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def AttEmail(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja encontrar: ')).title()
    if existeNome(agenda,nomePessoa):
        novoEmail = str(input(f'Digite o novo email de {nomePessoa}: '))
        agenda[nomePessoa]['email'] = novoEmail
        return f'Email atualizado para {novoEmail}!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def RemoverContato(agenda):
    nomePessoa = str(input('Digite o nome da pessoa que deseja remover: ')).title()
    if existeNome(agenda,nomePessoa):
        del agenda[nomePessoa]
        return f'{nomePessoa} Removido(a)!'
    else:
        return 'Essa pessoa não está em nosso sistema! Escreveu corretamente?' 
    
def ListarContatos(agenda):
    print()
    for nome, dados in agenda.items(): #nome = key ; dados = value
        print(f'Nome: {nome}\n Telefone: {dados['telefone']}\n Email: {dados['email']}')
        print()

while True:
    print('1 - Adicionar contato')
    print('2 - Buscar contato')
    print('3 - Atualizar telefone')
    print('4 - Atualizar email')
    print('5 - Remover contato')
    print('6 - Listar contatos')
    print('0 - Sair') 
    opcao = int(input('Digite uma das opções acima: '))
    match opcao: 
        case 1:
            print(addContato(agenda))
        case 2:
            print(BuscarContato(agenda))
        case 3:
            print(AttTelefone(agenda))
        case 4:
            print(AttEmail(agenda))
        case 5:
            print(RemoverContato(agenda))
        case 6:
            ListarContatos(agenda)
        case 0:
            break

# =====================================================================
# Exercício 010: Agrupador de produtos por categoria.
# Você tem uma lista de tuplas e deve transformá-la em um dicionário agrupado por categoria.
    #Regras:
    # - Use dicionário vazio.
    # - Categoria deve ser a chave.
    # - Produtos da mesma categoria devem ir para uma lista.

    # Resultado esperado:
    #   {
    #       "periférico": ["mouse", "teclado"],
    #       "vídeo": ["monitor", "webcam"],
    #       "móvel": ["cadeira"]
    #   }
# =====================================================================


produtos = [
    ("mouse","periférico"),  #0   
    ("teclado","periférico"),#1
    ("monitor","vídeo"),     #2
    ("webcam","vídeo"),      #3
    ("cadeira","móvel")      #4
    ]

Categoria = {

}
for tipo in produtos:
    if tipo[1] not in Categoria: #caso não exista, então crie
        Categoria[tipo[1]] = []
    Categoria[tipo[1]].append(tipo[0])  # caso ja exista, não crie, e adicione produto a lista criada

print(Categoria)

# =====================================================================
# Exercício 011: Ranking de jogadores.
# Você recebe uma lista de jogadas. Crie um dicionário com a pontuação total
# de cada jogador e mostre quem fez mais pontos.
# Resultado esperado:
#   {
#       "Alice": 45,
#       "Bob": 55,
#       "Carlos": 50
#   }
# =====================================================================
#
# Estrutura obrigatória:
#
# jogadas = [
#     ("Alice", 30),
#     ("Bob", 20),
#     ("Alice", 15),
#     ("Carlos", 40),
#     ("Bob", 35),
#     ("Carlos", 10)
# ]
#
# Regras:
#
# - Não precisa ordenar ainda.
# - Apenas descubra o maior manualmente.
# - Não use lambda.


# =====================================================================
# Exercício 012: Carrinho de compras.
# Crie um carrinho como dicionário e calcule subtotal, total geral, produto
# mais caro e produto com maior quantidade.
# =====================================================================
#
# Estrutura obrigatória:
#
# carrinho = {
#     "mouse": {"quantidade": 2, "preco": 80.0},
#     "teclado": {"quantidade": 1, "preco": 150.0}
# }
#
# Regras:
#
# - Calcule o subtotal de cada produto.
# - Calcule o total geral.
# - Mostre o produto mais caro no carrinho.
# - Mostre o produto com maior quantidade.
# - Produto mais caro considera preço unitário.
# - Maior quantidade considera quantidade.


# =====================================================================
# Exercício 013: Validador de registro obrigatório.
# Você recebe um cadastro e uma lista de campos obrigatórios. Verifique quais
# campos obrigatórios estão vazios ou ausentes.
# Resultado esperado:
#   ["email"]
# =====================================================================
#
# Estrutura obrigatória:
#
# cadastro = {
#     "nome": "Ana Silva",
#     "email": "",
#     "idade": 22,
#     "cidade": "Curitiba"
# }
#
# obrigatorios = ["nome", "email", "idade"]
#
# Regras:
#
# - Campo ausente também é erro.
# - String vazia conta como erro.
# - Ao final, gere uma lista com os nomes dos campos inválidos.


# =====================================================================
# Exercício 014: Resumo de vendas por vendedor.
# Você recebe uma lista de vendas. Gere um dicionário com o total vendido por
# vendedor e depois mostre o resumo das vendas.
# Resultado esperado:
#   {
#       "Ana": 550.0,
#       "Bruno": 250.0,
#       "Carlos": 400.0
#   }
# =====================================================================
#
# Estrutura obrigatória:
#
# vendas = [
#     ("Ana", 250.0),
#     ("Bruno", 100.0),
#     ("Ana", 300.0),
#     ("Carlos", 400.0),
#     ("Bruno", 150.0)
# ]
#
# Regras:
#
# - Mostre o total geral vendido.
# - Mostre o vendedor com maior venda acumulada.
# - Mostre os vendedores que venderam acima de R$300.


# =====================================================================
# Exercício 015: Mini relatório de logs com dicionário.
# Você recebe logs simples e deve criar um relatório usando dicionários.
# Resultado esperado aproximado:
#   contagem = {
#       "INFO": 2,
#       "ERRO": 2,
#       "AVISO": 1,
#       "DEBUG": 1
#   }
#
#   erros = [
#       "Falha na conexão",
#       "Timeout"
#   ]
# =====================================================================
#
# Estrutura obrigatória:
#
# logs = [
#     "INFO - Servidor iniciado",
#     "ERRO - Falha na conexão",
#     "INFO - Usuário conectado",
#     "AVISO - Memória alta",
#     "ERRO - Timeout",
#     "DEBUG - Variável carregada"
# ]
#
# Regras:
#
# - Mostre a quantidade por tipo de log.
# - Mostre a lista de mensagens de erro.
# - Mostre os tipos de log encontrados.
