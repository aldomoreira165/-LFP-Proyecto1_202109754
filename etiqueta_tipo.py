class EtiquetaTipo:

    def __init__(self, linea):
        self.linea = linea

    def apertura(self):
        cadena = ""
        self.estado = 1
        for i in range(0, len(self.linea)):
            self.transicion = self.linea[i]
            if self.transicion == " " or self.transicion == "\t":
                pass
            else: 
                if self.estado == 1:
                    if self.transicion == "<":
                        self.estado = 2
                elif self.estado == 2:
                    if self.transicion.isalpha() and self.linea[i+1] != ">":
                        cadena += self.transicion
                        self.estado = 2
                    elif self.transicion.isalpha() and self.linea[i+1] == ">":
                        cadena += self.transicion
                        self.estado = 3
                    elif self.transicion.isalpha() == False:
                        return False
                elif self.estado == 3:
                    if self.transicion == ">": 
                        self.estado = 3
        if cadena == "Tipo":
            return True
        else:
            return False