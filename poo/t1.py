
class Farmacia:
    def __init__(self, nombreFarmacia, direccionFarmacia):
        self.nombreFarmacia = nombreFarmacia
        self.direccionFarmacia = direccionFarmacia

    def getNombreFarmacia(self):
        return self.nombreFarmacia

class Medicamento(Farmacia):
    def __init__(self, nombreFarmacia, direccionFarmacia, precio, marca):
        super().__init__(nombreFarmacia, direccionFarmacia)
        self.precio = precio
        self.marca = marca

    def getPrecio(self):
        return self.precio

    def getMarca(self):
        return self.marca

    def __del__(self):
        print('Destructor called')



medicamentos = []
for i in range(0, int(input("Ingrese numero de medicamentos a ingresar: "))):
    medicamentos.append(Medicamento(input("Ingrese nombre farmacia: "), input("Ingrese dirreccion farmacia: "), float(input("Ingrese Precio: ")), input("Ingrese marca: ")))

    print("marca ->")
    print(medicamentos[len(medicamentos)-1].getMarca())
    print("precio ->")
    print(medicamentos[len(medicamentos)-1].getPrecio())
    print("Nombre Farmacia ->")
    print(medicamentos[len(medicamentos)-1].getNombreFarmacia())

    print('medicamento ingresado \n')
