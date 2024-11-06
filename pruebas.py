
import tkinter as tk
from tkinter import messagebox
import pyodbc as pyd

# Conectar a la base de datos
def conectar_bd():
    conexion = pyd.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-TDUR9AD;'
        'DATABASE=AdventureWorks2022;'
        'UID=RICK12;'
        'PWD=1243'
    )
    return conexion
if conectar_bd():
    print("Hay conexión!!!")
else:
    print("No hay conexión!!")

# Función para agregar un usuario
def agregar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    if nombre and correo and telefono:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO Usuarios (Nombre, Correo, Telefono) VALUES (?, ?, ?)"
        cursor.execute(query, (nombre, correo, telefono))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Usuario agregado correctamente")
        
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

## Función para listar usuarios en el widget Listbox
def listar_usuarios():
    listbox_usuarios.delete(0, tk.END)  # Limpiar la lista antes de mostrar
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    for usuario in cursor:
        listbox_usuarios.insert(tk.END, usuario)
    conexion.close()

# Configurar la ventana principal
root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("330x400")

## Etiquetas y entradas para los datos del usuario
tk.Label(root, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Correo").grid(row=1, column=0, padx=10, pady=5)
entry_correo = tk.Entry(root)
entry_correo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Teléfono").grid(row=2, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=2, column=1, padx=10, pady=5)

## Botones para las operaciones CRUD
btn_agregar = tk.Button(root, text="Agregar Usuario", command=agregar_usuario)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

## Listbox para mostrar usuarios
listbox_usuarios = tk.Listbox(root, width=50)
listbox_usuarios.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

## Botón para listar usuarios
btn_listar = tk.Button(root, text="Listar Usuarios", command=listar_usuarios)
btn_listar.grid(row=5, column=0, columnspan=2, pady=10)

## Ejecutar la aplicación
root.mainloop()










#import json
#while True:
#    try:
#        with open("Archivo.json", "r", encoding="utf-8") as f:
#           lista_registro=json.load(f)
#    except FileNotFoundError:
#        lista_registro = []
#    
#    listas_valor = []
#    for i in range(5):
#        ingresar_valor = input(f"Ingresa el valor {i+1}: ")
#        listas_valor.append(ingresar_valor)
#    lista_registro.append(listas_valor)
#    with open("Archivo.json","w",encoding="utf-8") as f:
#        json.dump(lista_registro,f, ensure_ascii=False,indent=4)
#
#
#    print("Desea continua?")
#    opcion = int(input("Ingresar 1.Salir \n2.Continuar"))    
#    if opcion == 1:
#        break
#    else:
#        print("El programa continua....")    