import random
pemain_1 = input('masukkan pilihan anda: ')
kemungkinan_suit = ['batu','gunting','kertas']
pemain_2 = random.choice(kemungkinan_suit)

print(f'\npemain 1 memilih {pemain_1}, pemain 2 memilih {pemain_2}.\n')

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
        print('pemain 2 memang')
elif pemain_1 == 'gunting':
    if pemain_2 == 'kertas':
        print('pemain 1 menang')
    else:
        print('pemain 2 menang')