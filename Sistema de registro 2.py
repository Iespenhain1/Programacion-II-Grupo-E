import tkinter as tk
from tkinter import messagebox
 
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)     # Toplevel= Crea una nueva ventana secundaria (independienete pero asociada a la ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="#7072A5")    
    #Nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:")
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="w")
    nombreLabel.configure(bg="#7072A5")
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")    
    #Direccion
    direccionLabel=tk.Label(ventanaRegistro,text="Dirección:")
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="w")
    direccionLabel.configure(bg="#7072A5")
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="we")  
    #Telefono
    telefonoLabel=tk.Label(ventanaRegistro,text="Teléfono:")
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="w")
    telefonoLabel.configure(bg="#7072A5")
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we") 
    #sexo(radiobutton)
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo:")
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="w")
    sexoLabel.configure(bg="#7072A5")
    sexo=tk.StringVar(value="Masculino")                #es una variable esplecial de Tkinter que se utiliza para enlazar widgets como Radiobuttons
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="Masculino",variable=sexo,value="Masculino")
    rbMasculino.grid(row=3,column=1,padx=10,pady=5,sticky="w",)
    rbMasculino.configure(bg="#7072A5")
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="Femenino",variable=sexo,value="Femenino")
    rbFemenino.grid(row=4,column=1,padx=10,pady=5,sticky="w")
    rbFemenino.configure(bg="#7072A5")
    #enfermedades base(checkbutton)
    enfLabel=tk.Label(ventanaRegistro,text="Enfermedades base:")
    enfLabel.grid(row=5,column=0,padx=10,pady=5,sticky="w")
    enfLabel.configure(bg="#7072A5")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes)
    cbDiabetes.grid(row=5,column=1,padx=10,pady=5,sticky="w")
    cbDiabetes.configure(bg="#A4A5D7")
    cbHipertension=tk.Checkbutton(ventanaRegistro,text="Hipertension",variable=hipertension)
    cbHipertension.grid(row=6,column=1,padx=10,pady=5,sticky="w")
    cbHipertension.configure(bg="#A4A5D7")
    cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma",variable=asma)
    cbAsma.grid(row=7,column=1,padx=10,pady=5,sticky="w")
    cbAsma.configure(bg="#A4A5D7")
    #Accion:registrar datos
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto='Ninguna'           
    #Cadena para mostrar todods los datos el formulario
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Sexo:{sexo.get()}\n"
            f"Enfermedades :{enfermedadesTexto}"
            )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy() #Cierra la ventana tras el mensaje
    btnRegistrar=tk.Button(ventanaRegistro,text="Datos Registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)

def buscarPaciente():
    messagebox.showinfo("Nuevo Paciente","Este es el espacio para buscar  paciente")
def eliminarPaciente():
    messagebox.showinfo("Nuevo Paciente","Este es el espacio para eliminar paciente")
def nuevoDoctor():
    messagebox.showinfo("Nuevo Doctor","Este es el espacio para crear nuevo Doctor")   
def buscarDoctor():
    messagebox.showinfo("Nuevo Doctor","Este es el espacio para buscar Doctor")
def eliminarDoctor():
    messagebox.showinfo("Nuevo Doctor","Este es el espacio para eliminar Doctor")
    
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#7179B4")
#Barra de menu
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#Menu Pacientes
menuPacientes=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente",command=buscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command=eliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir",command=ventanaPrincipal.quit)
#Menu ayuda
menuAyuda=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de",command=lambda:messagebox.showinfo("Acerca de","Version 1.0 - Sistema Biomedicina"))
#Menu Doctores
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command=nuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor",command=buscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor",command=eliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=ventanaPrincipal.quit)

ventanaPrincipal.mainloop()