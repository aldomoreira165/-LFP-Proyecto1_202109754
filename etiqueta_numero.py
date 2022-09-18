
class EtiquetaNumero:
    
    def __init__ (self, linea):
        self.linea = linea
        
    def apertura(self):
        cadenaUno = ""
        cadenaDos = ""
        numero = ""
        self.estado = 1
        
        for i in range(0, len(self.linea)):
            self.transicion = self.linea[i]
            if self.estado == 1:
                if self.transicion == "<":
                    cadenaUno += self.transicion
                    self.estado = 2
            elif self.estado == 2:
                if self.transicion.isalpha() and self.linea[i+1] != ">":
                    cadenaUno += self.transicion
                    self.estado = 2
                elif self.transicion.isalpha() and self.linea[i+1] == ">":
                    cadenaUno += self.transicion
                    self.estado = 3
            elif self.estado == 3:
                if self.transicion == ">":
                    cadenaUno += self.transicion
                    if self.linea[i+1] == "+" or self.linea[i+1] == "-":
                        self.estado = 4 
                    elif self.linea[i+1].isnumeric():
                        self.estado = 5
            elif self.estado == 4:
                if self.transicion == "+" or self.transicion == "-":
                    numero += self.transicion
                    self.estado = 5
            elif self.estado == 5:
                if self.transicion.isnumeric() and self.linea[i+1] != "." and self.linea[i+1] != "<":
                    numero += self.transicion
                    self.estado = 5
                elif self.transicion.isnumeric() and self.linea[i+1] == ".":
                    numero += self.transicion
                    self.estado = 6
                elif self.transicion.isnumeric() and self.linea[i+1] == "<":
                    numero += self.transicion
                    numero = int(numero)
                    self.estado = 7
            elif self.estado == 6:
                if self.transicion == ".":
                    numero += self.transicion
                    self.estado = 8
            elif self.estado ==  8:
                if self.transicion.isnumeric() and self.linea[i+1] != "<":
                    numero += self.transicion
                    self.estado = 8
                elif self.transicion.isnumeric() and self.linea[i+1] == "<":
                    numero += self.transicion
                    numero = float(numero)
                    self.estado = 7
            elif self.estado == 7:
                if self.transicion == "<":
                    cadenaDos += self.transicion
                    self.estado = 9
            elif self.estado == 9:
                if self.transicion == "/":
                    cadenaDos += self.transicion
                    self.estado = 10
            elif self.estado == 10:
                if self.transicion.isalpha() and self.linea[i+1] != ">":
                    cadenaDos += self.transicion
                    self.estado = 10
                elif self.transicion.isalpha() and self.linea[i+1] == ">":
                    cadenaDos += self.transicion
                    self.estado = 11
            elif self.estado == 11:
                if self.transicion == ">":
                    cadenaDos += self.transicion
                    self.estado = 12
                                    
        if cadenaUno == "<Numero>" and cadenaDos == "</Numero>":
            return numero
        else:
            return False
        