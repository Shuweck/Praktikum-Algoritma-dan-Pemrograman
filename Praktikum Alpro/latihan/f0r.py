print('''===Mini Market Daspro===
1.Sayur
2.Buah
3.Daging
0.Cek keranjang
\n''')


#mulai loop
cart =[] #empty list, yang akan diisi barang yang dibeli
stop = True
while (stop):
    # if stop == 0:
    #     stop = False
    produk = int(input('Pilih produk anda (1-3): '))
    if (produk == 1):
        print('Anda memilih sayur')
        jumlah_item = int(input('Jumlah barang: '))
        for _ in range(jumlah_item):
            cart.append('sayur')
    elif (produk == 2):
        print('Anda memilih Buah')
        jumlah_item = int(input('Jumlah barang: '))
        for _ in range(jumlah_item):
            cart.append('buah')
    elif (produk == 3):
        print('Anda memilih daging')
        jumlah_item = int(input('Jumlah barang: '))
        for _ in range(jumlah_item):
            cart.append('daging')
    elif (produk == 0):
        stop = False
    else:
        print('Produk tidak tersedia')
        
#summary belanja
#isi dari cart, e.g.
#	cart = ["sayur", "sayur", "daging", "buah", "buah"] etc

print('\n---List Barang Belanja---')
total_sayur = cart.count('sayur')
total_buah = cart.count('buah')
total_daging = cart.count('daging')
print(f'Jumlah sayur: {total_sayur}')
print(f'Jumlah buah: {total_buah}')
print(f'Jumlah daging: {total_daging}')