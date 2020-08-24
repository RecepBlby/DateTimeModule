from datetime import datetime
import time
import os

suan = datetime.now()
print(suan)
print(suan.year)
print("--------------------------------------")

liste = str(suan.date()).split("-")
print("Yıl: {}, Ay: {}, Gün: {}".format(liste[0], liste[1], liste[2]))
print(datetime.ctime(suan))
print("--------------------------------------")

# print("SET AN ALARM")
# while True:
#     now = datetime.now()
#     second = now.second
#     minute = now.minute
#     hour = now.hour
#     if (second == 0 and minute == 6 and hour == 9):
#         print("WAKE UP! IT IS 09:06:00")
#         break
#     print(now)
#     time.sleep(1)

# Dosyanın oluşturulduğu tarihi ulaşmak için :
# stamp=os.stat("C:\Users\Recep\Desktop\HOME\PY_Projects\ms.txt").st_mtime
# tarih=datetime._fromtimestamp(stamp)
# print(tarih)

print("--------------------------------------")
tarih=datetime(2020,10,3,9,0,0)
print(tarih-suan)