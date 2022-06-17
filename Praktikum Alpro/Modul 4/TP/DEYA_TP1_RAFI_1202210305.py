
# fungsi tambah ke keranjang
def tambahKeKeranjang(keranjang_lama, item_baru):
  keranjang_lama.append(item_baru)
  return keranjang_lama


print('===Daspro Market===')
cart = []
belanja = True

#masukloop
while belanja:
    print('Ketik stop untuk berhenti')
    belanja = input('Masukkan nama barang kedalam keranjang: ')
    
    if belanja == 'stop':
      break
        # belanja = False
        # cart.remove('stop')
        # print('Barang yang ada berada didalam keranjang: ', cart) #list barang dikeranjang
    else:
    	# panggil fungsi tambah ke keranjang
        cart = tambahKeKeranjang(cart, belanja)
        
print('Barang yang ada berada di dalam keranjang: ', cart)