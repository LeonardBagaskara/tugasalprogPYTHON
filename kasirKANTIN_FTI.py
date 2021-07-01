# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:49:31 2021

@author: leonardBagaskara
"""

print('========================KANTIN FTI==========================')
print('============================================================')
print('============================================================')
print('-----------------------DAFTAR MENU--------------------------')


menu=['A. NASI GORENG                  15.000','B. LONTONG GORENG               14.900','C. BAKSO GORENG                 12.900','D. RUJAK GORENG                 13.000','E. RUJAK BAKSO                  15.000','F. RUJAK BAKSO PECEL            17.000','G. TEH DINGIN/HANGAT/PANAS       2.500','H. KOPI DINGIN                   5.000','I. KOPI TEH PANAS                6.500','J. COCA COLA DINGIN              3.500','K. COCA COLA PANAS               5.000']

i=0;
while i<len(menu):
    print(menu[i])
    i=i+1;
    
kodemenu=['A','B','C','D','E','F','G','H','I','J','K']
itemmenu=['NASI GORENG','LONTONG GORENG','BAKSO GORENG','RUJAK GORENG','RUJAK BAKSO','RUJAK BAKSO PECEL','TEH DINGIN/HANGAT/PANAS','KOPI DINGIN','KOPI TEH PANAS','COCA COLA DINGIN','COCA COLA PANAS']
hargamenu=[15000,14900,12900,13000,15000,17000,2500,5000,6500,3500,5000]

jwb='y'
while jwb=='y' or jwb=='Y':
    
    pilmenu=input('MASUKAN KODE MENU PESANAN ANDA = ')
    pilmenu=pilmenu.upper()
    qty_men=input('MAU PESAN BERAPA? = ')
    qtyme=int(qty_men)

    p=0;
    while p<len(kodemenu):
        if kodemenu[p]==pilmenu:
            n_item=itemmenu[p]
            h_menu=hargamenu[p]
        p+=1
    
    print('ANDA MEMESAN '+ n_item)
    print('HARGA SATUANYA '+ str(h_menu))

    totsem=qtyme*h_menu
    print ('TOTAL= '+str(totsem))
    jwb=input('MAU PESAN LAGI? ')    
    if jwb=='t' or jwb=='T':
        print ('TOTAL= '+str(totsem))
        print('---------------------------------------')
        jmlbay=input('UANG YANG DIBAYARKAN = ')
        pay1=int(jmlbay)
        kem=pay1-totsem
        print('KEMBALI = '+str(kem))
        print(jwb)
        break
    
    piltambahan=input('MASUKAN TAMBAHAN= ')
    piltambahan=piltambahan.upper()
    qty_tam=input('MAU BERAPA? ')
    qtytam=int(qty_tam)
    
    ta=0;
    while ta<len(kodemenu):
        if kodemenu[ta]==piltambahan:
            n_item
            h_menu
        ta+=1
    print('ITEM TAMBAHAN ANDA = '+ n_item)
    print('HARGA SATUAN ITEM TAMBAHAN '+ str(h_menu))
    totam=qtytam*h_menu
    fixtot=totsem+totam
    print('TOTAL BELANJA = '+str(fixtot))
    print('---------------------------------------')
    uangy=input('UANG YANG DIBAYARKAN = ')
    pay=int(uangy)
    kembalian=pay-fixtot
    print('KEMBALI = '+str(kembalian))
    break