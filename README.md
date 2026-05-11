# Roadmap de Estudos em Python

Este repositório reúne meu plano de estudos em **Python**, organizado em fases progressivas.  
O objetivo é acompanhar minha evolução desde os fundamentos da linguagem até o uso profissional de Python em projetos, dados, testes, versionamento e portfólio.

---

## Objetivo do Roadmap

Este roadmap foi estruturado para consolidar uma base sólida em Python, com foco em:

- domínio da sintaxe e da lógica de programação;
- escrita de código limpo, legível e testável;
- organização de projetos reais;
- manipulação de arquivos e dados;
- fundamentos de programação orientada a objetos;
- testes automatizados;
- versionamento com Git e GitHub;
- preparação para projetos de dados e Engenharia de Dados.

---

## Status Geral

**Situação atual:** em andamento  
**Foco principal:** consolidação dos fundamentos, estruturas de dados, funções e evolução para código Python mais profissional.

---

## Sumário

- [Fase 1 — Fundamentos](#fase-1--fundamentos)
- [Fase 2 — Controle de Fluxo](#fase-2--controle-de-fluxo)
- [Fase 3 — Estruturas de Dados](#fase-3--estruturas-de-dados)
- [Fase 4 — Funções](#fase-4--funções)
- [Fase 4.5 — Mentalidade Python Profissional](#fase-45--mentalidade-python-profissional)
- [Fase 5 — Módulos e Organização](#fase-5--módulos-e-organização)
- [Fase 6 — Tratamento de Erros](#fase-6--tratamento-de-erros)
- [Fase 7 — Arquivos e Dados](#fase-7--arquivos-e-dados)
- [Fase 8 — Iteradores, Generators e Memória](#fase-8--iteradores-generators-e-memória)
- [Fase 9 — Programação Orientada a Objetos](#fase-9--programação-orientada-a-objetos)
- [Fase 10 — Python Profissional](#fase-10--python-profissional)
- [Fase 11 — Testes](#fase-11--testes)
- [Fase 12 — Git e Versionamento](#fase-12--git-e-versionamento)
- [Fase 13 — Python para Dados](#fase-13--python-para-dados)
- [Fase 14 — Algoritmos e Lógica](#fase-14--algoritmos-e-lógica)
- [Fase 15 — Portfólio](#fase-15--portfólio)

---

# Fase 1 — Fundamentos

Nesta fase, o objetivo é compreender a base da linguagem Python e dominar os elementos essenciais para escrever os primeiros programas.

## Checklist

- [x] Sintaxe básica
- [x] `print()`
- [x] `input()`
- [x] Variáveis
- [x] Tipos primitivos
- [x] Conversão de tipos: `str()`, `int()`, `float()`
- [x] Operadores aritméticos: `/`, `//`, `%`, `**`
- [x] Operadores lógicos
- [x] Operadores relacionais
- [x] Precedência de operadores
- [x] Comentários
- [x] f-strings

## Ao final desta fase, devo ser capaz de

- criar programas simples em Python;
- ler dados do usuário;
- converter tipos corretamente;
- montar expressões aritméticas e lógicas;
- exibir informações formatadas com f-strings.

---

# Fase 2 — Controle de Fluxo

Nesta fase, o foco é controlar o caminho de execução do programa usando estruturas condicionais e de repetição.

## Checklist

- [x] `if`
- [x] `elif`
- [x] `else`
- [x] `match/case`
- [x] `while`
- [x] `for`
- [x] `range()`
- [x] `break`
- [x] `continue`
- [x] `pass`

## Ao final desta fase, devo ser capaz de

- criar decisões condicionais;
- repetir blocos de código;
- controlar interrupções em laços;
- escolher a estrutura de controle mais adequada para cada problema.

---

# Fase 3 — Estruturas de Dados

Nesta fase, o objetivo é dominar as principais estruturas de dados nativas do Python e entender quando utilizar cada uma delas.

## Checklist

- [x] Strings
- [x] Indexação: `[0]`, `[-1]`
- [x] Slicing: `[inicio:fim:passo]`, `[::-1]`
- [x] Métodos de string: `.upper()`, `.lower()`, `.strip()`, entre outros
- [x] Listas
- [x] Métodos de lista
- [x] Tuplas
- [x] Sets
- [x] Dicionários
- [ ] List comprehension
- [ ] Dictionary comprehension
- [ ] Set comprehension
- [ ] Generator expression
- [ ] Comprehensions aninhadas
- [ ] Diferença entre lista, tupla, set e dicionário em problemas reais

## Ao final desta fase, devo ser capaz de

- armazenar coleções de dados;
- percorrer strings, listas, tuplas, sets e dicionários;
- escolher a estrutura correta para cada situação;
- escrever transformações simples usando comprehensions.

---

# Fase 4 — Funções

Nesta fase, o foco é criar funções reutilizáveis, legíveis e com responsabilidades bem definidas.

## Checklist

- [x] `def`
- [ ] Parâmetros
- [x] Retorno
- [x] Escopo local e global
- [ ] Argumentos nomeados
- [ ] `*args`
- [ ] `**kwargs`
- [ ] Lambda
- [ ] Recursão básica
- [ ] Docstrings
- [ ] Separação entre entrada, processamento e saída
- [ ] Funções puras básicas
- [ ] Type hints em funções
- [ ] Boas assinaturas de função

## Ao final desta fase, devo ser capaz de

- criar funções com entrada, processamento e retorno;
- evitar repetição desnecessária de código;
- separar responsabilidades;
- escrever funções mais fáceis de testar e reutilizar.

---

# Fase 4.5 — Mentalidade Python Profissional

Esta fase serve como uma ponte entre resolver exercícios e escrever código mais próximo de um padrão profissional.

## Checklist

- [x] Evitar excesso de `range(len(...))`
- [x] Usar `for item in lista`
- [x] Usar `enumerate()` quando precisar de índice
- [ ] Usar desempacotamento de tuplas
- [x] Retornar dados em vez de imprimir dentro da função
- [ ] Evitar variáveis globais desnecessárias
- [x] Melhorar nomes de variáveis
- [ ] Refatorar código antigo
- [ ] Distinguir exercício de algoritmo de código profissional
- [x] Ler código sugerido por IA antes de aceitar
- [x] Explicar linha por linha o próprio código
- [x] Escrever código testável

## Ao final desta fase, devo ser capaz de

- escrever código mais limpo e idiomático;
- diferenciar soluções didáticas de soluções profissionais;
- melhorar nomes, estrutura e legibilidade;
- refatorar códigos antigos sem alterar seu comportamento.

---

# Fase 5 — Módulos e Organização

Nesta fase, o objetivo é aprender a organizar melhor o código e usar módulos nativos da linguagem.

## Checklist

- [ ] `import`
- [ ] `from import`
- [ ] Aliases
- [ ] Módulos nativos
- [ ] `math`
- [ ] `random`
- [ ] `statistics`
- [ ] `datetime`
- [ ] `pathlib`
- [ ] `os`
- [ ] `sys`
- [ ] Separação em arquivos
- [ ] Estrutura básica de projeto Python
- [ ] Execução via terminal
- [ ] `if __name__ == "__main__"`

## Ao final desta fase, devo ser capaz de

- importar bibliotecas corretamente;
- separar o código em arquivos;
- usar módulos nativos úteis;
- executar scripts pelo terminal;
- estruturar pequenos projetos Python.

---

# Fase 6 — Tratamento de Erros

Nesta fase, o foco é lidar com erros de forma controlada, sem esconder problemas reais no código.

## Checklist

- [ ] `try`
- [ ] `except`
- [ ] `else`
- [ ] `finally`
- [ ] `raise`
- [ ] Exceptions comuns
- [ ] Validação de entrada
- [ ] Mensagens de erro úteis
- [ ] Tratamento de erro sem esconder bug

## Ao final desta fase, devo ser capaz de

- tratar erros previsíveis;
- validar entradas de usuário;
- criar mensagens de erro compreensíveis;
- evitar tratamentos genéricos que mascaram bugs.

---

# Fase 7 — Arquivos e Dados

Nesta fase, o objetivo é trabalhar com arquivos e formatos comuns de dados.

## Checklist

- [ ] `open()`
- [ ] Leitura de arquivos `.txt`
- [ ] Escrita de arquivos `.txt`
- [ ] `with open`
- [ ] CSV
- [ ] JSON
- [ ] `pathlib` para arquivos
- [ ] Encoding
- [ ] Leitura linha a linha
- [ ] Processamento de arquivos grandes
- [ ] Escrita estruturada de saída

## Ao final desta fase, devo ser capaz de

- ler e escrever arquivos;
- manipular CSV e JSON;
- processar dados linha a linha;
- criar saídas estruturadas;
- lidar com caminhos de arquivos de forma segura usando `pathlib`.

---

# Fase 8 — Iteradores, Generators e Memória

Nesta fase, o foco é entender como o Python trabalha com iteração e como processar dados de forma eficiente em memória.

## Checklist

- [ ] Iteráveis
- [ ] Iteradores
- [ ] `iter()`
- [ ] `next()`
- [ ] Generator functions com `yield`
- [ ] Generator expressions
- [ ] Diferença entre lista e generator
- [ ] Processamento preguiçoso, também chamado de lazy evaluation
- [ ] Pipeline simples com generators
- [ ] Processamento de grandes volumes sem carregar tudo na memória

## Ao final desta fase, devo ser capaz de

- diferenciar iteráveis de iteradores;
- criar generators;
- processar dados sob demanda;
- evitar carregar grandes volumes de dados desnecessariamente na memória.

---

# Fase 9 — Programação Orientada a Objetos

Nesta fase, o objetivo é entender os fundamentos da Programação Orientada a Objetos em Python e saber quando esse paradigma faz sentido.

## Checklist

- [ ] Classes
- [ ] Objetos
- [ ] `__init__`
- [ ] Atributos
- [ ] Métodos
- [ ] Encapsulamento
- [ ] Herança
- [ ] Polimorfismo
- [ ] `__str__`
- [ ] Quando usar POO e quando não usar
- [ ] Classes simples para modelar dados

## Ao final desta fase, devo ser capaz de

- criar classes e objetos;
- modelar entidades simples;
- entender atributos e métodos;
- aplicar herança e polimorfismo de forma básica;
- avaliar quando POO melhora ou piora a solução.

---

# Fase 10 — Python Profissional

Nesta fase, o foco é aproximar o código de práticas utilizadas em projetos reais.

## Checklist

- [ ] Boas práticas PEP 8
- [ ] Nomeação correta
- [ ] Refatoração
- [ ] Separação em módulos
- [ ] Type hints
- [ ] Virtualenv / venv
- [ ] Quando usar ambiente virtual
- [ ] `requirements.txt`
- [ ] `pyproject.toml` básico
- [ ] Logging
- [ ] Debug básico
- [ ] Decorators básicos
- [ ] Funções de alta ordem
- [ ] Organização de projeto real
- [ ] Leitura de traceback
- [ ] Uso profissional do terminal

## Ao final desta fase, devo ser capaz de

- organizar um projeto Python real;
- criar e usar ambientes virtuais;
- registrar logs;
- interpretar tracebacks;
- escrever código mais padronizado, legível e sustentável.

---

# Fase 11 — Testes

Nesta fase, o objetivo é aprender a validar o comportamento do código usando testes automatizados.

## Checklist

- [ ] Por que testar
- [ ] `assert` básico
- [ ] `pytest` básico
- [ ] Estrutura de testes
- [ ] Testes de funções puras
- [ ] Testes com entradas e saídas esperadas
- [ ] Testes de erro com `pytest`
- [ ] Casos de borda
- [ ] Organização da pasta `tests`
- [ ] Rodar testes pelo terminal

## Ao final desta fase, devo ser capaz de

- criar testes simples;
- validar funções com entradas e saídas esperadas;
- testar erros esperados;
- organizar uma pasta de testes;
- executar testes pelo terminal.

---

# Fase 12 — Git e Versionamento

Nesta fase, o foco é aprender controle de versão e publicar projetos no GitHub.

## Checklist

- [ ] O que é controle de versão
- [ ] `git init`
- [ ] `git status`
- [ ] `git add`
- [ ] `git commit`
- [ ] `git log`
- [ ] `git diff`
- [ ] `.gitignore`
- [ ] Branches básicas
- [ ] GitHub
- [ ] `README.md`
- [ ] Versionamento de projetos de portfólio
- [ ] Commits pequenos e descritivos

## Ao final desta fase, devo ser capaz de

- versionar projetos com Git;
- criar commits organizados;
- ignorar arquivos desnecessários;
- publicar projetos no GitHub;
- manter histórico claro da evolução dos estudos.

---

# Fase 13 — Python para Dados

Nesta fase, o objetivo é aplicar Python em tarefas relacionadas a dados, automação, APIs e bancos de dados.

## Checklist

- [ ] `requests`
- [ ] APIs REST
- [ ] pandas e NumPy básico
- [ ] Leitura de CSV
- [ ] Limpeza de dados
- [ ] Transformação de dados
- [ ] Automação ETL simples
- [ ] Conexão com banco de dados
- [ ] SQL via Python
- [ ] Variáveis de ambiente
- [ ] Configuração externa
- [ ] Pipeline simples de dados
- [ ] Logs em pipeline
- [ ] Validação de dados de entrada

## Ao final desta fase, devo ser capaz de

- consumir APIs;
- ler e transformar arquivos CSV;
- limpar dados básicos;
- conectar Python a bancos de dados;
- criar um pipeline simples de dados com logs e validações.

---

# Fase 14 — Algoritmos e Lógica

Nesta fase, o foco é reforçar raciocínio lógico, resolução de problemas e noções iniciais de complexidade.

## Checklist

- [ ] Busca linear
- [ ] Busca binária
- [ ] Ordenação simples
- [ ] Contadores
- [ ] Acumuladores
- [ ] Vetores/listas
- [ ] Matrizes/listas 2D
- [ ] Problemas reais
- [ ] Complexidade básica
- [ ] Diferença entre resolver manualmente e usar ferramenta nativa

## Ao final desta fase, devo ser capaz de

- resolver problemas usando listas e matrizes;
- aplicar contadores e acumuladores;
- entender a diferença entre busca linear e busca binária;
- compreender noções básicas de custo computacional;
- decidir quando usar implementação manual e quando usar recursos nativos.

---

# Fase 15 — Portfólio

Nesta fase, o objetivo é consolidar os conhecimentos em projetos práticos e publicáveis.

## Checklist

- [ ] CRUD em arquivo
- [ ] Sistema de estoque
- [ ] ETL CSV para JSON
- [ ] Consumo de API
- [ ] Dashboard simples
- [ ] Automação com Python
- [ ] Projeto com venv
- [ ] Projeto com `requirements.txt`
- [ ] Projeto com `README.md`
- [ ] Projeto com testes
- [ ] Projeto versionado no GitHub
- [ ] Mini pipeline de dados com logs
- [ ] Projeto final integrando Python, SQL, arquivos e API

## Ao final desta fase, devo ser capaz de

- construir projetos completos;
- documentar projetos no GitHub;
- aplicar boas práticas de organização;
- integrar Python com arquivos, APIs e banco de dados;
- criar projetos úteis para portfólio profissional.

---

# Critérios de Evolução

Para considerar uma fase concluída, devo ser capaz de:

- explicar os conceitos com minhas próprias palavras;
- resolver exercícios sem depender diretamente de exemplos prontos;
- aplicar o conteúdo em pequenos problemas reais;
- revisar e melhorar meu próprio código;
- versionar a evolução quando fizer sentido.

---

# Projetos Sugeridos Durante o Roadmap

Alguns projetos que podem ser desenvolvidos ao longo das fases:

| Projeto | Conteúdos praticados |
|---|---|
| Calculadora simples | Fundamentos, entrada, saída e operadores |
| Validador de dados | Condicionais, funções e tratamento de erros |
| Sistema de cadastro em arquivo | Funções, arquivos e organização |
| Sistema de estoque | Estruturas de dados, funções e arquivos |
| Conversor CSV para JSON | Arquivos, CSV, JSON e transformação |
| Consumidor de API | `requests`, APIs REST e tratamento de erros |
| Mini pipeline de dados | Arquivos, logs, validação e organização |
| Projeto final Python + SQL | Python, banco de dados, arquivos, API e GitHub |

---

# Observações

Este roadmap não é apenas uma lista de conteúdos para marcar como concluídos.  
A prioridade é desenvolver domínio real, praticar com frequência e transformar os tópicos em projetos concretos.

O foco principal é aprender Python com profundidade suficiente para avançar futuramente em áreas como:

- Análise de Dados;
- Engenharia de Dados;
- Ciência de Dados;
- Automação;
- Desenvolvimento de projetos profissionais.
