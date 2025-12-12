# %%

import pandas as pd

df = pd.read_csv("data/points_tmw.csv",sep=";",encoding='latin-1')
df.head()

# %%

freq_produto = (df.groupby(["descProduto"])[["idTransacao"]].count()).rename(columns={"idTransacao":"Freq. Abs."})

# %%

freq_produto["Freq. Abs. Acum"] = freq_produto["Freq. Abs."].cumsum()

freq_produto

# %%

freq_produto["Freq. Rel."] = freq_produto["Freq. Abs."] / freq_produto["Freq. Abs."].sum()

freq_produto
# %%

freq_produto["Freq. Rel. Acum."] = freq_produto["Freq. Rel."].cumsum()

freq_produto
# %%

freq_categoria = df.groupby(["descCategoriaProduto"])[["idTransacao"]].count().rename(columns={"idTransacao":"Freq. Abs."})

freq_categoria["Freq. Abs. Acum"] = freq_categoria["Freq. Abs."].cumsum()

freq_categoria["Freq. Rel."] = freq_categoria["Freq. Abs."] / freq_categoria["Freq. Abs."].sum()

freq_categoria["Freq. Rel. Acum."] = freq_categoria["Freq. Rel."].cumsum()

freq_categoria
# %%

import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")
df.to_sql("points",engine,if_exists="replace",index=False)

# %%
