# pequeno script da aula que teve como foco dar a introdução e revisar alguns fundamentos do pythonn

# STRINGS EM PYTHON: MANIPULAÇÃO BÁSICA

# concatenação (+)
# combina duas ou mais strings para formar uma nova
nome = "Marlon"
sobrenome = "da Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo) # saída: Marlon da Silva
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# repetição (*)
# repete uma string um número especificado de vezes
estrela = "*" * 5
print(estrela) # saída: *****
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
#  indexação
# acessa um caractere específico usando sua posição (índice)
fruta = "Maçã"
primeira_letra = fruta[0]
ultima_letra =  fruta[-1]
print(primeira_letra, ultima_letra) # saída: M ã
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# Fatiamento (Slicing)
# extrai uma porção (sub-string) de uma string, definindo um início e um fim
palavra = "Python"
sub = palavra[1:4]
print(sub) # saída: yht

# MÉTODOS ÚTEIS

# .upper()
# converte todos os caracteres para maiúsculas
print("olá".upper()) # saída: OLÁ
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# .strip()
# remove espaços em branco do início e do fim da string
print(" olá ".strip()) # olá (sem os espaços)
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# .lower()
# converte todos os caracteres para minúsculas
print("MUNDO".lower()) # saída: mundo
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# .replace()
# substitui ocorrências de uma sub-string por outra
print("laranja".replace("a", "o")) # saída: loronjo

# FUNÇÕES MATEMÁTICAS NATIVAS
# python oferece um conjunto robusto de funções matemáticas embutidas que facilitam a manipulação e o cálculo de números

# .round()
# arredondamento
# arrenda um número para o inteiro mais próximo ou para o um número específico de casas decimais
print(round(3.14149, 2)) # saída: 3.14
print(round(7.8)) # saída: 8
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# abs()
# valor absoluto
# retorna o valor absoluto de um número, removendo qualquer sinal negativo
print(abs(-10)) # saída: 10
print(abs(5)) # saída: 5

# OPERADORES ARITMÉTICOS EM PYTHON
# os operadores aritméticos são símbolos especias usados para realizar cálculos matemáticos em valores (operandos)

