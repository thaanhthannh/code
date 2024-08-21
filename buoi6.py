# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:13:16 2024

@author: TranThiThanhThanh-23715101
"""
"""
chuoi = "Dai hoc quoc gia, Khu pho 6, P.Linh Trung, Q.Thu duc, Tp.HCM"
#Tach chuoi
sub_string= [i.strip() for i in chuoi.split(",")]
for i in sub_string:
    print(i)
"""
"""
chuoi = "Dai hoc quoc gia, Khu pho 6, P.Linh Trung, Q.Thu duc, Tp.HCM"
sub_string_2=[a.strip() for a in chuoi.replace("P.", " ").replace("Q."," ").replace("Tp."," ").split(",")]
for a in sub_string_2:
    print(a)
"""
"""
chuoi="im a cat"
print("1.", chuoi.title())
print("2.", chuoi.upper())
chuoi_1 = chuoi.title()
print("3.", chuoi_1.swapcase())
print("4.", chuoi.capitalize())
"""
"""
#Viet chuong trinh xuat ra so ngau nhien trong mot doan bat ki cho truoc
import random
print(random.choice(range(100)))
"""

