from datetime import datetime

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = None
        self.descripcion = descripcion
        self.costo = None
        self.set_fecha(fecha)
        self.set_costo(costo)
        self.siguiente = None

    def set_fecha(self, fecha):
        try:
            self.fecha = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe tener el formato dd/mm/yyyy")

    def set_costo(self, costo):
        if costo > 0:
            self.costo = costo
        else:
            raise ValueError("El costo debe ser un valor positivo")

    def get_fecha(self):
        return self.fecha

    def get_descripcion(self):
        return self.descripcion

    def get_costo(self):
        return self.costo


class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.placa = None
        self.marca = marca
        self.modelo = modelo
        self.anio = None
        self.kilometraje = None
        self.historial_mantenimientos = None
        self.set_placa(placa)
        self.set_anio(anio)
        self.set_kilometraje(kilometraje)

    def set_placa(self, placa):
        if len(placa) == 7 and placa[0].isalpha() and placa[1:4].isdigit() and placa[4:].isalpha():
            self.placa = placa
        else:
            raise ValueError("La placa debe tener el formato A123AAA (una letra, tres dígitos y tres letras).")

    def set_anio(self, anio):
        if 1990 < anio <= datetime.now().year:
            self.anio = anio
        else:
            raise ValueError("El año debe ser un valor razonable")

    def set_kilometraje(self, kilometraje):
        if kilometraje >= 0:
            self.kilometraje = kilometraje
        else:
            raise ValueError("El kilometraje debe ser un número positivo")

    def agregar_mantenimiento(self, mantenimiento):
        if not isinstance(mantenimiento, Mantenimiento):
            raise ValueError("Debe ser una instancia de la clase Mantenimiento")
        if not self.historial_mantenimientos:
            self.historial_mantenimientos = mantenimiento
        else:
            mantenimiento.siguiente = self.historial_mantenimientos
            self.historial_mantenimientos = mantenimiento

    def consultar_historial(self):
        mantenimientos = []
        mantenimiento_actual = self.historial_mantenimientos
        while mantenimiento_actual:
            mantenimientos.append(f"{mantenimiento_actual.get_fecha().strftime('%d/%m/%Y')}: {mantenimiento_actual.get_descripcion()} - Q.{mantenimiento_actual.get_costo()}")
            mantenimiento_actual = mantenimiento_actual.siguiente
        return "\n".join(mantenimientos) if mantenimientos else "No se han registrado mantenimientos"

    def calcular_costo_total_mantenimientos(self):
        costo_total = 0
        mantenimiento_actual = self.historial_mantenimientos
        while mantenimiento_actual:
            costo_total += mantenimiento_actual.get_costo()
            mantenimiento_actual = mantenimiento_actual.siguiente
        return costo_total


class NodoVehiculo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None
        self.anterior = None


class FlotaVehiculos:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def registrar_vehiculo(self, vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise ValueError("Debe ser una instancia de la clase Vehiculo")
        nuevo_nodo = NodoVehiculo(vehiculo)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_vehiculo(self, placa):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.vehiculo.placa == placa:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_actual.siguiente
                if nodo_actual == self.cola:
                    self.cola = nodo_actual.anterior
                del nodo_actual
                print(f"Vehículo con placa {placa} eliminado.")
                return
            nodo_actual = nodo_actual.siguiente
        print(f"Vehículo con placa {placa} no encontrado.")

    def buscar_vehiculo(self, placa):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.vehiculo.placa == placa:
                return nodo_actual.vehiculo
            nodo_actual = nodo_actual.siguiente
        return None

    def listar_vehiculos(self):
        vehiculos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            vehiculos.append(f"Placa: {nodo_actual.vehiculo.placa}, Marca: {nodo_actual.vehiculo.marca}, Modelo: {nodo_actual.vehiculo.modelo}, Año: {nodo_actual.vehiculo.anio}, Kilometraje: {nodo_actual.vehiculo.kilometraje}")
            nodo_actual = nodo_actual.siguiente
        return "\n".join(vehiculos) if vehiculos else "No hay vehículos registrados."

