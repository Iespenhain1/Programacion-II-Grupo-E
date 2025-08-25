import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Crear ventana principal
ventana=tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")
ventana.configure(bg="LightBlue")
#Etiqueta
etiqueta=tk.Label(ventana, text="Seleccione especialidad:")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")
etiqueta.configure(bg="LightBlue")
#Crear combobox
opciones=["Cardiología", "Neurología", "Pediatría","Dermatología"]
combo=ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0) #selecciona primera opcion por defecto
combo.grid(row=0, column=1, padx=10, pady=10)
#Función para nostrar la selección
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Selección", f"Has elegido: {seleccion}")
#Botón para confirmar selección
boton=tk.Button(ventana, text="Aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()