
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import show

#https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

tiempo=np.arange(0,1000,0.1)
pob1=10-10*np.exp(-tiempo/189)
pob2=10*tiempo*np.exp(-tiempo/155)/100

# tiempo= [1, 2, 3]
# pob1= [3,2,4]
# pob2= [6,1,3]

print(tiempo)
print(pob1)
print(pob1)

plt.plot(tiempo, pob1, 'k', label='Población A', color='green')
plt.plot(tiempo, pob2, 'k:', label='Población B', color='red')
plt.xlabel("Tiempo (días)")
plt.ylabel("Individuos")
plt.legend()

show()


#end
