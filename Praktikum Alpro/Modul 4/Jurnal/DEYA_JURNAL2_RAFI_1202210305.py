class Studio: 
    
    def __init__(self,):
        self.band = input('Masukkan nama band lu\t: ')
        self.anggota = input('Berapa anggota band lu  : ')
        self.genre = input('Genre band lu apa\t: ')
    
    def print_info(self):
        print('\n')
        print('Nama band      : ',self.band)
        print('Jumlah anggota : ',self.anggota)
        print('Genre          : ',self.genre)

        if self.genre == 'Indie':
            print('\n')
            print('Cari Studio lain bro')
        else:
            print('band lu asik bro')
        
x1 = Studio()
x1.print_info()





        