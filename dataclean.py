import pandas as pd

df = pd.read_csv("train.csv", engine="python", on_bad_lines="warn")

print("Total rows loaded:", df.shape[0])

# Saaf data ko nayi file mein save karna
df.to_csv("train_super_clean.csv", index=False)
