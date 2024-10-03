# 3.	Faylda nechta so'z borligini hisoblaydigan dastur yozing.

import os
import json

text_file_search = [str(i) for i in os.listdir() if i.endswith(".txt") ]

summa_text_file_dir = {}
dct = {}

for i in text_file_search:

    with open(i,"r") as file_text_the_reader:

        a = list(map(str,file_text_the_reader.read().split()))
        text_summa = 0
        for j in a:
            if len(j) > 1:
                text_summa += 1    
        
        summa_text_file_dir[i] = str(f" fileda {text_summa} ta so'z mavjud ")
        print(f"  {i}     fileda {text_summa} ta so'z mavjud ")

with open("3-misol-uchun.json","w") as files:
   
    files.write("{")
   
    files.write("\n   ")
   
    files.write("\"Ro'yhat \" : [\n    ")

    length = len(summa_text_file_dir)    

    for key,value in summa_text_file_dir.items():
       
        dct[key] = value 
       
        json.dump(dct,files)
       
        length-=1
       
        if length>0:
            files.write(",")
       
        files.write("\n    ")
       
        dct.clear()                
    
    files.write("  ]\n}")