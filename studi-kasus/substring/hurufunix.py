#menghitung jumlah huruf unix dalam suatu string
def StatHuruf(s) :
    #mengubah string ke set
    #konversi set ke list
    DataHuruf = list(set(s))
    #sorting
    DataHuruf.sort()
    #inisialisasi dictionari huruf
    DictHuruf = {}
    #inisialisasi jumlah huruf
    for huruf in DataHuruf :
        DictHuruf[huruf] = 0
    #menghtung jumlah setiap huruf
    for huruf in s :
        DictHuruf[huruf] += 1
    return DictHuruf


s = input("masukan string :")
print(StatHuruf(s))
