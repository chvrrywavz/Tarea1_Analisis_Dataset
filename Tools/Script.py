import pandas as pd

df = pd.read_csv("data/bitcoin_tweets_latest.csv", on_bad_lines="skip")

print(len(df), "filas")
print(df.dtypes)
print(df.isnull().sum())
print(df["text"].head(3))
print(df["hashtags"].head(5))