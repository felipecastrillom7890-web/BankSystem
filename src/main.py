from controllers.cliente_controller import ClienteController
from controllers.cuenta_controller import CuentaController


def menu():

    cliente_controller = ClienteController()
    cuenta_controller = CuentaController()


    while True:

        print("\n========== SISTEMA BANCARIO ==========")

        print("\n--- CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")


        print("\n--- CUENTAS ---")
        print("5. Crear cuenta")
        print("6. Listar cuentas")
        print("7. Buscar cuenta")
        print("8. Consignar dinero")
        print("9. Retirar dinero")


        print("\n10. Salir")


        opcion = input("\nSeleccione una opción: ")


        # CRUD CLIENTES

        if opcion == "1":

            cliente_controller.registrar_cliente()


        elif opcion == "2":

            cliente_controller.listar_clientes()


        elif opcion == "3":

            cliente_controller.actualizar_cliente()


        elif opcion == "4":

            cliente_controller.eliminar_cliente()



        # GESTIÓN DE CUENTAS

        elif opcion == "5":

            cuenta_controller.crear_cuenta()


        elif opcion == "6":

            cuenta_controller.listar_cuentas()


        elif opcion == "7":

            cuenta_controller.buscar_cuenta()


        elif opcion == "8":

            cuenta_controller.consignar_dinero()


        elif opcion == "9":

            cuenta_controller.retirar_dinero()



        elif opcion == "10":

            print("\nGracias por usar el sistema bancario.")
            break


        else:

            print("\n❌ Opción no válida.")



if __name__ == "__main__":
    menu()