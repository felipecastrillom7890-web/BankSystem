from controllers.cuenta_controller import CuentaController


def menu():

    cuenta_controller = CuentaController()

    while True:

        print("\n========== SISTEMA BANCARIO ==========")
        print("1. Crear cuenta")
        print("2. Listar cuentas")
        print("3. Buscar cuenta")
        print("4. Consignar dinero")
        print("5. Retirar dinero")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            cuenta_controller.crear_cuenta()

        elif opcion == "2":
            cuenta_controller.listar_cuentas()

        elif opcion == "3":
            cuenta_controller.buscar_cuenta()

        elif opcion == "4":
            cuenta_controller.consignar_dinero()

        elif opcion == "5":
            cuenta_controller.retirar_dinero()

        elif opcion == "6":
            print("\nGracias por usar el sistema bancario.")
            break

        else:
            print("\n❌ Opción inválida.")


if __name__ == "__main__":
    menu()