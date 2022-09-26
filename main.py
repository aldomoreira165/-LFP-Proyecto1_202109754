from importlib.resources import path
import tkinter as tk
import subprocess
import sys
from tkinter import scrolledtext as st
from tkinter.font import BOLD
from tkinter import filedialog as fd
from tkinter import messagebox as mb 
from etiqueta_tipo import EtiquetaTipo
from etiqueta_operacion import EtiquetaOperacion
from operacion import Operacion
from generadorHTML import generadorHTML
from tkinter import messagebox
from temas_ayuda import temas_ayuda

class VentanaPrincipal:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana, width=50, height=20)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        tk.Wm.title(self.ventana, f"Analizador léxico")
        self.ventana.mainloop()
        self.nombre_archivo = None
        
    def abrir_temas_ayuda(self):
        ventana = temas_ayuda()
    
    def abrir_manual_usuario(self):
        path = "Manuales/Manual de Usuario.pdf"
        subprocess.Popen([path], shell=True)
    
    def abrir_manual_tecnico(self):
        path = "Manuales/Manual Técnico.pdf"
        subprocess.Popen([path], shell=True)
    
    def agregar_menu(self):
        barra_menus = tk.Menu(self.ventana)
        #cascada de menu archivo
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Abrir", command=self.abrir)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_command(label="Guardar Como", command=self.guardar_como)
        menu_archivo.add_command(label="Analizar", command=self.analizar)
        menu_archivo.add_command(label="Salir", command=self.salir)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        
        #cascada de menu ayuda
        menu_ayuda = tk.Menu(barra_menus, tearoff=False)
        menu_ayuda.add_command(label="Manual de Usuario", command=self.abrir_manual_usuario)
        menu_ayuda.add_command(label="Manual Técnico", command=self.abrir_manual_tecnico)
        menu_ayuda.add_command(label="Temas de Ayuda", command=self.abrir_temas_ayuda)
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        
        self.ventana.config(menu=barra_menus, bg="#8FEBD6")

    def salir(self):
        sys.exit(0)
        
    def guardar_como(self):
        self.nombre_archivo = fd.asksaveasfilename(title = "Guardar como", filetypes=(("xml files", "*.txt"), ("todos los archivos", "*.*")))
        if self.nombre_archivo != "":
            archivo = open(self.nombre_archivo, "w", encoding="utf-8")
            archivo.write(self.scrolledtext1.get("1.0", tk.END))
            archivo.close()
            mb.showinfo("información", "El archivo se guardó correctamente")
        
    def guardar(self):
        archivo = open(self.nombre_archivo, "w", encoding="utf-8")
        archivo.write(self.scrolledtext1.get("1.0", tk.END))
        archivo.close()
        mb.showinfo("información", "El archivo se guardó correctamente")
    
    def abrir(self):
        self.nombre_archivo = fd.askopenfilename(title="Seleccione el archivo", filetypes=(("txt file", "*.txt"), ("todos los arhivos", "*.*")))
        if self.nombre_archivo != " ":
            archivo = open(self.nombre_archivo, "r", encoding="utf-8")
            contenido = archivo.read()
            archivo.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
            
    def analizar(self):
        datos = []
        num_linea = 0
        operacion = None
        total_lineas = 0
        with open(self.nombre_archivo, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.replace(" ", "")
                linea = linea.replace("\n", "")
                linea = linea.replace("\t", "")
                datos.append(linea)
                
        #creando html de errores
        html_errores = open("ERRORES_202109754.html", "w")
        html_errores.write("<title>Errores</title>")
        html_errores.write("<h1>Generacion Archivo de Errores HTML</h1>")
        html_errores.write("<table border=1>")
        html_errores.write("<tr><th>Tipo</th><th>Fila</th></tr>")

        #creando html de resultados        
        html = open("RESULTADOS_202109754.html", "w")
        html.write("<title>Resultados</title>")
        html.write("<h1>Generacion Archivo HTML</h1>")
        
        #realizando analisis del archivo por medio de los automatas finitos
        etiqueta_tipo = EtiquetaTipo(datos[num_linea])
        if etiqueta_tipo.apertura() == True:
            num_linea += 1           
             
            #iniciando creacion de archivo html
            linea_html = 0
            texto = " "
                
            #buscando apertura de etiqueta texto
            while generadorHTML(datos[linea_html]).textoApertura() == False:
                linea_html += 1
        
            if generadorHTML(datos[linea_html]).textoApertura() == True:
                linea_html += 1
                while generadorHTML(datos[linea_html]).textoCierre() == False:
                    texto += datos[linea_html]
                    linea_html += 1
            else:
                pass
            
            html.write(f"<p>{texto}</p>")
            estado = True
            csuma = 0
            cresta = 0
            cmulti = 0
            cdivi = 0
            cpote = 0
            craiz = 0
            cinverso = 0
            cseno = 0
            ccoseno = 0
            ctan = 0
            cmod = 0
                        
            #verificando el tipo de operacion
            while estado == True:
                if EtiquetaTipo(datos[num_linea]).cierre() == False:
                    etiqueta_operacion = EtiquetaOperacion(datos[num_linea])
                    if etiqueta_operacion.apertura() == "<Operacion=SUMA>":
                        csuma += 1
                        operacion = "suma"
                        num_linea += 1
                        html.write(f"<p>Operacion {operacion} {csuma}:</p>")
                    elif etiqueta_operacion.apertura() == "<Operacion=RESTA>":
                        cresta += 1
                        operacion = "resta"
                        html.write(f"<p>Operacion {operacion} {cresta}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=MULTIPLICACION>":
                        cmulti += 1
                        operacion = "multiplicacion"
                        html.write(f"<p>Operacion {operacion} {cmulti}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=DIVISION>":
                        cdivi += 1
                        operacion = "division"
                        html.write(f"<p>Operacion {operacion} {cdivi}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=POTENCIA>":
                        cpote += 1
                        operacion = "potencia"
                        html.write(f"<p>Operacion {operacion} {cpote}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=RAIZ>":
                        craiz += 1
                        operacion = "raiz"
                        html.write(f"<p>Operacion {operacion} {craiz}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=INVERSO>":
                        cinverso += 1
                        operacion = "inverso"
                        html.write(f"<p>Operacion {operacion} {cinverso}</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=SENO>":
                        cseno += 1
                        operacion = "seno"
                        html.write(f"<p>Operacion {operacion} {cseno}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=COSENO>":
                        ccoseno += 1
                        operacion = "coseno"
                        html.write(f"<p>Operacion {operacion} {ccoseno}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=TANGENTE>":
                        ctan += 1
                        operacion = "tangente"
                        html.write(f"<p>Operacion {operacion} {ctan}:</p>")
                        num_linea += 1
                    elif etiqueta_operacion.apertura() == "<Operacion=MOD>":
                        cmod += 1
                        operacion = "mod"
                        html.write(f"<p>Operacion {operacion} {cmod}:</p>")
                        num_linea += 1
                    else:
                        if etiqueta_operacion.cierre() == False and etiqueta_operacion.apertura() == False:
                            html_errores.write(f"<tr><td>Error</td><td>{num_linea+1}</td></tr>")
                            messagebox.showerror(message="Verifique los detalles del error", title="Error")
                            estado = False
                        else:
                            pass
                        
                    if estado == True:    
                        #tomando los datos de cada operacion segun su tipo
                        op = Operacion(num_linea, datos, operacion)
                        resultado, num_linea = op.obtenerResultados()
                        html.write(f"<p>{resultado}</p>")
                    else:
                        pass
                else:
                    break
        else:
            html_errores.write(f"<tr><td>Error</td><td>{num_linea+1}</td></tr>")
            messagebox.showerror(message="Verifique los detalles del error", title="Error")
            
        #cerrando documentos html
        html_errores.write("</table>")  
        html.close()
        html_errores.close()
        messagebox.showinfo(message="Análisis terminado correctamente")
            
aplicacion = VentanaPrincipal()