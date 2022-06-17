login =("Sosmed Daspro: {'nama': 'Daspro Lab', 'password:' 'D45P120'}")
print(login)

print('\n === Menu ===')
print('1. Ganti Nama')
print('2. Ganti Password')
print('3. Tampilkan Hasil ')

while True:
    z = int(input('\nPilih Menu: '))
    if z == 1:
        Nama = (input('Masukkan nama Baru: '))
        login['nama'] = Nama
    elif z == 2:
        Password = input('Masukkan password Baru: ')
        login['password'] = Password
    elif z == 3:
        print(login)
    else: 
        print('Pilihan tidak ada')
        break
