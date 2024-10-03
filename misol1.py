# 1-misol.	
# Fayl yaratish va unga yozish: 
# Yangi matn fayli yarating va unga o'zingiz tanlagan matnni yozing.

import random as rd

def input_info_is_file():
    name = input("Ismingiz : ")
    last = input("Familiyangiz : ")
    adrres = input("Manzilingiz : ")
    dict_all_info = {"Ism : ":name,
                     "Familiya : ":last,
                     "Manzil : ":adrres}
    a = rd.randint(1,1000)

    with open(f"{name}_{last}-{a}.txt","w+") as user_info_txt_file:
        for key,value in dict_all_info.items():
            info_stdin = "".join(key)
            info_stdin =  info_stdin+value
            user_info_txt_file.write(info_stdin)
            user_info_txt_file.write("\n")

input_info_is_file()