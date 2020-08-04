# menganalisa korelasi antar data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'weight-height.csv'
data = pd.read_csv(file)
berat = data['Weight']
tinggi = data['Height']

meanBerat = np.mean(berat)
meanTinggi = np.mean(tinggi)
stdBerat = np.std(berat)
stdTinggi = np.std(tinggi)
dataClean = data[(np.abs((data['Weight'] - meanBerat) / stdBerat) <= 3) &
                 (np.abs((data['Height'] - meanTinggi) / stdTinggi) <= 3)]

tinggi = dataClean['Weight']
berat = dataClean['Height']

plt.scatter(berat, tinggi)
plt.xlabel('Berat')
plt.ylabel('Tinggi')
plt.show()