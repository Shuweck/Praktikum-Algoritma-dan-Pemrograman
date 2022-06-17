print('\n=== Hasil Penjualan PT.Perindo ===\n')

semen=float(input('Masukkan hasil penjualan semen bulan ini\t:'))
batu_bata=float(input('Masukkan hasil penjualan batu bata bulan ini\t:'))
paku=float(input('Masukkan hasil penjualan paku bulan ini\t\t:'))

hasil=(semen+batu_bata+paku)/3

print('\nHasil rata-rata penjualan bulan ini adalah\t:{}'.format(hasil))