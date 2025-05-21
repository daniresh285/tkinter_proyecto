#Lista de tareas

import tkinter as tk


ventana = tk.Tk()

#Una lista con las tareas que hay que hacer
lista_tarea = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

#Este bucle crea un checkbutton por cada tarea en la lista, lo que hace simplicarte el codigo
for tarea in lista_tarea:
    #Crea el checkbutton con el texto de la tarea que lo coge de la lista gracias al for
    tk.Checkbutton(ventana,text=tarea, font=("Arial", 18)).pack(pady=10, padx=20)


ventana.mainloop()