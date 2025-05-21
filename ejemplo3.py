#Ejemplo de login minimalista
import tkinter as tk

ventana = tk.Tk()

#Funcion para el login
def login():
    nombre= nombre_var.get()
    password= password_var.get()

    if nombre == "admin" and password == "admin1234":
        mensaje_label.config(text="Sistema inciado correctamente")
    else:
        mensaje_label.config(text="Usuario o contraseña incorrectos")

#variables

#Aqui se declaran las variables que se van a utilizar y los StringVar sirve para almacenar el texto solo
nombre_var= tk.StringVar()
password_var= tk.StringVar()

#El titulo de la ventana, que no hace falta pero yo lo pongo para que se vea mas bonito
ventana.title("Login")

# Aqui el label lo que hace es crear un texto en la ventana 
# también podemos modificar la fuente y el tamaño de la letra y el color tanto del fondo como del texto
username= tk.Label(ventana, text="Nombre de usuario", font=("Arial", 18)).pack(padx=20, pady=10)

#El entry es el como un input 
nombre_entry= tk.Entry(ventana, font=("Arial", 16), textvariable=nombre_var).pack(padx=20, pady=10)

# Aqui el label lo que hace es crear un texto en la ventana 
# también podemos modificar la fuente y el tamaño de la letra y el color tanto del fondo como del texto
password= tk.Label(ventana, text="password", font=("Arial", 18)).pack(padx=20, pady=10)

#El entry es el como un input 
password_entry= tk.Entry(ventana, font=("Arial", 16), text=password_var).pack(padx=20, pady=10)

#El boton es el que se le da al usuario para que haga click y ejecute la funcion para eso se utiliza el command
boton_ingresar= tk.Button(ventana, text="Ingresar", font=("Arial", 18), command=login).pack(padx=20, pady=10)

#Si esta el .pack en la misma linea que el label, despues en la funcion no se puede utilizar el .config
mensaje_label= tk.Label(ventana, text="", font=("Arial", 18))
mensaje_label.pack(padx=20, pady=5)



tk.mainloop()