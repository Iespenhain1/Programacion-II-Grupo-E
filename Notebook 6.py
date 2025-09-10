#Importación de librerías
import tkinter as tk
from tkinter import messagebox,ttk
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
#Guardar en archivo paciente
def guardar_en_archivo():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                          f"{paciente['Genero']}|{paciente['Grupo Sanguíneo']}|"f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n")
#Guardar en archivo doctores
def guardar_en_archivo_doctor():
    with open("doctor.txt","w",encoding="utf-8") as archivoD:
        for doctor in Doctor_data:
            archivoD.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Teléfono']}\n")
#Cargar desde archivo paciente
def cargar_desde_archivo_pacientes():
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Genero":datos[3],
                        "Grupo Sanguíneo":datos[4],
                        "Tipo de Seguro":datos[5],
                        "Centro Medico":datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt", "w", encoding="utf-8").close()
#Función para eliminar paciente
def eliminarPaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Está seguro de eliminar el paciente'{treeview.item(id_item,'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo() #Guardar los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente")
    else: #Este else es del if seleccionado
        messagebox.showwarning("Eliminar Paciente","No se ha seleccionado ningún paciente")
        return 
#Cargar desde archivo doctor
def cargar_desde_archivo_doctores():
    try:
        with open("doctor.txt", "r", encoding="utf-8") as archivoD:
            Doctor_data.clear()
            for lineaD in archivoD:
                datosD=lineaD.strip().split("|")
                if len(datosD)==4:
                    doctor={
                        "Nombre":datosD[0],
                        "Especialidad":datosD[1],
                        "Edad":datosD[2],
                        "Teléfono":datosD[3]
                    }
                    Doctor_data.append(doctor)
        cargarD_treeview()
    except FileNotFoundError:
        open("doctor.txt", "w", encoding="utf-8").close()
#Función eliminar doctores
def eliminarDoctor():
    seleccionadoD=treeviewD.selection()
    if seleccionadoD:
        indiceD=int(seleccionadoD[0])
        id_itemD=seleccionadoD[0]
        if messagebox.askyesno("Eliminar Doctor", f"¿Está seguro de eliminar el doctor'{treeviewD.item(id_itemD,'values')[0]}'?"):
            del Doctor_data[indiceD]
            guardar_en_archivo_doctor()
            cargarD_treeview()
            messagebox.showinfo("Eliminar Doctor","Doctor eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Doctor","No se ha seleccionado ningún doctor")
        return
#Lista de pacientes (inicialmente vacia)
paciente_data=[]
#Funcion registrar paciente
def registrarPaciente():
    #Crear un diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Grupo Sanguíneo":entryGrupoSanguíneo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Medico":centro_medico.get()
    }
    #Agregar paciente a la lista
    paciente_data.append(paciente)
    #Linea modificada a la lista
    guardar_en_archivo()
    #Cargar al Treeview
    cargar_treeview()
def cargar_treeview():
    #Limpiar el TreeView
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i,item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Medico"]
            )
        )
#Funcion registrar doctor
Doctor_data=[]
#Funcion registrar doctor
def registrarDoctor():
    #Crear diccionario con los datos ingresados
    Doctor={
        "Nombre": nombreD.get(),
        "Especialidad": combo.get(),
        "Edad": spin.get(),
        "Teléfono": Telefono.get()      
    }
    #Agregar doctor a la lista
    Doctor_data.append(Doctor)
    #Lista modificada
    guardar_en_archivo_doctor()
    #Cargar al treeview
    cargarD_treeview()
def cargarD_treeview():
    #Limpiar el treeview
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    #Insertar cada paciente
    for i,item in enumerate(Doctor_data):
        treeviewD.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Teléfono"]                
            )
        )
#Evento al cambiar pestaña
def al_cambiar_pestaña(event):
    pestaña_activa=Pestañas.index(Pestañas.select())
    if pestaña_activa==0: #Pacientes
        cargar_desde_archivo_pacientes()
    elif pestaña_activa==1: #Doctores
        cargar_desde_archivo_doctores()
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
labelCentroMedico.grid(row=8, column=0, sticky="w", pady=5, padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=8, column=1, sticky="w", pady=5, padx=5)
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=19, column=0,columnspan=2, sticky="w", pady=5)
#Botón registrar
btn_registrar=tk.Button(btn_frame, text="Registar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
#Botón eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=eliminarPaciente)
btn_eliminar.grid(row=0, column=1, padx=5)
#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")
#Definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguínero")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")
#Definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
#Ubicar el treeview en la cuadricula
treeview.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar vertical
Scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=9, column=2, sticky="ns")
#Pestaña doctor
#Titulo
Titulo=tk.Label(frame_doctores, text="REGISTRO DE DOCTORES")
Titulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#Nombre-Doctor
labelNombreD=tk.Label(frame_doctores, text="Nombre Completo :")
labelNombreD.grid(row=1, column=0, sticky="w", pady=5, padx=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Especialidad
etiqueta=tk.Label(frame_doctores, text="Especialidad :")
etiqueta.grid(row=2, column=0, padx=5, pady=5, sticky="w")
opciones=["Cardiología", "Neurología", "Pediatría","Dermatología"]
combo=ttk.Combobox(frame_doctores, values=opciones, state="readonly")
combo.current(0) #selecciona primera opcion por defecto
combo.grid(row=2, column=1, padx=5, pady=5,sticky="W")
#Edad
labelEdadD=tk.Label(frame_doctores, text="Edad :")
labelEdadD.grid(row=3, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frame_doctores, from_=1, to=100)
spin.grid(row=3, column=1, padx=5, pady=5,sticky="w")
#Telefono
labelTelefonoD=tk.Label(frame_doctores, text="Teléfono :")
labelTelefonoD.grid(row=4, column=0, sticky="w", pady=5, padx=5)
Telefono=tk.Entry(frame_doctores)
Telefono.grid(row=4, column=1, sticky="w", pady=5, padx=5)
#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=5, column=0,columnspan=2, sticky="w", pady=5)
#Botón registrar
btn_registrarD=tk.Button(btn_frameD, text="Registar", command=registrarDoctor)
btn_registrarD.grid(row=0, column=0, padx=5)
btn_registrarD.configure(bg="Green")
#Botón eliminar
btn_eliminarD=tk.Button(btn_frameD, text="Eliminar", command=eliminarDoctor)
btn_eliminarD.grid(row=0, column=1, padx=5)
btn_eliminarD.configure(bg="Red")
#Crear TreeView para mostrar pacientes
treeviewD=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
#Definir encabezados
treeviewD.heading("Nombre", text="Nombre Completo")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Telefono", text="Teléfono")
#definir anchos
treeviewD.column("Nombre", width=120)
treeviewD.column("Especialidad", width=120)
treeviewD.column("Edad", width=50, anchor="center")
treeviewD.column("Telefono", width=120)
#Ubicar el treeview en la cuadricula
treeviewD.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar vertical
Scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
treeviewD.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=6, column=2, sticky="ns")
#Asociar evento de cambio de pestaña
Pestañas.bind("<<NotebookTabChanged>>",al_cambiar_pestaña)
cargar_desde_archivo_pacientes()#Cargar al iniciar la aplicacion
cargar_desde_archivo_doctores()
ventana_principal.mainloop()