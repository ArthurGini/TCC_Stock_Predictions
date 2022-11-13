import pandas as pd
import matplotlib.pyplot as plt

# , index_col='date', header=['date','open_ibova','open_oil','open_usd']
df = pd.read_csv("../Data/2_Stage/bruto_ibova_oil_usd_abev_jbs_petra_vale.csv")

# Calculo da média movel de 10 dias  - Parte não utilizada na versão final
# df['open_ibova'] = df.open_ibova.rolling(window=10)
# df['open_oil'] = df.open_oil.rolling(window=10)
# df['open_usd'] = df.open_usd.rolling(window=10)
# df['open_abev'] = df.open_abev.rolling(window=10)
# df['open_jbs'] = df.open_jbs.rolling(window=10)
# df['open_petr4'] = df.open_petr4.rolling(window=10)
# df['open_vale'] = df.open_vale.rolling(window=10)

# # Por causa da janela média dos dados começam no index 9
# df = df.dropna()

# Transformando na variação
import pandas_ta as ta

df["roc_open_ibova"] = ta.roc(
    df["open_ibova"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_oil"] = ta.roc(
    df["open_oil"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_usd"] = ta.roc(
    df["open_usd"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_abev"] = ta.roc(
    df["open_abev"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_jbs"] = ta.roc(
    df["open_jbs"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_petr4"] = ta.roc(
    df["open_petr4"], length=1, scalar=None, talib=None, offset=None
)
df["roc_open_vale"] = ta.roc(
    df["open_vale"], length=1, scalar=None, talib=None, offset=None
)

# Selecionando colunas desejadas e resetando o index
df = df.reset_index()
df = df[
    [
        "date",
        "roc_open_ibova",
        "roc_open_oil",
        "roc_open_usd",
        "roc_open_abev",
        "roc_open_jbs",
        "roc_open_petr4",
        "roc_open_vale",
    ]
]
df = df.dropna()

PATH = f"C:/Users/arthu/Documents/GitHub/TCC_Stock_Predictions/Data/2_Stage/ROC_all_data.csv"
df.to_csv(PATH)
