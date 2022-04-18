

def ord_seleccion():
    listSelection = []
    for i in range(0, 3):
        listSelection.append(int(input(('ingrese numero ' + str(i+1) + ' :'))))

    print('input list ->')
    print(listSelection)
    return max(listSelection)


print('max value ->', ord_seleccion())
