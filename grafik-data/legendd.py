import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = 2 * x
y2 = 2 ** x
plt.plot(x, y1, 'r-', x, y2, 'b--')
plt.title('memberikan keterangan pada grafik')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['Y = 2x', 'Y = 2^x'], loc = 'best')
plt.show()