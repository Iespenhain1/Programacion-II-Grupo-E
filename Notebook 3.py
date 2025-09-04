#Importación de librerías
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

#funcion enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=''
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)      
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set('')
    return True
        

#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x600")
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
#Llamado a la funcion de enmascarar fecha
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate='key', validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad :")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar, state="readonly")
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
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0,columnspan=2, sticky="w", pady=5)
#Botón registrar
btn_registrar=tk.Button(btn_frame, text="Registar", command="")
btn_registrar.grid(row=0, column=0, padx=5)
#Botón eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)
#Crear TreeView para mostrar pacientes
treeView=ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")
#Definir encabezados
treeView.heading("Nombre", text="Nombre Completo")
treeView.heading("FechaN", text="Fecha Nacimiento")
treeView.heading("Edad", text="Edad")
treeView.heading("Genero", text="Género")
treeView.heading("GrupoS", text="Grupo Sanguínero")
treeView.heading("TipoS", text="Tipo Seguro")
treeView.heading("CentroM", text="Centro Médico")
#Definir anchos de columnas
treeView.column("Nombre", width=120)
treeView.column("FechaN", width=120)
treeView.column("Edad", width=50, anchor="center")
treeView.column("Genero", width=60, anchor="center")
treeView.column("GrupoS", width=100, anchor="center")
treeView.column("TipoS", width=100, anchor="center")
treeView.column("CentroM", width=120)
#Ubicar el treeview en la cuadricula
treeView.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar vertical
Scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeView.yview)
treeView.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=7, column=2, sticky="ns")

#Titulo
Titulo=tk.Label(frame_doctores, text="REGISTRO DE DOCTORES")
Titulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#Nombre-Doctor
labelNombre=tk.Label(frame_doctores, text="Nombre Completo :")
labelNombre.grid(row=1, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Especialidad
etiqueta=tk.Label(frame_doctores, text="Especialidad :")
etiqueta.grid(row=2, column=0, padx=5, pady=5, sticky="w")
opciones=["Cardiología", "Neurología", "Pediatría","Dermatología"]
combo=ttk.Combobox(frame_doctores, values=opciones, state="readonly")
combo.current(0) #selecciona primera opcion por defecto
combo.grid(row=2, column=1, padx=5, pady=5,sticky="W")
#Edad
labelEdad=tk.Label(frame_doctores, text="Edad :")
labelEdad.grid(row=3, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frame_doctores, from_=1, to=100)
spin.grid(row=3, column=1, padx=5, pady=5,sticky="w")
#Telefono
labelTelefono=tk.Label(frame_doctores, text="Teléfono :")
labelTelefono.grid(row=4, column=0, sticky="w", pady=5, padx=5)
Telefono=tk.Entry(frame_doctores)
Telefono.grid(row=4, column=1, sticky="w", pady=5, padx=5)
#Frame para los botones
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=5, column=0,columnspan=2, sticky="w", pady=5)
#Botón registrar
btn_registrar=tk.Button(btn_frame, text="Registar", command="")
btn_registrar.grid(row=0, column=0, padx=5)
btn_registrar.configure(bg="Green")
#Botón eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)
btn_eliminar.configure(bg="Red")
#Crear TreeView para mostrar pacientes
treeView=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
#Definir encabezados
treeView.heading("Nombre", text="Nombre Completo")
treeView.heading("Especialidad", text="Especialidad")
treeView.heading("Edad", text="Edad")
treeView.heading("Telefono", text="Teléfono")
#definir anchos
treeView.column("Nombre", width=120)
treeView.column("Especialidad", width=120)
treeView.column("Edad", width=50, anchor="center")
treeView.column("Telefono", width=120)
#Ubicar el treeview en la cuadricula
treeView.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar vertical
Scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeView.yview)
treeView.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=6, column=2, sticky="ns")

ventana_principal.mainloop()
