#menghitung jumlah substring x dari string s
def cekSubString(x, s) :
    #cek keberadaan x dalam s
    status = x in s
    #nilai awal sum
    sum = 0
    for i in range(len(s)) :
        #jika ditemukan x dalam s maka sum bertambah
        if s[i:i+len(x)] == x :
            sum += 1
    return (status, sum)

st = input("masukan string : ")
sst = input("masukan substring : ")
print(cekSubString(sst, st))