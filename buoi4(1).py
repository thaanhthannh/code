# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:16:40 2024

@author: TranThiThanhThanh-23715101
a = float(input("Nhap he so a:"))
b = float(input("Nhap he so b:"))
c = float(input("Nhap he so c:"))
if a + b > c and b + c > a and c + a > b: 
    print("a,b,c la 3 canh cua tam giac")
if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
    print("Tam giac vuong")
if a == b or a == c or b == c:
    print("Tam giac can")
if a == b and b == c and a == c:
    print("Tam giac deu")
else: print("Tam giac thuong")
"""
"""
S = float(input("Quang duong di duoc:"))
if S <= 1:
    print("Tien taxi: 20k")
elif 1<= S <= 4:
    print("Tien taxi:", (S*13), "k")
elif 4 <= S <= 8:
    print("Tien taxi:", 3*13+(S-3)*12, "k")
elif (3*13+5*12)+(S-8)*10 > 100:
    print("Tien taxi:", (3*13+5*12 + (S-8)*10*0.92), "k")
else:
    print("Tien taxi:", (3*13+5*12 + (S-8)*10), "k")
"""
from random import randint
print("Tro choi Keo - Bua - Bao")
Nguoi_choi = input()
May_tinh = randint(0,2)

print("Nguoi choi chon:", Nguoi_choi)
print("May tinh chon:", May_tinh)

if May_tinh == 0:
    May_tinh = "Bua"
if May_tinh == 1:
    May_tinh = "Keo"
if May_tinh == 2:
    May_tinh = "Bao"
    
if Nguoi_choi == "Bua":
    if May_tinh == "Bua":
        print("Hoa")
    elif May_tinh == "Keo":
        print("Thang")
    else:
        print("Thua")
        
elif Nguoi_choi == "Keo":
    if May_tinh == "Bua":
        print("Thua")
    elif May_tinh == "Keo":
        print("Hoa")
    else:
        print("Thang")

elif Nguoi_choi == "Bao":
    if May_tinh == "Bua":
        print("Thang")
    elif May_tinh == "Keo":
        print("Thua")
    else:
        print("Hoa")
else:
    print("Nhap sai, nhap lai:", Nguoi_choi)

      