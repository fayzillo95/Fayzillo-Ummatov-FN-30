# 4-misol.	
# Fayldagi eng uzun va eng qisqa so'zlarni aniqlovchi dastur yarating.

import os

line_tskil = "\n____________________________________________________________________________________________\n"

ls_txt_file = [i for i in os.listdir() if i.endswith(".txt")]

for i in ls_txt_file:

    with open(i,"r") as f_reader:
        ls_txt_read_files = list(map(str,f_reader.read().split()))

        ls_txt_read_files = [ads for ads in ls_txt_read_files if len(ads)>1]
        
        ls_sum_txt = [len(a) for a in ls_txt_read_files]
        
        index_max = ls_sum_txt.index(max(ls_sum_txt))    
        index_min = ls_sum_txt.index(min(ls_sum_txt))

        # print(i)
        # print(index_max,index_min) 
        # print(ls_txt_read_files[index_max])   
        # print(ls_txt_read_files[index_min])   

    print(line_tskil)
    
    print(f"{i} fayilidaga \n eng uzun so'z : {ls_txt_read_files[index_max]}\
\n eng qisqa so'z : {ls_txt_read_files[index_min]}")

print(line_tskil)