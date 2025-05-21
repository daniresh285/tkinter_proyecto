#Saluda a un nombre que le pasemos por un entry
import tkinter as tk

ventana = tk.Tk()

#El titulo de la ventana, que no hace falta pero yo lo pongo para que se vea mas bonito
ventana.title("Ejemplo 2")

#El StringVar es una variable que se puede usar para almacenar texto
nombre_var= tk.StringVar()

#Con el get podemos obtener el valor de la variable, y con el config podemos cambiar el texto del label
def cambio_nombre():
    holanombre.config(
        holanombre.configure(text="Hola " + nombre_var.get()) #Por que cojo la variable del label y la concateno con el texto que tiene dentro y ya lo que hace es cambiar el texto del label
    )
    

holanombre= tk.Label(ventana, text="Hola nombre", font=("Arial", 18), padx=20, pady=10)

#El padx y pady es mejor aplicarlos en el pack
holanombre.pack()

#El entry es un campo de texto donde el usuario puede escribir
nombre= tk.Entry(ventana, font=("Arial", 18), textvariable=nombre_var)
nombre.pack(padx=20, pady=20)

boton_cambio= tk.Button(ventana, text="cambio",font=("Arial", 18), command=cambio_nombre)

boton_cambio.pack(padx=20, pady=20)


ventana.mainloop()