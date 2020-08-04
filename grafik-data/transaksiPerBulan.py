# statistik jumlah transaksi per bulan
import pandas as pd
import matplotlib.pyplot as plt

file = '../lamda/Sample - Superstore.xls'
data = pd.read_excel(file, sheet_name='Orders')
datesOrder = data['Order Date']
datesOrderStr = list(map(lambda x: str(x), datesOrder))
datesOrder2015 = list(filter(lambda x: str(x[:4]) == '2015', datesOrderStr))
rekapOrder = {}
for tgl in  datesOrder2015:
    if tgl[5:7] in rekapOrder:
        rekapOrder[tgl[5:7]] += 1
    else:
        rekapOrder[tgl[5:7]] = 1
bulanOrder = list(rekapOrder.keys())
bulanOrder.sort()
jumlahOrder = []
for bln in bulanOrder:
    jumlahOrder.append(rekapOrder[bln])

plt.bar(bulanOrder, jumlahOrder, color='red')
plt.title('Jumlah Order 2015')
plt.xlabel('Bulan')
plt.ylabel('Jumlah')
plt.show()