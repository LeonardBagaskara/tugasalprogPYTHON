# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:17:22 2021

@author: Leonard
"""

jwb='y'
while jwb=='y'or jwb=='Y':
    print('MENGECEK STATUS BILANGAN BULAT DARI 0-100')
    print('_____________________________________________________')
    n = input('masukan bilangan')
    b = int(n)
    if b>=80 and b<=100:
        status='BAIK SEKALI'
    elif b>=65 and b<=79:
        status='BAIK'
    elif b>=55 and b<=65:
        status='CUKUP'
    elif b>=40 and b<=55:
        status='KURANG'
    elif b>=0 and b<=40:
        status= 'KURANG SEKALI'
    else:
        status='MOHON DIISI MENGGUNAKAN BILANGAN 0-100 SAJA'
    print (status)
    jwb = input('MAU MENGECEK LAGI?')
    if jwb=='t' or jwb=='T':
        print(jwb)
        break
