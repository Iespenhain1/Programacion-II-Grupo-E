import tkinter as tk
from tkinter import messagebox

def mostrarEdad():
    tk.messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
def mostrarGenero():
    tk.messagebox.showinfo("Género", f"El género seleccionado es: {genero.get()}")
    
ventana=tk.Tk()
ventana.title("Ejemplo con edad")
ventana.configure(bg="LightBlue")
labelEdad=tk.Label(ventana, text="Edad")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventana, from_=1, to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana, text="Obtener valor", command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
#Género
labelGenero=tk.Label(ventana, text="Género")
labelGenero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
#SpinBox de texto para género
genero=tk.Spinbox(ventana, values=("Masculino","Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
botonGenero=tk.Button(ventana, text="Obtener género", command=mostrarGenero)
botonGenero.grid(row=3, column=0, padx=10, pady=10)

ventana.mainloop()