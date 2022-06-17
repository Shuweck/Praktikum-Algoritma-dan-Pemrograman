from ast import Match, match_case


print ('\n=== Toko Komputer David ===\n')
merek_laptop = input('Masukkan merek laptop anda: (HP, Asus, Lenovo): ')

match merek_laptop:
    case 'HP':
        print('\n==katalog pembelian Laptop HP==')
        print('Model: HP spectre ')
        print('Harga: 20.000.000')
        print('\n')
        print('Model: HP Omen 15')
        print('Harga: 24.000.000 ')
    
    case 'Asus':
        print('\n==katalog pembelian Laptop Asus==')
        print('Model: Asus ROG Zepyhrus')
        print('Harga: 35.000.000 ')
        print('\n')
        print('Model: Asus TUF')
        print('Harga: 12.000.000')
        
    case 'Lenovo':
        print('\n==katalog pembelian Laptop Lenovo==')
        print('Model: Lenovo Ideapad')
        print('Harga: 6.000.000 ')
        print('\n')
        print('Model: Lenovo ThinkPad')
        print('Harga: 10.000.000 ')
        
    case _ :
        print('tidak tersedia')


        
        



