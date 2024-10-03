# 12-misol.	
# Lug'atdan (dictionary) berilgan kalit bo'yicha qiymat oling, 
# agar kalit mavjud bo'lmasa, 
# try va except orqali xatoni ushlang va foydalanuvchiga tegishli xabar bering.

dct = {"Mevalar":["Olma","Anor","Behi"],
       "Ismlar": ["Jonny","Anderson","Agata"],
       "Ranglar":["Qora","Oq","Qizil"]}

kalit = input("Kalitni kiriting : ")

try:
    print(dct[kalit])
except Exception as xatolik:
    print("Xatolik yuz berdi : ")
    print(xatolik.__class__.__name__)