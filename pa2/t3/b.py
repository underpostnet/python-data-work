



def evalNum(test):
    for num in test:
        if num < 0:
            print('numero '+str(num)+' es negativo')
        else:
            print('numero '+str(num)+' es positivo')

testList = [9, -2, 3]
print('input list ->', testList)
evalNum(testList)
