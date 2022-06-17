def volume_balok(panjang = 10, lebar = 5, tinggi = 4):
    volume = panjang*lebar*tinggi
    print("panjang: ", panjang)
    print("lebar: ",lebar)
    print("tingi: ",tinggi)
    print(f"Volume balok adalah {volume}")

print("contoh dengan default argument")
volume_balok()

print("\ncontoh dengan mengubah argument default")
volume_balok(5,8,10)