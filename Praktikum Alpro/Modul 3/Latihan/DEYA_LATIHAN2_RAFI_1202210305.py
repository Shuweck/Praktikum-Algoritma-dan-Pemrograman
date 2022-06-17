print('=== Toko fashion melromarc ===\n')
print('''List produk:
1.kemeja >= Rp.50000
2.celana >= Rp.60000
3.sepatu >= Rp.30000\n''')

cart = []
buy = True
total = 0
while buy:
    produk = int(input('Masukkan kode barang yang akan dibeli (1/2/3/selesai): '))
    if produk == 1:
        item = int(input('Masukkan jumlah barang '))
        print('Kemeja ditambahakan')
        harga = 50000
        total = item *harga + total
        cart.append(f'{item} x Kemeja')

    elif produk ==2:
        item = int(input('Masukkan jumlah barang '))
        print('Celana ditambahkan')
        harga = 60000
        total = item *harga + total
        cart.append (f'{item} x celana')
    
    elif produk ==3:
        item = int(input('Masukkan jumlah barang '))
        print('Sepatu ditambahkan')
        harga = 30000
        total = item *harga + total
        cart.append (f'{item} x sepatu')
    
    else: 
        buy = False


    print('\n---list barang---')
    print(f'\nTotal harga: {total}')
    for element in cart:
        print(f'item: {element}')

        