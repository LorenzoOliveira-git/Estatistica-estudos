# %%

import pandas as pd

df = pd.read_csv("../data/points_tmw.csv",encoding="latin-1",sep=";")

df

#%%

statistics_measures_points = pd.DataFrame()

statistics_measures_points["Minimum"] = pd.Series(df["qtdPontos"].min())

statistics_measures_points["Mean"] = df["qtdPontos"].mean()

statistics_measures_points["1o quantile"] = df["qtdPontos"].quantile(0.25)

statistics_measures_points["Median"] = df["qtdPontos"].median()

statistics_measures_points["3o quantile"] = df['qtdPontos'].quantile(0.75)

statistics_measures_points["Maximum"] = df["qtdPontos"].max()

statistics_measures_points["Variance"] = df['qtdPontos'].var()

statistics_measures_points["Standard Deviation"] = df["qtdPontos"].std()

statistics_measures_points["Coefficient of variation"] = statistics_measures_points["Standard Deviation"] / statistics_measures_points["Mean"]

statistics_measures_points
# %%

#Users
df_users = df.groupby(["idUsuario"]).agg(
    {
        "idTransacao":"count",
        "qtdPontos": "sum"
    }
).reset_index().rename(columns={"idTransacao":"Amount of Transactions","qtdPontos":"Sum of points"})

df_users

#%%

statistics_measures_users = pd.DataFrame(index=["Transactions","Points"])

#%%

#Transactions
statistics_measures_users["Minimum"] = pd.Series()
statistics_measures_users["Minimum"].loc["Transactions"] = df_users["Amount of Transactions"].min()

statistics_measures_users["Mean"] = pd.Series
statistics_measures_users["Mean"].loc["Transactions"] = df_users["Amount of Transactions"].mean()

statistics_measures_users["1o quantile"] = pd.Series()
statistics_measures_users["1o quantile"].loc["Transactions"] = df_users["Amount of Transactions"].quantile(0.25)

statistics_measures_users["Median"] = pd.Series()
statistics_measures_users["Median"].loc["Transactions"] = df_users["Amount of Transactions"].quantile(0.50)

statistics_measures_users["3o quantile"] = pd.Series()
statistics_measures_users["3o quantile"].loc["Transactions"] = df_users["Amount of Transactions"].quantile(0.75)

statistics_measures_users["Maximum"] = pd.Series()
statistics_measures_users["Maximum"].loc["Transactions"] = df_users["Amount of Transactions"].max()

statistics_measures_users["Variance"] = pd.Series()
statistics_measures_users["Variance"].loc["Transactions"] = df_users["Amount of Transactions"].var()

statistics_measures_users["Standard Deviation"] = pd.Series()
statistics_measures_users["Standard Deviation"].loc["Transactions"] = df_users["Amount of Transactions"].std()

statistics_measures_users["Coefficience of variation"] = pd.Series()
statistics_measures_users["Coefficience of variation"].loc["Transactions"] = statistics_measures_users["Standard Deviation"].loc["Transactions"]/statistics_measures_users["Mean"].loc["Transactions"]

statistics_measures_users["Amplitude"] = pd.Series()
statistics_measures_users["Amplitude"].loc["Transactions"] = statistics_measures_users["Maximum"].loc["Transactions"] - statistics_measures_users["Minimum"].loc["Transactions"]

#Points
statistics_measures_users["Minimum"].loc["Points"] = df_users["Sum of points"].min()

statistics_measures_users["Mean"].loc["Points"] = df_users["Sum of points"].mean()

statistics_measures_users["1o quantile"].loc["Points"] = df_users["Sum of points"].quantile(0.25)

statistics_measures_users["Median"].loc["Points"] = df_users["Sum of points"].quantile(0.50)

statistics_measures_users["3o quantile"].loc["Points"] = df_users["Sum of points"].quantile(0.75)

statistics_measures_users["Maximum"].loc["Points"] = df_users["Sum of points"].max()

statistics_measures_users["Variance"].loc["Points"] = df_users["Sum of points"].var()

statistics_measures_users["Standard Deviation"].loc["Points"] = df_users["Sum of points"].std()

statistics_measures_users["Coefficience of variation"].loc["Points"] = statistics_measures_users["Standard Deviation"].loc["Points"]/statistics_measures_users["Mean"].loc["Points"]

statistics_measures_users["Amplitude"].loc["Points"] = statistics_measures_users["Maximum"].loc["Points"] - statistics_measures_users["Minimum"].loc["Points"]

statistics_measures_users

# %%
