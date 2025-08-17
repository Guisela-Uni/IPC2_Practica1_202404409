class materialBiblioteca:
    def __init__(self, titulo, autor, codigo): #atributos de la clase
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.estado = True #disponible/NO prestado= True ; PRESTADO/ NO disponible= False

    #Métodos
    def prestarLibro(self):
        self.estado = False

    def devolverLibro(self):
        self.estado = True

    def mostrarInfo(self):
        print(f"-" + "-" * 61)
        # "*" * 5 = "*****"
        print(f"|{"Biblioteca":^61}|")
        print(f"|" + "-" *30 + "|" + "-" * 30 + "|")
        print(f"|{"Titulo":<30}|{self.titulo:<30}|")
        print(f"|{"autor:":<30}|{self.autor:<30}|")
        print(f"|{"codigo:":<30}|{self.codigo:<30}|")
        print(f"|{"Estado:":<30}|{self.estado:<30}|")
        print(f"-" + "-" * 61)

#GETTERS-> acceder a los atributos
    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getCodigo(self):
        return self.codigo
    
    def getEstado(self):
        return self.estado    

#SETTERS-> modificar los atributos
    def setTitulo(self, titulo):
        self.titulo = titulo

    def setAutor(self, autor):
        self.autor = autor

    def setCodigo(self, codigo):
        self.codigo = codigo
        
    def setEstado (self, estado):
        self.estado = estado