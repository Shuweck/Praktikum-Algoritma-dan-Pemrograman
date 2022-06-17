print("========== Daspro Market ==========")
belanja = True
keranjang = []

while(belanja):
    print("Ketik stop untuk berhenti")
    belanja = input("Masukkan nama barang kedalam keranjang:  ")
    keranjang.append(belanja)


    if belanja == "stop":
        belanja=False


        keranjang.remove("stop")
        print("barang yang berada didalam keranjang: ",keranjang)
    
