#%%

import pandas as pd

df = pd.read_csv("../data/points_tmw.csv",sep=";",encoding="latin-1")
df.head()

# %%

print("Statistics of transactionals:")

average = df["qtdPontos"].mean()
print("Average: ",average)

minimum = df["qtdPontos"].min()
print("Minimum: ",minimum)

first_quantile = df["qtdPontos"].quantile(0.25)
print("1o Quantile: ",first_quantile)

median = df["qtdPontos"].median()
print("Median: ",median)

third_quantile = df["qtdPontos"].quantile(0.75)
print("3o Quantile: ",third_quantile)

maximum = df["qtdPontos"].max()
print("Maximum: ",maximum)

# %%

#Describe have informations as quantile, median, maximum, minimum, average, etc.
df["qtdPontos"].describe()

# %%

print("Statistics of users:")

users = df.groupby(["idUsuario"]).agg(
    {
        "idTransacao":"count",
        "qtdPontos": "sum",
    }
).reset_index()

sumario = users[["idTransacao","qtdPontos"]].describe().rename(columns={"idTransacao":"Transactional Descriptions","qtdPontos":"Poins Descriptions"})

print(sumario.to_markdown())

# %%

