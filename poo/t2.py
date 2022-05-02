

class Libro:
    def __init__(self, autor, paginas, precio):
        self.precio = precio
        self.autor = autor
        self.paginas = paginas
        self.USD_CLP = 860

    def getPrecio(self):
        return self.precio

    def getAutor(self):
        return self.autor

    def getPaginas(self):
        return self.paginas

    def getUsdValue(self):
        return self.precio/self.USD_CLP

    def __del__(self):
        print('Destructor called')



libro = Libro(input('Ingrese Auto: '), input('Ingrese Paginas: '), float(input('Ingrese precio (CLP): ')));
print('El valor del libro ingresado es de: [USD] $',libro.getUsdValue());
