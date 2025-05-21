#Un hola mundo en tkinter
import tkinter as tk

#Esto es lo que hacemos para crear una ventana
ventana = tk.Tk()

#El titulo de la ventana, que no hace falta pero yo lo pongo para que se vea mas bonito
ventana.title("Hola Mundo") #Esto es el título de la ventana

# Aqui el label lo que hace es crear un texto en la ventana 
# también podemos modificar la fuente y el tamaño de la letra y el color tanto del fondo como del texto
titulo = tk.Label(ventana, text="Hola Mundo", font=("Arial", 16, "bold"), padx=20, pady=20, bg="#000000", fg="#00ff00")
titulo.pack() #Empaqueta el label en la ventana

#Lo que hace esto es literalmente que no se pueda cerrar la ventana mientras el programa esté funcionando
ventana.mainloop()