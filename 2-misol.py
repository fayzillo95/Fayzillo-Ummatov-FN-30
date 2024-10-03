
# 2-misol.	
# Forydalanuvchidan ma’lumotlar qabul qiling va  
# ism bilan .txt file yarating va foydalanuvchidan qabul qilgan ma’lumotlarni saqlang.

import random as rd

def input_info_is_file():
    name = input("Ismingiz : ")
    last = input("Familiyangiz : ")
    
    a = rd.randint(1,1000)

    with open(f"{name}_{last}-{a}.txt","w+") as user_info_txt_file:

        info_to_file = input("Ma'lumotlaringiz : ")
        user_info_txt_file.write(info_to_file)
        print("M'alumotlar yozildi : ")

input_info_is_file()