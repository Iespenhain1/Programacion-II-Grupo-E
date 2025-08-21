import tkinter as tk
from tkinter import messagebox #Para utilizar messagebox

#funcion Enviar datos
def enviarDatos():
    nombre1=nombreEntry.get()
    edad1=edadEntry.get()
    messagebox.showinfo("Datos del paciente", f"Nombre: {nombre1}\n Edad: {edad1}")
#Creacion de la ventana
ventana=tk.Tk()
ventana.title("Registro de pacientes")
ventana.geometry("600x600")
ventana.configure(bg="LightSteelBlue")
#Pedir nombre
nombreLabel=tk.Label(ventana, text="Nombre:")
nombreLabel.grid(row=0, column=0, padx=5, pady=5)
nombreEntry=tk.Entry(ventana)
nombreEntry.grid(row=0, column=1, padx=5, pady=5)
#Pedir edad
edadLabel=tk.Label(ventana, text="Edad:")
edadLabel.grid(row=1, column=0, padx=5, pady=5)
edadEntry=tk.Entry(ventana)
edadEntry.grid(row=1, column=1, padx=5, pady=5)
#Boton para enviar datos a una ventana
botonEnviar=tk.Button(ventana, text="Enviar datos", command=enviarDatos) #Metodo para programar una funcion
botonEnviar.grid(row=3, column=0, padx=5, pady=5)

ventana.mainloop() # Fin, cierre de ventanas