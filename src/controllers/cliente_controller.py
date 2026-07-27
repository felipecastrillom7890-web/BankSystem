import json
import os

from models.cliente import Cliente


RUTA = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "clientes.json"
)


class ClienteController:


    # ==========================
    # CREAR CLIENTE
    # ==========================

    def registrar_cliente(self):

        print("\n=== REGISTRO DE CLIENTE ===")

        documento = input("Documento: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        direccion = input("Direccion: ")


        nuevo_cliente = Cliente(
            documento,
            nombre,
            apellido,
            telefono,
            correo,
            direccion
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                clientes = json.load(archivo)

        except FileNotFoundError:
            clientes = []


        clientes.append(nuevo_cliente.to_dict())


        with open(RUTA, "w", encoding="utf-8") as archivo:
            json.dump(
                clientes,
                archivo,
                indent=4,
                ensure_ascii=False
            )


        print("\n✅ Cliente registrado correctamente.")



    # ==========================
    # LEER CLIENTES
    # ==========================

    def listar_clientes(self):

        print("\n=== LISTA DE CLIENTES ===")


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                clientes = json.load(archivo)

        except FileNotFoundError:
            clientes = []


        if not clientes:
            print("No hay clientes registrados.")
            return


        for cliente in clientes:

            print("----------------------")
            print("Documento:", cliente["documento"])
            print("Nombre:", cliente["nombre"])
            print("Apellido:", cliente["apellido"])
            print("Telefono:", cliente["telefono"])
            print("Correo:", cliente["correo"])
            print("Direccion:", cliente["direccion"])



    # ==========================
    # ACTUALIZAR CLIENTE
    # ==========================

    def actualizar_cliente(self):

        print("\n=== ACTUALIZAR CLIENTE ===")


        documento_buscar = input(
            "Ingrese documento del cliente: "
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                clientes = json.load(archivo)

        except FileNotFoundError:
            clientes = []


        encontrado = False


        for cliente in clientes:

            if cliente["documento"] == documento_buscar:


                cliente["nombre"] = input(
                    "Nuevo nombre: "
                )

                cliente["apellido"] = input(
                    "Nuevo apellido: "
                )

                cliente["telefono"] = input(
                    "Nuevo telefono: "
                )

                cliente["correo"] = input(
                    "Nuevo correo: "
                )

                cliente["direccion"] = input(
                    "Nueva direccion: "
                )


                encontrado = True
                break



        if encontrado:

            with open(RUTA, "w", encoding="utf-8") as archivo:

                json.dump(
                    clientes,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )


            print("\n✅ Cliente actualizado correctamente.")


        else:

            print("\n❌ Cliente no encontrado.")




    # ==========================
    # ELIMINAR CLIENTE
    # ==========================

    def eliminar_cliente(self):

        print("\n=== ELIMINAR CLIENTE ===")


        documento_buscar = input(
            "Ingrese documento del cliente: "
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                clientes = json.load(archivo)

        except FileNotFoundError:
            clientes = []


        clientes_filtrados = []

        eliminado = False


        for cliente in clientes:

            if cliente["documento"] == documento_buscar:

                eliminado = True

            else:

                clientes_filtrados.append(cliente)



        if eliminado:

            with open(RUTA, "w", encoding="utf-8") as archivo:

                json.dump(
                    clientes_filtrados,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )


            print("\n✅ Cliente eliminado correctamente.")


        else:

            print("\n❌ Cliente no encontrado.")