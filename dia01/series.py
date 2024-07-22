# %%
import pandas as pd

# %%
idades = [30,42,90,34]
idades

# %%
# Transformando lista, conertendo para uma serie e passando a nova variael
series_idades = pd.Series(idades)
series_idades
# %%
series_idades.mean()
# %%
series_idades.var()
# %%
series_idades.median()
# %%
# Describe descreve os dados da serie
series_idades.describe()
# %%
series_idades[0]
# %%
series_idades.iloc[-1]
# %%
