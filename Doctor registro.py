#Importación de librerías
import tkinter as tk
from tkinter import ttk
#Guardar en archivo doctores
def guardar_en_archivo_doctor():
    with open("doctor.txt","w",encoding="utf-8") as archivoD:
        for doctor in Doctor_data:
            archivoD.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Genero']}|{doctor['CentroM']}\n")
#Cargar desde archivo doctor
def cargar_desde_archivo_doctores():
    try:
        with open("doctor.txt", "r", encoding="utf-8") as archivoD:
            Doctor_data.clear()
            for lineaD in archivoD:
                datosD=lineaD.strip().split("|")
                if len(datosD)==5:
                    doctor={
                        "Nombre":datosD[0],
                        "Especialidad":datosD[1],
                        "Edad":datosD[2],
                        "Genero":datosD[3],
                        "CentroM":datosD[4]
                    }
                    Doctor_data.append(doctor)
        cargarD_treeview()
    except FileNotFoundError:
        open("doctor.txt", "w", encoding="utf-8").close()
    #Linea modificada a la lista
#Funcion registrar doctor
Doctor_data=[]
#Funcion registrar doctor
def registrarDoctor():
    #Crear diccionario con los datos ingresados
    Doctor={
        "Nombre": nombreD.get(),
        "Especialidad": combo.get(),
        "Edad": spin.get(),
        "Genero":generoD.get(),
        "CentroM":centro_medicoD.get()
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
                item["Genero"],
                item["CentroM"]                
            )
        )
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
labelEdadD=tk.Label(frame_doctores, text="Años de experiencia :")
labelEdadD.grid(row=3, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frame_doctores, from_=1, to=100)
spin.grid(row=3, column=1, padx=5, pady=5,sticky="w")
#Género
labelGeneroD=tk.Label(frame_doctores, text="Género :")
labelGeneroD.grid(row=4, column=0, sticky="w", pady=5, padx=5)
generoD=tk.StringVar()
generoD.set("Masculino") #valor por defecto
radioMasculinoD=ttk.Radiobutton(frame_doctores, text="Masculino", variable=generoD, value="Masculino")
radioMasculinoD.grid(row=4, column=1, sticky="w", pady=5, padx=5)
radioFemeninoD=ttk.Radiobutton(frame_doctores, text="Femenino", variable=generoD, value="Femenino")
radioFemeninoD.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#Centro Médico
labelCentroMedicoD=tk.Label(frame_doctores, text="Centro de Salud :")
labelCentroMedicoD.grid(row=6, column=0, sticky="w", pady=5, padx=5)
centro_medicoD=tk.StringVar()
centro_medicoD.set("Hospital Central") #Valor por defecto
comboCentroMedicoD=ttk.Combobox(frame_doctores, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centro_medicoD)
comboCentroMedicoD.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=20, column=0,columnspan=2, sticky="w", pady=5)
#Botón registrar
btn_registrarD=tk.Button(btn_frameD, text="Registar", command=registrarDoctor)
btn_registrarD.grid(row=0, column=0, padx=5)
btn_registrarD.configure(bg="Green")
#Crear TreeView para mostrar pacientes
treeviewD=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Genero","CentroM"), show="headings")
#Definir encabezados
treeviewD.heading("Nombre", text="Nombre Completo")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Años de experiencia")
treeviewD.heading("Genero", text="Genero")
treeviewD.heading("CentroM", text="Centro Médico")
#definir anchos
treeviewD.column("Nombre", width=120,anchor="center")
treeviewD.column("Especialidad", width=120,anchor="center")
treeviewD.column("Edad", width=120, anchor="center")
treeviewD.column("Genero", width=120,anchor="center")
treeviewD.column("CentroM",width=120,anchor="center")
#Ubicar el treeview en la cuadricula
treeviewD.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Asociar evento de cambio de pestaña
cargar_desde_archivo_doctores()
ventana_principal.mainloop()