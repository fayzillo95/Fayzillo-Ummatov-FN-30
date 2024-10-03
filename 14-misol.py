# 14-misol.	
# Foydalanuvchi raqam kiritganda, 
# u ma'lum bir oralikda bo'lishi kerak. 
# Agar raqam ushbu oralikdan tashqarida bo'lsa, 
# raise yordamida Exception qo'zg'ating.

raqam = int(input("Raqamni kiriting : "))

if raqam > 0 and raqam < 1000:
    print("Hammasi joyida : ")
else:
    raise Exception("Xatolik raqam chegaradan oshdi : ") 