import json
import os

from models.cuenta import Cuenta


RUTA = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "cuentas.json"
)


class CuentaController:


    def crear_cuenta(self):

        print("\n===== CREAR CUENTA =====")

        numero_cuenta = input("Número de cuenta: ")
        documento_cliente = input("Documento del cliente: ")
        tipo_cuenta = input(
            "Tipo de cuenta (Ahorros/Corriente): "
        )


        nueva_cuenta = Cuenta(
            numero_cuenta,
            documento_cliente,
            tipo_cuenta
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                cuentas = json.load(archivo)

        except FileNotFoundError:
            cuentas = []


        cuentas.append(nueva_cuenta.to_dict())


        with open(RUTA, "w", encoding="utf-8") as archivo:
            json.dump(
                cuentas,
                archivo,
                indent=4,
                ensure_ascii=False
            )


        print("\n✅ Cuenta creada correctamente.")



    def listar_cuentas(self):

        print("\n===== LISTA DE CUENTAS =====")


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                cuentas = json.load(archivo)

        except FileNotFoundError:
            cuentas = []


        if len(cuentas) == 0:
            print("No hay cuentas registradas.")
            return


        for cuenta in cuentas:

            print("-------------------------")
            print("Número de cuenta:", cuenta["numero_cuenta"])
            print("Documento:", cuenta["documento_cliente"])
            print("Tipo:", cuenta["tipo_cuenta"])
            print("Saldo: $", cuenta["saldo"])




    def buscar_cuenta(self):

        print("\n===== BUSCAR CUENTA =====")


        numero_cuenta = input(
            "Número de cuenta: "
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                cuentas = json.load(archivo)

        except FileNotFoundError:
            cuentas = []


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero_cuenta:

                print("\n✅ Cuenta encontrada")
                print("Número:", cuenta["numero_cuenta"])
                print("Documento:", cuenta["documento_cliente"])
                print("Tipo:", cuenta["tipo_cuenta"])
                print("Saldo: $", cuenta["saldo"])

                return


        print("\n❌ Cuenta no encontrada.")




    def consignar_dinero(self):

        print("\n===== CONSIGNAR DINERO =====")


        numero_cuenta = input(
            "Número de cuenta: "
        )

        valor = float(
            input("Valor a consignar: ")
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                cuentas = json.load(archivo)

        except FileNotFoundError:
            cuentas = []


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero_cuenta:


                cuenta["saldo"] += valor


                with open(RUTA, "w", encoding="utf-8") as archivo:
                    json.dump(
                        cuentas,
                        archivo,
                        indent=4,
                        ensure_ascii=False
                    )


                print("\n✅ Consignación realizada correctamente.")
                print("Nuevo saldo: $", cuenta["saldo"])

                return


        print("\n❌ Cuenta no encontrada.")




    def retirar_dinero(self):

        print("\n===== RETIRAR DINERO =====")


        numero_cuenta = input(
            "Número de cuenta: "
        )

        valor = float(
            input("Valor a retirar: ")
        )


        try:
            with open(RUTA, "r", encoding="utf-8") as archivo:
                cuentas = json.load(archivo)

        except FileNotFoundError:
            cuentas = []


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero_cuenta:


                if cuenta["saldo"] >= valor:


                    cuenta["saldo"] -= valor


                    with open(RUTA, "w", encoding="utf-8") as archivo:
                        json.dump(
                            cuentas,
                            archivo,
                            indent=4,
                            ensure_ascii=False
                        )


                    print("\n✅ Retiro realizado correctamente.")
                    print("Saldo actual: $", cuenta["saldo"])

                else:

                    print("\n❌ Saldo insuficiente.")


                return


        print("\n❌ Cuenta no encontrada.")