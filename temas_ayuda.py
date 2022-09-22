import tkinter as tk
from tkinter.font import BOLD

class temas_ayuda:
    
    def __init__ (self):
        self.ventana = tk.Tk()
        self.configurar_ventana()
        tk.Wm.title(self.ventana, f"Temas de ayuda")
        self.ventana.mainloop()
        
    def configurar_ventana(self):
        #dando tamaño a la ventana
        self.ventana.geometry("420x370")
        #creando etiquetas
        uni = tk.Label(self.ventana, text="Universidad de San Carlos de Guatemala", font=("Arial", 12, BOLD))
        uni.place(x = 50, y=50)
        curso = tk.Label(self.ventana, text="Lab. Lenguajes Formales y de Programación", font=("Arial", 12, BOLD))
        curso.place(x = 40, y=75)
        nombre = tk.Label(self.ventana, text="Nombre: Aldo Saúl Vásquez Moreira", font=("Arial", 12, BOLD))
        nombre.place(x = 70, y=100)
        carnet = tk.Label(self.ventana, text="Carnet: 202109754", font=("Arial", 12, BOLD))
        carnet.place(x = 130, y=125)
        #cambiando color
        self.ventana.configure(bg="#8FEBD6")