# 6-misol.	
# Yangi fayl yarating va unga tasodifiy raqamlarni yozing. 
# Keyin, ushbu raqamlar orasidan faqat juft raqamlarni ajratib boshqa faylga yozing.

import os
import random as rd
import shutil

if ("6-misol") not in os.listdir():
    os.mkdir("6-misol")

else:
    shutil.rmtree("6-misol")
    os.mkdir("6-misol")

os.chdir("6-misol")

print("\n____________________________________________________________________________________")        

with open("6-misol-uchun-tasodifiy-raqamlar-toplami.txt","w") as rand_nums:
    a = []
    for i in range(21):
        a.append(rd.randint(1,100))
        print(a[i]," ",end="")
        rand_nums.write(str(f"{a[i]} "))

print("\n____________________________________________________________________________________")        

with open("6-misol-uchun-juft-raqamlar-toplami.txt","w") as even_nums:
    for i in a:    
        if i % 2 ==0:
            print(i," ",end="")
            even_nums.write(str(f"{i} "))

print("\n____________________________________________________________________________________")        
