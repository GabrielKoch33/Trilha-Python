# Roadmap de Estudos — Ciência de Dados

Este roadmap foi montado para um estudante de Sistemas de Informação que está começando por Python, seguirá para modelagem de dados e SQL, e tem como objetivo evoluir até Ciência de Dados em nível profissional.

A ordem foi pensada para formar base antes de avançar para ferramentas complexas. O foco não é apenas aprender tecnologias, mas desenvolver raciocínio analítico, domínio de dados, capacidade de modelagem, programação, estatística, Machine Learning, engenharia de dados e entrega de projetos reais.

---

## Sumário

- [Visão geral da trilha](#visão-geral-da-trilha)
- [Fase 0: Fundamentos de computação, ambiente e método de estudo](#fase-0-fundamentos-de-computação-ambiente-e-método-de-estudo)
- [Fase 1: Python básico](#fase-1-python-básico)
- [Fase 2: Python intermediário, organização de código e POO](#fase-2-python-intermediário-organização-de-código-e-poo)
- [Fase 3: Fundamentos de banco de dados e modelagem](#fase-3-fundamentos-de-banco-de-dados-e-modelagem)
- [Fase 4: SQL para criação e manipulação de dados](#fase-4-sql-para-criação-e-manipulação-de-dados)
- [Fase 5: SQL para consulta e análise](#fase-5-sql-para-consulta-e-análise)
- [Fase 6: Python para dados — NumPy, pandas e análise exploratória](#fase-6-python-para-dados--numpy-pandas-e-análise-exploratória)
- [Fase 7: Estatística e probabilidade para dados](#fase-7-estatística-e-probabilidade-para-dados)
- [Fase 8: Visualização de dados e comunicação](#fase-8-visualização-de-dados-e-comunicação)
- [Fase 9: Machine Learning clássico](#fase-9-machine-learning-clássico)
- [Fase 10: Projetos práticos e portfólio](#fase-10-projetos-práticos-e-portfólio)
- [Fase 11: Engenharia de dados para cientistas de dados](#fase-11-engenharia-de-dados-para-cientistas-de-dados)
- [Fase 12: Deploy, APIs e MLOps](#fase-12-deploy-apis-e-mlops)
- [Fase 13: Deep Learning, NLP e IA generativa](#fase-13-deep-learning-nlp-e-ia-generativa)
- [Fase 14: Matemática avançada para Machine Learning](#fase-14-matemática-avançada-para-machine-learning)
- [Fase 15: Evolução para nível pleno](#fase-15-evolução-para-nível-pleno)
- [Fase 16: Evolução para nível sênior](#fase-16-evolução-para-nível-sênior)
- [Projetos recomendados por etapa](#projetos-recomendados-por-etapa)
- [Critérios para avançar entre fases](#critérios-para-avançar-entre-fases)
- [Rotina de estudo sugerida](#rotina-de-estudo-sugerida)
- [Observação final](#observação-final)

---

## Visão geral da trilha

### Ordem principal

1. Fundamentos de computação, ambiente e método de estudo
2. Python básico e intermediário
3. Python profissional, organização de código e POO
4. Fundamentos de banco de dados e modelagem
5. SQL para criação e manipulação de dados
6. SQL para consulta e análise
7. Python para dados: NumPy, pandas e análise exploratória
8. Estatística e probabilidade
9. Visualização de dados e comunicação
10. Machine Learning clássico
11. Projetos práticos e portfólio
12. Engenharia de dados para cientistas de dados
13. Deploy, APIs e MLOps
14. Deep Learning, NLP e IA generativa
15. Matemática avançada para Machine Learning
16. Evolução para nível pleno
17. Evolução para nível sênior

---

## Fase 0: Fundamentos de computação, ambiente e método de estudo

Antes de entrar profundamente em Ciência de Dados, é necessário ter autonomia básica com computador, terminal, organização de arquivos, ambiente de desenvolvimento e versionamento.

### Checklist

- [ ] Entender diretórios, arquivos e extensões.
- [ ] Usar terminal em nível básico.
- [ ] Navegar entre pastas pelo terminal.
- [ ] Criar, mover, copiar e remover arquivos pelo terminal.
- [ ] Entender caminhos absolutos e relativos.
- [ ] Entender diferença entre arquivo `.py` e notebook `.ipynb`.
- [ ] Criar ambiente virtual com `venv`.
- [ ] Instalar bibliotecas com `pip`.
- [ ] Entender o que é dependência de projeto.
- [ ] Criar arquivo `requirements.txt`.
- [ ] Usar Git em nível básico.
- [ ] Usar `git init`.
- [ ] Usar `git status`.
- [ ] Usar `git add`.
- [ ] Usar `git commit`.
- [ ] Usar `git log`.
- [ ] Criar repositórios no GitHub.
- [ ] Enviar projetos para o GitHub.
- [ ] Criar arquivos `README.md`.
- [ ] Organizar rotina de estudos.
- [ ] Separar teoria, prática, revisão e projeto.

### Ao final desta fase, espera-se que eu saiba

Criar um projeto simples do zero, organizar arquivos, usar terminal, instalar bibliotecas, versionar código com Git e publicar no GitHub sem depender completamente de um tutorial.

---

## Fase 1: Python básico

Esta fase tem como objetivo formar a base da programação em Python. Aqui o foco é sintaxe, lógica e controle de fluxo.

### Checklist

- [ ] Entender variáveis.
- [ ] Entender tipos primitivos: `int`, `float`, `str`, `bool`.
- [ ] Fazer conversão de tipos.
- [ ] Usar operadores aritméticos.
- [ ] Usar operadores relacionais.
- [ ] Usar operadores lógicos.
- [ ] Usar `if`, `elif` e `else`.
- [ ] Usar `for`.
- [ ] Usar `while`.
- [ ] Usar `break`.
- [ ] Usar `continue`.
- [ ] Manipular strings.
- [ ] Usar f-strings.
- [ ] Criar listas.
- [ ] Acessar elementos de listas.
- [ ] Percorrer listas.
- [ ] Usar fatiamento.
- [ ] Usar tuplas.
- [ ] Usar dicionários.
- [ ] Usar conjuntos.
- [ ] Entender mutabilidade.
- [ ] Criar funções.
- [ ] Usar parâmetros.
- [ ] Usar retorno com `return`.
- [ ] Entender escopo de variáveis.
- [ ] Tratar erros com `try` e `except`.
- [ ] Ler arquivos `.txt`.
- [ ] Escrever arquivos `.txt`.
- [ ] Ler arquivos `.csv` simples.
- [ ] Usar módulos da biblioteca padrão.
- [ ] Resolver exercícios de lógica.

### Ao final desta fase, espera-se que eu saiba

Criar scripts simples em Python, resolver problemas de lógica, manipular listas e dicionários, criar funções e estruturar pequenos programas.

---

## Fase 2: Python intermediário, organização de código e POO

Nesta fase, o objetivo é sair do código puramente procedural e começar a escrever programas mais organizados, reutilizáveis e próximos de um padrão profissional.

### Checklist

- [ ] Usar list comprehension.
- [ ] Usar dictionary comprehension.
- [ ] Usar `enumerate`.
- [ ] Usar `zip`.
- [ ] Usar `sorted`.
- [ ] Usar `lambda` em casos simples.
- [ ] Entender funções como objetos.
- [ ] Separar código em múltiplos arquivos.
- [ ] Criar módulos próprios.
- [ ] Importar módulos próprios.
- [ ] Entender pacotes em Python.
- [ ] Entender tratamento de exceções com mais profundidade.
- [ ] Criar exceções personalizadas em nível básico.
- [ ] Usar type hints básicos.
- [ ] Entender `list[str]`, `dict[str, int]`, `tuple`, `Optional`.
- [ ] Entender classes.
- [ ] Entender objetos.
- [ ] Criar atributos.
- [ ] Criar métodos.
- [ ] Usar `__init__`.
- [ ] Entender `self`.
- [ ] Entender encapsulamento em nível básico.
- [ ] Entender composição.
- [ ] Entender herança.
- [ ] Entender polimorfismo em nível básico.
- [ ] Saber quando não usar POO.
- [ ] Criar classes para representar entidades reais.
- [ ] Criar projetos pequenos com múltiplas classes.
- [ ] Usar `pytest` em nível inicial.
- [ ] Escrever funções testáveis.
- [ ] Aplicar nomes claros para variáveis, funções e classes.
- [ ] Refatorar código repetitivo.

### Ao final desta fase, espera-se que eu saiba

Criar programas Python mais organizados, dividir responsabilidades, usar classes quando fizer sentido, criar módulos próprios e escrever código mais legível e reutilizável.

---

## Fase 3: Fundamentos de banco de dados e modelagem

Esta fase deve vir antes do SQL pesado. Na prática profissional, primeiro entendemos o problema, modelamos os dados e depois implementamos o banco.

### 3.1 Conceitos fundamentais

- [ ] Entender o que é banco de dados.
- [ ] Entender o que é SGBD.
- [ ] Entender diferença entre dado, informação e conhecimento.
- [ ] Entender tabela.
- [ ] Entender linha/registro.
- [ ] Entender coluna/campo.
- [ ] Entender domínio de atributo.
- [ ] Entender esquema do banco.
- [ ] Entender instância do banco.
- [ ] Entender integridade dos dados.
- [ ] Entender restrições de integridade.
- [ ] Entender redundância.
- [ ] Entender inconsistência.
- [ ] Entender banco transacional.
- [ ] Entender banco analítico.
- [ ] Entender diferença entre OLTP e OLAP em nível inicial.

### 3.2 Modelo conceitual

- [ ] Entender o que é modelo conceitual.
- [ ] Entender entidade.
- [ ] Entender conjunto de entidades.
- [ ] Entender entidade forte.
- [ ] Entender entidade fraca.
- [ ] Entender atributo.
- [ ] Entender atributo simples.
- [ ] Entender atributo composto.
- [ ] Entender atributo monovalorado.
- [ ] Entender atributo multivalorado.
- [ ] Entender atributo derivado.
- [ ] Entender atributo identificador.
- [ ] Entender relacionamento.
- [ ] Entender grau de relacionamento.
- [ ] Entender relacionamento binário.
- [ ] Entender relacionamento ternário.
- [ ] Entender relacionamento n-ário.
- [ ] Entender auto-relacionamento ou relacionamento recursivo.
- [ ] Entender papel da entidade em um relacionamento.
- [ ] Entender cardinalidade.
- [ ] Entender cardinalidade 1:1.
- [ ] Entender cardinalidade 1:N.
- [ ] Entender cardinalidade N:N.
- [ ] Entender cardinalidade mínima e máxima.
- [ ] Entender participação obrigatória.
- [ ] Entender participação opcional.
- [ ] Entender participação total.
- [ ] Entender participação parcial.
- [ ] Entender entidade associativa.
- [ ] Entender agregação, caso usada na disciplina.
- [ ] Entender especialização.
- [ ] Entender generalização.
- [ ] Entender herança em modelo entidade-relacionamento.
- [ ] Criar DER.
- [ ] Ler DERs criados por outras pessoas.
- [ ] Representar regras de negócio no modelo conceitual.

### 3.3 Relacionamentos avançados

- [ ] Modelar auto-relacionamento.
- [ ] Modelar relacionamento ternário.
- [ ] Modelar relacionamento n-ário.
- [ ] Identificar quando um relacionamento ternário não deve ser quebrado em relacionamentos binários.
- [ ] Identificar papéis diferentes de uma mesma entidade no relacionamento.
- [ ] Representar hierarquias com auto-relacionamento.
- [ ] Representar supervisão, dependência ou composição entre registros da mesma entidade.
- [ ] Representar relacionamentos com atributos próprios.
- [ ] Identificar quando um relacionamento deve virar entidade associativa.

### 3.4 Modelo lógico relacional

- [ ] Entender o que é modelo lógico.
- [ ] Transformar entidades em tabelas.
- [ ] Transformar atributos em colunas.
- [ ] Definir chaves primárias.
- [ ] Definir chaves estrangeiras.
- [ ] Definir chaves candidatas.
- [ ] Definir chave natural.
- [ ] Definir chave substituta/surrogate key.
- [ ] Resolver relacionamento 1:1.
- [ ] Resolver relacionamento 1:N.
- [ ] Resolver relacionamento N:N.
- [ ] Transformar relacionamento N:N em tabela associativa.
- [ ] Mapear entidade fraca.
- [ ] Mapear atributo multivalorado.
- [ ] Mapear auto-relacionamento.
- [ ] Mapear relacionamento ternário.
- [ ] Mapear especialização/generalização.
- [ ] Definir obrigatoriedade de campos.
- [ ] Definir unicidade.
- [ ] Definir integridade referencial.
- [ ] Evitar colunas repetitivas como `telefone1`, `telefone2`, `telefone3`.
- [ ] Criar tabelas de domínio/catálogo quando necessário.

### 3.5 Modelo físico

- [ ] Entender o que é modelo físico.
- [ ] Escolher tipos de dados adequados.
- [ ] Definir nomes de tabelas.
- [ ] Definir nomes de colunas.
- [ ] Definir `PRIMARY KEY`.
- [ ] Definir `FOREIGN KEY`.
- [ ] Definir `NOT NULL`.
- [ ] Definir `UNIQUE`.
- [ ] Definir `DEFAULT`.
- [ ] Definir `CHECK`.
- [ ] Definir ações de `ON DELETE`.
- [ ] Definir ações de `ON UPDATE`.
- [ ] Pensar em índices básicos.
- [ ] Pensar em performance inicial.
- [ ] Criar script físico de criação do banco.
- [ ] Criar script de inserção de dados de teste.
- [ ] Validar se o banco respeita as regras de negócio.

### 3.6 Normalização

- [ ] Entender anomalia de inserção.
- [ ] Entender anomalia de atualização.
- [ ] Entender anomalia de exclusão.
- [ ] Entender dependência funcional.
- [ ] Entender dependência parcial.
- [ ] Entender dependência transitiva.
- [ ] Aplicar Primeira Forma Normal, 1FN.
- [ ] Aplicar Segunda Forma Normal, 2FN.
- [ ] Aplicar Terceira Forma Normal, 3FN.
- [ ] Conhecer BCNF.
- [ ] Conhecer 4FN em nível básico.
- [ ] Saber quando normalizar.
- [ ] Saber quando desnormalizar pode ser aceitável.
- [ ] Identificar tabelas com responsabilidades misturadas.
- [ ] Identificar atributos que deveriam estar em outra tabela.

### Ao final desta fase, espera-se que eu saiba

Analisar um cenário real, identificar entidades, atributos, relacionamentos, cardinalidades e regras de negócio, criar um DER, transformar o modelo conceitual em modelo lógico e preparar uma estrutura física coerente para implementação em SQL.

---

## Fase 4: SQL para criação e manipulação de dados

Depois de modelar, vem a implementação do banco. Aqui o foco é usar SQL para criar e alterar estruturas e manipular registros.

### Checklist

- [ ] Entender o que é SQL.
- [ ] Entender diferença entre DDL, DML, DQL, DCL e TCL.
- [ ] Criar banco de dados.
- [ ] Criar tabelas com `CREATE TABLE`.
- [ ] Escolher tipos de dados.
- [ ] Criar chaves primárias.
- [ ] Criar chaves estrangeiras.
- [ ] Usar `NOT NULL`.
- [ ] Usar `UNIQUE`.
- [ ] Usar `DEFAULT`.
- [ ] Usar `CHECK`.
- [ ] Usar `SERIAL` ou `IDENTITY`, dependendo do SGBD.
- [ ] Inserir dados com `INSERT`.
- [ ] Atualizar dados com `UPDATE`.
- [ ] Remover dados com `DELETE`.
- [ ] Alterar tabelas com `ALTER TABLE`.
- [ ] Remover tabelas com `DROP TABLE`.
- [ ] Esvaziar tabelas com `TRUNCATE`.
- [ ] Criar scripts SQL organizados.
- [ ] Criar dados fictícios para teste.
- [ ] Entender transações em nível básico.
- [ ] Usar `BEGIN`, `COMMIT` e `ROLLBACK`.
- [ ] Entender integridade referencial na prática.

### Ao final desta fase, espera-se que eu saiba

Transformar um modelo físico em um banco real, criando tabelas, chaves, restrições e dados de teste com SQL.

---

## Fase 5: SQL para consulta e análise

Aqui o foco muda: não é apenas criar o banco, mas extrair informação dele. Essa fase é essencial para Ciência de Dados.

### Checklist

- [ ] Usar `SELECT`.
- [ ] Usar `FROM`.
- [ ] Usar `WHERE`.
- [ ] Usar `ORDER BY`.
- [ ] Usar `LIMIT`.
- [ ] Usar operadores relacionais.
- [ ] Usar operadores lógicos.
- [ ] Usar `IN`.
- [ ] Usar `LIKE`.
- [ ] Usar `BETWEEN`.
- [ ] Usar `IS NULL`.
- [ ] Usar `IS NOT NULL`.
- [ ] Usar `DISTINCT`.
- [ ] Usar funções agregadas: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- [ ] Usar `ROUND`.
- [ ] Usar `GROUP BY`.
- [ ] Usar `HAVING`.
- [ ] Usar `CASE WHEN`.
- [ ] Trabalhar com datas.
- [ ] Usar `EXTRACT`.
- [ ] Usar `DATE_PART`.
- [ ] Usar `TO_CHAR`.
- [ ] Fazer `INNER JOIN`.
- [ ] Fazer `LEFT JOIN`.
- [ ] Fazer `RIGHT JOIN`.
- [ ] Fazer `FULL JOIN`.
- [ ] Entender diferença entre filtro no `ON` e filtro no `WHERE`.
- [ ] Entender o impacto de `NULL` em joins.
- [ ] Usar subconsultas.
- [ ] Usar CTEs com `WITH`.
- [ ] Criar views.
- [ ] Usar funções de janela em nível inicial.
- [ ] Usar `ROW_NUMBER`.
- [ ] Usar `RANK`.
- [ ] Usar `PARTITION BY`.
- [ ] Criar consultas para perguntas de negócio.
- [ ] Otimizar consultas simples.
- [ ] Ler planos de execução em nível básico.

### Ao final desta fase, espera-se que eu saiba

Responder perguntas de negócio usando SQL, cruzar tabelas, agrupar dados, calcular métricas, lidar com datas, usar joins corretamente e escrever consultas analíticas com clareza.

---

## Fase 6: Python para dados — NumPy, pandas e análise exploratória

Nesta fase, Python começa a ser usado diretamente para análise de dados.

### Checklist

- [ ] Entender o papel do NumPy.
- [ ] Criar arrays NumPy.
- [ ] Fazer operações vetorizadas.
- [ ] Entender diferença entre lista Python e array NumPy.
- [ ] Entender o papel do pandas.
- [ ] Criar `Series`.
- [ ] Criar `DataFrame`.
- [ ] Ler arquivos CSV.
- [ ] Ler arquivos Excel.
- [ ] Ler arquivos JSON.
- [ ] Ler dados de banco SQL.
- [ ] Usar `head`.
- [ ] Usar `tail`.
- [ ] Usar `info`.
- [ ] Usar `describe`.
- [ ] Usar `shape`.
- [ ] Selecionar colunas.
- [ ] Selecionar linhas.
- [ ] Filtrar dados.
- [ ] Criar colunas derivadas.
- [ ] Remover colunas.
- [ ] Renomear colunas.
- [ ] Tratar valores ausentes.
- [ ] Tratar duplicatas.
- [ ] Converter tipos de dados.
- [ ] Trabalhar com datas no pandas.
- [ ] Usar `groupby`.
- [ ] Usar agregações.
- [ ] Usar `merge`.
- [ ] Usar `join`.
- [ ] Usar `concat`.
- [ ] Usar `pivot_table`.
- [ ] Ordenar dados.
- [ ] Criar rankings.
- [ ] Identificar outliers.
- [ ] Calcular correlação.
- [ ] Fazer análise exploratória de dados.
- [ ] Exportar dados tratados.
- [ ] Conectar pandas com PostgreSQL.
- [ ] Criar notebooks organizados.

### Ao final desta fase, espera-se que eu saiba

Carregar bases de dados, limpar dados, transformar colunas, agregar informações, cruzar tabelas e realizar análises exploratórias usando Python.

---

## Fase 7: Estatística e probabilidade para dados

Estatística é uma das bases mais importantes para Ciência de Dados. Sem ela, o risco é apenas gerar gráficos e modelos sem interpretação correta.

### Checklist

- [ ] Entender população e amostra.
- [ ] Entender variável qualitativa.
- [ ] Entender variável quantitativa.
- [ ] Entender variável discreta.
- [ ] Entender variável contínua.
- [ ] Calcular média.
- [ ] Calcular mediana.
- [ ] Calcular moda.
- [ ] Calcular amplitude.
- [ ] Calcular variância.
- [ ] Calcular desvio padrão.
- [ ] Calcular quartis.
- [ ] Calcular percentis.
- [ ] Entender distribuição de frequência.
- [ ] Entender histograma.
- [ ] Entender boxplot.
- [ ] Identificar outliers.
- [ ] Entender correlação.
- [ ] Diferenciar correlação e causalidade.
- [ ] Entender probabilidade básica.
- [ ] Entender eventos independentes.
- [ ] Entender eventos dependentes.
- [ ] Entender probabilidade condicional.
- [ ] Entender Teorema de Bayes em nível inicial.
- [ ] Entender distribuição normal.
- [ ] Entender distribuição binomial.
- [ ] Entender distribuição de Poisson.
- [ ] Entender amostragem.
- [ ] Entender viés amostral.
- [ ] Entender intervalo de confiança.
- [ ] Entender teste de hipótese.
- [ ] Entender hipótese nula.
- [ ] Entender hipótese alternativa.
- [ ] Entender valor-p.
- [ ] Entender erro tipo I.
- [ ] Entender erro tipo II.
- [ ] Entender teste t.
- [ ] Entender qui-quadrado.
- [ ] Entender ANOVA em nível básico.
- [ ] Entender A/B testing.
- [ ] Entender regressão linear do ponto de vista estatístico.

### Ao final desta fase, espera-se que eu saiba

Interpretar dados com mais rigor, entender variação, incerteza, distribuição, correlação, amostragem e testes estatísticos básicos.

---

## Fase 8: Visualização de dados e comunicação

Um cientista de dados precisa comunicar resultados. Não basta gerar análise; é necessário explicar o que foi descoberto, com clareza e responsabilidade.

### Checklist

- [ ] Entender quando usar gráfico de barras.
- [ ] Entender quando usar gráfico de linhas.
- [ ] Entender quando usar gráfico de dispersão.
- [ ] Entender quando usar histograma.
- [ ] Entender quando usar boxplot.
- [ ] Entender quando usar mapa de calor.
- [ ] Evitar gráficos enganosos.
- [ ] Usar títulos claros.
- [ ] Usar eixos bem definidos.
- [ ] Usar legendas corretamente.
- [ ] Criar gráficos com Matplotlib.
- [ ] Criar gráficos com Seaborn.
- [ ] Criar gráficos com Plotly em nível básico.
- [ ] Criar dashboards simples.
- [ ] Aprender Power BI ou Tableau.
- [ ] Criar medidas e indicadores em dashboard.
- [ ] Explicar métricas para público não técnico.
- [ ] Criar storytelling com dados.
- [ ] Separar fato, interpretação e recomendação.
- [ ] Explicar limitações da análise.
- [ ] Criar relatórios analíticos.
- [ ] Apresentar resultados com objetividade.

### Ao final desta fase, espera-se que eu saiba

Transformar análises em gráficos, dashboards, relatórios e apresentações compreensíveis para pessoas técnicas e não técnicas.

---

## Fase 9: Machine Learning clássico

Machine Learning deve vir depois de Python, SQL, pandas e estatística. Antes disso, o risco é apenas decorar comandos sem entender os resultados.

### Checklist

- [ ] Entender o que é Machine Learning.
- [ ] Diferenciar aprendizado supervisionado e não supervisionado.
- [ ] Entender features.
- [ ] Entender target.
- [ ] Entender treino, validação e teste.
- [ ] Entender overfitting.
- [ ] Entender underfitting.
- [ ] Criar baseline.
- [ ] Usar Scikit-learn.
- [ ] Treinar regressão linear.
- [ ] Treinar regressão logística.
- [ ] Treinar KNN.
- [ ] Treinar árvore de decisão.
- [ ] Treinar Random Forest.
- [ ] Treinar Gradient Boosting.
- [ ] Conhecer XGBoost.
- [ ] Conhecer LightGBM.
- [ ] Conhecer CatBoost.
- [ ] Usar K-means.
- [ ] Usar PCA em nível básico.
- [ ] Fazer pré-processamento.
- [ ] Tratar variáveis categóricas.
- [ ] Tratar variáveis numéricas.
- [ ] Normalizar dados.
- [ ] Padronizar dados.
- [ ] Criar pipelines no Scikit-learn.
- [ ] Fazer validação cruzada.
- [ ] Ajustar hiperparâmetros.
- [ ] Avaliar modelos de regressão com MAE.
- [ ] Avaliar modelos de regressão com MSE.
- [ ] Avaliar modelos de regressão com RMSE.
- [ ] Avaliar modelos de regressão com R².
- [ ] Avaliar classificação com acurácia.
- [ ] Avaliar classificação com precisão.
- [ ] Avaliar classificação com recall.
- [ ] Avaliar classificação com F1-score.
- [ ] Avaliar classificação com ROC-AUC.
- [ ] Interpretar matriz de confusão.
- [ ] Fazer feature engineering.
- [ ] Fazer feature selection.
- [ ] Interpretar importância de variáveis.
- [ ] Conhecer SHAP em nível inicial.

### Ao final desta fase, espera-se que eu saiba

Construir modelos preditivos básicos e intermediários, avaliar corretamente os resultados e explicar o comportamento do modelo.

---

## Fase 10: Projetos práticos e portfólio

Projetos são essenciais para transformar estudo em evidência prática. Um bom portfólio deve mostrar raciocínio, organização, código, análise e comunicação.

### Checklist

- [ ] Criar projeto de análise exploratória com pandas.
- [ ] Criar projeto de SQL com perguntas de negócio.
- [ ] Criar projeto de modelagem de banco de dados.
- [ ] Criar dashboard em Power BI, Tableau ou Streamlit.
- [ ] Criar projeto de regressão.
- [ ] Criar projeto de classificação.
- [ ] Criar projeto de clusterização.
- [ ] Criar projeto de previsão de vendas.
- [ ] Criar projeto de churn.
- [ ] Criar projeto com dados públicos reais.
- [ ] Criar projeto com dados extraídos de API.
- [ ] Criar projeto com banco PostgreSQL.
- [ ] Criar projeto de ponta a ponta.
- [ ] Criar README profissional.
- [ ] Explicar problema de negócio.
- [ ] Explicar origem dos dados.
- [ ] Explicar tratamento dos dados.
- [ ] Explicar decisões técnicas.
- [ ] Explicar métricas utilizadas.
- [ ] Explicar limitações do projeto.
- [ ] Publicar projetos no GitHub.
- [ ] Organizar portfólio com 4 a 6 projetos fortes.

### Ao final desta fase, espera-se que eu tenha

Um portfólio com projetos que demonstrem domínio de Python, SQL, modelagem, análise exploratória, visualização, estatística e Machine Learning.

---

## Fase 11: Engenharia de dados para cientistas de dados

Um cientista de dados não precisa necessariamente ser engenheiro de dados, mas precisa entender como os dados são coletados, armazenados, processados e disponibilizados.

### Checklist

- [ ] Entender ETL.
- [ ] Entender ELT.
- [ ] Criar pipelines simples em Python.
- [ ] Consumir APIs.
- [ ] Extrair dados de arquivos.
- [ ] Extrair dados de banco SQL.
- [ ] Salvar dados tratados em banco.
- [ ] Criar scripts de carga.
- [ ] Automatizar tarefas simples.
- [ ] Usar Docker em nível básico.
- [ ] Rodar PostgreSQL com Docker.
- [ ] Entender volumes em Docker.
- [ ] Entender variáveis de ambiente.
- [ ] Entender Data Warehouse.
- [ ] Entender Data Lake.
- [ ] Entender Data Lakehouse em nível conceitual.
- [ ] Entender modelagem dimensional.
- [ ] Entender tabela fato.
- [ ] Entender tabela dimensão.
- [ ] Criar modelo estrela simples.
- [ ] Entender particionamento de dados.
- [ ] Entender arquivos Parquet.
- [ ] Entender Airflow em nível básico.
- [ ] Entender Spark em nível inicial.
- [ ] Entender qualidade de dados.
- [ ] Criar validações de dados.
- [ ] Conhecer BigQuery, Redshift ou Snowflake em nível inicial.

### Ao final desta fase, espera-se que eu saiba

Criar fluxos simples de coleta, tratamento, armazenamento e validação de dados, além de entender a estrutura básica de ambientes analíticos.

---

## Fase 12: Deploy, APIs e MLOps

Nesta fase, o objetivo é entender como modelos e análises saem do notebook e viram algo utilizável.

### Checklist

- [ ] Salvar modelos com `joblib`.
- [ ] Salvar modelos com `pickle`.
- [ ] Criar API simples com FastAPI.
- [ ] Criar aplicação simples com Streamlit.
- [ ] Criar endpoint de inferência.
- [ ] Enviar dados para o modelo via API.
- [ ] Receber previsão do modelo.
- [ ] Containerizar aplicação com Docker.
- [ ] Criar `Dockerfile`.
- [ ] Criar `docker-compose.yml`.
- [ ] Entender ambiente de desenvolvimento.
- [ ] Entender ambiente de produção.
- [ ] Criar logs.
- [ ] Criar testes básicos para pipeline.
- [ ] Entender versionamento de modelos.
- [ ] Entender versionamento de dados.
- [ ] Usar MLflow em nível básico.
- [ ] Criar pipeline de treino.
- [ ] Criar pipeline de inferência.
- [ ] Monitorar métricas do modelo.
- [ ] Entender data drift.
- [ ] Entender model drift.
- [ ] Entender CI/CD em nível inicial.
- [ ] Fazer deploy simples em cloud ou servidor.

### Ao final desta fase, espera-se que eu saiba

Transformar um modelo em uma solução utilizável, seja como API, aplicação, dashboard ou serviço simples.

---

## Fase 13: Deep Learning, NLP e IA generativa

Esta fase é avançada. Deve vir depois de uma boa base em Python, estatística, Machine Learning e álgebra linear.

### Checklist

- [ ] Entender redes neurais artificiais.
- [ ] Entender neurônio artificial.
- [ ] Entender função de ativação.
- [ ] Entender forward propagation.
- [ ] Entender backpropagation conceitualmente.
- [ ] Entender função de perda.
- [ ] Usar PyTorch ou TensorFlow.
- [ ] Criar rede neural simples.
- [ ] Entender embeddings.
- [ ] Entender CNNs para imagens.
- [ ] Entender RNNs e LSTMs historicamente.
- [ ] Entender Transformers.
- [ ] Entender mecanismo de atenção.
- [ ] Entender NLP básico.
- [ ] Entender tokenização.
- [ ] Entender vetorização de texto.
- [ ] Criar classificador de texto simples.
- [ ] Usar modelos pré-treinados.
- [ ] Fazer fine-tuning básico.
- [ ] Entender LLMs em nível prático.
- [ ] Usar APIs de modelos de linguagem.
- [ ] Criar aplicação com RAG.
- [ ] Entender embeddings para busca semântica.
- [ ] Entender bancos vetoriais em nível básico.
- [ ] Avaliar respostas de modelos generativos.
- [ ] Entender riscos de alucinação.
- [ ] Entender riscos de viés.
- [ ] Entender riscos de privacidade.

### Ao final desta fase, espera-se que eu saiba

Criar aplicações básicas com Deep Learning, NLP e IA generativa, entendendo quando essas técnicas fazem sentido e quais são seus limites.

---

## Fase 14: Matemática avançada para Machine Learning

Esta fase pode ser estudada em paralelo, mas deve ser aprofundada conforme os modelos ficarem mais complexos.

### Checklist

- [ ] Entender vetores.
- [ ] Entender matrizes.
- [ ] Fazer operações matriciais.
- [ ] Entender produto escalar.
- [ ] Entender norma de vetor.
- [ ] Entender distância euclidiana.
- [ ] Entender espaços vetoriais em nível básico.
- [ ] Entender autovalores e autovetores conceitualmente.
- [ ] Entender derivadas.
- [ ] Entender derivadas parciais.
- [ ] Entender gradiente.
- [ ] Entender regra da cadeia.
- [ ] Entender otimização.
- [ ] Entender gradiente descendente.
- [ ] Entender função de custo.
- [ ] Entender regularização L1.
- [ ] Entender regularização L2.
- [ ] Entender máxima verossimilhança.
- [ ] Entender entropia.
- [ ] Entender cross-entropy.
- [ ] Entender KL divergence em nível conceitual.
- [ ] Entender estatística bayesiana básica.

### Ao final desta fase, espera-se que eu saiba

Compreender melhor o funcionamento interno dos algoritmos, indo além do uso superficial das bibliotecas.

---

## Fase 15: Evolução para nível pleno

O nível pleno exige autonomia. A pessoa já não depende de tutoriais para cada passo e consegue lidar com problemas reais com certo grau de ambiguidade.

### Checklist

- [ ] Escolher técnica adequada para cada problema.
- [ ] Saber quando não usar Machine Learning.
- [ ] Entender custo-benefício de uma solução.
- [ ] Definir métricas de sucesso.
- [ ] Criar experimentos bem definidos.
- [ ] Comparar modelos corretamente.
- [ ] Lidar com dados incompletos.
- [ ] Lidar com dados inconsistentes.
- [ ] Investigar problemas sem depender de tutorial.
- [ ] Trabalhar com stakeholders.
- [ ] Transformar perguntas vagas em análises objetivas.
- [ ] Documentar decisões técnicas.
- [ ] Criar pipelines reutilizáveis.
- [ ] Melhorar performance de consultas SQL.
- [ ] Melhorar performance de código pandas.
- [ ] Criar projetos de ponta a ponta.
- [ ] Revisar código de dados.
- [ ] Explicar trade-offs técnicos.
- [ ] Priorizar entregas por impacto.

### Ao final desta fase, espera-se que eu saiba

Receber um problema relativamente aberto, estruturar a análise, buscar dados, modelar, testar, comunicar resultados e entregar uma solução funcional.

---

## Fase 16: Evolução para nível sênior

Senioridade não é apenas saber mais ferramentas. É tomar decisões melhores, orientar pessoas, evitar soluções ruins e gerar impacto real para o negócio.

### Checklist

- [ ] Transformar problemas de negócio em problemas analíticos.
- [ ] Priorizar projetos por impacto.
- [ ] Definir estratégia de dados.
- [ ] Avaliar riscos técnicos.
- [ ] Avaliar riscos de negócio.
- [ ] Liderar experimentos.
- [ ] Criar padrões de qualidade para projetos.
- [ ] Mentorar pessoas iniciantes.
- [ ] Revisar arquitetura de soluções de dados.
- [ ] Decidir entre regra de negócio, estatística, Machine Learning ou IA generativa.
- [ ] Negociar escopo com áreas não técnicas.
- [ ] Comunicar incerteza de forma clara.
- [ ] Medir impacto depois da entrega.
- [ ] Entender ética em dados.
- [ ] Entender privacidade.
- [ ] Entender governança de dados.
- [ ] Participar de decisões de produto.
- [ ] Conectar dados, tecnologia e resultado financeiro/operacional.
- [ ] Evitar complexidade desnecessária.
- [ ] Criar soluções sustentáveis.

### Ao final desta fase, espera-se que eu saiba

Atuar não apenas como executor técnico, mas como alguém capaz de orientar decisões estratégicas usando dados, liderar soluções e gerar impacto mensurável.

---

## Projetos recomendados por etapa

### Após Python básico

- [ ] Calculadora de orçamento pessoal.
- [ ] Sistema simples de cadastro em memória.
- [ ] Leitor e analisador de arquivos CSV.
- [ ] Pequeno sistema de estoque usando listas e dicionários.

### Após POO

- [ ] Sistema de biblioteca com classes.
- [ ] Sistema de pedidos com cliente, produto e pedido.
- [ ] Simulador de carrinho de compras.
- [ ] Projeto com módulos separados e testes básicos.

### Após modelagem de dados

- [ ] Modelo conceitual de sistema de vendas.
- [ ] Modelo lógico de biblioteca.
- [ ] DER de sistema acadêmico.
- [ ] Modelo com auto-relacionamento de funcionários e supervisores.
- [ ] Modelo com relacionamento ternário entre fornecedor, produto e projeto.

### Após SQL

- [ ] Banco de vendas com clientes, produtos, pedidos e itens.
- [ ] Consultas de faturamento.
- [ ] Consultas de clientes mais ativos.
- [ ] Consultas de produtos mais vendidos.
- [ ] Consultas usando joins, agrupamentos e datas.

### Após pandas

- [ ] Análise exploratória de vendas.
- [ ] Limpeza de base com dados ausentes.
- [ ] Análise de clientes.
- [ ] Análise de produtos.
- [ ] Relatório com gráficos e conclusões.

### Após estatística

- [ ] Análise de distribuição de vendas.
- [ ] Comparação entre grupos de clientes.
- [ ] Teste de hipótese simples.
- [ ] Análise de correlação entre variáveis.
- [ ] Simulação de A/B testing.

### Após Machine Learning

- [ ] Modelo de previsão de preços.
- [ ] Modelo de classificação de clientes.
- [ ] Modelo de churn.
- [ ] Modelo de previsão de vendas.
- [ ] Projeto completo com treino, avaliação e explicação.

### Após Engenharia de Dados

- [ ] Pipeline que consome API e salva no PostgreSQL.
- [ ] Pipeline que lê arquivos CSV, trata e salva em banco.
- [ ] Pipeline com Docker e PostgreSQL.
- [ ] Pipeline agendado com Airflow em nível básico.
- [ ] Projeto com dados em Parquet.

---

## Critérios para avançar entre fases

Não devo avançar apenas porque assisti aulas. Devo avançar quando conseguir aplicar.

### Para avançar de Python básico

- [ ] Consigo resolver exercícios sem copiar código.
- [ ] Consigo criar funções.
- [ ] Consigo manipular listas e dicionários.
- [ ] Consigo ler e escrever arquivos simples.

### Para avançar de modelagem

- [ ] Consigo sair de uma descrição textual e criar um DER.
- [ ] Consigo identificar entidades, atributos e relacionamentos.
- [ ] Consigo modelar cardinalidades.
- [ ] Consigo modelar auto-relacionamento.
- [ ] Consigo modelar relacionamento ternário.
- [ ] Consigo transformar modelo conceitual em modelo lógico.

### Para avançar de SQL

- [ ] Consigo criar tabelas com chaves e restrições.
- [ ] Consigo inserir dados de teste.
- [ ] Consigo fazer joins.
- [ ] Consigo agrupar dados.
- [ ] Consigo responder perguntas de negócio com consultas.

### Para avançar de pandas

- [ ] Consigo carregar uma base real.
- [ ] Consigo limpar dados.
- [ ] Consigo tratar nulos e duplicatas.
- [ ] Consigo agrupar e cruzar dados.
- [ ] Consigo gerar conclusões iniciais.

### Para avançar de estatística

- [ ] Consigo interpretar média, mediana e desvio padrão.
- [ ] Consigo entender distribuição.
- [ ] Consigo diferenciar correlação de causalidade.
- [ ] Consigo interpretar teste de hipótese básico.

### Para avançar de Machine Learning

- [ ] Consigo separar treino e teste.
- [ ] Consigo criar baseline.
- [ ] Consigo treinar modelos simples.
- [ ] Consigo avaliar modelos com métricas corretas.
- [ ] Consigo explicar limitações do modelo.

---

## Rotina de estudo sugerida

Considerando uma rotina de 5 a 6 dias por semana, com cerca de 5 horas por dia:

### Distribuição diária

- 2 horas de teoria
- 2 horas de prática
- 1 hora de revisão, projeto ou documentação

### Distribuição semanal

- 3 dias para conteúdo novo
- 2 dias para exercícios
- 1 dia para projeto ou revisão geral

### Regra principal

Todo tópico importante deve gerar algum entregável:

- código;
- consulta SQL;
- modelo de banco;
- notebook;
- gráfico;
- relatório;
- dashboard;
- modelo preditivo;
- README;
- projeto publicado.

---

## Observação final

Este roadmap não deve ser tratado como uma corrida. A base mais importante para Ciência de Dados é:

1. Python bem dominado;
2. modelagem de dados;
3. SQL forte;
4. pandas e análise exploratória;
5. estatística;
6. visualização e comunicação;
7. Machine Learning;
8. projetos reais.

Ferramentas como Spark, Airflow, cloud, MLOps, Deep Learning e IA generativa são importantes, mas devem entrar depois que a base estiver sólida.
