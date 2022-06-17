#Masukkan list bulan
Januari_Juni = ['Januari','Februari','Maret','April','Mei','Juni'] 
Juli_December = ['Juli','Agustus','September','October','november','Desember']

#mulai loop
Tanya_bulan = True

while (Tanya_bulan):
    nama_bulan = int(input('Masukkan nomor bulan (1-12)?:'))
    if nama_bulan >= 1 and nama_bulan <= 6:
        print('Bulannya sekarang adalah:', Januari_Juni[nama_bulan - 1])
    
    elif nama_bulan >= 7 and nama_bulan <= 12:
        print('Bulannya sekarang adalah:', Juli_December[nama_bulan -7])

    else:
        #Bila bulan yang dicantum tidak ada
        print('Bulan tersebut tidak ada')
        continue
    
    Tanya_bulan = input('Apakah anda ingin tanya lagi (yes/no):')
    if Tanya_bulan == 'no' or Tanya_bulan == 'No' or Tanya_bulan == 'nO' or Tanya_bulan == 'NO':
        Tanya_bulan = False

        
  



