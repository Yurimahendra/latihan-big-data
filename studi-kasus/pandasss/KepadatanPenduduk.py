import mysql.connector as sql
import pandas as pd

#koneksi ke mysql
mydb = sql.connect(host='localhost', database='world', user='yuri', password='Yuri_ma6')

#baca semua record pada tabel country
data = pd.read_sql('SELECT * FROM country', con=mydb)

#mendapatkan semua nama benua scr unix
setBenua = set(data['Continent'])

#inisialisasi nilai listmax
listMax = {}
for benua in setBenua :
    listMax[benua] = ['', 0]

#mencari nama negara dg density maks
for index, row in data.iterrows() :
    negara = row['Name']
    benua = row['Continent']
    density = row['Population'] / row['SurfaceArea']
    if density > listMax[benua][1] :
        listMax[benua] = [negara, density]

#output
print('Benua'.ljust(15), 'Negara'.ljust(10), 'Kepadatan'.rjust(10))
print('-----------------------------------------------------------------')
for benua, value in listMax.items() :
    print(str(benua).ljust(15), value[0].ljust(10), '{:.2f}'.format(value[1]).rjust(10))