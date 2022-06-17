print('>>Himpunan<<')

print('Set A berisikan angka: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}')
print('Set B berisikan angka: {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}')

a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print('1. Menggabungkan 2 set (union)')
print('2. Irisan 2 set (intersection)')
print('3. Selisih 2 set (difference)')
print('4. New Set (update)')

while True:
    x = int(input('Masukkan opsi menu yang anda mau: '))
    if x == 1:
        print('Hasil union: ', a.union(b))
    elif x ==2:
        print('Hasil intersection: ', a.intersection(b))
    elif x ==3:
        print('Hasil difference: ', a.difference(b))
    elif x ==4:
        print('Set A telah diupdate menjadi: ', a.update(b))
    else:
        print('Kamu hanya boleh pilih menu sampai 4!')
        break