# 110-misol.	
# JSON fayldagi raqamli ma'lumotlardan eng katta va eng kichik qiymatni toping 
# (masalan, foydalanuvchilar yoshi orasidan).


import os
import random as rd
import shutil
import json

if ("10-misol") not in os.listdir():
    os.mkdir("10-misol")

else:
    shutil.rmtree("10-misol")
    os.mkdir("10-misol")


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

os.chdir("10-misol")

with open("Task_10.json","w") as f:
    json.dump(users_dict,f,indent=4)    

with open("Task_10.json","r") as f_r:
    dct_reader = json.load(f_r)    

ls_age_int = []

for key,value in dct_reader.items():
    dct_values = dict(value)
    for keyj,valuej in dct_values.items():
        if type(valuej) == int:
            ls_age_int.append(valuej)
            
print(f"Yoshlar \n {ls_age_int}")                
print(f"Eng kattasi = : {max(ls_age_int)}\nEng kichigi = : {min(ls_age_int)}")        