# (+) adição
# soma dois valores
print(5 + 3) # saída: 8
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (-) subtração
# subtrai o segundo valor do primeiro
print(10 - 4) # saída: 6
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (*) multiplicação
# multiplica dois valores
print(6 * 2) # saída: 12
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (/) divisão
# divide o primeiro valor pelo segundo, retornando um float
print(10 / 3) # saída: 3.33... (o resultado é uma dizima períodica simples)
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (//) divisão inteira
# divide e retorna apenas a parte inteira do resultado
print(10 // 3) # saída: 3
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (%) módulo ou resto
# retorna o resto da divisão
print(10 % 3) # saída: 1
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (**) exponenciação
# eleva um número à potência de outro
print(2 ** 3) # saída: 8

# ORDEM DE PRECECÊNCIA (PARÊNTESES)
# sem parênteses = ordem padrão
print(2 + 3 * 4) # saída: 14
# python calcula 3 * 4
# depois ele pega o resultado da operação e continua o cálculo da seguinte forma: 2 + 12, resultando 14
# quando não usamos parênteses, python segue rigorosamente a ordem de precedência

# com parênteses = prioridade explícita
print((2 + 3) * 4) # saída: 20
# python calcula primeiro o que está dentro dos parênteses (2 + 3)
# depois ele pega o resultado da operação e continua o cálculo da seguinte forma: 5 * 4, resultando 20
# ao adicionar parênteses, forçamos a operação dentro delas a ser avalida primeiro, alterando o fluxo de cálculo da expressão

# OPERADORES DE COMPARAÇÃO
# os operadores de comparação avaliam a relação entre dois valores, retornando um resultado booleando: True (verdadeiro) ou False (falso)

# (==) igual a
# verifica se dois valores são idênticos
print(5 == 5) # saída: True
print(5 == 3) # saída: False
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
#  (!=) diferente de
# verifica se dos valores são distintos
print(5 != 5) # saída: False
print(5 != 3) # saída: True
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (>) maior que
# verifica se o valor da esquerda é estritamente maior
print(5 > 5) # saída: False
print(5 > 3) # saída: True
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (<) menor que
# verifica se o valor da esquerda é estritamente menor
print(5 < 3) # saída: False
print(2 < 3) # saída: True
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (>=) maior ou igual
# verifica se o valor da esquerda é maior ou igual
print(5 >= 3) # saída: True
print(5 >= 10) # saída: False
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (<=) menor ou igual
# verifica se o valor da esquerda é menor ou igual
print(5 <= 5) # saída: True
print(8 <= 3) # saída: False

# CÓDIGO NA PRÁTICA
vendas = 15000
meta = 10000

print(vendas > meta) # saída: True
print(vendas < meta) # saída: False
print(vendas == meta) # saída: False

# aplicação real: verificar se a meta foi atingida
if (vendas > meta):
    print("Meta superada! ✓")

# OPERADORES LÓGICOS
# os operadores lógicos permitem combinar expressões booleanas, resultando em um único valor lógico (True ou False)

# (and) E lógico
# ammbas as condições devem ser verdadeiras
print(True and False) # saída: False
print(True and True) # saída: True
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (or) OU lógico
# pelo menos uma condição precisa ser verdadeira
print(True or False) # saída: True
print(True or True) # saída: True
# ------------------------- # ------------------------- # ------------------------- # ------------------------- #
# (not) NÃO lógico
# inverte o valor booleano da condição
print(not True) # saída: False
print(not False) # saída: True

# LISTAS - A ESTRUTURA BASE
# uma lista em python é uma sequência ordenada e mutável. pense nela como uma coluna do excel, mas com superpoderes
# conceito: indexação zero
# por que índice zero? herança de C e Unix: o índice representa o deslocamento em memória a partir do endereço base. 
# zero deslocamento = primeiro elemento

# criando e acessando uma lista
produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]

# índice começa em ZERO
print(produtos[0]) # saída: Notebook
print(produtos[1]) # saída: Mouse
print(produtos[-1]) # saída: Monitor (último elemento da lista, também conhecido como produtos[3])

# SLICING EM LISTAS
# sintaxe: lista[inicio:parada:passo]

vendas_semana = [120, 340, 210, 890, 450, 670, 300]
# pegar os dias úteis da semana (segunda a sexta = índices 0 a 4)
dias_uteis = vendas_semana[0:5]
print(dias_uteis) # [120, 340, 210, 890, 450]

# pegar só os 3 últimos dias da semana (fim de semana)
final_semana = vendas_semana[-3:]
print(final_semana) # [450, 670, 300]

# pegar de 2 em 2
pares = vendas_semana[::2]
print(pares) # [120, 210, 450, 300]

# slicing cria uma cópia rasa (shallow copy) - não modifica a lista original

# SLICING EM STRINGS

cnpj = "1234567800099"

# extraindo partes do CNPJ
raiz = cnpj[:8] # saída: 12345678
ordem = cnpj[8:12] # saída: 0001
digitos = cnpj[12:] # saída: 99

print(f"Raiz: {raiz} | Ordem: {ordem} | DV: {digitos}") # saída: Raiz: 12345678 | Ordem: 0001 | DV: 99

# MÉTODO .APPEND() - LISTAS DINÂMICAS
# o método .append() adiciona um elemento ao final de uma lista. é a forma mais comum de construir listas dinamicamente conforme novos dados chegam.

# simulando entrada de dados de vendas
vendas_do_dia = []

# adicionando conforme chegam
vendas_do_dia.append(1500)
vendas_do_dia.append(2300)
vendas_do_dia.append(870)
print(vendas_do_dia) #saída: [1500, 2300, 870]

# somando as vendas do dia e retornando o total
print(f"Total: R$ {sum(vendas_do_dia)}") # saída: Total: R$4670

# DICIONÁRIOS - CHAVE-VALOR
# o dicionário python (dict) é a estrutura mais próxima do JSON e bancos NoSQL. acesso por chave em tempo constante

# criando um dicionário de produto
produto = {
    "id": 101,
    "nome": "Notebook Pro",
    "preco": 4500.00,
    "estoque": 23
}

# acessando por chave
print(produto["nome"]) # saída: Notebook Pro
print(produto["preco"]) # saída: 4500.00

# adicionando uma nova chave
produto["categoria"] = "Eletrônicos"

# ACESSO POR NOMES (CHAVES)
# dicionários permitem que você organize e acesse seus dados usando nomes significativos (chaves), em vez de números de posição (índices).
# isso torna o código mais fácil de ler e entender, pois você pode referenciar diretamente o que precisa, como produto["nome",],
# que é muito mais intuitivo do que lembrar qual número corresponde ao nome

# ESTRUTURA IF - ELIF - ELSE
# a estrutura if - elif - else avalia as condições sequecialmente, de cima para baixo.
# assim que uma condição é verdadeira, o bloco de código é executado e o restante da estrutura é ignorado.
# se nenhuma condição for verdadeira, o bloco else (se presente) é executado.

# estrutura básica
if (1 > 2):
    print("Bom dia!") 
elif (2 > 3):
    print("Boa tarde!")
else:
    print("Boa noite!")

review_score = 5 # nota de 1 a 5

if (review_score == 5):
    print("EXCELENTE - Cliente Satisfeito")
elif (review_score == 4):
    print("BOM - Acompanhar Feedback")
else:
    print("CRÍTICO - Ação Imediata")

# CLEAN CODE
# o clean code é uma abordagem para escrever software que é fácil de ler, entender e manter
# priorizar a clareza é fundamental para a colaboração e a longevidade de qualquer projeto

# CÓDIGO CONFUSO
# if 1 > 2 and 2 > 3 and not 4:
#     if 1 == "ok" or "ko" == "bk":
#         print("Go!")

# CÓDIGO LIMPO
# nomeie condições complexas

# operacao_lucrativa = lucro > 0
# dentro_do_limite = volume < 100
# cliente_aprovado = not em_blacklist

# if operacao_lucrativa and dentro_do_limite:
#     if cliente_aprovado:
#         processar_venda()

# FUNÇÕES - ENCAPSULANDO REGRAS DE NEGÓCIO
# por que usar funções? uma regra de negócio escrita uma única vez em função é:
#  * testável isoladamente * reutilizável em  múltiplos pontos * fácil de atualizar sem quebrar o resto

# regra encapsulada em função
def classificar_margem(margem):
    """ classifica operação por margem """
    if (margem >= 30):
        return "Premium"
    if (margem >= 15):
        return "Saúdavel"
    if (margem >= 0): 
        return "Atenção"
    return "Prejuízo"

# reutilizando em qualquer contexto (fora da função)
classificar_margem(35) # saída: Premium
classificar_margem(5) # saída: Atenção

# O LOOP FOR
# por que loops importam?
# um loop for em python pode substituir centenas de linhas de VLOOKUP no Excel, aplicando a mesma transformação 
# a cada registro de forma consistente e auditável

# sintaxe e conceito
# use o for quando ireando sobre uma coleção definida

# iterar sobre qualquer sequência
for produto in produtos:
    print(f"Processando: {produto}")

# saída: Processando: Notebook
# saída: Processando: Mouse
# saída: Processando: Teclado
# saída: Processando: Monitor

# com enumerate (índice + valor)
for i, produto in enumerate(produtos):
    print(f"{i+1}. {produto}")

# saída: 1. Notebook
# saída: 2. Mouse
# saída: 3. Teclado
# saída: 4. Monitor

# O LOOP WHILE - CONDIÇÃO DE PARADA
# use o while quando o número de iterações não é conhecido previamente

vendas_diarias = [120, 340, 210, 890, 450]
meta_mensal = 2000
total = 0
dia = 0

while (total < meta_mensal):
    total += vendas_diarias[dia]
    dia += 1
    print(f"Dia {dia}: Total = R$ {total}")

# LISTA COMPREHENSION - LOOP EM UMA LINHA
# pythônico e eficiente
# list comprehensions são 30-50% mais rápidos que loops equivalentes em benchmarks CPython, 
# pois evitam chamadas repetidas do método .append()

# forma tradicional (4 linhas)
precos = [100, 250, 89, 430, 175]
precos_com_iva = []
for p in precos:
    precos_com_iva.append(p * 1.12)

# list comprehension (1 linha, mais pythônico)
precos_com_iva = [p * 1.12 for p in precos]

# com condição (filtro integrado)
caros = [p for p in precos if p > 150]
print(caros) # saída: [250, 430, 175]

# INTRODUÇÃO AO PANDAS
# DataFrame: tabela bidimensional com rótulos. pense numa planilha excel, mas com toda a potência do python

# o DataFrame é a estrutura central do Pandas: uma tabela bidimensional (linhas e colunas)
#  que funciona como uma planilha de Excel turbinada dentro do python. para levar dados de um arquivo externo para essa estrutura, 
# utilizamos funções de leitura, sendo a pd.read_csv() a mais comum.
# ao executar o comando pd.read_csv(), o Pandas realiza três tarefas automáticas:

# 1. mapeamento: identifica a primeira linha como cabeçalho (nomes das colunas).
# 2. tipagem: tenta inferir se cada coluna contém números, textos ou datas.
# 3. indexação: cria um índice numérico para que cada linha seja única e fácil de localizar.

# Perfomance: operações vetorizadas via NumPy - até 100x mais rápido que loops manuais em dados tabulares
# Referência: criado por Wes McKinney no ARQ Capital Management (2008). hoje, padrão de mercado em data science

# exemplo prático
# Imagine que temos um arquivo chamado dados_vendas.csv. o código para transformá-lo em um objeto manipulável é:

import pandas as pd, os

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio, "data", "ecommerce_dataset.csv")

