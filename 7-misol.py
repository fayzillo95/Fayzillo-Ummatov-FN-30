# 7-misol.	
# Dastur orqali JSON formatdagi fayl yarating 
# va uni turli ma'lumotlar bilan to'ldiring 
# (masalan, foydalanuvchi haqida ma'lumotlar).


import os
import random as rd
import shutil
import json

if ("7-misol") not in os.listdir():
    os.mkdir("7-misol")

else:
    shutil.rmtree("7-misol")
    os.mkdir("7-misol")

print("Faylga yozilgan malumotlar \n________________________________________________________________________________\n")    

ls_txt_f = [i for i in os.listdir() if i.endswith(".txt")]

os.chdir("7-misol")

with open("7-misol-uchun.json","w") as json_file_adds_info:
    json_file_adds_info.write("{ \" Ma'lumotlar \" : [\n    ")    

    os.chdir("..")

for i in ls_txt_f:
    

    with open(i,"r") as reader:
        a = reader.read()
        print(i,"\n")
        print(a)
        print("____________________________________________________________________________________")
    os.chdir("7-misol")
   
    with open("7-misol-uchun.json","a") as json_file_adds_info:
        
        dct = {i:a}
        json.dump(dct,json_file_adds_info)
            
        if i!=ls_txt_f[-1]:
            json_file_adds_info.write(",\n   ")
        else:
            json_file_adds_info.write("\n   ")

    os.chdir("..")

os.chdir("7-misol")

with open("7-misol-uchun.json","a") as json_file_adds_info:
    json_file_adds_info.write("      ]\n} ")    

print("\n________________________________________________________________________________\n")    