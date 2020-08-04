# menggabungkan dua plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 13, 8]
plt.plot(x, y, 'r-', x, y, 'bo')
plt.title('menggabungkan dua plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()