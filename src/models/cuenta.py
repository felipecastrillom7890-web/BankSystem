class Cuenta:

    def __init__(self, numero_cuenta, documento_cliente, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.documento_cliente = documento_cliente
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0


    def to_dict(self):

        return {
            "numero_cuenta": self.numero_cuenta,
            "documento_cliente": self.documento_cliente,
            "tipo_cuenta": self.tipo_cuenta,
            "saldo": self.saldo
        }