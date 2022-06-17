from ast import match_case

print('''===Menu===
1. Pintu dan Jendela
2. CCTV
3. Alarm\n''')

Pilihan_anda= str(input('Masukkan Pilihan anda: '))
match Pilihan_anda:
    case '1':
       print('''\n 1.Kunci \n 2.Buka kunci \n''')
       pilih=input('Masukkan Pilihan anda: ')
       match pilih == 1:
           case '1':
            print('Pintu & jendela telah dikunci')
           case '2':
            print('Pintu & jendela telah terbuka')
           case _:
            print('Pilihan tidak tersedia')
    case '2':
        print('''\n 1.Nyalakan \n 2.Matikan \n''')
        pilih=int(input('Masukkan Pilihan anda: '))
        if pilih == 1:
            print('CCTV dinyalakan')
        elif pilih == 2:
            print('CCTV dimatikan')
        else:
            print('Pilihan tidak tersedia')
    case '3':
        print('''\n 1.Nyalakan \n 2.Matikan \n''')
        pilih=int(input('Masukkan pilihan anda: '))
        if pilih == 1: 
            print('Alarm dinyalakan ')
        elif pilih == 2:
            print('Alarm dimatikan')
        else:
            print('Pilihan tidak tersedia')

    

        

    
      
    
        
    
