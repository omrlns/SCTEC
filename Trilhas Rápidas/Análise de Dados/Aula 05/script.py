# análise do SuperStore

import os, warnings
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
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