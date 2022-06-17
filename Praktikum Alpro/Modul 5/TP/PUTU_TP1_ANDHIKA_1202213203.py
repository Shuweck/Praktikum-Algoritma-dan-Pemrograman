print("===>>> PROGRAM MANAJEMEN DATA PENDAPATAN PENJUALAN CILOK <<<===")
print("1. Tambah Data Pendapatan")
print("2. Mengurut Data (dari yang terbesar)")
print("3. Menghitung Total Data Pendapatan")
print("4. Menghapus Data Pendapatan")
print("5. Menampilkan Seluruh Data Pendapatan")
print("0. Exit")

pendapatan = []

def tambah_data(data_cilok):       
    pendapatan.append(data_cilok)    
    print(f"Data pendapatan penjualan cilok sebesar Rp.{data_cilok} berhasil ditambahkan.")

def urut_data():
    pendapatan.sort(reverse=True)
   
def hapus_data(hapus):
        try:   
            pendapatan.remove(hapus)
            print(f"Data pendapatan penjualan cilok sebesar Rp.{hapus} berhasil dihapus.")
        except:
            print("Nominal tersebut tidak tersedia, silahkan coba lagi.")


while True:
    menu = int(input("\nMasukkan menu yang Anda inginkan: "))

    if menu == 1:
        data_cilok = int(input("Masukkan data pendapatan penjualan cilok: "))
        tambah_data(data_cilok)
    elif menu == 2:
        urut_data
        print("Data penjualan cilok telah diurutkan.")
    elif menu == 3:           
        data_menu3=0   
        for menu3 in range (0,len(pendapatan)):
            data_menu3 = data_menu3 + pendapatan[menu3]
              
        print(f"Jumlah pendapatan penjualan cilok adalah Rp.{data_menu3}")
    elif menu == 4:
        hapus=int(input("Masukan nominal data yang akan dihapus: "))
        hapus_data(hapus)
    elif menu == 5: 
        print("Data penjualan cilok: ")
        for i in range (0,len(pendapatan)):
            print(f"{i+1}. Rp{pendapatan[i]}")
    elif menu == 0:
        print("Terima kasih telah menggunakan program kami:)")
        break
    else:
        print(f"Menu nomer {menu} tidak tersedia, silahkan coba menu yang lain")


exit()
