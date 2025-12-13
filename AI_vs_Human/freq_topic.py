#%%

import pandas as pd

dt = pd.read_csv("../data/ai_vs_human_dataset_medium.csv")

dt.head()
# %%

# TABLE OF FREQUENCY ABOUT TOPIC MOST POPULAR

#Absolute Frequency
freq_topic = dt.groupby(["topic"])[["id"]].count().rename(columns={"id":"Freq. Abs."})

# %%

#Cumulative absolute frequency
freq_topic["Freq. Abs. Acum."] = freq_topic["Freq. Abs."].cumsum()

freq_topic

# %%

#Relative Frequency
freq_topic["Freq. Rel."] = freq_topic["Freq. Abs."] / freq_topic["Freq. Abs."].sum()


freq_topic

# %%

#Cumulative Relative Frequency
freq_topic["Freq. Rel. Acum."] = freq_topic["Freq. Rel."].cumsum()

freq_topic

# %%

#Insights than we can get about this analyze:
# The most popular topic are Finance, Food, science and sports.
# The less popular is technology


