# Extraindo dados do IBOVA
from pandas_datareader._utils import RemoteDataError
import pandas as pd
from pandas_datareader import data as wb

"""
    Maiores componentes do Ibovespa:
        https://valorinveste.globo.com/mercados/renda-variavel/bolsas-e-indices/noticia/2021/11/22/as-10-maiores-acoes-do-ibovespa-ruim-com-elas-pior-sem-elas.ghtml

	Definições do Script:

    lista_acoes = ['BOVA11.SA', 'SPX', 'USDBRL=X', 'TNX', 'DJT', 'CL=F', 'VALE', 'PETR4.SA', 'JBSAY', 'ABEV3.SA']
                    IBOVA, SP500, USDBRL, US10Y, Dow jones Transport, Crude oil,Vale, Petrobras, JBS, Ambev

"""

extract_data = "^BVSP"
init_extract_date = "2010-6-30"
end_extract_date = "2021-11-10"
PATH = f"C:/Users/arthu/Documents/GitHub/TCC_Stock_Predictions/Data/1_Raw/Open_{extract_data}_2.csv"

df = pd.DataFrame()

try:
    # data = wb.DataReader(lista_acoes[0], data_source ='yahoo', start = init_extract_date, end=end_extract_date)['Adj Close Open']
    data = wb.DataReader(
        name=extract_data,
        data_source="yahoo",
        start=init_extract_date,
        end=end_extract_date,
    )
    print(data)

except RemoteDataError:
    print("yahoo fora do ar")

df_stock = data["Open"]

df_stock.to_csv(PATH)
print(f"Arquivo salvo com sucesso em: {PATH}")
