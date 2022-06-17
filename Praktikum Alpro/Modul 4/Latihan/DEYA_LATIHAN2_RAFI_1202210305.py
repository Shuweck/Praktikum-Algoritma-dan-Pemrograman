print("========== Rekomendasi Tempat Wisata di Indonesia ==========")

class Wisata: 
    #Constructor
    def __init__(self, nama, tempat, julukan):
        self.nama = nama
        self.tempat = tempat 
        self.julukan = julukan
    
    #methods for place info
    def rec(self):
        print('\n')
        print(f'Nama Daerah \t: {self.nama}')
        print(f'Tempat Wisata \t: {self.tempat}')
        print(f'Julukan \t: {self.julukan} ')
        
    
x1 = Wisata ('Medan','Danau Toba','Paris Van Sumatera') 
x2 = Wisata ('Malang','Museum Angkut','Kota Hujan')
x3 = Wisata ('Labuan Bajo','Pulau Komodo','Kota seribu sunset')

x1.rec()
x2.rec()
x3.rec()