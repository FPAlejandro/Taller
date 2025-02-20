import os
from Listas import Vehiculo, Mantenimiento, FlotaVehiculos

def limpiar_pantalla():
    os.system('cls') 
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Registrar nuevo vehículo")
    print("2. Eliminar vehículo")
    print("3. Buscar vehículo por placa")
    print("4. Listar vehículos registrados")
    print("5. Agregar mantenimiento a un vehículo")
    print("6. Consultar historial de mantenimientos")
    print("7. Calcular costo total de mantenimientos")
    print("8. Salir")

def main():
    flota = FlotaVehiculos()
    
    while True:
        limpiar_pantalla() 
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            anio = int(input("Ingrese el año del vehículo: "))
            kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
            try:
                vehiculo = Vehiculo(placa, marca, modelo, anio, kilometraje)
                flota.registrar_vehiculo(vehiculo)
                print("Vehículo registrado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo a eliminar: ")
            flota.eliminar_vehiculo(placa)

        elif opcion == "3":
            placa = input("Ingrese la placa del vehículo a buscar: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Vehículo encontrado: Placa {vehiculo.placa}, Marca {vehiculo.marca}, Modelo {vehiculo.modelo}, Año {vehiculo.anio}, con {vehiculo.kilometraje} Kilometros recorridos")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "4":
            print(flota.listar_vehiculos())

        elif opcion == "5":
            placa = input("Ingrese la placa del vehículo para agregar mantenimiento: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                fecha = input("Ingrese la fecha del mantenimiento (dd/mm/yyyy): ")
                descripcion = input("Ingrese la descripción del servicio: ")
                costo = float(input("Ingrese el costo del mantenimiento: Q."))
                try:
                    mantenimiento = Mantenimiento(fecha, descripcion, costo)
                    vehiculo.agregar_mantenimiento(mantenimiento)
                    print("Mantenimiento agregado exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "6":
            placa = input("Ingrese la placa del vehículo para consultar su historial: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Historial de mantenimientos para {placa}:\n{vehiculo.consultar_historial()}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "7":
            placa = input("Ingrese la placa del vehículo para calcular el costo total de mantenimientos: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Costo total de mantenimientos para {placa}: Q.{vehiculo.calcular_costo_total_mantenimientos()}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "8":
            print("Feliz día! :)")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        input("Presione Enter para continuar...") 
if __name__ == "__main__":
    main()
