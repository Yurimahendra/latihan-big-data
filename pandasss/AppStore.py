import pandas as pd
from operator import itemgetter
data = pd.read_csv("/pandasss/AppleStore.csv")

sumGenre = {}
for x in data['prime_genre'] :
    if x in sumGenre.keys() :
        sumGenre[x] += 1
    else:
        sumGenre[x] = 1

#print(sumGenre)

#mensorting data dictionary
#berdasarkan value scr descending
sort_data = sorted(sumGenre.items(), key=itemgetter(1), reverse= True)
for i in range(5) :
    print(sort_data[i])