import matplotlib.pyplot as plt

berat = [80, 78, 77, 68, 84, 73, 70, 69]
tinggi = [170, 168, 165, 171, 169, 170, 163, 166]

plt.scatter(berat, tinggi)
plt.xlim(60, 90)
plt.ylim(160, 175)
plt.xlabel('Berat')
plt.ylabel('Tinggi')
plt.show()