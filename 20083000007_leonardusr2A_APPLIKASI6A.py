# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:53:11 2021

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
    total = h*j
    print(total)
    jwb=input('mau beli lagi?')
    if jwb=='t'or jwb=='T':
        print(jwb)
        break