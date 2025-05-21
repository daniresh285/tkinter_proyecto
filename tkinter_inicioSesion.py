import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requiere instalar Pillow (pip install pillow)

# Esta funcion se ejecuta al hacer clic en el botón de inicio de sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Inicio de sesión", "¡Bienvenido!")
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

# Crear ventana
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("600x300")
ventana.resizable(False, False)

# Crear marco principal
marco_principal = tk.Frame(ventana)
marco_principal.pack(fill="both", expand=True)

# ---------- LADO IZQUIERDO: Imagen ----------
frame_izquierdo = tk.Frame(marco_principal, bg="#2C3E50", width=300)
frame_izquierdo.pack(side="left", fill="both")

# Cargar imagen
imagen = Image.open("imagen.jpg") # Cambia "imagen.jpg" por la ruta de tu imagen
imagen = imagen.resize((200, 200))
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(frame_izquierdo, image=imagen_tk, bg="#2C3E50")
label_imagen.pack(expand=True)

# ---------- LADO DERECHO: Formulario ----------
frame_derecho = tk.Frame(marco_principal, bg="#ECF0F1", width=300)
frame_derecho.pack(side="right", fill="both", expand=True)

# Etiqueta y entrada de usuario
tk.Label(frame_derecho, text="Usuario:", bg="#ECF0F1", font=("Arial", 12)).pack(pady=(40, 5))
entry_usuario = tk.Entry(frame_derecho, width=25, font=("Arial", 12))
entry_usuario.pack(pady=5)

# Etiqueta y entrada de contraseña
tk.Label(frame_derecho, text="Contraseña:", bg="#ECF0F1", font=("Arial", 12)).pack(pady=5)
entry_contrasena = tk.Entry(frame_derecho, show="*", width=25, font=("Arial", 12))
entry_contrasena.pack(pady=5)

# Botón de inicio de sesión
tk.Button(frame_derecho, text="Iniciar sesión", command=iniciar_sesion, bg="#3498DB", fg="white", font=("Arial", 12), width=20).pack(pady=20)

ventana.mainloop()
