# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:46:14 2021

@author: Leonard
"""

jwb='y'
while jwb=='y' or jwb=='Y':
    print('MENGHITUNG PEMBELIAN PRINTER')
    print('''______________________________
          HARGA Printer Epson T20 = 660.000
          __________________________________''')
    n = input('Jumlah yang dibeli')
    j =int(n)
    h =int(660000)
    d =(0.15)
    total = (h*j)
    totalD = (total-total*d)
    if total>=1500000:
        print(totalD)
    else:
        print(total)
        
    jwb=input('mau beli lagi?')
    if jwb=='t' or jwb=='T':
        print(jwb)
        break