indo = int(input('masukan nilai bahasa indonesia : '))
ipa = int(input('masukan nilai ipa : '))
mtk = int(input('masukan nilai matematika : '))

if indo >= 0 and indo <=100 and ipa >= 0 and ipa <= 100 and mtk >= 0 and mtk <=100:
    if indo >= 60 and ipa >= 60 and mtk > 70 :
        hasil = 'lulus'
    elif indo < 60 or ipa < 60 or mtk <= 70 :
        hasil = 'tidak lulus'

    print('status : ', hasil)

else:
    print('nilai tidak validd')

def sebab():
    if indo < 60 and ipa < 60 and mtk <=70:
       print('nilai ipa kurang dari 60')
       print('nilai bahasa indonesia kurang dari 60' )
       print('nilai matematika kurang dari atau sama dengan 70')
    elif indo < 60 and ipa < 60:
       print('nilai bahasa indonesia kurang dari 60')
       print('nilai ipa kurang dari 60')
    elif indo < 60 and mtk <= 70:
       print('nilai bahasa indonesia kurang dari 60')
       print('nilai matematika kurang dari atau sama dengan 70')
    elif ipa < 60 and mtk <= 70:
       print('nilai bahasa indonesia kurang dari 60')
       print('nilai matematika kurang dari atau sama dengan 70')
    elif mtk <= 70:
        print('nilai matematika kurang dari atau sama dengan 70')
    elif indo < 60 :
        print('nilai bahasa indonesia kurang dari 60')
    elif ipa < 60:
        print('nilai ipa kurang dari 60')

sebab()