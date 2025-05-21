import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

#Funcion
def inicio_sesion():
    usuario=entry_usuario.get() #Con los dos == no va, tiene que ser con una sintaxis asi: usuario=entry_usuario.get(), el get sirve para recoger ese dato
    contrasena=entry_contrasena.get()
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Credenciales Correctas", "Has iniciado sesion correctamente")
    else:   
        messagebox.showerror("Error", "Credenciales Incorrectas")


#Creo la ventana
ventana= tk.Tk()

#Modifico el tamaño de la ventana
ventana.geometry("600x400")

#Creo el marco principal
marcoprincipal= tk.Frame(ventana)
marcoprincipal.pack(expand=True, fill="both")

#Creo el frame izquierda

frameIzquierda= tk.Frame(marcoprincipal, bg="red", width=300)
frameIzquierda.pack(fill="both", side="left")


#Creo la imagen y hago un resize para que se vea grande

imagen= Image.open("imagen.jpg")
imagen= imagen.resize((200,200))
imagenTk= ImageTk.PhotoImage(imagen)

imagen_Label= tk.Label(frameIzquierda, image=imagenTk)
imagen_Label.pack(expand=True)


#Creo el frame derecho

frameDerecho= tk.Frame(marcoprincipal, bg="aquamarine", width=300)
frameDerecho.pack(fill="both", expand=True, side="right")

#titulo
titulo= tk.Label(frameDerecho, text="Inicio De Sesion \nde ChatGPT", bg="aquamarine",font=("Arial", 18))
titulo.pack(pady=20)

#Creo el usuario y la contraseña y les creo el entry y todo eso va al frame izquierdo

usuario= tk.Label(frameDerecho, text="Nombre de usuario", bg="aquamarine", font=("Arial", 18))
usuario.pack(pady=(20,2))

entry_usuario= tk.Entry(frameDerecho, font=("Arial", 18))
entry_usuario.pack(pady=5)

contrasena= tk.Label(frameDerecho, text="Contraseña", bg="aquamarine", font=("Arial", 18))
contrasena.pack(pady=5)

entry_contrasena= tk.Entry(frameDerecho, show="*", font=("Arial", 18))
entry_contrasena.pack(pady=5)

boton=tk.Button(frameDerecho, text="Iniciar Sesion", command=inicio_sesion)
boton.pack(pady=20)


#Creo el mainloop
ventana=tk.mainloop()