import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = 2 * x
y2 = 2 ** x
plt.plot(x, y1, 'ro', x, y2, 'x')
plt.title('menggabungkan dua plot berbeda')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()