# Importamos la libreria de Tkinter
import tkinter as tk
# importamos el modulo de messagebox de tkinter
from tkinter import messagebox
# importamos nuestra funcionalidad
from Logic.consulta_clima import obtener_clima

def iniciar_app():
    # creamos variable para obtener busqueda del clima
    respuesta = obtener_clima(entrada.get())
    if respuesta:
        messagebox.showinfo("Resultado del Clima: ", respuesta)
    else:
        messagebox.showinfo("Resultado del Clima", "Ocurrio un error en la busqueda. Por favor verifique que se envie la ubicación")
# configuraciones de nuestra ventana (generales)
app = tk.Tk()
app.geometry("340x400")
app.configure(background="black")
app.title("Consulta del clima")

#creamos una variable de tipo StringVar para guardar la ubicacion
entrada = tk.StringVar(app)


# etiqueta para mostrar info
tk.Label(
    app,
    text = "Ingrese la ubicacion a buscar: ",
    font = ("Arial", 12)
).pack(pady=10)

# entrada para ingresar texto
tk.Entry(
    app,
    font = ("Arial", 12),
    justify = "center",
    textvariable = entrada
).pack(pady=10)

# boton para dar click
tk.Button(
    app,
    text = "Consultar",
    font = ("Arial", 12),
    command = iniciar_app
).pack(pady=10)

app.mainloop()