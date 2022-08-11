import pandas as pd
import matplotlib.pyplot as plt


def shift_data(roc_values):
    prices = list(df.roc_open_ibova.values)
    for day in dates:
        count += 1
        if count >= lookback:
            price_series.append(prices[count - lookback : count])

    df_lookback = pd.DataFrame(price_series)
    price_series = []
    return df_lookback


# , index_col='date', header=['date','open_ibova','open_oil','open_usd']
df = pd.read_csv("../Data/2_Stage/ROC_all_data.csv")

df_treino = df.iloc[:1438]
df_validacao = df.iloc[1438:1916]
df_teste = df.iloc[1916:]

df = df_treino

separados = {}
price_series = []
lookback = 6
count = -1
dates = df.index

# FIXME: Estamos usando o df total, nao os de cada um separado...
#  Precisamos fazer com todas as colunas de todos os dfs
# Atualmente só fiz para o conjunto de treino LINHA 10
df_lookback_ibova = shift_data(df.roc_open_ibova.values)
df_lookback_oil = shift_data(df.roc_open_oil.values)
df_lookback_usd = shift_data(df.roc_open_usd.values)
df_lookback_abev = shift_data(df.roc_open_abev.values)
df_lookback_jbs = shift_data(df.roc_open_jbs.values)
df_lookback_petr4 = shift_data(df.roc_open_petr4.values)
df_lookback_vale = shift_data(df.roc_open_vale.values)


# Select columns
df_lookback_ibova.columns = [
    "ibova_0",
    "ibova_1",
    "ibova_2",
    "ibova_3",
    "ibova_4",
    "ibova_5",
]
df_lookback_oil.columns = ["oil_0", "oil_1", "oil_2", "oil_3", "oil_4", "oil_5"]
df_lookback_usd.columns = ["usd_0", "usd_1", "usd_2", "usd_3", "usd_4", "usd_5"]
df_lookback_abev.columns = ["abev_0", "abev_1", "abev_2", "abev_3", "abev_4", "abev_5"]
df_lookback_jbs.columns = ["jbs_0", "jbs_1", "jbs_2", "jbs_3", "jbs_4", "jbs_5"]
df_lookback_petr4.columns = ["petr_0", "petr_1", "petr_2", "petr_3", "petr_4", "petr_5"]
df_lookback_vale.columns = ["vale_0", "vale_1", "vale_2", "vale_3", "vale_4", "vale_5"]

# Drop 9 firt line
df_lookback_ibova = df_lookback_ibova.dropna()
df_lookback_oil = df_lookback_oil.dropna()
df_lookback_usd = df_lookback_usd.dropna()
df_lookback_abev = df_lookback_abev.dropna()
df_lookback_jbs = df_lookback_jbs.dropna()
df_lookback_petr4 = df_lookback_petr4.dropna()
df_lookback_vale = df_lookback_vale.dropna()

# Union dataframes
df_final = pd.concat(
    [
        df_lookback_ibova,
        df_lookback_oil,
        df_lookback_usd,
        df_lookback_abev,
        df_lookback_jbs,
        df_lookback_petr4,
        df_lookback_vale,
    ],
    axis=1,
    join="outer",
)

PATH = f"C:/Users/arthu/Documents/GitHub/TCC_Stock_Predictions/Data/3_Gold/Treino_all_stocks.csv"
df_final.to_csv(PATH)
