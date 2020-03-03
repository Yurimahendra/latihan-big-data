# jumlah kamar tidur
n = 4
# ukuran sebuah kamar tidur (meter -> cm)
pKamar = 4 * 100
lKamar = 4 * 100
# ukuran sebuah keramik (cm)
pKeramik = 30
lKeramik = 40
# hitung luas total lantai kamar
luasTotalKamar = n * pKamar * lKamar
# hitung luas sebuah keramik
luasKeramik = pKeramik * lKeramik
# hitung jumlah keramik
jumKeramik = luasTotalKamar / luasKeramik
print('Jumlah keramik : ', jumKeramik)