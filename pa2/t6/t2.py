



class MiClase:
    def __init__(self, items):
        self.lista = items
    def __iter__(self):
        return iter(self.lista)
    def __test__(self):
        print('test')



miobjeto = MiClase([5, 4, 3])
for item in miobjeto:
    print(item)



libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)

print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))

print(libro.copy())
print(miobjeto.__test__())

a = 'a'
b = a
b = 'b'
print(a)
