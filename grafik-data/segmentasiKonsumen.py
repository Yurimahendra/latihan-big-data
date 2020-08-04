# segmentasi konsumen superstore
import pandas as pd
import matplotlib.pyplot as plt

file = '../lamda/Sample - Superstore.xls'
data = pd.read_excel(file, sheet_name='Orders')
segments = list(data['Segment'])
rekapSegments = {}
for s in segments:
    if s in rekapSegments:
        rekapSegments[s] += 1
    else:
        rekapSegments[s] = 1

segmentsType = rekapSegments.keys()
jml = rekapSegments.values()

plt.pie(jml, autopct='%1.0f%%', labels=segmentsType, startangle=60)
plt.axis('equal')
plt.title('Superstore Buyer Segmentation')
plt.show()