import matplotlib.pyplot as plt

kelas = ['A', 'B', 'C', 'D', 'E']
jumSiswa = [30, 45, 37, 50, 53]
plt.bar(kelas, jumSiswa, color = 'red')
#membuat diagram secra horizobtal
#plt.barh(kelas, jumSiswa, color = 'red')
plt.title("Jumlah Siswa Kelas 6")
plt.xlabel('Kelas')
plt.ylabel('Jumlah')
plt.show()