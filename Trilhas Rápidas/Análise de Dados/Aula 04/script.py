import pandas as pd, os

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio, "data", "superstore.csv")

# carrega o arquivo e o transforma em um DataFrame
try:
    # latin-1 é utilizado para ler caracteres especias, é uma solução diferente do utf-8, que nem sempre funciona
    print("Arquivo carregado com sucesso!")
    df = pd.read_csv(caminho_arquivo, encoding="latin-1", dtype={"Postal Code": str})
    # exibe as 5 primeiras linhas para conferências
    print(df.head())
except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontado em {caminho_arquivo}")

# DATA SANITY CHECK
# um sanity check sistemático detecta corrupções, erros de tipagem e anomalias estruturais antes que contaminem toda a análise

# .head()
# valida o cabeçalho e as primeiras linhas, confirma que a leitura iniciou corretamente

# .tail()
# caça linhas corrompidas, totalizadores automáticos ou metadados no fim do arquivo, problema clássico em exports de ERP.
print(f"RESULTADO DO .tail():\n\n{df.tail()}")
print("-" * 100)

# .sample()
# amostragem aleatória sem vipés de ordenação, revela o comportamento real dos dados no miolo do dataset
print(f"RESULTADO DO .sample():\n\n{df.sample(10)}")
print("-" * 100)

# .info() / .describe()
# panorama completo: tipos, nulos e estatísticas descritivas, indispensáveis no primeiro contato com qualquer base.
print(f"RESULTADO DO .info():\n\n{df.info()}")
print("-" * 100)
print(f"RESULTADO DO .describe():\n\n{df.describe}")