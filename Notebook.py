#Importación de librerías
import tkinter as tk
from tkinter import messagebox, ttk
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#Crear contenedor NoteBook(Pestañas)
Pestañas=ttk.Notebook(ventana_principal)
#Crear Frames(uno por pestaña)
frame_pacientes=ttk.Frame(Pestañas)
frame_doctores=ttk.Frame(Pestañas)
#Agregar pastañas al Notebook
Pestañas.add(frame_pacientes, text="Pacientes")
Pestañas.add(frame_doctores, text="Doctores")
#Mostrar las pestañas en la ventana
Pestañas.pack(expand=True, fill="both")
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo :")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento :")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad :")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#Género
labelGenero=tk.Label(frame_pacientes, text="Género :")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", pady=5, padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", pady=5, padx=5)
#Grupo sanguíneo
labelGrupoSanguíneo=tk.Label(frame_pacientes, text="Grupo Sanguíneo :")
labelGrupoSanguíneo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguíneo=tk.Entry(frame_pacientes)
entryGrupoSanguíneo.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#Tipo de seguro
labelTipoDeSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro :")
labelTipoDeSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público") #Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#Centro Médico
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud :")
labelCentroMedico.grid(row=7, column=0, sticky="w", pady=5, padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", pady=5, padx=5)

ventana_principal.mainloop()