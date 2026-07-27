import json
import os

RUTA_ARCHIVO = "src/data/cuentas.json"


class CuentaController:

    def crear_cuenta(self):
        print("\n===== CREAR CUENTA =====")

        numero = input("Número de cuenta: ")
        documento = input("Documento del cliente: ")
        tipo = input("Tipo de cuenta (Ahorros/Corriente): ")

        nueva_cuenta = {
            "numero_cuenta": numero,
            "documento_cliente": documento,
            "tipo_cuenta": tipo,
            "saldo": 0
        }

        if os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                try:
                    cuentas = json.load(archivo)
                except json.JSONDecodeError:
                    cuentas = []
        else:
            cuentas = []

        cuentas.append(nueva_cuenta)

        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(cuentas, archivo, indent=4)

        print("\n✅ Cuenta creada correctamente.")

    def listar_cuentas(self):

        if not os.path.exists(RUTA_ARCHIVO):
            print("\nNo existen cuentas registradas.")
            return

        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            cuentas = json.load(archivo)

        if len(cuentas) == 0:
            print("\nNo existen cuentas registradas.")
            return

        print("\n========== CUENTAS REGISTRADAS ==========")

        for cuenta in cuentas:
            print(f"Número: {cuenta['numero_cuenta']}")
            print(f"Documento: {cuenta['documento_cliente']}")
            print(f"Tipo: {cuenta['tipo_cuenta']}")
            print(f"Saldo: ${cuenta['saldo']}")
            print("----------------------------------------")

    def buscar_cuenta(self):

        numero = input("\nIngrese el número de cuenta: ")

        if not os.path.exists(RUTA_ARCHIVO):
            print("\nNo existen cuentas registradas.")
            return

        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            cuentas = json.load(archivo)

        for cuenta in cuentas:
            if cuenta["numero_cuenta"] == numero:
                print("\n========== CUENTA ENCONTRADA ==========")
                print(f"Número: {cuenta['numero_cuenta']}")
                print(f"Documento: {cuenta['documento_cliente']}")
                print(f"Tipo: {cuenta['tipo_cuenta']}")
                print(f"Saldo: ${cuenta['saldo']}")
                print("=======================================")
                return

        print("\n❌ No se encontró la cuenta.")