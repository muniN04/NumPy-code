import numpy as np 
import matplotlib.pyplot as plt

x=np.random.randint(1,11,size=10)
y=np.random.randint(1,11,size=10)
print(x)
print(y)
plt.plot(x,y,
         marker='o',
         markersize=8,
         markeredgecolor='blue',
         markerfacecolor='yellow',
         label='data',
         color='red',
         linestyle='-.',
         linewidth=1)



plt.legend()
plt.axvline(x=4)
plt.show()