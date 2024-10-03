# 15-misol.	
# Foydalanuvchi kiritgan sonlar ketma-ketligi Fibonacci ekanligini 
# assert orqali tekshiring. Agar ketma-ketlik Fibonacci bo'lmasa, xato chiqaring.

def funk(n):
    
    a = 0
    b = 1
    c = a+b

    if c>n:
        return False
    elif c == n:
        return True
    while c<n:

        a = b
        b = c
        c = a+b

        if c>n:
            return False
        elif c == n:
            return True

n = int(input ("Son kiriting : "))
a = funk(n)
assert a,("Fibonachi emas : ")
print(f"{n} fibonachi son ")