#pengecekan karakter non huruf atau angka
#jika tidak ada karakter selain huruf atau angka maka True

import re

def cekString(s) :
    x = re.search("[^a-zA-Z0-9]", s)
    return not bool(x)

print(cekString('regexx'))