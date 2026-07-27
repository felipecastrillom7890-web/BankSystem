from controllers.cliente_controller import ClienteController


def menu():

    cliente_controller = ClienteController()

    while True:

        print("\n========== SISTEMA BANCARIO ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cliente_controller.registrar_cliente()

        elif opcion == "2":
            cliente_controller.listar_clientes()

        elif opcion == "3":
            cliente_controller.buscar_cliente()

        elif opcion == "4":
            cliente_controller.actualizar_cliente()

        elif opcion == "5":
            cliente_controller.eliminar_cliente()

        elif opcion == "6":
            print("\nGracias por usar el sistema.")
            break

        else:
            print("\n❌ Opción no válida.")


if __name__ == "__main__":
    menu()