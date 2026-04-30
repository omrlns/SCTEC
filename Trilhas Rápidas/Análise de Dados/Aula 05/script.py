# análise do SuperStore

import os, warnings
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

"""
- **pandas**: para manipulação de tabelas de dados
- **numpy**: para cálculos numéricos
- **matplotlib** e **seaborn**: para criar gráficos estáticos
- **plotly**: para criar gráficos interativos
- **kagglehub**: para baixar o dataset diretamente do Kaggle
"""

warnings.filterwarnings("ignore")

# configurações visuais padrão para gráficos matplotlib/seaborn
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (12, 5)
plt.rcParams["font.size"] = 12

# caminho do arquivo CSV
arquivo_csv = os.path.join(os.path.dirname(__file__), "data", "superstore.csv")

df = pd.read_csv(arquivo_csv, encoding="latin1", dtype={"Postal Code": str}) # df = dataframe
# print(df.head())
# print(df.tail())

# exibe informações sobre os tipos de dados de cada coluna
# 'object' = texto, 'int64' = número inteiro, 'float64' = número decimal
# print(df.info())

# #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Row ID         9994 non-null   int64  
#  1   Order ID       9994 non-null   str    
#  2   Order Date     9994 non-null   str    
#  3   Ship Date      9994 non-null   str    
#  4   Ship Mode      9994 non-null   str    
#  5   Customer ID    9994 non-null   str    
#  6   Customer Name  9994 non-null   str    
#  7   Segment        9994 non-null   str    
#  8   Country        9994 non-null   str    
#  9   City           9994 non-null   str    
#  10  State          9994 non-null   str    
#  11  Postal Code    9994 non-null   str    
#  12  Region         9994 non-null   str    
#  13  Product ID     9994 non-null   str    
#  14  Category       9994 non-null   str    
#  15  Sub-Category   9994 non-null   str    
#  16  Product Name   9994 non-null   str    
#  17  Sales          9994 non-null   float64
#  18  Quantity       9994 non-null   int64  
#  19  Discount       9994 non-null   float64
#  20  Profit         9994 non-null   float64
# dtypes: float64(3), int64(2), str(16)

# print(df.describe())

#             Row ID         Sales     Quantity     Discount       Profit
# count  9994.000000   9994.000000  9994.000000  9994.000000  9994.000000
# mean   4997.500000    229.858001     3.789574     0.156203    28.656896
# std    2885.163629    623.245101     2.225110     0.206452   234.260108
# min       1.000000      0.444000     1.000000     0.000000 -6599.978000
# 25%    2499.250000     17.280000     2.000000     0.000000     1.728750
# 50%    4997.500000     54.490000     3.000000     0.200000     8.666500
# 75%    7495.750000    209.940000     5.000000     0.200000    29.364000
# max    9994.000000  22638.480000    14.000000     0.800000  8399.976000

traducao_colunas = {
    "Row ID": "id_linha",
    "Order ID": "id_pedido",
    "Order Date": "data_pedido",
    "Ship Date": "data_envio",
    "Ship Mode": "modo_envio",
    "Customer ID": "id_cliente",
    "Customer Name": "nome_cliente",
    "Segment": "segmento",
    "Country": "pais",
    "City": "cidade",
    "State": "estado",
    "Postal Code": "cep",
    "Region": "regiao",
    "Product ID": "id_produto",
    "Category": "categoria",
    "Sub-Category": "subcategoria",
    "Product Name": "nome_produto",
    "Sales": "vendas",
    "Quantity": "quantidade",
    "Discount": "desconto",
    "Profit": "lucro"
}

df = df.rename(columns=traducao_colunas)
# print(df.head())

