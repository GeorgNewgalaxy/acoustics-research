import numpy as np
a = np.sin(440*np.sin(np.sin(440*np.pi*np.linspace(0, 1, 1000000))))**2
b = np.linspace(0, 2, 1000000)
c = a + b
print(len(c))
