jumblahtinggi = int(input('Masukkan Tinggi Baris : '))

n = 0
for i in range (1, jumblahtinggi+1) :
    spasi = ''
    for j in range(n) :
        spasi += ' '

    print(spasi,'*')
    n += 1