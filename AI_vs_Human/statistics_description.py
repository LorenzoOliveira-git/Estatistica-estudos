#%%
import pandas as pd

df = pd.read_csv("../data/ai_vs_human_dataset_medium.csv")

df.head()
# %%

import matplotlib.pyplot as plt

#In this case, the label "lenght_chars" shows a lot outliers, so, the mean is not a good ideia.
plt.boxplot(df["length_chars"])

mean = df["length_chars"].mean()
print("Average: ",mean)

#%%

median = df["length_chars"].median()
plt.hist(df["length_chars"],bins=18,density=True)
plt.axvline(median,color="red",linestyle="dashed")
plt.axvline(mean)
plt.show()

# %%



