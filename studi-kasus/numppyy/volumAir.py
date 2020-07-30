# ada 6 buah kaleng,
# hitung volume air dalam kaleng yang memiliki jari-jari dan tinggi adalah bilangan bilangan bulat 5 sampai 40


import numpy as np

np.random.seed(0)
data = np.random.randint(5, 40, 12)
data.resize(6, 2)
vol = np.pi * data[:, 0] ** 2 * data[:, 1]
print("volume setiap kaleng =", vol, sep=" ")
print("volume semua kaleng =", vol.sum())
print("rata-rata volume  kaleng =", vol.mean())
print("volume kaleng terbesar =", vol.argmax())
print("volume kaleng terkecil =", vol.argmin())

