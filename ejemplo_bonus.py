import tkinter as tk
import random
import string
from tkinter import messagebox



root = tk.Tk()
root.title("Generador Password")

#El geometry es el tamaño de la ventana, tipo resolucion
root.geometry("400x300")


def generar():
    
    #Lo que hace longitud es convertir el valor de la entrada a un entero
    longitud= int(entry_longitud.get())
    
    #Aqui hago que la variable caracteres sea igual a una cadena de caracteres que contiene letras mayusculas, minusculas, digitos y simbolos
    caracteres= string.ascii_letters + string.digits + string.punctuation
    
    #Y con la variable password lo que genera el random que es un caracter aleatorio de los caracteres que he definido antes, 
    #Que después eso se va guardando en la variable vacia y con el join voy sumando todos los caracteres aleatorios que va generando el random.choice,
    #Y lo que hace el bucle for es que se repita tantas veces como la longitud que le he dado
    password= "".join(random.choice(caracteres) for i in range(longitud))
    
    #Limpiamos el campo password y lo rellenamos con la password generada aleatoriamente
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password) 

def portapapeles():
    root.clipboard_clear()  # Limpiar el portapapeles
    root.clipboard_append(entry_password.get())  # Añadir la contraseña generada al portapapeles
    messagebox.showinfo("Información", "Password Copiada")
    
label_longitud= tk.Label(root, text="Longitud de la password")
label_longitud.pack(pady=10)

entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)

label_longitud= tk.Label(root, text="Contraseña Generada")
label_longitud.pack(pady=10)

entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

boton= tk.Button(root, text="Generar Password", command=generar)
boton.pack(pady=10)

boton2= tk.Button(root, text="Copiar", command=portapapeles)
boton2.pack(pady=10)

root.mainloop()