# carrega o arquivo e o transforma em um DataFrame
try:
    df = pd.read_csv(caminho_arquivo)
    print("Arquivo carregado com sucesso!")
    # exibe as 5 primeiras linhas para conferências
    print(df.head())
except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontado em {caminho_arquivo}")

# EFICIÊNCIA DE ALGORITMOS - POR QUE IMPORTA?
# processar 500.000 transações de vendas para calcular total por produto. mesma tarefa, duas abordagens.

# loop manual (iniciante) ❌
# abordagem ingênua

dados = {}
totais = {}

for linha in dados: # 500k transações
    produto = linha["produto"]
    if (produto not in totais):
        totais[produto] = 0
    totais[produto] += linha["valor"]

# tempo de execução: 8 minutos e 12 segundos

# pandas groupby (profissional) ✅
totais = (
    df.groupby("produtos")["valor"]
    .sum()
)

# tempo de execução: 1.2 segundos

# 400x mais rápido
# pandas usa algoritmos otimizados em C

# menos código
# 3 linhas vs 6 linhas

# mais legível
# inteção clara e declarativa

# a diferença não é só velocidade. é a diferença entre esperar 8 minutos ou ter o resultado instantâneo.
# em produção, isso significa processar dados em tempo real.

# EXEMPLO PRÁTICO - groupby COM DATASET OLIST
# vamos aplicar o poderoso método groupby do Pandas em nosso conjunto de dados. 
# Este exemplo demonstrará como agregar informações para identificar as categorias de produtos mais lucrativas.

