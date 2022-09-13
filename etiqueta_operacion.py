class Operacion: 
    
    def __init__(self, linea): 
        self.linea = linea
        
    def apertura(self):
        cadena = ""
        self.estado = 1
        for i in range(len(self.linea)):
            self.transicion = self.linea[i]
            if self.transicion == " " or self.transicion == "\t":
                pass
            else: 
                