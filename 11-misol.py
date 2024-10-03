# 11-misol.	
# Foydalanuvchi ko'rsatilgan faylni o'qishga harakat qiladigan dastur tuzing. 
# Agar fayl topilmasa, foydalanuvchiga "Fayl topilmadi" degan xabar chiqsin.(try, except)

import os


# fayl_nomi = "Fayzillo_Ummatov-297.txt"

fayl_nomi = input("Fayl nomini kiriting : ")

try:
    with open(fayl_nomi,"r") as f:
        matn = f.read()
        print(matn)
except:
    print("Xato fayl topilmadi")