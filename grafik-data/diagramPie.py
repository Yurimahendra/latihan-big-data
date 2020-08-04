import matplotlib.pyplot as plt

jobs = ['Guru', 'Programmer', 'Dokter', 'Wiraswasta', 'Lain-lain']
jml = [70, 30, 25, 82, 10]
plt.pie(jml, autopct='%1.0f%%', labels=jobs, startangle=60)
plt.axis('equal')
plt.title('Pekerjaan alumni')
plt.show()