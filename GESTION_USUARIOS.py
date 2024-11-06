import tkinter as tk
from tkinter import messagebox, filedialog
import pyodbc as pyd
import openpyxl

# Conectar a la base de datos
def conectar_bd():
    conexion = pyd.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-TDUR9AD;'
        'DATABASE=AdventureWorks2022;'
        'UID=RICK12;'
        'PWD=rico4532'
    )
    return conexion

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

# Función para listar usuarios en el widget Listbox
def listar_usuarios():
    listbox_usuarios.delete(0, tk.END)  # Limpiar la lista antes de mostrar
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    for usuario in cursor:
        listbox_usuarios.insert(tk.END, usuario)
    conexion.close()

# Función para eliminar un usuario seleccionado
def eliminar_usuario():
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        usuario = listbox_usuarios.get(seleccion)
        user_id = usuario[0]  # Suponiendo que el ID es el primer valor de la tupla
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE ID = ?", (user_id,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
        listar_usuarios()  # Actualiza la lista de usuarios
    else:
        messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar")

# Función para editar un usuario seleccionado
def editar_usuario():
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()
        
        if nombre and correo and telefono:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE Usuarios SET Nombre = ?, Correo = ?, Telefono = ? WHERE Nombre = ?",
                (nombre, correo, telefono, nombre)
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario editado correctamente")
            listar_usuarios()  # Actualiza la lista de usuarios
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un usuario para editar")

# Función para exportar usuarios a un archivo Excel
def exportar_excel():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        
        # Obtener los datos en una lista
        datos = cursor.fetchall()
        conexion.close()
        
        # Preguntar dónde guardar el archivo
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                                    filetypes=[("Archivos Excel", "*.xlsx")],
                                                    title="Guardar como")
        # Verifica si se seleccionó una ruta de archivo
        if ruta_archivo:
            workbook = workbook()
            sheet = workbook.active
            sheet.title = "Usuarios"
            
            # Encabezados
            headers = ["ID", "Nombre", "Correo", "Teléfono"]
            sheet.append(headers)
            
            # Agregar datos
            for fila in datos:
                sheet.append(fila)
            
            # Guardar el archivo
            workbook.save(ruta_archivo)
            messagebox.showinfo("Éxito", "Usuarios exportados a Excel correctamente")
        else:
            messagebox.showwarning("Cancelado", "No se seleccionó ninguna ubicación para guardar.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al exportar: {e}")

# Configurar la ventana principal
root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("340x500")

# Etiquetas y entradas para los datos del usuario
tk.Label(root, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Correo").grid(row=1, column=0, padx=10, pady=5)
entry_correo = tk.Entry(root)
entry_correo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Teléfono").grid(row=2, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=2, column=1, padx=10, pady=5)

# Botones para las operaciones CRUD
btn_agregar = tk.Button(root, text="Agregar Usuario", command=agregar_usuario)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

btn_editar = tk.Button(root, text="Editar Usuario", command=editar_usuario)
btn_editar.grid(row=5, column=0, columnspan=2, pady=5)

btn_exportar = tk.Button(root, text="Exportar a Excel", command=exportar_excel)
btn_exportar.grid(row=6, column=0, columnspan=2, pady=5)

# Listbox para mostrar usuarios
listbox_usuarios = tk.Listbox(root, width=50)
listbox_usuarios.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Botón para listar usuarios
btn_listar = tk.Button(root, text="Listar Usuarios", command=listar_usuarios)
btn_listar.grid(row=8, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
