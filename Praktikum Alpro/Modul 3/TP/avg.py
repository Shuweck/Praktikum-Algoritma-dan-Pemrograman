from statistics import mean

n_murid = int(input('Masukkan jumlah muridnya: '))
n_nilai = []
for x in range (n_murid):
    n_nilai.append(int(input(f'Nilai murid ke {x} adalah: ')))

average_nilai = sum(n_nilai) / (n_murid)
print(f'Nilai rata-rata murid dihitung manual: {average_nilai}')

mean_nilai = mean(n_nilai)
print(f'Nilai rata-rata kelas dihitung dengan mean: {mean_nilai}')