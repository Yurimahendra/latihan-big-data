import pandas as pd


#seting nama file
file = "/home/yuri/Documents/latihan-big-data/studi-kasus/pandasss/Sample - Superstore.xls"
#baca data excel pada sheet 'Orders'
DataOrders = pd.read_excel(file, sheet_name='Orders')
#inisialisasi counter awal
SumKanada = 0
SumAs = 0
#baca data hanya pada field Order ID
for data in DataOrders['Order ID'] :
    #jika digit 0-1 adalah 'CA' atau 'US'
    if data[:2] == 'CA' :
        #counter bertambah
        SumKanada += 1
    elif data[:2] == 'US':
        #counter bertambah
        SumAs += 1

#output
print("Jumlah transaksi di Canada : ", SumKanada)
print("Jumlah transaksi di US : ", SumAs)