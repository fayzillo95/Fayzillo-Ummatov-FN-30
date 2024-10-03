# 17-misol.py.	
# Foydalanuvchi sanani quyidagi formatda kiritadi: "2024-09-30 14:45:12". 
# Bu sanani shunday formatda chiqaring: "30/Sentyabr/2024, soat 02:45:12 PM"

from datetime import datetime as dt
   
sana_vaqt_obj = input("Sana va vaqtni kiriting : ")

sana_vaqt = dt.strptime(sana_vaqt_obj, "%Y %m %d %H %M %S")


oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
oy_index = oylar[sana_vaqt.month - 1]

sana_vaqt = sana_vaqt.strftime(f"%d/ {oy_index}/%Y soat %I:%M:%S %p")

print(sana_vaqt)