#    id_linha       id_pedido data_pedido  data_envio      modo_envio id_cliente     nome_cliente   segmento           pais  ... regiao       id_produto        categoria subcategoria                                       nome_produto    vendas quantidade desconto     lucro
# 0         1  CA-2016-152156   11/8/2016  11/11/2016    Second Class   CG-12520      Claire Gute   Consumer  United States  ...  South  FUR-BO-10001798        Furniture    Bookcases                  Bush Somerset Collection Bookcase  261.9600          2     0.00   41.9136
# 1         2  CA-2016-152156   11/8/2016  11/11/2016    Second Class   CG-12520      Claire Gute   Consumer  United States  ...  South  FUR-CH-10000454        Furniture       Chairs  Hon Deluxe Fabric Upholstered Stacking Chairs,...  731.9400          3     0.00  219.5820
# 2         3  CA-2016-138688   6/12/2016   6/16/2016    Second Class   DV-13045  Darrin Van Huff  Corporate  United States  ...   West  OFF-LA-10000240  Office Supplies       Labels  Self-Adhesive Address Labels for Typewriters b...   14.6200          2     0.00    6.8714
# 3         4  US-2015-108966  10/11/2015  10/18/2015  Standard Class   SO-20335   Sean O'Donnell   Consumer  United States  ...  South  FUR-TA-10000577        Furniture       Tables      Bretford CR4500 Series Slim Rectangular Table  957.5775          5     0.45 -383.0310
# 4         5  US-2015-108966  10/11/2015  10/18/2015  Standard Class   SO-20335   Sean O'Donnell   Consumer  United States  ...  South  OFF-ST-10000760  Office Supplies      Storage                     Eldon Fold 'N Roll Cart System   22.3680          2     0.20    2.5164

# verifica a quantidade e o percentual de valores nulos por coluna
nulos = pd.DataFrame({
    "Quantidade": df.isnull().sum(),
    "Percentual (%)": (df.isnull().sum() / len(df) * 100).round(2)
})

# tamanho atual do dataframe
# print(len(df)) # saída: 9994

df.drop_duplicates(inplace=True)
# print(len(df)) # saída: 9994

# mudando as colunas em específico de objeto para datetime
df["data_pedido"] = pd.to_datetime(df["data_pedido"])
df["data_envio"] = pd.to_datetime(df["data_envio"])

# extração de componentes de data
df["ano"] = df["data_pedido"].dt.year
df["mes"] = df["data_pedido"].dt.month
df["nome_mes"] = df["data_pedido"].dt.strftime("%b") # jan, fev, ...

# dias de entrega: quanto tempo levou para o cliente receber o pedido?
df["dias_entrega"] = (df["data_envio"] - df["data_pedido"]).dt.days

# margem de lucro por transação (%)]
df["margem_lucro"] = np.where(
    df["vendas"] != 0,
    (df["lucro"] / df["vendas"] * 100).round(2),
    0
)

# print(df['margem_lucro'].head())

# 0    16.00
# 1    30.00
# 2    47.00
# 3   -40.00
# 4    11.25

# tradução das categorias para português
df["categoria"] = df["categoria"].map({
    "Furniture": "Móveis",
    "Office Supplies": "Papelaria",
    "Technology": "Tecnologia"
})

# tradução das subcategorias para o português
df["subcategoria"] = df["subcategoria"].map({
    "Bookcases": "Estantes",
    "Chairs": "Cadeiras",
    "Tables": "Mesas",
    "Furnishings": "Mobiliário",
    "Appliances": "Eletrodomésticos",
    "Art": "Arte",
    "Binders": "Fichários",
    "Envelopes": "Envelopes",
    "Fasteners": "Grampos",
    "Labels": "Etiquetas",
    "Storage": "Armazenamento",
    "Supplies": "Suprimentos",
    "Accessories": "Acessórios",
    "Copiers": "Copiadoras",
    "Machines": "Máquinas",
    "Phones": "Telefones"
})

# tradução dos segmentos para português
df["segmento"] = df["segmento"].map({
    "Consumer": "Consumidor",
    "Corporate": "Corporativo",
    "Home Office": "Home Office"
})

# tradução das regiões para português
df["regiao"] = df["regiao"].map({
    "West": "Oeste",
    "East": "Leste",
    "Central": "Central",
    "South": "Sul"
})

# tradução dos modos de envio
df["modo_envio"] = df["modo_envio"].map({
    "Standard Class": "Padrão",
    "Second Class": "Segunda Classe",
    "First Class": "Primeira Classe",
    "Same Day": "Mesmo Dia"
})

# filtar apenas os anos de 2016-2017
linhas_antes = len(df)
# print(linhas_antes) # saída: 9994

