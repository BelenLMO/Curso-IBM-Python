# Clase que representa un asiento en la sala de cine
class Asiento:
    def __init__(self, numero, fila, precio_base):
        self.__numero = numero      # Número del asiento
        self.__fila = fila          # Fila del asiento
        self.__reservado = False    # Estado inicial: no reservado
        self.__precio = precio_base # Precio inicial (sin descuentos)

    # Getters y setters para cada atributo
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    # Métodos para reservar y cancelar reservas
    def reservar(self):
        """Marca el asiento como reservado."""
        if not self.__reservado:   # Si el asiento no está reservado
            self.__reservado = True
            return True
        else:
            return False  # Ya está reservado

    def cancelar_reserva(self):
        """Devuelve el asiento a su estado no reservado."""
        if self.__reservado:    # Si el asiento está reservado
            self.__reservado = False
            return True
        else:
            return False  # No se puede cancelar si no está reservado

# Clase que administra la sala de cine y los asientos
class SalaCine:
    from datetime import datetime   # Import para manejar fechas y horas

    def __init__(self, precio_base):
        self.__asientos = []  # Lista privada de asientos en la sala
        self.__precio_base = precio_base  # Precio base de las entradas
   
    # Método para agregar un asiento a la sala
    def agregar_asiento(self, numero, fila):
        """Agrega un asiento si no existe uno con el mismo número y fila."""
        for a in self.__asientos:
            if a.get_numero() == numero and a.get_fila() == fila:
                print("El asiento ya está registrado.")
                return False
        asiento = Asiento(numero, fila, self.__precio_base)
        self.__asientos.append(asiento)
        return True

    def reservar_asiento(self, numero, fila, precio_base, edad):
        """Reserva un asiento aplicando el precio con descuentos si está disponible."""
        # Obtener el día de la semana actual
        dia_semana = self.datetime.now().weekday()
        
        # Calcular el precio final aplicando descuentos
        precio_final = self.calcular_precio(precio_base, edad, dia_semana)
        
        # Buscar asiento y realizar la reserva
        asiento = self.buscar_asiento(numero, fila)
        if asiento and not asiento.is_reservado():
            asiento.set_precio(precio_final)
            return asiento.reservar()
        return False  # No se pudo reservar porque ya estaba reservado o no existe

    def cancelar_reserva(self, numero, fila):
        """Cancela la reserva de un asiento específico."""
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            return asiento.cancelar_reserva()
        return False  # No se pudo cancelar porque no existe o no estaba reservado

    def mostrar_asientos(self):
        """Muestra todos los asientos indicando si están reservados y el precio."""
        for asiento in self.__asientos:
            estado = "Reservado" if asiento.is_reservado() else "Disponible"
            print(f"Asiento {asiento.get_numero()} - Fila {asiento.get_fila()}: {estado}, Precio: ${asiento.get_precio()}")

    def buscar_asiento(self, numero, fila):
        """Busca y devuelve un asiento por número y fila."""
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None # Retorna None si no se encuentra el asiento

    def calcular_precio(self, precio_base, edad, dia_semana):
        """Calcula el precio del asiento aplicando descuentos según el día y la edad."""
        # Aplicar descuento del 20% si es miércoles (día 2 de la semana en Python)
        if dia_semana == 2:
            precio_base *= 0.8
        
        # Aplicar descuento del 30% si la edad es mayor a 65 años
        if edad > 65:
            precio_base *= 0.7
        
        return round(precio_base, 2)

    def validar_asiento(self, numero, fila):
        """Valida el número y fila del asiento."""
        if not isinstance(numero, int) or not isinstance(fila, str):
            raise ValueError("El número del asiento debe ser un entero y la fila una cadena.")
        if numero <= 0:
            raise ValueError("El número del asiento debe ser un valor positivo.")
        if not fila.isalpha():
            raise ValueError("La fila debe ser una letra o conjunto de letras.")

    def validar_edad(self, edad):
        """Valida que la edad sea positiva."""
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo.")

    def reservar_asiento_con_validacion(self, numero, fila, precio_base, edad):
        """Reserva un asiento con validaciones y manejo de excepciones."""
        try:
            # Validar datos de asiento y edad
            self.validar_asiento(numero, fila)
            self.validar_edad(edad)
            
            # Realizar la reserva con el precio calculado
            return self.reservar_asiento(numero, fila, precio_base, edad)
        except ValueError as e:
            print(f"Error: {e}")
            return False


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear una sala con precio base de $10
    sala = SalaCine(precio_base=10)

    # Agregar asientos a la sala
    try:
        sala.agregar_asiento(1, "A")
        sala.agregar_asiento(2, "A")
    except ValueError as e:
        print(f"Error al agregar asiento: {e}")

    # Mostrar asientos disponibles
    print("Estado inicial de los asientos:")
    sala.mostrar_asientos()

    # Reservar un asiento
    try:
        sala.reservar_asiento_con_validacion(1, "A", 10, 70)  # Mayor de 65 años
        print("\nEstado de los asientos después de la reserva:")
        sala.mostrar_asientos()
    except ValueError as e:
        print(f"Error al reservar: {e}")

    # Cancelar la reserva
    try:
        sala.cancelar_reserva(1, "A")
        print("\nEstado de los asientos después de cancelar la reserva:")
        sala.mostrar_asientos()
    except ValueError as e:
        print(f"Error al cancelar reserva: {e}")
