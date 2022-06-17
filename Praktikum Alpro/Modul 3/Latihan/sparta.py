print('=== Toko fashion melromarc ===\n')
print('''List produk:
1.kemeja
2.celana
3.sepatu\n''')

#mulai loop
cart= [] #emptylist
berhenti = True
total = 0
while berhenti:
    item =int(input('Pilih barang anda (1-3):'))
    if item == 1:
        print('Anda memilih kemeja')
        jumlah_item = int(input('jumlah barang: '))
        harga = 50000
        cart.append(f'{jumlah_item * harga} x Kemeja')
    elif item == 2:
        print('anda memilih celana')
        jumlah_item = int(input('jumlah barang:'))
        harga = 60000
        total = (total + jumlah_item) * harga
        cart.append(f'{jumlah_item} x Celana')
    elif item == 3:
        print('anda memilih Sepatu')
        jumlah_item = int(input('jumlah barang:'))
        harga = 30000
        total = (total + jumlah_item) * harga
        cart.append(f'{jumlah_item} x Sepatu')
    else:
        print('Produk tidak tersedia')
        berhenti = False
    
    #summary
    print(f'\nTotal harga: {total}')
    print('\n---list barang---')
    for element in cart:
        print(f'item: {element}')
    
