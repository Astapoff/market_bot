import pandas as pd
import numpy as np
import statsmodels.api as sm

# Считываем данные о ценах фьючерсов из CSV файлов
df_eth = pd.read_csv("ETHUSDT.csv")
df_btc = pd.read_csv("BTCUSDT.csv")

# Удаляем ненужные столбцы
df_eth = df_eth.drop(columns=["open", "high", "low", "vol"])
df_btc = df_btc.drop(columns=["open", "high", "low", "vol"])

# Переименовываем столбец с ценой
df_eth = df_eth.rename(columns={"close": "eth_close"})
df_btc = df_btc.rename(columns={"close": "btc_close"})

# Объединяем данные по дате
df = pd.merge(df_eth, df_btc, on="dt")

# Рассчитываем уравнение регрессии
X = df["btc_close"]
Y = df["eth_close"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()

# Выводим коэффициенты уравнения регрессии
print("Coefficients: ", model.params)

# Рассчитываем собственные движения цены фьючерса ETHUSDT
df["eth_no_btc"] = df["eth_close"] - (model.params[1] * df["btc_close"] + model.params[0])

# Выводим данные по ценам с учетом собственных движений
print(df[["dt", "eth_close", "btc_close", "eth_no_btc"]])