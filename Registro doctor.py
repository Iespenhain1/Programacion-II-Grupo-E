import tkinter as tk
from tkinter import messagebox

def nuevoDoctor():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de doctor")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="LightBlue")
    #Nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:")
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="w")
    nombreLabel.configure(bg="LightBlue")
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we") 
    #Direccion
    direccionLabel=tk.Label(ventanaRegistro,text="Dirección:")
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="w")
    direccionLabel.configure(bg="LightBlue")
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="we")
    #Telefono
    telefonoLabel=tk.Label(ventanaRegistro,text="Teléfono:")
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="w")
    telefonoLabel.configure(bg="LightBlue")
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")
     #Especialidad
    especialidadLabel=tk.Label(ventanaRegistro, text="Especialidad:")
    especialidadLabel.grid(row=3,column=0,padx=10,pady=5,sticky="w")
    especialidadLabel.configure(bg="LightBlue")
    especialidad=tk.StringVar(value="LightBlue")
    rbCardiologia=tk.Radiobutton(ventanaRegistro, text="Cardiología", variable=especialidad, value="Cardiología")
    rbCardiologia.grid(row=3,column=1,padx=10,pady=5,sticky="w")
    rbCardiologia.configure(bg="LightBlue")
    rbPediatria=tk.Radiobutton(ventanaRegistro, text="Pediatría", variable=especialidad, value="Pediatría")
    rbPediatria.grid(row=4,column=1,padx=10,pady=5,sticky="w")
    rbPediatria.configure(bg="LightBlue")
    rbDermatologia=tk.Radiobutton(ventanaRegistro, text="Dermatología", variable=especialidad, value="Dermatología")
    rbDermatologia.grid(row=5,column=1,padx=10,pady=5,sticky="w")
    rbDermatologia.configure(bg="LightBlue")
    #Disponibilidad
    turnoLabel=tk.Label(ventanaRegistro, text="Turno:")
    turnoLabel.grid(row=6,column=0,padx=10,pady=5,sticky="w")
    turnoLabel.config(bg="LightBlue")
    Mañana=tk.BooleanVar()
    Tarde=tk.BooleanVar()
    Noche=tk.BooleanVar()
    cbMañana=tk.Checkbutton(ventanaRegistro, text="Mañana", variable=Mañana)
    cbMañana.grid(row=6,column=1,padx=10,pady=5,sticky="w")
    cbMañana.configure(bg="LightBlue")
    cbTarde=tk.Checkbutton(ventanaRegistro, text="Tarde", variable=Tarde)
    cbTarde.grid(row=7,column=1,padx=10,pady=5,sticky="w")
    cbTarde.configure(bg="LightBlue")
    cbNoche=tk.Checkbutton(ventanaRegistro, text="Noche", variable=Noche)
    cbNoche.grid(row=8,column=1,padx=10,pady=5,sticky="w")
    cbNoche.configure(bg="LightBlue")
    #Registrar datos
    def registrarDatos():
        Turno=[]
        if Mañana.get():
            Turno.append("Mañana")
        if Tarde.get():
            Turno.append("Tarde")
        if Noche.get():
            Turno.append("Noche")
        if len(Turno)>0:
            TurnoTexto=','.join(Turno)
        else:
            TurnoTexto='Ninguna'
    #Cadena para mostrar todods los datos el formulario
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Especialidad:{especialidad.get()}\n"
            f"Turno :{TurnoTexto}"
            )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy() #Cierra la ventana tras el mensaje
    btnRegistrar=tk.Button(ventanaRegistro,text="Datos Registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)

def buscarDoctor():
    messagebox.showinfo("Nuevo Doctor","Este es el espacio para buscar Doctor")
def eliminarDoctor():
    messagebox.showinfo("Nuevo Doctor","Este es el espacio para eliminar Doctor") 
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Registro de Doctores")
ventanaPrincipal.geometry("600x450")
ventanaPrincipal.configure(bg="LightBlue")
#Barra menu
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#Menu Doctor
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command=nuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor",command=buscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor",command=eliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=ventanaPrincipal.quit)

ventanaPrincipal.mainloop()