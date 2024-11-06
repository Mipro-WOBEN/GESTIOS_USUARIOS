import json

class Contacto:
    def __init__(self, id_contacto, nombre, telefono, correo):
        self.id_contacto = id_contacto
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def Devolver(self):
        return f"{self.id_contacto} - {self.nombre} - {self.telefono} - {self.correo}"
    
    def Guardar_datos(self):
        # Intentar leer el archivo para obtener registros existentes
        try:
            with open("Registro.json", "r", encoding="utf-8") as f:
                lista_registro = json.load(f)
        except FileNotFoundError:
            # Si el archivo no existe, crear una lista vacía
            lista_registro = []

        # Agregar el nuevo contacto a la lista de registros
        lista_registro.append({
            "id_contacto": self.id_contacto,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo
        })

        # Escribir toda la lista de registros en el archivo
        with open("Registro.json", "w", encoding="utf-8") as f:
            json.dump(lista_registro, f, ensure_ascii=False, indent=4)

while True:
    # Crear la instancia de Contacto pasando los datos necesarios
    Ingresar_contacto = int(input("Ingresar numero id: "))
    Ingresar_nombre = input("Ingresar tu nombre: ")
    Ingresar_telefono = int(input("Ingresar tu telefono: "))
    Ingresar_correo = input("Ingresar tu correo electrónico: ")
    contacto = Contacto(Ingresar_contacto, Ingresar_nombre, Ingresar_telefono, Ingresar_correo)    
    
    # Llamar al método Devolver para mostrar el contacto ingresado
    print(contacto.Devolver())

    # Guardar el contacto en el archivo JSON
    print("Guardando usuario...")
    contacto.Guardar_datos()

    # Preguntar si se desea continuar o salir
    print("Desea salir o continuar agregando usuarios? \n 1. Salir 2. Continuar")
    opcion_salida = int(input("Escribe: "))
    if opcion_salida == 1:
        break
    else:
        print("El programa continúa....")
