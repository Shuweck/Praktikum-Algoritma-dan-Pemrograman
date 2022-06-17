print('===Daspro Market===')
cart = []
belanja = True

#masukloop
while belanja:
    print('Ketik stop untuk berhenti')
    belanja = input('Masukkan nama barang kedalam keranjang: ')
    cart.append(belanja)
    
    if belanja == 'stop':
        belanja = False

        cart.remove('stop')
        print('Barang yang ada berada didalam keranjang: ',cart) #list barang dikeranjang


