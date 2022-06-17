print("Welcome to the Miss Skin Glow")
print("-----------------------------")
print("")
print("List product: ")
print("(1) Whitening")
print("(2) Ultimate")
print("(3) Acne")
print("")

# mulai loop disini
belum_puas = True
total = 0
total_diskon = 0
keranjang = []  # empty list, nanti diisi nama barang yg dibeli
while (belum_puas):
    produk_id = int(input("Pilih produk anda (1-3): "))

    if (produk_id == 1):
        # hitung whitening
        print("Anda memilih Whitening series")
        jumlah_item = int(input("jumlah barang: "))
        harga = 670000
        diskon = 0.5
        potongan = diskon * harga
        total_diskon = total_diskon + jumlah_item * potongan
        total = total + jumlah_item * (harga - potongan)
        keranjang.append(f" {jumlah_item} x Whitening Series")

    elif (produk_id == 2):
        # hitung ultimate
        print("Anda memilih Ultimate series")
        jumlah_item = int(input("jumlah barang: "))
        harga = 880000
        diskon = 0.3
        potongan = diskon * harga
        total_diskon = total_diskon + jumlah_item * potongan
        total = total + jumlah_item * (harga - potongan)
        keranjang.append(f" {jumlah_item} x Ultimate Series")

    elif (produk_id == 3):
        # hitung acne
        print("Anda memilih Acne series")
        jumlah_item = int(input("jumlah barang: "))
        harga = 450000
        diskon = 0.0
        potongan = diskon * harga
        total_diskon = total_diskon + jumlah_item * potongan
        total = total + jumlah_item * (harga - potongan)
        keranjang.append(f" {jumlah_item} x Acne Series")

    else:
        # feedback ke user kalau angka tidak benar
        print("produk id tidak tercatat di database")
        continue # skip the rest of the loop, and continue from the beginning of the loop

    puaskah = input("Apakah anda sudah puas (Y/N): ")
    if puaskah == "Y" or puaskah == "y" or puaskah == "yes" or puaskah == "Yes" or puaskah == "YES":
        belum_puas = False

        # tulis summary pembelian
        print(f"\nTotal harga yang anda harus bayar: {total}")
        print(f"Total diskon untuk anda {total_diskon}")
        print("\n---list barang---")
        for element in keranjang:
            print(f"item: {element}")