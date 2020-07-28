import pandas as pd


#list tahun
ListThn = ['2014', '2015', '2016', '2017']

#inisialisasi awal jumlah transaksi per tahun
#per negara
SumCanada = {}
SumAs = {}
for thn in ListThn :
    SumCanada[thn] = 0
    SumAs[thn] = 0

#seting nama file
file = "/home/yuri/Documents/latihan-big-data/studi-kasus/pandasss/Sample - Superstore.xls"

#baca data pada sheet 'Orders'
DataOrder = pd.read_excel(file, sheet_name='Orders')

#pencacahan data transaksi per tahun
#per negara
for data in DataOrder['Order ID'] :
    #ambil tahun dari data Order ID
    thn = data[3:7]
    if data[:2] == 'CA' :
        SumCanada[thn] += 1
    elif data[:2] == 'US' :
        SumAs[thn] += 1

#output
print('Negara'.ljust(18), end='')
for thn in ListThn :
    print(thn.rjust(5), end='')
print()
print('-----------------------------------------------')
print('Amerika Serikat'.ljust(19), end='')
for thn in ListThn :
    print(str(SumAs[thn]).ljust(5), end='')
print()
print('Kanada'.ljust(18), end='')
for thn in ListThn :
    print(str(SumCanada[thn]).rjust(5), end='')