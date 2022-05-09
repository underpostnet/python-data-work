


class Empleado:
    def __init__(self, nombre, apellido, rut, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.direccion = direccion

class Cliente:
    def __init__(self, nombre, apellido, rut, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.direccion = direccion


def getDireccionCliente(cliente):
    return lambda cliente : "tests"

def getDireccionCliente(cliente):
    return lambda cliente : cliente.direccion


testCliente = Cliente("fco", "verdugo", "18234234-5", "lira 33")
test = getDireccionCliente(testCliente)
print(test(testCliente))










# end
