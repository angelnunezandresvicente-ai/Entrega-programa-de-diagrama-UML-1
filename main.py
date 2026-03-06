from models import Pelicula, Usuario, Empleado, Sala, Promocion, Funcion, Reserva

usuarios = [
    Usuario(1,"Andres",100),
    Usuario(2,"Carlos",50),
    Usuario(3,"Maria",70),
    Usuario(4,"Luis",20),
    Usuario(5,"Ana",80),
    Usuario(6,"Pedro",40),
    Usuario(7,"Sofia",60),
    Usuario(8,"Miguel",30),
    Usuario(9,"Laura",90),
    Usuario(10,"Diego",10)
]

empleados = [
    Empleado(1,"Jose","Taquillero"),
    Empleado(2,"Marta","Administrador")
]

peliculas = [
    Pelicula(1,"Avatar 2",120,"3D"),
    Pelicula(2,"Dune 2",150,"IMAX"),
    Pelicula(3,"Batman",130,"2D"),
    Pelicula(4,"Spiderman",125,"3D"),
    Pelicula(5,"Matrix",140,"2D"),
    Pelicula(6,"Interstellar",165,"IMAX"),
    Pelicula(7,"Titanic",195,"2D"),
    Pelicula(8,"Joker",122,"2D"),
    Pelicula(9,"Mario",110,"3D"),
    Pelicula(10,"Transformers",130,"3D")
]

salas = [
    Sala(1,"IMAX",50),
    Sala(2,"3D",40)
]

promociones = [
    Promocion("DESC10",0.10),
    Promocion("PROMO20",0.20)
]

funciones = [
    Funcion(peliculas[0], salas[0], "18:00"),
    Funcion(peliculas[1], salas[1], "19:30"),
    Funcion(peliculas[2], salas[0], "21:00"),
    Funcion(peliculas[3], salas[1], "16:00"),
    Funcion(peliculas[4], salas[0], "14:00"),
    Funcion(peliculas[5], salas[1], "20:00"),
    Funcion(peliculas[6], salas[0], "17:00"),
    Funcion(peliculas[7], salas[1], "19:00"),
    Funcion(peliculas[8], salas[0], "15:00"),
    Funcion(peliculas[9], salas[1], "21:30")
]


print("\n=== Bienvenido a CinePapoy ===")

while True:
    # Primero se elige si es usuario o empleado
    tipo = input("\nEres Usuario o Empleado? (u/e): ").lower()

    if tipo == "u":
        # ===== USUARIO =====
        print("\nUsuarios disponibles:")
        for u in usuarios:
            u.mostrar()

        nombreUsuario = input("\nIngresa tu nombre: ")
        usuarioActual = None
        for u in usuarios:
            if u.nombre.lower() == nombreUsuario.lower():
                usuarioActual = u

        if usuarioActual is None:
            print("Usuario no encontrado. ¿Deseas registrarte? (si/no)")
            if input().lower() == "si":
                puntos = int(input("Ingresa tus puntos iniciales: "))
                nuevo_id = len(usuarios) + 1
                usuarioActual = Usuario(nuevo_id, nombreUsuario, puntos)
                usuarios.append(usuarioActual)
                print(f"Usuario {nombreUsuario} registrado con éxito.")
            else:
                continue

        # Mostrar funciones disponibles
        print("\nFunciones disponibles:")
        for idx,f in enumerate(funciones):
            print(f"{idx+1}. ", end="")
            f.mostrar()

        seleccion = input("\nSelecciona la función por número: ")
        try:
            seleccion = int(seleccion) - 1
            funcionElegida = funciones[seleccion]
        except:
            print("Selección inválida")
            continue

        # Reserva de asientos
        while True:
            asientos = input("Ingresa los asientos separados por coma (ej: 1,2,3): ")
            try:
                listaAsientos = [int(a) for a in asientos.split(",")]
            except:
                print("Debes ingresar números válidos")
                continue

            if funcionElegida.sala.reservarAsientos(listaAsientos):
                break
            else:
                print("Intenta con otros asientos")

        # Aplicar promoción
        precio = len(listaAsientos) * 70
        usarPromo = input("¿Aplicar promoción? (si/no): ")
        if usarPromo.lower() == "si":
            print("Promociones disponibles:")
            for idx, promo in enumerate(promociones):
                print(f"{idx+1}. {promo.codigo} ({int(promo.descuento*100)}% de descuento)")
            sel = int(input("Selecciona la promoción por número: ")) - 1
            precio = promociones[sel].aplicarDescuento(precio)
            print("Promoción aplicada")

        # Crear y mostrar reserva
        reserva = Reserva(usuarioActual, funcionElegida, listaAsientos, precio)
        reserva.mostrar()

    elif tipo == "e":
        # ===== EMPLEADO =====
        print("\nEmpleados disponibles:")
        for emp in empleados:
            emp.mostrar()

        nombreEmpleado = input("\nIngresa tu nombre: ")
        empleadoActual = None
        for emp in empleados:
            if emp.nombre.lower() == nombreEmpleado.lower():
                empleadoActual = emp

        if empleadoActual is None:
            print("Empleado no encontrado")
            continue

        print(f"\nBienvenido {empleadoActual.nombre} | Rol: {empleadoActual.rol}")

        if empleadoActual.rol.lower() == "administrador":
            # Solo administrador puede limpiar salas
            print("\nSalas disponibles para limpiar:")
            for s in salas:
                print(f"Sala {s.numero} | Tipo: {s.tipo} | Asientos ocupados: {len(s.asientosOcupados)}")
            sel = int(input("Selecciona la sala a limpiar (numero): "))
            salaElegida = None
            for s in salas:
                if s.numero == sel:
                    salaElegida = s
                    break
            if salaElegida:
                salaElegida.limpiarEspacio()
            else:
                print("Sala no encontrada")
        else:
            print("Rol no tiene permisos especiales.")

    else:
        print("Opción inválida")
        continue

    if input("\n¿Desea continuar? (si/no): ").lower() != "si":
        print("Gracias por usar CinePapoy. ¡Hasta luego!")
        break