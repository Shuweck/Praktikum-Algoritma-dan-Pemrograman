
x = int(input('Masukkan Banyak Angka: '))
cart = []
for t in range (x):
    number = int(input(f'Masukkan Angka: '))
    angka = number in cart
    if angka == True:
        continue
    cart.append(number)
cart.sort()
print(cart)

