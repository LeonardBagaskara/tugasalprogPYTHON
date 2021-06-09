# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
jwb='y'
while jwb=='y' or jwb=='Y':
    
    print('cek kelulusan')
    print('__________________')
    n = input('masukan nilai')
    if int(n)>60:
        status = "LULUS"
    else:
        status='TIDAK LULUS'
    print (status)
    jwb = input('masukan nilai lagi')
    if jwb=='t' or jwb=='T':
        print(jwb)
        break
