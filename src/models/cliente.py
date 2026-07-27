class Cliente:

    def __init__(self, documento, nombre, apellido, telefono, correo, direccion):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def to_dict(self):
        return {
            "documento": self.documento,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion
        }