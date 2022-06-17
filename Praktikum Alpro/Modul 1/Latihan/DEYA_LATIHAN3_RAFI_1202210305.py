#Membuat program yang dapat mengetahui siapa saja siswa yang mendapakatkan indeks A pada tahun ini
nama = input('masukkan nama anak didik:')
nilai_membaca= int(input('masukkan nilai membaca:'))
nilai_berhitung=int(input('masukkan nilai berhitung:'))

print('Nama anak didik:',nama)
print('nilai membaca:',nilai_membaca)
print('nilai berhitung',nilai_berhitung)




index = (nilai_membaca + nilai_berhitung)/2
if index >= 90 and index <=100:
    print('index nilai A: True')
else:
    print('indeks nilai A: false')