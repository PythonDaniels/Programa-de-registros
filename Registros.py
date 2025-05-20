                        # //// Programa de registros ////

password = "program2025"

# /// Verificación de contraseña
while True:
    passw = input("Ingrese la contraseña: ")
    if passw == password:
        break
    else:
        print("ERROR: Contraseña incorrecta")

# /// Menú principal
while True:
    print("\n--Programa de registros--")
    print("1 - Ingresar dato a la base")
    print("2 - Cancelar operación")
    print("3 - Lectura de datos")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese tu nombre: ")
        apellido = input("Ingrese tu apellido: ")
        año = int(input("Ingrese año de nacimiento: "))
        edad = (2025-año)
        pais = str(input("Ingrese su país: "))

        # Guardar datos en archivo
        with open("base2025.txt", "a") as archivo:
            archivo.write(f"{nombre},{apellido},{año},{edad},{pais}\n")

        print(f"\nUsuario {nombre} registrado con éxito.")

    elif opcion == "2":
        print("Operación cancelada.")
        break

    elif opcion == "3":
        try:
            with open("base2025.txt", "r") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("No hay datos en la base.")
                else:
                    print("\n--Usuarios registrados--")
                    for i, linea in enumerate(lineas, 1):
                        datos = linea.strip().split(",")
                        print(f"{i}. Nombre: {datos[0]} Apellido: {datos[1]}, Nacimiento: {datos[2]}, Edad: {datos[3]}, País: {datos[4]}")
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")

    else:
        print("Ingrese una opción correcta.")



#### ACTUALIZACIONES ####
# - Calcula automaticamente la dedad usando la variable "año"
# - Error anulado - (Input de textos introducidos como INT)