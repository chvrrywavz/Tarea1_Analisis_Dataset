class NodoPost:
    def __init__(self, id_post, texto):
        self.id_post = id_post      
        self.texto = texto         
        self.likes = []            
        self.siguiente = None       # Puntero al siguiente nodo (solo python)
class ListaEnlazadaPosts:
    def __init__(self):
        self.cabeza = None         
    def insertar(self, id_post, texto):
        nuevoNodo = NodoPost(id_post, texto)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevoNodo
        
    def agregar_likes_a_post(self, id_post, lista_likes):
        actual = self.cabeza
        while actual is not None:
            if actual.id_post == id_post:
                actual.likes = lista_likes
                return
            actual = actual.siguiente