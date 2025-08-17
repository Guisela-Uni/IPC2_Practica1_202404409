from clases.materialBiblioteca import materialBiblioteca #importando la clase padre, para heredar

class lbroFisico(materialBiblioteca):
    def __init__(self, titulo, autor, codigo, ejemplar):
        super.__init__(titulo, autor, codigo) #heredando atributos
        self.ejemplar == ejemplar #atributo propio

#Metodos
    def mostrarInfo(self):
        print(f"-" + "-" * 61)
        # "*" * 5 = "*****"
        print(f"|{"Biblioteca":^61}|")
        print(f"|" + "-" *30 + "|" + "-" * 30 + "|")
        print(f"|{"Titulo":<30}|{self.titulo:<30}|")
        print(f"|{"autor:":<30}|{self.autor:<30}|")
        print(f"|{"codigo:":<30}|{self.codigo:<30}|")
        print(f"|{"Estado:":<30}|{self.estado:<30}|")
        print(f"|{"No.Ejemplar:":<30}|{self.ejemplar:<30}|")
        print(f"-" + "-" * 61)

#GETTERS
    def getEjemplar(self):
        return self.ejemplar
#SETTERS
    def setEjemplar(self, ejemplar):
        set.ejemplar == ejemplar
