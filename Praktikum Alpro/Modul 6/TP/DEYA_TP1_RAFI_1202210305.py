print('[]===== Kalkulator Pintar =====[]')

try:
    angka1 = int(input('Masukkan Angka Pertama: '))  
    angka2 = int(input('Masukkan Angka Kedua: '))
    print('Pilih Operasi Bilangan: ')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    pilihan = int(input('Masukkan Pilihan: '))

    if pilihan == 1:
        hasil = angka1 + angka2
        print(f'Hasil Penjumlahan {angka1} + {angka2} = {hasil}')
    elif pilihan == 2:
        hasil = angka1 - angka2
        print(f'Hasil Pengurangan {angka1} - {angka2} = {hasil}')
    elif pilihan == 3:
        hasil = angka1 * angka2
        print(f'Hasil Perkalian {angka1} * {angka2} = {hasil}')
    elif pilihan == 4:
        hasil = angka1 / angka2
        print(f'Hasil Pembagian {angka1} / {angka2} = {hasil}')
    else:
        print('Pilihan tidak ada!')
        print('Terimakasih sudah menggunakan kalkulator pintar!')

except ValueError:
    print('Program ini hanya menerima jenis nilai Integer!')
    print('Terimakasih sudah menggunakan kalkulator pintar!')
except ZeroDivisionError:
    print('Tidak Bisa Membagikan Nilai 0!')
    print('Terimakasih sudah menggunakan kalkulator pintar!')
except TypeError:
    print('Program ini hanya menerima jenis nilai Integer!')
    print('Terimakasih sudah menggunakan kalkulator pintar!')
except NameError:
    print('Program ini hanya menerima jenis nilai Integer!')
else: 
    print('Terimakasih sudah menggunakan kalkulator pintar!')

