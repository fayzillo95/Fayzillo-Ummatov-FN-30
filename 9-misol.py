# 9-misol.	
# JSON fayl ichidagi massivda mavjud ma'lumotlarni 
# berilgan mezon bo'yicha filtrlab ekranga chiqaring 
# (masalan, yosh > 30 bo'lgan foydalanuvchilar).

import os
import random as rd
import shutil
import json

if ("9-misol") not in os.listdir():
    os.mkdir("9-misol")

else:
    shutil.rmtree("9-misol")
    os.mkdir("9-misol")

# Bu dictni gptdan o'ldim vaqdan yutish uchun
# qolgan ko'dlar o'zimniki
users_dict = {
    "user1": {"name": "Ali", "age": 25, "email": "ali@example.com"},
    "user2": {"name": "Vali", "age": 30, "email": "vali@example.com"},
    "user3": {"name": "Salim", "age": 22, "email": "salim@example.com"},
    "user4": {"name": "Zarina", "age": 28, "email": "zarina@example.com"},
    "user5": {"name": "Dilshod", "age": 35, "email": "dilshod@example.com"},
    "user6": {"name": "Nodir", "age": 27, "email": "nodir@example.com"},
    "user7": {"name": "Malika", "age": 23, "email": "malika@example.com"},
    "user8": {"name": "Gulnoza", "age": 31, "email": "gulnoza@example.com"},
    "user9": {"name": "Farrux", "age": 29, "email": "farrux@example.com"},
    "user10": {"name": "Jamshid", "age": 24, "email": "jamshid@example.com"},
    "user11": {"name": "Shahnoza", "age": 26, "email": "shahnoza@example.com"},
    "user12": {"name": "Akbar", "age": 32, "email": "akbar@example.com"},
    "user13": {"name": "Madina", "age": 21, "email": "madina@example.com"},
    "user14": {"name": "Oybek", "age": 34, "email": "oybek@example.com"},
    "user15": {"name": "Shirin", "age": 25, "email": "shirin@example.com"},
    "user16": {"name": "Hasan", "age": 30, "email": "hasan@example.com"},
    "user17": {"name": "Nigora", "age": 28, "email": "nigora@example.com"},
    "user18": {"name": "Ravshan", "age": 33, "email": "ravshan@example.com"},
    "user19": {"name": "Maqsud", "age": 27, "email": "maqsud@example.com"},
    "user20": {"name": "Doston", "age": 22, "email": "doston@example.com"}
}

chegara = int(input("Yosh chegarasini tanlang : "))

os.chdir("9-misol")

with open("users_info.json","w") as f:
    json.dump(users_dict,f,indent=4) # indentni internetdan o'rgandim  dictni faylga formatlab yozish uchun ishlatiar ekan

ls_age_30 = []

with open("users_info.json","r") as f_r:
    dict_reader = json.load(f_r)
    ls_age_30 = {ism: yosh for ism,yosh in dict_reader.items() if yosh['age'] > (chegara-1)}

for key, value in ls_age_30.items():
    print(key,value)

