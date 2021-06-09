# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:43:50 2021

@author: LeonardBagaskara
"""

jwb='y'
while jwb=='y' or jwb=='Y':
    print('MENGECEK GOLONGAN UMUR')
    print('__________________________')
    n = input('masukan umur')
    u = int(n)
    if u>60:
        status='LANSIA'
    elif u<=59 and u>35:
        status='DEWASA'
    elif u<=34 and u>18:
        status='PEMUDA'
    elif u<=17 and u>15:
        status='REMAJA'
    else:
        status='BOCIL FF'
    print (status)
    jwb = input('MAU MENGECEK LAGI?')
    if jwb=='t' or jwb=='T':
        print(jwb)
        break