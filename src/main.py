from controllers.cliente_controller import ClienteController


def menu():

    cliente_controller = ClienteController()

    while True:

        print("\n==============================")
        print("     SISTEMA BANCARIO")
        print("==============================")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")


        if opcion == "1":

            cliente_controller.registrar_cliente()


        elif opcion == "2":

            cliente_controller.listar_clientes()


        elif opcion == "3":

            cliente_controller.actualizar_cliente()


        elif opcion == "4":

            cliente_controller.eliminar_cliente()


        elif opcion == "5":

            print("\nGracias por usar el sistema.")
            break


        else:

            print("\n❌ Opcion no valida.")



if __name__ == "__main__":
    menu()