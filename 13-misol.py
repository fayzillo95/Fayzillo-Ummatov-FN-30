# 13-misol.	
# Foydalanuvchi string kiritganda, 
# string ichida faqat harflar bo'lishini tekshiring. 
# Agar unda boshqa belgi bo'lsa, raise orqali xato qo'zg'ating.

in_text = input("String kiriting : ")

for i in in_text:
    if str.isalpha(i):
        print(i,end="")
    else:
        raise KeyError("Xatolik matndsa harfdan boshqa belgi qatnashgan")    