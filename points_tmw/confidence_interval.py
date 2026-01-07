#%%

import pandas as pd

df = pd.read_csv("../data/points_tmw.csv",encoding="latin-1",sep=";")

df.head()
# %%

users = (df.groupby(["idUsuario"])["qtdPontos"].sum().reset_index())

users.head()

# %%

n = 100
alpha = 0.05
sample = users["qtdPontos"].sample(n)

x_bar = sample.mean()
s = sample.std()

from scipy.stats import t as t_student

t = t_student.ppf(1-alpha/2, n-1)

min = x_bar - t * s / (n**0.5)
max = x_bar + t * s / (n**0.5)

interval = [min,max]

interval

# %%

alpha = 0.05

def generate_interval(sample,alpha):
    n = len(sample)
    x_bar = sample.mean()
    s = sample.std()
    t = t_student.ppf(1-alpha/2, n-1)
    min = x_bar - t*s / (n**0.5)
    max = x_bar + t*s / (n**0.5)

    return x_bar,s,min,max

stats = []
for i in range(100):
    sample = users['qtdPontos'].sample(100)
    stats.append(generate_interval(sample,alpha))


stats = pd.DataFrame(stats)
stats.columns = ["x_bar","std","min","max"]

stats["mean_true"] = users["qtdPontos"].mean()

stats["check"] = (stats["mean_true"] > stats["min"]) & (stats["mean_true"] < stats["max"])

percent_true = stats["check"].mean()
percent_true
# %%

import matplotlib.pyplot as plt

for i in range(30):
    data = stats.iloc[i]
    color = "green" if data["check"] else "red"
    plt.plot(data[['min','max']],[i,i],"o--",color=color, alpha=0.5)

plt.vlines(data["mean_true"],-1,i+1,color='black',alpha=0.5)
plt.xlabel("Valor esperado")
plt.ylabel("Amostra")
plt.title("Intervalo de confiança")
plt.grid()
plt.show()

# %%
