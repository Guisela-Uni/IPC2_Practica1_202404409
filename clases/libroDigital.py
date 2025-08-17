from clases.materialBiblioteca import materialBiblioteca #importando la clase padre, para heredar

class libroDigital(materialBiblioteca):
    def __init__(self, titulo, autor, codigo, pesoArchivo):
        super().__init__(titulo, autor, codigo) #heredando atributos
        self.pesoArchivo = pesoArchivo #atributo propio: tamaño del archivo

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
        print(f"|{"Tamaño del archivo:":<30}|{self.pesoArchivo:<30}|")
        print(f"-" + "-" * 61)

    def getPesoArchivo(self):
        return self.pesoArchivo
    
    def setPesoArchivo(self, pesoArchivo):
        self.pesoArchivo = pesoArchivo