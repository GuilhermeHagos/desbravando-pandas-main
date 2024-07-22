# %%

import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")

# %%
df

# %%
df['Points_double'] = df["Points"] * 2
# %%
df['Points_ratio'] = df['Points_double'] / df['Points']
df
# %%
df['Constante'] = None
df

# %%
df['Points_log'] = np.log(df['Points'])
df
# %%
df['Name'].str.upper()
# %%
df
# %%
def get_first(nome: str):
    nome = nome.upper()
    return nome.split('_')[0]

# %%
# apply aplica uma funcao em todas as linhas da série
df['Name_First'] = df['Name'].apply(get_first)
# %%
df['Name_First']
# %%
# lambda, funcao anonima, a ideia éutilizar quando quer usar em apenas uma linha de forma muito rápida
get_f = lambda nome : nome.split('_')[0]
# %%
get_f('Téo')
# %%
df['Name'].apply(lambda x: x.upper().split('_')[0])
# %%
def intervalo_pontos (pontos: int):
    if pontos < 2500:
        return 'Baixo'
    elif pontos < 3500:
        return 'Médio'
    else:
        return 'Alto'
# %%
df['Faixa_Pontos'] = df['Points'].apply(intervalo_pontos)
# %%
df.dtypes
# %%
df['UUID'].apply(lambda x : x[-3:])

# %%
