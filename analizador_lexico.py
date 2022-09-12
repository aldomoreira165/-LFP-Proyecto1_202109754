
class analizador:
    
    def __init__(self, texto):
        self.texto = texto
        
    def etiquetaTipo(self):  
        self.estado = 1
        for i in range(0, len(self.texto)):
            self.transicion = self.texto[i]
            if self.estado == 1:
                if self.transicion == "<":
                    self.estado = 2
                else:
                    return False
            elif self.estado == 2:
                if self.transicion == "T":
                    self.estado = 3
                else:
                    return False
            elif self.estado == 3:
                if self.transicion == "i" or self.transicion == "p":
                    self.estado =  3
                elif self.transicion == "o":
                    self.estado = 4
                else:
                    return False
            elif self.estado == 4:
                if self.transicion == ">":
                    self.estado == 4 
                else:
                    return False
        if self.estado == 4:
            return True
        else:
            return False
        

            