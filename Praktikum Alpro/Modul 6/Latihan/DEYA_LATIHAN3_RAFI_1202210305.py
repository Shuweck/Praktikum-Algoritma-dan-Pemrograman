nama = input('Masukkan Nama\t: ')
nim = input('Masukkan NIM\t: ')
kelas = input('Masukkan Kelas\t: ')
motto = input('Masukkan Motto\t: ')

d = open('C:\Workspace\Alpro\Praktikum Alpro\Modul 6\Latihan\\Tambahin.txt','a')
d.write(f'Nama\t: {nama}\n')
d.write(f'NIM\t\t: {nim}\n')
d.write(f'Kelas\t: {kelas}\n')
d.write(f'Motto\t: {motto}')
d.close()