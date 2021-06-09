# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:28:01 2021

@author: Leonard
"""

jwb='y'
while jwb=='y' or jwb=='Y':
    print('PENGGOLONGAN NILAI MAHASISWA')
    print('_______________________________________')
    n = input('masukan nilai mahasiswa 0-100')
    x = int(n)
    if x>=91 and x<=100:
        status='A'
    elif x>=81 and x<91:
        status='B'
    elif x>=71 and x<81:
        status='C'
    else:
        status='D'
    print (status)
    jwb = input('MAU MENGGOLONGKAN NILAI LAGI?')
    if jwb=='t' or jwb=='T':
        print(jwb)
        break