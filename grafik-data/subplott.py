import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = x ** 2
y2 = x ** 3

plt.subplot(1, 2, 1)
plt.plot(x, y1, 'r-')
plt.legend(['Y = x^2'])

plt.subplot(1, 2, 2)
plt.plot(x, y2, 'b-')
plt.legend(['Y = x^3'])

plt.suptitle('contoh grafik fungsi')
plt.show()