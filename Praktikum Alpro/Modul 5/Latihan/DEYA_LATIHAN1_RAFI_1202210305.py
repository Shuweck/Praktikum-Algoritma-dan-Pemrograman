print('===>> Program Whishlist Anime ===<<')
print('1. Tambah Judul Anime')
print('2. Mengurutkan Daftar Anime')
print('3. Menampilkan Seluruh Judul Anime')
print('0. Exit')

Animex = []
AnimexSorted = []

while True:
    menu = int(input('Masukkan menu yang anda inginkan: '))
    if menu == 1:
        judul = input('Masukkan Judul Anime: ').title()
        print('Judul Anime yang anda masukkan adalah: ', judul)
        Animex.append(judul)
    elif menu == 2:
        print('Daftar Anime yang anda masukkan: ', Animex)
        print('Daftar Anime yang anda masukkan: ', sorted(Animex))

        i = 1
        for element in sorted(AnimexSorted):
            print(str(i) + '. ' + element)
            i = i + 1
        
    elif menu == 3:
        i = 1
        for element in (Animex):
            print(str(i) + '. ' + element)
            i = i + 1
    elif menu == 0:
        print('Terima Kasih')
        break
    
        