# 5-misol.
# 	Fayldagi barcha satrlarni teskari qilib, natijani boshqa faylga yozib qo'ying.

import os 
import random as rd
import shutil
import time

if "Task_5" in os.listdir():
    shutil.rmtree("Task_5")

time.sleep(3)

os.mkdir("Task_5")

ls_txt_file_the_dir = [i for i in os.listdir() if i.endswith(".txt")]


for i in range(len(ls_txt_file_the_dir)):
    

    with open(ls_txt_file_the_dir[i],"r") as f:
        text_reader = f.read()
    
    os.chdir("Task_5")

    a = rd.randint(1,1000)

    with open(f"Task_5_file_{a}.txt","w") as f:
        f.write(text_reader[::-1])
    os.chdir("..")
