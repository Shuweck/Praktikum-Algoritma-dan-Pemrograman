print ('=== Menu Tuple ===')
print('1. Tampilkan kata dalam bentuk Tuple')
print('2. Jumlah huruf')
print('3. Membalik urutan')

kata = input('\nMasukkan kata: ')

while True:
    x = int(input('Masukkan opsi menu yang anda inginkan: '))
    if x == 1:
        print('Kata dalam bentuk Tuple:',tuple(kata))
    elif x == 2:
        print('Jumlah huruf: ',len (kata))
    elif x == 3:
        print('Membalik urutan kata: ',(kata)[::-1])
    else:
        print('Pilihan tidak ada')
        break