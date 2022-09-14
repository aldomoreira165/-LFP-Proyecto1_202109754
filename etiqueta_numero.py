
class EtiquetaNumero:
    
    def __init__ (self, linea):
        self.linea = linea
        
    def apertura(self):
        cadena = ""
        numero = None
        self.estado = 1
        
        for i in range(0, len(self.linea)):
            self.transicion = self.linea[i]
            if self.transicion == " " or self.transicion == "\t":
                pass
            else:
                if self.estado == 1:
                    if self.transicion == "<":
                        cadena += self.transicion
                        self.estado = 2
                elif self.estado == 2:
                    if self.transicion.isalpha() and self.linea[i+1] != ">":
                        cadena += self.transicion
                        self.estado = 2
                    elif self.transicion.isalpha() and self.linea[i+1] == ">":
                        cadena += self.transicion
                        self.estado = 3
                elif self.estado == 3:
                    if self.transicion == ">":
                        cadena += self.transicion
                        self.estado = 4
                elif self.estado == 4:
                    if self.transicion.isnumeric():
                        cadena += self.transicion
                        numero = int(self.transicion)
                        self.estado = 5
                elif self.estado == 5:
                    if self.transicion == "<":
                        cadena += self.transicion
                        self.estado = 6
                elif self.estado == 6:
                    if self.transicion == "/":
                        cadena += self.transicion
                        self.estado = 7
                elif self.estado == 7:
                    if self.transicion.isalpha() and self.linea[i+1] != ">":
                        cadena += self.transicion
                        self.estado = 7
                    elif self.transicion.isalpha() and self.linea[i+1] == ">":
                        cadena += self.transicion
                        self.estado = 8
                elif self.estado == 8:
                    cadena += self.transicion
                    self.estado = 8
                        
        return numero