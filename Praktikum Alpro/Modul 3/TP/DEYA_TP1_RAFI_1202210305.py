Jumlah_murid = int(input('Masukkan jumlah muridnya: '))
nilai = []
for y in range (1, Jumlah_murid+1):
    nilai.append(int(input(f'Nilai murid ke {y} adalah: ')))

rata_rata = sum(nilai) /Jumlah_murid
print(f'Nilai rata-rata murid yaitu {rata_rata}')