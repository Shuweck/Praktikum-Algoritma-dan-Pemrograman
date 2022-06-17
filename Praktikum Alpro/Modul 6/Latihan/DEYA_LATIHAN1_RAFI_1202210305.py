
print('PROGRAM MENGHITUNG RATA-RATA')
grade = []
try:
    N = int(input('Masukkan jumlah data: '))
    i = 0
    while i < N:
        i += 1
        grade.append(int(input(f'Masukkan nilai ke-{i}: ')))
    print(f'Rata-rata nilai adalah {sum(grade) / len(grade)}')

except:
    print('Program hanya menerima inputan angka')
finally:
    print('Program selesai')
