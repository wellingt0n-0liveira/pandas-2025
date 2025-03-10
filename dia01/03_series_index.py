# %%

import pandas as pd


idades = [ 
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39, 
]

series_idades = pd.Series(idades)
series_idades

# %%

idades[0]
series_idades[0]
# %%
series_idades[0]

# %%

series_idades.iloc[0]

# %%

series_idades.iloc[-1]

# %%

series_idades.iloc[::-1]

# %%
series_idades.iloc[:3]

# %%

idades = [ 
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39, 
]

indexs = [
    "teo","maria", "jose", "luiz","ana"
]

series_idades = pd.Series(idades, index=indexs)
series_idades
