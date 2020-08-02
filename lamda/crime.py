# berapa lama rata-rata kriminalitas terjadi dan jam berapa yang paling banyak di kota denver
# link dataset http://rosihanari.net/python-suplemen/

import pandas as pd
import numpy as np
import datetime as dt
import operator as op

file = '/studi-kasus/denver-crimes/crime.csv'
dataCrime = pd.read_csv(file, sep=',')
dataCrimeOccur = dataCrime.filter(items=['FIRST_OCCURRENCE_DATE', 'LAST_OCCURRENCE_DATE'])
dataCrimeOccurList = dataCrimeOccur.values.tolist()
filterDataCrimeOccur = list(filter(lambda x: str(x[1]) != 'nan', dataCrimeOccurList))

for i in range(len(filterDataCrimeOccur)):
    a = dt.datetime.strptime(filterDataCrimeOccur[i][0], '%m/%d/%Y %I:%M:%S %p')
    filterDataCrimeOccur[i][0] = a
    b = dt.datetime.strptime(filterDataCrimeOccur[i][1], '%m/%d/%Y %I:%M:%S %p')
    filterDataCrimeOccur[i][1] = b
#print(filterDataCrimeOccur[:5])
deltaTime = list(map(lambda x: (x[1] - x[0]).days + (x[1] - x[0]).seconds/86400, filterDataCrimeOccur))
arrayDeltaTime = np.array(deltaTime)
arrayDeltaTime.mean()

rekap = {}
for i in range(len(filterDataCrimeOccur)):
    if filterDataCrimeOccur[i][0].hour in rekap:
        rekap[filterDataCrimeOccur[i][0].hour] += 1
    else:
        rekap[filterDataCrimeOccur[i][0].hour] = 1
sortRekap = sorted(rekap.items(), key=op.itemgetter(1), reverse=True)
print(sortRekap[:5])