df = df[df["ano"].isin([2016, 2017])].copy()

linhas_depois = len(df)
# print(linhas_depois) # saída: 5899

# print(f"Linhas Antes do Filtro: {linhas_antes:,}")
# print(f"Linhas Depois do Filtro: {linhas_depois:,}")
# print(f"Linhas Removidas: {linhas_antes - linhas_depois:,}")

# Linhas Antes do Filtro: 9,994
# Linhas Depois do Filtro: 5,899
# Linhas Removidas: 4,095

# verifica a distribuição por ano e mês após o filtro
dist = df.groupby(["ano", "mes"]).size().reset_index(name="registros")
# print("Registros por Mês (2016-2017):")
# print(dist.pivot(index="mes", columns="ano", values="registros").fillna(0).astype(int).to_string())

# Registros por Mês (2016-2017):
# ano  2016  2017
# mes            
# 1      89   155
# 2      83   107
# 3     163   238
# 4     170   203
# 5     225   242
# 6     199   245
# 7     201   226
# 8     176   218
# 9     363   459
# 10    196   298
# 11    370   459
# 12    352   462

# visualiza o dataset após a limpeza
print(df[['data_pedido', 'categoria', 'segmento', 'regiao', 'vendas', 'lucro', 'desconto', 'margem_lucro', 'dias_entrega']].head(10))

#    data_pedido   categoria     segmento   regiao   vendas     lucro  desconto  margem_lucro  dias_entrega
# 0   2016-11-08      Móveis   Consumidor      Sul  261.960   41.9136       0.0         16.00             3
# 1   2016-11-08      Móveis   Consumidor      Sul  731.940  219.5820       0.0         30.00             3
# 2   2016-06-12   Papelaria  Corporativo    Oeste   14.620    6.8714       0.0         47.00             4
# 12  2017-04-15   Papelaria   Consumidor      Sul   15.552    5.4432       0.2         35.00             5
# 13  2016-12-05   Papelaria   Consumidor    Oeste  407.976  132.5922       0.2         32.50             5
# 21  2016-12-09   Papelaria  Corporativo  Central   19.460    5.0596       0.0         26.00             4
# 22  2016-12-09   Papelaria  Corporativo  Central   60.340   15.6884       0.0         26.00             4
# 23  2017-07-16      Móveis   Consumidor    Leste   71.372   -1.0196       0.3         -1.43             2
# 25  2016-01-16   Papelaria   Consumidor    Oeste   11.648    4.2224       0.2         36.25             4
# 26  2016-01-16  Tecnologia   Consumidor    Oeste   90.570   11.7741       0.0         13.00             4

# distribuição de vendas
# usamos o percentil 95 como limite do eixo X para focar onde está a maioria dos dados
# os outliers existem, mas não precisam distorcer a visualização

p95_vendas = df["vendas"].quantile(0.99)  # valor que cobre 95% dos dados
media_vendas = df["vendas"].mean()
mediana_vendas = df["vendas"].median()

fig, ax = plt.subplots(figsize=(12, 5))

ax.hist(df["vendas"], bins=60, color="steelblue", edgecolor="white", alpha=0.85)
ax.axvline(media_vendas,   color="red",    linestyle="--", linewidth=1.5, label=f"Média: ${media_vendas:.0f}")
ax.axvline(mediana_vendas, color="orange", linestyle="--", linewidth=1.5, label=f"Mediana: ${mediana_vendas:.0f}")

ax.set_xlim(0, p95_vendas)
ax.set_title("Distribuição de Vendas por Transação", fontsize=14)
ax.set_xlabel("Valor da venda (USD)")
ax.set_ylabel("Frequência")
ax.legend()

pct_outlier = (df["vendas"] > p95_vendas).mean() * 100
ax.text(0.98, 0.95, f"* {pct_outlier:.0f}% dos dados estão\nacima de ${p95_vendas:.0f} (fora do gráfico)",
        transform=ax.transAxes, ha="right", va="top", fontsize=9, color="gray")

plt.tight_layout()
plt.show()

# print("\nEstatísticas de Vendas:")
df["vendas"].describe().apply(lambda x: f"${x:,.2f}") # colocar o print para visualização
