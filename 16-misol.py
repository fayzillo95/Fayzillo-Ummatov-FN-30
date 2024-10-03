# 16-misol.	
# Foydalanuvchi kiritgan sonlar ro'yxatining o'sish tartibida ekanligini 
# assert bilan tekshiring. 
# Agar ketma-ketlik noto'g'ri bo'lsa, xato chiqaring.

ls = list(map(int,input("Sonlari kiriting : ").split()))

ls1 = [i for i in ls]

ls1.sort()

print(ls,ls1,sep="\n")

assert ls1==ls,("To'g'ri emas : ")

print("To'g'ri ")