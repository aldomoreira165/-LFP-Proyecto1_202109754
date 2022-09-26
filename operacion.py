from etiqueta_operacion import EtiquetaOperacion
from etiqueta_numero import EtiquetaNumero
import math

class Operacion: 
    
    def __init__ (self, num_linea, datos, operacion):
        self.num_linea = num_linea
        self.datos = datos
        self.operacion = operacion
        
    #metodo para retonar los valores de cada operacion  
    def obtenerValores(self, num_linea):
        contador = 0
        veces = 0
        operandos = []
        while EtiquetaOperacion(self.datos[num_linea]).cierre() != True:
            if EtiquetaOperacion(self.datos[num_linea]).apertura() == False:
                etiqueta_numero = EtiquetaNumero(self.datos[num_linea])
                retorno = etiqueta_numero.apertura()
                if retorno != False:
                    operandos.append(retorno)
                    num_linea += 1
                    contador += 1
                else:
                    break
            else:
                if veces == 0:
                    etiqueta_operacion = EtiquetaOperacion(self.datos[num_linea])
                    if etiqueta_operacion.apertura() == "<Operacion=SUMA>":
                        operacion = "suma"
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=RESTA>":
                        operacion = "resta"
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=MULTIPLICACION>":
                        operacion = "multiplicacion"
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=DIVISION>":
                        operacion = "division"
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=MOD>":
                        operacion = "mod"
                        num_linea += 1
                    valores, cont = self.obtenerValores(num_linea)
                    resultado = self.retornar_resultado_anidado(operacion, valores)
                    num_linea += cont
                    print("ejecutado metodo")
                    operandos.append(resultado)
        num_linea += 1
        contador += 1
        if retorno != False:                    
            return [operandos, contador]
        else:
            return [False, contador]
        
    #metodo retornar detos ya operados
    def retornar_resultado_anidado(self, operacion,datos):
        total = 0
        cont = 0
        if operacion == "suma":
            total = 0
            cont = 0
            for i in datos: 
                total += i
        elif operacion == "resta":
            total = 0
            cont = 0
            for i in datos:
                cont += 1 
                if cont == 1:
                    total = i
                else: 
                    total -= i
        elif operacion == "multiplicacion":
            total = 0
            cont = 0
            for i in datos:
                cont += 1
                if cont == 1:
                    total = i
                else: 
                    total *= i
        elif operacion == "division":
            total = 0
            cont = 0
            for i in datos:
                cont += 1 
                if cont == 1:
                    total = i
                else: 
                    total /= i
        elif operacion == "mod":
            total = 0
            cont = 0
            for i in datos:
                cont += 1 
                if cont == 1:
                    total = i
                else: 
                    total %= i
        return total
        
    #metodo para operar 
    def operar(self, datos):
        if self.operacion == "suma":
            total = 0
            cadena = ""
            cont = 0
            for i in datos:
                cont += 1
                cadena += str(i)  
                if cont == (len(datos)):
                    pass
                else:
                    cadena += "+" 
                total += i
            cadena += "="
            cadena += str(round(total,2))
        elif self.operacion == "resta":
            total = 0
            cadena = ""
            cont = 0
            for i in datos:
                cont += 1
                cadena += str(i)  
                if cont == (len(datos)):
                    pass
                else:
                    cadena += "-"
                if cont == 1:
                    total = i
                else: 
                    total -= i
            cadena += "="
            cadena += str(round(total,2))
        elif self.operacion == "multiplicacion":
            total = 0
            cadena = ""
            cont = 0
            for i in datos:
                cont += 1
                cadena += str(i)  
                if cont == (len(datos)):
                    pass
                else:
                    cadena += "*" 
                if cont == 1:
                    total = i
                else: 
                    total *= i
            cadena += "="
            cadena += str(round(total,2))
        elif self.operacion == "division":
            total = 0
            cadena = ""
            cont = 0
            for i in datos:
                cont += 1
                cadena += str(i)  
                if cont == (len(datos)):
                    pass
                else:
                    cadena += "/" 
                if cont == 1:
                    total = i
                else: 
                    total /= i
            cadena += "="
            cadena += str(round(total,2))
        elif self.operacion == "potencia":
            total = datos[0]**datos[1]
            cadena = str(datos[0])+"^"+str(datos[1])+"="+str(round(total,2))
        elif self.operacion == "raiz":
            total = pow(datos[0], 1/datos[1])
            cadena = "sqrt"+"("+str(datos[0])+")"+"="+str(round(total,2))
        elif self.operacion == "inverso":
            total = (1/datos[0])
            cadena = str(datos[0])+"^-1"+"="+str(round(total,2))
        elif self.operacion == "seno":
            total = math.sin(datos[0])
            cadena = "sin("+str(datos[0])+")"+"="+str(round(total,2))
        elif self.operacion == "coseno":
            total = math.cos(datos[0])
            cadena = "cos("+str(datos[0])+")"+"="+str(round(total,2))
        elif self.operacion == "tangente":
            total = math.tan(datos[0])
            cadena = "tan("+str(datos[0])+")"+"="+str(round(total,2))
        elif self.operacion == "mod":
            total = 0
            cadena = ""
            cont = 0
            for i in datos:
                cont += 1
                cadena += str(i)  
                if cont == (len(datos)):
                    pass
                else:
                    cadena += "%" 
                if cont == 1:
                    total = i
                else: 
                    total %= i
            cadena += "="
            cadena += str(round(total,2))
        return cadena
                
    def obtenerResultados(self):
        error = False
        linea = 0
        resultado = ""
        if self.operacion == "suma":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "resta":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "multiplicacion":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "division":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")    
        elif self.operacion == "potencia":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "raiz":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "inverso":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "seno":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "coseno":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "tangente":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        elif self.operacion == "mod":
            if self.obtenerValores(self.num_linea)[0] != False:
                operandos, contador = self.obtenerValores(self.num_linea)
                resultado = self.operar(operandos)
                self.num_linea += contador
            else:
                print(f"Error en la linea {self.num_linea+self.obtenerValores(self.num_linea)[1]}")
        
        return resultado, self.num_linea