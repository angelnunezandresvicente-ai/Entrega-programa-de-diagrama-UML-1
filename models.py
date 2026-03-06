# Clase base Persona
class Persona:
    def __init__(self, idPersona, nombre):
        self.idPersona = idPersona
        self.nombre = nombre

    def mostrar(self):
        print("Nombre:", self.nombre)

# Usuario hereda de Persona
class Usuario(Persona):
    def __init__(self, idUsuario, nombre, puntos):
        super().__init__(idUsuario, nombre)
        self.puntos = puntos

    def mostrar(self):
        print(f"Usuario: {self.nombre} | Puntos: {self.puntos}")

# Empleado hereda de Persona
class Empleado(Persona):
    def __init__(self, idEmpleado, nombre, rol):
        super().__init__(idEmpleado, nombre)
        self.rol = rol

    def mostrar(self):
        print(f"Empleado: {self.nombre} | Rol: {self.rol}")

# Clase base Espacio
class Espacio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

# Sala hereda de Espacio
class Sala(Espacio):
    def __init__(self, numero, tipo, capacidad):
        super().__init__(f"Sala {numero}", capacidad)
        self.numero = numero
        self.tipo = tipo
        self.asientosOcupados = []

    def reservarAsientos(self, listaAsientos):
        for asiento in listaAsientos:
            if asiento in self.asientosOcupados:
                print("ERROR: el asiento", asiento, "ya está ocupado")
                return False
        self.asientosOcupados.extend(listaAsientos)
        print("Asientos reservados:", listaAsientos)
        return True

    # Método para limpiar todos los asientos
    def limpiarEspacio(self):
        self.asientosOcupados = []
        print(f"Todos los asientos de la Sala {self.numero} han sido liberados.")

# ZonaComida hereda de Espacio
class ZonaComida(Espacio):
    def __init__(self, nombre, capacidad, productos):
        super().__init__(nombre, capacidad)
        self.productos = productos

    def mostrarProductos(self):
        print("Productos disponibles en", self.nombre)
        for p in self.productos:
            print("-", p)

# Pelicula
class Pelicula:
    totalPeliculas = 0
    def __init__(self, idPelicula, nombre, duracion, tipo):
        self.idPelicula = idPelicula
        self.nombre = nombre
        self.duracion = duracion
        self.tipo = tipo
        Pelicula.totalPeliculas += 1

    def mostrar(self):
        print(f"ID: {self.idPelicula} | Nombre: {self.nombre} | Tipo: {self.tipo} | Duracion: {self.duracion} min")

# Promocion
class Promocion:
    def __init__(self, codigo, descuento):
        self.codigo = codigo
        self.descuento = descuento

    def aplicarDescuento(self, monto):
        return monto - (monto * self.descuento)

# Funcion (pelicula + sala + horario)
class Funcion:
    def __init__(self, pelicula, sala, horario):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario

    def mostrar(self):
        print(f"Funcion: {self.pelicula.nombre} | Sala: {self.sala.numero} | Tipo: {self.sala.tipo} | Horario: {self.horario}")

# Reserva
class Reserva:
    def __init__(self, usuario, funcion, asientos, precio):
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.precio = precio

    def mostrar(self):
        print("\nResumen de Reserva")
        print("Usuario:", self.usuario.nombre)
        print("Película:", self.funcion.pelicula.nombre)
        print("Sala:", self.funcion.sala.numero)
        print("Horario:", self.funcion.horario)
        print("Asientos:", self.asientos)
        print("Total:", self.precio)