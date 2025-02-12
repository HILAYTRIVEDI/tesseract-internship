import dask.dataframe as dd

df = dd.read_csv("large_dataset.csv")

print(df.head())
print(df.shape)
df_filtered = df[df["column_name"] > 1000]
df_filtered.compute()
