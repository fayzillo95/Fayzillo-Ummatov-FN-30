# 8-misol.	
# JSON fayldagi ma'lum bir element qiymatini yangilang va faylga qayta yozing.

import os
import shutil
import json
import time

# Fayillar 8-misol papkasi yartilib
# Anashu 8-misol papkasiga joylanadi va
# Eski ma'lumotni siz kiritgan nom_1.json fayiliga
# Yangilangan ma'lumot yangi nom_2.json faylga yoziladi

if ("8-misol") not in os.listdir(): # papka mavjudligini tekshirish 
    time.sleep(3)
    os.mkdir("8-misol") # Agar mavjud bo'lmasa yangi ochish

else:
    # shutilni qayta run qilinganda hatolik bermasligi va fayllarni harsafar chavermasligi uchun qo'shdim
    # shutil.rmtree   remocve tree daraxt ko'rinishidagi papkalarni remove qilish yani hotiradan olib tashlash
    shutil.rmtree("8-misol")  # rmtre Ichma ich kirib papkani o'chirish yani papka pustoy bo'lmagan holatda 
    time.sleep(3) # jarayonni to'xtatish 
    os.mkdir("8-misol") # Yangi papka yaratish

# Eski ma'lumotlar uchun
dct = {"Mevalar":["Olma","Anor","Behi"],
       "Ismlar": ["Jonny","Anderson","Agata"],
       "Ranglar":["Qora","Oq","Qizil"]}

files_new = input("Fayl uchun nom bering : ")

os.chdir("8-misol") # Yangi papkaga kirish

# Eski ma'lumogtlarni faylga yozish
with open(f"{files_new}_1.json","w") as f:
    json.dump(dct,f,indent=4)


ls = [i for i in dct.values()] # Eski dct ning valuelarini olish

# Eski ma'lumotlarni olish
with open(f"{files_new}_1.json","r") as f1:
    file_reader = json.load(f1)

n = len(ls) 

for i,j in file_reader.items():
    n -=1
    file_reader[i] = ls[n] # dictaniry ga ma'lumotlarni o'zgartrib joylash

# yangilangan ma'lumotlarni yangi nom_2.json fayiliga yozish
with open(f"{files_new}_2.json","w") as f2:
    json.dump(file_reader,f2,indent=4) 

os.chdir("..")