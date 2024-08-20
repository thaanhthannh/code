# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:33:08 2024

@author: TranThiThanhThanh-23715101
"""
"""

#Bai7
print("============ MENU ============ ")
print("1. Hu tieu ")
print("2. Chao long ")
print("3. Banh canh ")
print("4. Bun rieu ")
print("5. Pho bo ")
choice=input("Moi nhap lua chon:")
if choice == "1":
    print("Hu tieu")
elif choice == "2":
    print("Chao long")
elif choice == "3":
    print("Banh canh")
elif choice == "4":
    print("Bun rieu")
elif choice == "5":
    print("Pho bo")
else: print("Khong xac dinh")
"""
"""
#Bai8
A = (32**0.2) - (1/64)**(-0.25) + (8/27)**(1/3)
B = round(A, 3)
print("Ket qua:", B)
"""
"""
#Bai9
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
import math
term1 = (math.sqrt(a) - math.sqrt(b)) / (math.sqrt(math.sqrt(a)) - math.sqrt(math.sqrt(b)))
term2 = (math.sqrt(a) + math.sqrt(math.sqrt(a*b)) / math.sqrt(math.sqrt(a)) + math.sqrt(math.sqrt(b)))
result = term1 - term2
print("Ket qua:", result)