#Importamos librerias necesarias para que el codigo funcione y pueda leer el csv, ademas de limpiarlo
import pandas as pd
import re
import ast

df = pd.read_csv("data/bitcoin_tweets_latest.csv", on_bad_lines="skip") #Le colocamos un csv que sea una variable df y le decimos que salte las lineas rotas o incorrectas 

df = df[["user_name", "text", "hashtags", "is_retweet", "user_followers", "user_friends"]] #Seleccionamos solo las variables que nos interesan para el analisis, ya que tiene muchas que estan vacias o no aportan nada al analisis

df = df.dropna(subset=["text", "user_name"]) #Elimanos las que no tienen texto o nombre de usuario para que quede mas limpio el dataset 

df = df[df["is_retweet"] != "True"]#Elimanos los retweets ya que son lo mismo de un tweet original siendo copia de este, por lo que no aportan nada nuevo al analisis y solo genera espacios vacios o duplicados

df = df.head(100000)#Limitamos a 100000 filas para no sobrecargar el programa


def limpiar_texto(texto):#Limpiamos el texto de cada tweet para que se vea mas ordenado y no tenga simbolos o caracteres que no aportan nada al analisis, ademas de que todo este en minusculas para que sea mas facil de analizar
    texto = texto.lower()                          # todo minusculas
    texto = re.sub(r'http\S+', '', texto)          # sacar URL
    texto = re.sub(r'@\w+', '', texto)             # sacar @menciones
    texto = re.sub(r'#\w+', '', texto)             # sacar #hashtags
    texto = re.sub(r'[^a-z0-9 ]', '', texto)       # sacar simbolos
    texto = re.sub(r'\s+', ' ', texto).strip()     # sacar espacios extras
    return texto

df["text"] = df["text"].apply(limpiar_texto)#Toma la funcion limpiar_texto y la aplica a cada fila de la columna texto para que se limpie cada tweet
print(df["text"].head(3))#Imprimimos las 3 primeras filas de la columna texto para ver que realmente se limpio el dataset y se ve mas ordenado, ademas de que se elimino todo lo que no aportaba nada al analisis y se dejo solo el texto limpio para poder analizarlo mejor

def limpiar_hashtags(valor):#Limpiamos la columna hashtags
    try:
        lista = ast.literal_eval(valor)#Convertimos el string a una lista de python utilizando ast.literal_eval, ya que los hashtags estan guardados como un string con formato de lista, por lo que necesitamos convertirlo para poder manipularlo y limpiarlo
        return [h.lower() for h in lista]
    except:
        return []

df["hashtags"] = df["hashtags"].apply(limpiar_hashtags)#Toma la funcion limpiar_hashtags y la aplica a cada fila de la columna hashtags para que se limpie cada hashtag 

print(df["hashtags"].head(5))#Imprimimos las 5 primeras filas de la columna hashtags para ver que realmente se limpio el dataset y se ve mas ordenado, ademas de que se elimino todo lo que no aportaba nada al analisis y se dejo solo los hashtags limpios para poder analizarlos mejor

df.to_csv("data/tweets_limpios.csv", index=False)#Guardamos el nuevo dataset que creamos con el nombre de tweets_limpios.csv en la carpeta data, ademas de que le decimos que no guarde el indice para que quede mas limpio el nuevo csv y solo tenga las columnas que nos interesan para el analisis
print("archivo guardado")#Imprimimos para que nos confirme que el dataset nuevo se guardo bien