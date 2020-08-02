# mendapatkan nomer hp dalam string

import re
s = "nomor HP saya +62857-1619-1979 dan +62811-1922-882"
nhp = re.findall("[+]628[0-9]{2}[-][0-9]{4}[-][0-9]{3,4}", s)
print(nhp)