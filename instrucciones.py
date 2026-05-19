#vamos a usar nlpk https://www.geeksforgeeks.org/nlp/removing-stop-words-nltk-python/ 
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stopwords = set(stopwords.words('english'), set(stopwords.words('spanish')))


class nodoPost: 
    def __init__(self, autor, texto, likes):
        self.autor = autor
        self.texto = texto
        self.likes = likes
        self.siguiente = None

class NodoContacto:
    def __init__(self, nombreAmigo):
        self.nombreAmigo = nombreAmigo
        self.siguiente = None

class ListaEnlazadaPosts:
    def __init__(self):
        self.cabeza = None

    def insertar(self, autor, texto, likes):
        nuevoNodo = nodoPost(autor, texto, likes)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

class ListaEnlazadaContactos:
    def __init__(self):
        self.cabeza = None

    def insertar(self, nombre_amigo):
        nuevoNodo = NodoContacto(nombre_amigo)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo