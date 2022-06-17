panjang = int(input('Masukkan panjang: '))
lebar = int(input('Masukkan lebar: '))

def luas(panjang, lebar):
    luas = panjang * lebar 
    return  luas
print('Luas tanah adalah: {} m^2'.format(luas(panjang, lebar)))
def keliling(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling
print('Keliling tanah adalah: {} m'.format(keliling(panjang, lebar)))
