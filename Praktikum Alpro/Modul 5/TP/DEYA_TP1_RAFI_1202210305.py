print('===>>> PROGRAM MANAJEMEN DATA PENDAPATAN PENJUALAN CILOK <<<===')
print('1. Tambah Data Pendapatan')
print('2. Mengurut Data (dari yang terbesar)')
print('3. Menghitung Total Data Pendapatan')
print('4. Menghapus Data Pendapatan')
print('5. Menampilkan Seluruh Data Pendapatan')
print('0. Exit')

cart = []

#append data yang diingingkan
def tambah_data(cilok):
    cart.append(cilok)
    print(f'Data pendapatan penjualan cilok sebesar: {cilok} berhasil ditambahkan')

#mengurutkan data
def sorting_data():
    cart.sort()(reverse=True)

#menghapus data yang diinginkan
def delete_data(delete):
    cart.remove(delete)
    print(f'Data penjualan cilok sebesar {delete} berhasil dihapus')

while True: 
    menu = int(input('Masukkan menu yang anda inginkan: '))
    
    if menu == 1:
        cilok = int(input('Masukkan data pendapatan penjualan cilok: '))
        tambah_data(cilok)
    elif menu == 2:
        sorting_data
        print('Data penjualan cilok telah diurutkan')
    elif menu == 3:
        menu_data3 = 0
        for menu_3 in range (0,len(cart)):
            menu_data3 = menu_data3 + cart [menu_3]
            pass
        print(f'Jumlah pendapatan cilok adalah {menu_data3}')
    elif menu == 4:
        delete = int(input('Masukkan nominal data yang akan dihapus: '))
        delete_data(delete)
    elif menu == 5:
        print('Data penjualan cilok: ')
        for x in range (0,len(cart)):
            print(f'{x+1} {cart[x]}')
    elif menu == 0:
        print('Terimakasih sudah menggunakan program kami :D')
        break
    else:
        print(f'Menu nomer {menu} tidak tersedia, silahkan coba kembali :)')

exit()

         
        




