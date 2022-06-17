#peserta input sinyal tangan


peserta_1 = input('masukkan sinyal tangan: ')
peserta_2 = input('masukkan sinyal tangan: ')

b = 'batu'
g = 'gunting'
k = 'kertas'
#mulai nested if
if peserta_1 == 'batu':
    print('peserta 1: batu')
    if peserta_1 == 'gunting':
        print('peserta 1: gunting')
        if peserta_1 == 'kertas':
            print('peserta 1: kertas')

if peserta_2 == 'batu':
    print('peserta 2: batu')
    if peserta_2 == 'gunting':
        print('peserta 2: gunting')
        if peserta_2 == 'kertas':
            print('peserta 2: kertas')

    