vendas_por_categoria = df.groupby('categoria')['total'].sum().reset_index()

print("Soma do Valor Total por Categoria:")
display(vendas_por_categoria.head()) # display é um método fictício
# este código agrupa todas as vendas por categoria de produto e soma o valor total de cada categoria

# sort_values - RANKING DE CATEGORIAS MAIS LUCRATIVAS
# após agrupar os dados, o próximo passo é ordená-los para identificar os produtos ou categorias com maior impacto.
# o método sort_values() do Pandas permite organizar os dados de um DataFrame ou Series com base nos valores de uma ou mais colunas,
# criando um ranking claro.

# ordenamos do MAIOR para o MENOR (ascending=False)
vendas_por_categoria = vendas_por_categoria.sort_values(by='total', ascending=False)
print("Soma do Valor Total por Categoria:")
display(vendas_por_categoria.head()) # display é um método fictício
# neste trecho, continuamos de onde paramos anterioremente com a Series vendas_por_categoria.
# aplicamos sort_values(ascending=False) para listar as categorias do maior para o menor valor de receita.
# o poder do groupby se expande quando você o aplica a múltiplas dimensões. 
# isso permite desvendar padrões complexos, como entender preferências regionais específicas para diferentes categorias de produtos.

# nbstripout — A FERRAMENTA ESSENCIAL
# nbstripout é uma ferramenta Python que remove automaticamente os outputs dos notebooks antes de commitar no Git. 
# você continua vendo seus gráficos localmente, mas o Git só versiona o código.

# 1. você trabalha normal: roda células, gera gráficos, vê resultados.
# 2. git commit: nbstripout intercepta e remove outputs automaticamente
# 3. resultado: GitHub recebe só código limpo, sem comflitos.

# INSTALAÇÃO E CONFIGURAÇÃO

# 1. Instalar (uma vez)
# pip install nbstripout

# 2. Configurar no projeto (uma vez)
# cd seu-projeto
# nbstripout --install

# 3. Pronto! Funciona automaticamente
# git add analise.ipynb
# git commit -m "feat: adiciona análise"

# outputs removidos automaticamente ✓

# requirements.txt — AMBIENTE REPRODUTÍVEL
# lista todas as bibliotecas python necessárias com versões fixas. garante que o projete rode igual em qualquer máquina

# exemplo básico

# requirements.txt
# pandas==2.1.4
# numpy==1.26.3
# matplotlib==3.8.2
# jupyter==1.0.0

# comandos essenciais

# gerar do ambiente atual
# pip freeze > requirements.txt

# instalar dependências
# pip install -r requirements.txt

# versões fixas evitam o problema 'funcionava ontem'. Todo mundo usa exatamente as mesmas bibliotecas.

# FIM, por enquanto! voltamos na próxima aula ou assim que possível! BAITA REVISÃO.