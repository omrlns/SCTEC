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

print(df['margem_lucro'].head())

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