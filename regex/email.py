# validasi email

import  re

email = input("Masukan email address : ")
hasil = re.findall("^[a-zA-Z][\w.\-]+@[\w\-]+[.][a-zA-Z]{2,3}", email)

if (hasil) :
    print("email valid")
else:
    print("email tidak valid")