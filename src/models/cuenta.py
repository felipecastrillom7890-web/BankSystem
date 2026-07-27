class Cuenta:
    def __init__(self, numero_cuenta, documento_cliente, tipo_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.documento_cliente = documento_cliente
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def mostrar_datos(self):
        print("========== CUENTA ==========")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Documento del cliente: {self.documento_cliente}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo: ${self.saldo}")
        print("============================")