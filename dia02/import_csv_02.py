# %%
import pandas as pd

df = pd.read_csv("../data/products.csv",
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%

#alterando nome das colunas(passamos um dicionário no rename)
df = df.rename(columns={"Name":"Nome","Description": "Descrição"})
df
# %%
#inplace permite alterar o dataframe sem associar a obnjeto
df.rename(columns={"Name":"Nome","Description": "Descrição"},inplace= True)
df
