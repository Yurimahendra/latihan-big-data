def findrange(*MyData):
    #nilai initialisasi maks dan min awal
    maks = MyData[0]
    min = MyData[0]
    #proses pencarian min dan maks
    for data in MyData:
        if data > maks:
            maks = data
        if data < min:
            min = data
    return maks-min

print(findrange(5,1,4,6,10,33,12,6,9,13))