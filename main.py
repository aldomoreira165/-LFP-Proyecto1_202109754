import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter.font import BOLD
from tkinter import filedialog as fd
from tkinter import messagebox as mb 
from etiqueta_tipo import EtiquetaTipo
from etiqueta_operacion import EtiquetaOperacion
from etiqueta_numero import EtiquetaNumero

class VentanaPrincipal:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana, width=50, height=20)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        tk.Wm.title(self.ventana, f"Analizador léxico")
        self.ventana.mainloop()
        self.nombre_archivo = None
        
    def agregar_menu(self):
        barra_menus = tk.Menu(self.ventana)
        
        #cascada de menu archivo
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Abrir", command=self.abrir)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_command(label="Guardar Como", command=self.guardar_como)
        menu_archivo.add_command(label="Analizar", command=self.analizar)
        menu_archivo.add_command(label="Errores")
        menu_archivo.add_command(label="Salir", command=self.salir)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        
        #cascada de menu ayuda
        menu_ayuda = tk.Menu(barra_menus, tearoff=False)
        menu_ayuda.add_command(label="Manual de Usuario")
        menu_ayuda.add_command(label="Manual Técnico")
        menu_ayuda.add_command(label="Temas de Ayuda")
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        
        self.ventana.config(menu=barra_menus)

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
        with open(self.nombre_archivo, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos.append(linea.strip("\n"))
        
        etiqueta_tipo = EtiquetaTipo(datos[num_linea])
        if etiqueta_tipo.apertura() == True:
            num_linea += 1
            etiqueta_operacion = EtiquetaOperacion(datos[num_linea])
            if etiqueta_operacion.apertura() == "Operacion=SUMA":
                operacion = "Suma"
                num_linea += 1
            
            etiqueta_numero = EtiquetaNumero(datos[num_linea])
            print(etiqueta_numero.apertura())
            
        
aplicacion = VentanaPrincipal()