# terdapat 36 kartu, diberikan secara merata kepada 6 orang secara random
# hitung skor kartunya untuk masing-masing orang tersebut.

import numpy as np

#mendapatkan angka urut mulai dari 1 sampai 36
kartu = np.arange(1, 37)

#mengacak urutan kartu
np.random.shuffle(kartu)

#merubah ke array dua dimensi menjadi matrix (6x6)
kartu.resize(6, 6)

#membuat matrix 6x6 (matrix a)
a = np.eye(6)

b = kartu * a

#membuat matrix 1 berukuran 6x6 (matrix c)
c = np.ones((6, 6))

d = a - c

e = d * kartu

f = b + e

print(np.sum(f, axis=0))