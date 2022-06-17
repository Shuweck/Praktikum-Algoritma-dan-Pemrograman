#masukkan input
pemain_1 = input('Pemain 1 masukkan pilihan anda: ')
pemain_2 = input('Pemain 2 masukkan pilihan anda: ')
#list suit
kemungkinan_suit = ['batu','gunting','kertas']

print(f'\npemain 1 memilih {pemain_1}, pemain 2 memilih {pemain_2}')

#mulai nested if
if pemain_1 == pemain_2:
    print(f'{pemain_1} kedua pemain seri')
elif pemain_1 == 'batu':
    if pemain_2 == 'gunting':
        print('pemain 1 menang')
    else:
        print('pemain 2 menang')
elif pemain_1 == 'kertas':
    if pemain_2 == 'batu':
        print('pemain 1 menang')
    else:
        print('pemain 2 menang')
elif pemain_1 == 'gunting':
    if pemain_2 == 'kertas':
        print('pemain 1 menang')
    else:
        print('pemain 2 menang')
