# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:30:08 2021

@author: leonardBagaskara
"""


print('-----------------------SLIP GAJI------------------------')
import datetime
x=datetime.datetime.now()
print('TANGGAL :             ' + str(x))

input('NAMA          :                   ')
gol=['1','2','3']
gaji=[2500000,4500000,6500000]
tis=[0.01,0.03,0.05]
tin=0.02

ingol=input('GOLONGAN      :                   ')
inkel=input('JENIS KELAMIN :                   ')
stat=input('STATUS KAWIN   :                    ')

k=0;
while k<len(gol):
    if gol[k]==ingol:
        gpok=gaji[k]
        ti=tis[k]
    k+=1;
print('GAJI POKOK         :              '+ str(gpok))

if inkel=='laki laki' or inkel=='LAKI LAKI':
   if stat=='kawin' or stat=='KAWIN':
    tistri=gpok*ti
    print('TUNJANGAN ISTRI    :             '+str(tistri))
else:
    tistri=0
    print('TUNJANGAN ISTRI          : 0')
pa=input('SUDAH PUNYA ANAK? (y/n) : ')
if pa=='Y' or pa=='y':
    tan=gpok*tin
    print('TUNJANGAN ANAK     : '+str(tan))
    gbrut=tistri+tan+gpok
    print('>>> GAJI BRUTO         :'+str(gbrut))
    print('--------------------------------------------------------')
    bj=0.005
    bJABa=gbrut*bj
    bJAB=(gbrut*bj)+gbrut
    iPEN=15500
    iORG=3500
    print('BIAYA JABATAN          : '+'Rp. '+str(bJABa))
    print('IURAN PENSIUN          : Rp. 15.500')
    print('IURAN ORGANISASI       : Rp. 3.500')

    gNET=bJAB-iPEN-iORG
    print('>>> GAJI NETTO         :'+'Rp.'+str(gNET))
elif pa=='N' or pa=='n':
    tan2=gpok*0
    print('TUNJANGAN ANAK     : '+ str(tan2))
    gbrut2=tistri+tan2+gpok
    print('>>> GAJI BRUTO         :'+str(gbrut2))
    print('--------------------------------------------------------')
    bj=0.005
    bJABb=gbrut2*bj
    bJAB2=(gbrut2*bj)+gbrut2
    iPEN=15500
    iORG=3500
    print('BIAYA JABATAN          : '+'Rp. '+str(bJABb))
    print('IURAN PENSIUN          : Rp. 15.500')
    print('IURAN ORGANISASI       : Rp. 3.500')

    gNET2=bJAB2-iPEN-iORG
    print('>>> GAJI NETTO         :'+'Rp.'+str(gNET2))