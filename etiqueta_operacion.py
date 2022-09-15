class EtiquetaOperacion: 
    
    def __init__(self, linea): 
        self.linea = linea
        
    def apertura(self):
        cadena = ""
        self.estado = 1
        for i in range(0, len(self.linea)):
            self.transicion = self.linea[i]
            if self.estado == 1:
                if self.transicion == "<":
                    self.estado = 2
            elif self.estado == 2:
                if self.transicion.isalpha() and self.linea[i+1] != "=":
                    cadena += self.transicion
                    self.estado = 2
                elif self.transicion.isalpha() and self.linea[i+1] == "=":
                    cadena += self.transicion
                    self.estado = 3
            elif self.estado == 3:
                if self.transicion == "=":
                    cadena += self.transicion
                    self.estado = 4
            elif self.estado == 4:
                if self.transicion.isalpha() and self.linea[i+1] != ">":
                    cadena += self.transicion
                    self.estado = 4
                elif self.transicion.isalpha() and self.linea[i+1] == ">":
                    cadena += self.transicion
                    self.estado = 5
            elif self.estado == 5:
                if self.transicion == ">":
                    self.estado = 5
        return cadena
    
    def cierre(self):
        cadena = ""
        self.estado = 1
        for i in range(0, len(self.linea)):
            self.transicion = self.linea[i]
            if self.estado == 1:
                if self.transicion == "<":
                    cadena += self.transicion
                    self.estado = 2
            elif self.estado == 2:
                if self.transicion == "/":
                    cadena += self.transicion
                    self.estado = 3
            elif self.estado == 3:
                if self.transicion.isalpha() and self.linea[i+1] != ">":
                    cadena += self.transicion
                    self.estado = 3
                elif self.transicion.isalpha() and self.linea[i+1] == ">":
                    cadena += self.transicion
                    self.estado = 4
                elif self.transicion.isalpha() == False:
                    return False
            elif self.estado == 4:
                if self.transicion == ">":
                    cadena += self.transicion 
                    self.estado = 4
        if cadena == "</Operacion>":
            return True
        else:
            return False
                    
                    