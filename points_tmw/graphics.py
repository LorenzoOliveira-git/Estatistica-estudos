# %%

import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns


# %%

df = pd.read_csv("../data/points_tmw.csv",encoding="latin-1",sep=";")

df.head()
# %%

#Bar chart
amount_of_transactions = df.groupby(["descProduto"]).agg(
    {
        "idTransacao":"count"
    }
).reset_index()

# plt.bar(amount_of_transactions["descProduto"],amount_of_transactions["idTransacao"])

sns.set_theme(style="whitegrid")
sns.barplot(amount_of_transactions, y="descProduto", x="idTransacao")
plt.xlabel("Amount of transactions")
plt.ylabel("Description of product")


# %%
