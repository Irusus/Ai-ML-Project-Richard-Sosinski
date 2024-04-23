import pandas as pd

df1 = pd.read_csv("finalBenign1.csv")
df2 = pd.read_csv("finalDict1.csv")

merger=pd.DataFrame()

merger = merger._append(df1)
merger = merger._append(df2)

merger.to_csv("Combined.csv")
print(df1)
print(df2)
print(merger)