#Texto a binario

import tkinter as tk


"""texto= "Hola mundo"
texto_binario= ""


for letra in texto:
    texto_binario + texto_binario = bin(ord(letra))[2:]

print(texto_binario)"""

ventana = tk.Tk()

#El 1.0 y el tk.END indica la primera linea y el carácter 0 hasta el final de la linea
def convertir_a_binario():
    text=(texto.get("1.0", tk.END))
    texto_binario= ""
    for letra in text: #Aqui hago el bucle para recorrer el texto que haya 
        texto_binario += bin(ord(letra))[2:] # Y con esto lo que hago es convertir el texto a binario
    #Lo que hago aqui es eliminar el texto que ya había ahi
    texto.delete("1.0", tk.END)
    #Con este insert lo que hago es insertar el texto binario en el texto despues de eliminar el texto anterior
    texto.insert("1.0", texto_binario)

#El label se ajusta automaticamente al texto que se le asigna,
#Para controlar el tamaño se le puede asignar un font o incluso tecnicas de alineacion
label_texto= tk.Label(ventana, text="texto", font=("Arial", 18)).pack(padx=20, pady=10)

#El width se utiliza en la variable de texto para controlar los caracteres que se pueden escribir
#El height se utiliza para controlar el numero de lineas que se pueden escribir
texto= tk.Text(ventana, width=40, height=15)
texto.pack(padx=20, pady=10)

boton_cambio= tk.Button(ventana,text="A binario", font=("Arial", 18), command=convertir_a_binario).pack(padx=20, pady=10)




ventana.mainloop()