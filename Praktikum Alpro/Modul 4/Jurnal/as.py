class Studio:

    def __init__(self):
        self.band = input("Masukkan nama band anda: ")
        self.anggota = input("Tuliskan jumlah anggota anda: ")
        self.genre = input("Masukkan genre band anda: ")


    def print_hasil(self):
        print("\n====================")
        print("Nama band: ",self.band)
        print("Jumlah anggota: ",self.anggota)
        print("Genre: ",self.genre)
        if self.genre == "indie":
            print("\nCari studio lain bro")
        else:
            print("\nband lu asik bro")

s1 = Studio()
s1.print_hasil()