


class Cliente:
    def __init__(self, nombre, apellido, rut, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.direccion = direccion


# iterar clientes
clientes = [
    Cliente("fco", "verdugo", "18234234-5", "lira 33"),
    Cliente("pepe", "rojas", "14344234-5", "nono 453")
]
iterCliente = iter(clientes)

print(next(iterCliente).direccion)
print(next(iterCliente).direccion)

# clonar lista de clientes
print(clientes.copy())
