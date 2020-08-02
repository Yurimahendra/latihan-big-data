# mencari produk paling menguntungkan dan merugikan

import pandas as pd
import operator as op

file = 'Sample - Superstore.xls'
data = pd.read_excel(file, sheet_name='Orders')
data.head()
data = data.filter(items=['Sub-Category', 'Product Name', 'Profit'])
#print(data[:5])
dataList = data.values.tolist()
#print(dataList[:5])
dataRugi = list(filter(lambda x: x[2] < 0, dataList))
#print(dataRugi[:5])
dataUntung = list(filter(lambda x: x[2] > 0, dataList))
#print(dataUntung[:5])
totalRugi = {}
for i in range(len(dataRugi)):
    if dataRugi[i][0] in totalRugi:
        totalRugi[dataRugi[i][0]] += dataRugi[i][2]
    else:
        totalRugi[dataRugi[i][0]] = dataRugi[i][2]
print("Total rugi berdasarkan sub kategori : ")
#print(totalRugi)
sortTotalRugi = sorted(totalRugi.items(), key=op.itemgetter(1), reverse=False)
print(sortTotalRugi)
print("====================================================")
totalUntung = {}
for i in range(len(dataUntung)):
    if dataUntung[i][0] in totalUntung:
        totalUntung[dataUntung[i][0]] += dataUntung[i][2]
    else:
        totalUntung[dataUntung[i][0]] = dataUntung[i][2]
print("Total untung berdasarkan sub kategori : ")
#print(totalUntung)
sortTotalUntung = sorted(totalUntung.items(), key=op.itemgetter(1), reverse=True)
print(sortTotalUntung)
print("=====================================================")
dataBinders = list(filter(lambda x: x[0] == 'Binders', dataList))
#print(dataBinders[:5])
bindersUntung = list(filter(lambda x: x[2] > 0, dataBinders))
#print(bindersUntung[:5])

totalBinderUntung = {}
for i in range(len(bindersUntung)):
    if bindersUntung[i][1] in totalBinderUntung:
        totalBinderUntung[bindersUntung[i][1]] += bindersUntung[i][2]
    else:
        totalBinderUntung[bindersUntung[i][1]] = bindersUntung[i][2]
sortTotalBinderUntung = sorted(totalBinderUntung.items(), key=op.itemgetter(1), reverse=True)
print("total untung binder berdasarkan nama produk : ")
print(sortTotalBinderUntung)
print("=================================================")

bindersRugi = list(filter(lambda x: x[2] < 0, dataBinders))
totalBinderRugi = {}
for i in range(len(bindersRugi)):
    if bindersRugi[i][1] in totalBinderRugi:
        totalBinderRugi[bindersRugi[i][1]] += bindersRugi[i][2]
    else:
        totalBinderRugi[bindersRugi[i][1]] = bindersRugi[i][2]
sortTotalBinderRugi = sorted(totalBinderRugi.items(), key=op.itemgetter(1), reverse=False)
print("total rugi binder berdasarkan nama produk : ")
print(sortTotalBinderRugi)

