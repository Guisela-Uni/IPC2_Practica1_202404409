from clases.materialBiblioteca import materialBiblioteca

class mastermind:
    def __init__(self):
        self.libros = [] #lista que va a guardar los libros

    def nuevoLibro(self, libro: materialBiblioteca): #el parametro libro, debe ser una instancia de la clse materialBiblioteca
        self.libros.append(libro) #añade un objeto materialBiblioteca a la lista libros

    def mostrarLibros(self):
        for libro in self.libros:
            libro.mostrarInfo()

    def buscarPorCodigo(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                libro.mostrarInfo()

    def eliminarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)

