# %%

import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns


# %%

df = pd.read_csv("../data/points_tmw.csv",encoding="latin-1",sep=";")

df.head()
# %%

#Bar chart - plt.bar()
amount_of_transactions = df.groupby(["descProduto"]).agg(
    {
        "idTransacao":"count"
    }
).reset_index()

#%%
# plt.bar(amount_of_transactions["descProduto"],amount_of_transactions["idTransacao"])

sns.set_theme(style="whitegrid")
plt.xlabel("Amount of transactions")
plt.ylabel("Description of product")
plt.title("Freq. of products")
sns.barplot(amount_of_transactions, y="descProduto", x="idTransacao")


# %%

amount_of_transactions = amount_of_transactions.sort_values(by="idTransacao")

# %%

#Line graphc - plt.plot()
df.head()

df["DataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date

group_date = df.groupby(["DataTransacao"]).agg(
    {
        "idTransacao": "count",
        "qtdPontos": "sum"
    }
).reset_index()

group_date.sort_values(by="DataTransacao",inplace=True)

plt.figure(figsize=[16,8])
plt.plot(group_date["DataTransacao"],group_date["idTransacao"])
plt.title("Historic series of transactions")
plt.ylabel("Amout of transactions")
plt.xlabel("Date")
plt.legend(["Amount of transactions"])

# %%

#histogram - plt.hist()

plt.hist(group_date["qtdPontos"],bins=18,density=True)
plt.xlabel("Points")
plt.ylabel("Density")
plt.show()

# %%

#Box-plot - plt.boxplot()
#OBS: All points out of LS and LI are "outliers", in this case, there are many points because my data is more concentrated between -500 and 500.
plt.boxplot(group_date["qtdPontos"])
plt.title("Box-plot of points")

#%%

#it's worse when we get the data of source dataframe, see:
df["qtdPontos"] = df["qtdPontos"].fillna(0)
df["qtdPontos"] = df["qtdPontos"].astype("int64")

plt.figure(figsize=(8,8))
plt.grid()
plt.boxplot(df["qtdPontos"])        

# %%

group_points = df.groupby(["qtdPontos"]).agg({
    "idTransacao":"count"
}).reset_index()

group_points
# %%

plt.boxplot(group_points["idTransacao"])
plt.grid()
plt.ylabel("Points")
plt.title("Box-plot test of count of points")

# %%

sns.barplot(group_points,x="qtdPontos",y="idTransacao")
plt.show()

# %%

#scatter plot

sns.scatterplot(group_date,x="qtdPontos",y="idTransacao")
plt.show()

# %%
