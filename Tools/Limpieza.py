import pandas as pd
import re

df = pd.read_csv("bitcoin_tweets_latest.csv", on_bad_lines="skip")

df = df[["user_name", "text", "hashtags", "is_retweet", "user_followers", "user_friends"]]

df = df.dropna(subset=["text", "user_name"])

df = df[df["is_retweet"] != "True"]

df = df.head(100000)
print(len(df), "filas después de la limpieza")

# Limpiar el texto
def limpiar_texto(texto):
    texto = texto.lower()                          # todo minusculas
    texto = re.sub(r'http\S+', '', texto)          # sacar URLs
    texto = re.sub(r'@\w+', '', texto)             # sacar @menciones
    texto = re.sub(r'#\w+', '', texto)             # sacar #hashtags
    texto = re.sub(r'[^a-z0-9 ]', '', texto)      # sacar simbolos raros
    texto = re.sub(r'\s+', ' ', texto).strip()     # sacar espacios extra
    return texto

df["text"] = df["text"].apply(limpiar_texto)

print(df["text"].head(3))