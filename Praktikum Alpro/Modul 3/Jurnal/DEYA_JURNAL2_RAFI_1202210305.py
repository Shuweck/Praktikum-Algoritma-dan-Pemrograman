print('=== Program Perhitungan Data Infinity===')
print("Ketik 'stop' untuk menghentikan perulangan")


mlaku = True

height = []
while mlaku:
    tinggi =(input('masukkan tinggi: '))
    if tinggi == 'stop':
        mlaku = False
        avg = sum(height) / len(height)
        print(f'Tinggi rata-rata pasien adalah: {avg}')
    else:
        height.append(int(tinggi))
