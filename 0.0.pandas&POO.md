 PANDAS — DOMÍNIO COMPLETO

A. Estruturas Base
    Series
    DataFrame
    Index
    MultiIndex
    Criação
    from dict
    from list
    from records
    read_csv
    read_excel
    read_json
    read_sql

B. Exploração de Dados
    head()
    tail()
    sample()
    info()
    describe()
    shape
    columns
    dtypes
    nunique()
    value_counts()

C. Seleção
    []
    .loc[]
    .iloc[]
    filtros booleanos
    múltiplas condições
    isin()
    query()

D. Limpeza
    isnull()
    notnull()
    fillna()
    dropna()
    replace()
    astype()
    duplicates
    drop_duplicates()
    strip()
    strings sujas
    datas inválidas

E. Transformação
    assign()
    apply()
    map()
    replace()
    rename()
    sort_values()
    sort_index()
    reset_index()
    set_index()

F. Colunas e Features
    criar colunas
    colunas condicionais
    np.where
    pd.cut
    pd.qcut

G. Agrupamento
    groupby()
    agg()
    named agg
    transform()
    filter()
    pivot_table()

H. Junções
    merge()
    join()
    concat()
    Tipos:
        inner
        left
        right
        outer
    Problemas reais:
        duplicidade
        cardinalidade
        chaves quebradas

I. Datas e Tempo
    to_datetime()
    dt.year
    dt.month
    dt.day
    dt.weekday
    resample()
    rolling()
    timezone

J. Strings
    str.lower()
    str.upper()
    str.contains()
    str.extract()
    regex

K. Performance
    vectorization
    evitar loops
    categorical dtype
    memory usage
    chunk reading
    usecols
    parse_dates

L. Avançado
    method chaining
    pipe()
    MultiIndex
    explode()
    melt()
    stack()
    unstack()
    crosstab()
    rolling windows
    expanding windows

M. Exportação
    to_csv
    to_excel
    to_json
    to_parquet
    to_sql

N. Pandas Profissional
    pipelines reproduzíveis
    funções puras de transformação
    validação antes/depois
    testes de DataFrame
    logs
    schemas

4. NUMPY (OBRIGATÓRIO INDIRETO)
    ndarray
    reshape
    broadcasting
    slicing
    máscaras booleanas
    agregações
    arrays vetorizados
    random

=================================================

Base
    classe
    objeto
    instância
    atributo
    método
    self
Inicialização
    init
Representação
    str
    repr
Encapsulamento
    atributos públicos
    _protegido
    __privado
    getters/setters
    @property
Herança
    classe pai
    classe filha
    super()
Polimorfismo
    sobrescrita
    mesma interface
Abstração
    classes abstratas
    ABC
    abstractmethod
Composição (muito importante)
    objeto dentro de objeto

Exemplo:
Pipeline contém Extractor, Transformer, Loader

Métodos especiais
    len
    iter
    call
    eq
    lt
    Classmethod / Staticmethod
    @classmethod
    @staticmethod
    Dataclasses
    @dataclass
    frozen
    default_factory

SOLID em Python
    responsabilidade única
    aberto/fechado
    substituição
    interface segregation
    dependency inversion