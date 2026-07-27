from controllers.cliente_controller import ClienteController
from controllers.cuenta_controller import CuentaController


def menu():

    cliente_controller = ClienteController()
    cuenta_controller = CuentaController()

    while True:

        print("\n========== SISTEMA BANCARIO ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Crear cuenta")
        print("4. Listar cuentas")
        print("5. Buscar cuenta")
        print("6. Consignar dinero")
        print("7. Retirar dinero")
        print("8. Salir")

        opcion = input("\nSeleccione una opción: ")


        if opcion == "1":
            cliente_controller.registrar_cliente()

        elif opcion == "2":
            cliente_controller.listar_clientes()

        elif opcion == "3":
            cuenta_controller.crear_cuenta()

        elif opcion == "4":
            cuenta_controller.listar_cuentas()

        elif opcion == "5":
            cuenta_controller.buscar_cuenta()

        elif opcion == "6":
            cuenta_controller.consignar_dinero()

        elif opcion == "7":
            cuenta_controller.retirar_dinero()

        elif opcion == "8":
            print("\nGracias por usar el sistema.")
            break

        else:
            print("\n❌ Opción no válida.")



if __name__ == "__main__":
    menu()