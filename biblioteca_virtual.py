# Biblioteca Virtual

# Lista para gestionar los libros disponibles
libros_disponibles = []

# Lista para gestionar los libros prestados
libros_prestados = []

# Función para agregar un libro a la biblioteca
def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.

    Args:
        id (int): Identificador único del libro.
        titulo (str): Título del libro.
        autor (str): Autor del libro.
    """
    libro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible"
    }
    libros_disponibles.append(libro)
    print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

# Función para prestar un libro
def prestar_libro(id, usuario):
    """
    Mueve un libro de la lista de disponibles a la lista de prestados, asociándolo a un usuario.

    Args:
        id (int): Identificador único del libro.
        usuario (str): Nombre del usuario que solicita el libro.
    """
    for libro in libros_disponibles:
        if libro["id"] == id and libro["estado"] == "Disponible":
            libro["estado"] = "Prestado"
            libro["usuario"] = usuario
            libros_prestados.append(libro)
            libros_disponibles.remove(libro)
            print(f"El libro '{libro['titulo']}' ha sido prestado a {usuario}.")
            return
    print("El libro no está disponible o no existe.")

# Función para devolver un libro
def devolver_libro(id):
    """
    Regresa un libro de la lista de prestados a la lista de disponibles.

    Args:
        id (int): Identificador único del libro.
    """
    for libro in libros_prestados:
        if libro["id"] == id and libro["estado"] == "Prestado":
            libro["estado"] = "Disponible"
            del libro["usuario"]
            libros_disponibles.append(libro)
            libros_prestados.remove(libro)
            print(f"El libro '{libro['titulo']}' ha sido devuelto.")
            return
    print("El libro no pertenece a los libros prestados o no existe.")

# Función para buscar un libro por título
def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por su título en las listas de disponibles y prestados.

    Args:
        titulo (str): Título del libro a buscar.
    """
    for libro in libros_disponibles + libros_prestados:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Libro encontrado: ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}.")
            if "usuario" in libro:
                print(f"Prestado a: {libro['usuario']}.")
            return
    print("El libro no se encontró.")

# Función para mostrar libros disponibles
def mostrar_libros_disponibles():
    """
    Imprime todos los libros disponibles en la biblioteca.
    """
    print("\nLibros disponibles:")
    if not libros_disponibles:
        print("No hay libros disponibles.")
    else:
        for libro in libros_disponibles:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

# Función para mostrar libros prestados
def mostrar_libros_prestados():
    """
    Imprime todos los libros prestados junto con la información del usuario que los tiene.
    """
    print("\nLibros prestados:")
    if not libros_prestados:
        print("No hay libros prestados.")
    else:
        for libro in libros_prestados:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Prestado a: {libro['usuario']}")

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar libros a la biblioteca
    agregar_libro(1, "Cien años de soledad", "Gabriel García Márquez")
    agregar_libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes")
    agregar_libro(3, "1984", "George Orwell")

    # Mostrar libros disponibles
    mostrar_libros_disponibles()

    # Prestar un libro
    prestar_libro(2, "Juan Pérez")

    # Mostrar libros prestados
    mostrar_libros_prestados()

    # Buscar un libro por título
    buscar_libro_por_titulo("1984")

    # Devolver un libro
    devolver_libro(2)

    # Mostrar libros disponibles después de devolver
    mostrar_libros_disponibles()
