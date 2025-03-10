# %%

idades = [
    32, 38, 30, 31, 35, 27
]

media =  sum(idades) / len(idades)
print("Media:" ,media)

diffs = 0
for i in idades:
    diffs += (i - media) **2

variancia = diffs / (len(idades)-1)

print("Variancia:", variancia)

# %% 

idades = [
    32, 38, 30, 31, 35, 27
]


import pandas as pd

series_idades = pd.Series(idades)
series_idades 

# %%
# estatisticas da séries

idades = [
    32, 38, 30, 31, 35, 27
]


media_idades = series_idades.mean()
var_idades = series_idades.var()
summary = series_idades.describe()