from ast import Match, match_case


print ('\n=== Toko Komputer David ===\n')
merek_laptop = input('Masukkan merek laptop anda: (HP, Asus, Lenovo): ')

match merek_laptop:
    case 'HP':
        merek_hp = input('masukkan model yang diingingkan: ')
        harga=int(input('masukkan harga: '))
        print('\n==katalog pembelian Laptop HP==')
        print (f'\nModel: {merek_hp}')
        print (f'Harga: {harga}')
    

    case 'Asus':
        merek_asus = input('masukkan model yang diingingkan: ')
        harga = int(input('masukkan harga: '))
        print('\n==Katalog pembelian Laptop Asus==')
        print(f'\nModel: {merek_asus}')
        print(f'Harga: {harga}')
        
        
    case 'Lenovo':
        merek_lenovo = input('masukkan model yang diingingkan: ')
        harga = int(input('masukkan harga: '))
        print('\n==Katalog pembelian Laptop Lenovo==')
        print(f'\nModel: {merek_lenovo}')
        print(f'Harga: {harga}')

    case _ :
        print('tidak tersedia')


        
        



