


def replicar(_list, n):

    if n == 1:
        return _list

    returnList = []
    for num in _list:
        for rep in range(0, n):
            returnList.append(replicar(num, 1))

    return returnList

test = [1,3,4];
print('input test ->')
print(test)
print(replicar(test, int(input('ingrese numero de veces: '))))
