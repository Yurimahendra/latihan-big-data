# jarak dalam cm
jarak = 128783082
# hitung nilai a ( 1 km = 100.000 cm)
a = jarak // 100000
# hitung sisa hasil bagi jarak dengan 100000
b = jarak % 100000
# hitung nilai c ( 1 m = 100 cm)
c = b // 100
# hitung sisa hasil bagi b dengan 100
d = b % 100

print(jarak, 'cm =', a, 'km +', c,'m +', d, 'cm')