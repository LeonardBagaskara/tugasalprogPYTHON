# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:05:49 2021

@author: leonardBagaskara
"""

print('==============================================================')
print('OLI MOTOR UD. MATAHARI')
print(' KODE>>> A. Duration SW20 1L     = 53.000')
print(' KODE>>> B. Castrol Magnatec 1L  = 50.000')
print(' KODE>>> C. Federal Supreme XX 1L= 54.000')
print(' KODE>>> D. Yamalube 1L          = 45.000')
print(' KODE>>> E. Shell 1L             = 46.000')
print('==============================================================')
print(' harga belum temasuk PPN 1%')
print('PROMO diskon 5% minimal pembelian 200rb sebelum ppn')
print('==============================================================')

disc=0.05
ppn=0.01
pilihan= input('Masukan kode Oli motor yang dibeli = ')
kode= ['A','B','C','D','E']
brand= ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme 1L','Yamalube 1L','Shell 1L']
harga= [53000,50000,54000,45000,46000]

if pilihan=='A' or pilihan=='a':
    idx=0
elif pilihan=='B' or pilihan =='b':
    idx=1
elif pilihan=='C' or pilihan =='c':
    idx=2
elif pilihan=='D' or pilihan =='d':
    idx=3
elif pilihan=='E' or pilihan =='e':
    idx=4
else:
    idx=0
    
print('>>> Pilihan Oli = '+ brand[idx])
print('>>> Harga Oli   = '+ 'Rp.' + str(harga[idx]))
print('>>> PPN         = 1%')

jumlah= input('Masukan jumlah oli yang akan dibeli = ')
n= int(jumlah)

print('>>> Jumlah Oli  = '+ jumlah)
totharga= n * (harga[idx])
pajak= totharga * ppn
harppn= totharga + pajak
potongan= totharga * disc

print('-------------------------------------------')

if totharga >= 200000:
    sts= totharga-potongan+pajak
    print('>>> Dapat Diskon 5%')
    print('>>> Total Harga = '+ 'Rp.' + str(sts))
else:
    print('>>> Total Harga = '+ 'Rp.' + str(harppn))
    