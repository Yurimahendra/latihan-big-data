# penjualan terbanyak di kanada

import pandas as pd

file = 'Sample - Superstore.xls'
data = pd.read_excel(file, sheet_name='Orders')
orderId = list(data['Order ID'])
caOrderId = list(filter(lambda x: x[:2] == 'CA', orderId))
#print(len(caOrderId))
rekap = {}
for i in range(len(caOrderId)):
    if caOrderId[i][3:7] in rekap:
        rekap[caOrderId[i][3:7]] += 1
    else:
        rekap[caOrderId[i][3:7]] = 1

print(rekap)