import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, 10)
plt.show()