a = int(input('Masukkan angka: '))
paw = [3, 6, 9, 12, 15]
pow = [5, 10, 15]

tanya_angka = True

while tanya_angka:
    a = int(input('Masukkan angka: '))
    print(a)
    if a == paw:
        print(a,'paw')
    elif a== pow:
        print(a,'pow')
    
    if a == 16:
        tanya_angka = False



    
   