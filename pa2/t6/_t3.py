

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


class Clientes:
    def __init__(self, clientes):
        self.clientes = clientes
    def __iter__(self):
        return iter(self.clientes)


class Empleados:
    def __init__(self, empleados):
        self.empleados = empleados
    def __iter__(self):
        return iter(self.empleados)



clientes = Clientes([
    Cliente("fco", "verdugo", "18234234-5", "lira 33"),
    Cliente("pepe", "rojas", "14344234-5", "nono 453")
]);

empleados = Empleados([
    Cliente("fco2", "verdugo2", "18234234-5", "lira 33"),
    Cliente("pepe2", "rojas2", "14344234-5", "nono 453")
]);

for item in clientes:
    print(item.nombre)

for item in empleados:
    print(item.nombre)
