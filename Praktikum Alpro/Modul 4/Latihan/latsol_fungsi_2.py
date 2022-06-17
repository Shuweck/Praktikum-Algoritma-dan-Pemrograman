print("========== Rekomendasi Tempat Wisata di Indonesia ==========")

class wisata:

    def __init__(self, nama,julukan,tempat):
        self.nama = nama
        self.julukan = julukan
        self.tempat = tempat

    
    def rekomendasi_wisata (self):
        print(f"Nama Daerah \t : {self.nama}")
        print(f"Julukan \t : {self.julukan}")
        print(f"Tempat Wisata \t : {self.tempat}")
        print("\n")

wisata1 = wisata("Makassar","Kota Daeng","Pantai Losari")
wisata2 = wisata("Bandung","Kota Kembang","Kawah Putih Ciwidey")
wisata3 = wisata("Bali","Pulau Dewata","Pantai Kuta")

wisata1.rekomendasi_wisata()
wisata2.rekomendasi_wisata()
wisata3.rekomendasi_wisata()