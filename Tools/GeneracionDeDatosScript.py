#este script permite generar datos sinteticos debido a los requerimientos del trabajo.
import pandas as pd
import random as rad

try:
    df = pd.read_csv("tweets_limpios.csv", low_memory=False)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Extraemos los usuarios únicos para poder relacionarlos
usuariosUnicos = df['user_name'].dropna().unique().tolist()
totalUsuarios = len(usuariosUnicos)
print(f"-> Procesando relaciones para {totalUsuarios} usuarios únicos.")


#RED SINTETICA 
#esto es para extraer los usuarios unicos
usuariosUnicos = df['user_name'].dropna().unique().tolist()
totalUsuarios = len(usuariosUnicos)
print(f"Total de usuarios únicos: {totalUsuarios}")

#este bloque genera los datos 
diccionarioAmigos = {}
for usuario in usuariosUnicos:
    #para simplificar, se asigna un numero aleatorio de amigos entre 0 y 10 a cada usuario
    #amigos puede ser usuarios que el usuario sigue y hacen follow back o el caso contrario.
    numAmigos = rad.randint(0, 10)
    #idealmente no se tiene que elegir a el mismo, asi que filtramos
    posiblesAmigos = [u for u in usuariosUnicos if u != usuario]
    amigosAsignados = rad.sample(posiblesAmigos, min(numAmigos, len(posiblesAmigos)))
    #para unir la lista sin el ; se rompe, porfavor nadie modifique esto.
    diccionarioAmigos[usuario] = ";".join(amigosAsignados)
    
df['user_friends'] = df['user_name'].map(diccionarioAmigos)

#Generacion De Likes. 
#Como Twitter tiene los likes ocultos, tambien tenemos que generar likes per post.
listaLikes = []
for _ in range(len(df)):
    # Asignamos entre 0 y 15 likes aleatorios por publicación
    numLikes = rad.randint(0, 15)
    usuariosLike = rad.sample(usuariosUnicos, min(numLikes, totalUsuarios))
    listaLikes.append(";".join(usuariosLike))

#archivo final
df['liked_by'] = listaLikes
df.to_csv("datasetFinal.csv", index=False)