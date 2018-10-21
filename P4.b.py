class persegi:
    def __init__(self, jumlah_persegi = 4 , bentuk_persegi = "persegi"):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi

    def deskripsi(self):
        print("persegi bebas")

    def display(self):
        print(self.jumlah_persegi, self.bentuk_persegi)

class persegipanjang(persegi):
    def __init__(self, jumlah_persegi = 4 , bentuk_persegi = "persegi panjang"):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi
    def deskripsi(self):
        print("persegi panjang dan ada 2 pasang mempunyai panjang sisi yang sama.")
class bujursangkar(persegi):
    def __init__(self, jumlah_persegi = 4 , bentuk_persegi = "bujur sangkar"):
        self.jumlah_persegi = jumlah_persegi
        self.bentuk_persegi = bentuk_persegi
    def deskripsi(self):
        print("Keduanya sama panjang")

persegi1 = persegi("")
persegi2 = persegipanjang("")
persegi3 = bujursangkar("")

persegi1.deskripsi()
persegi2.deskripsi()
persegi3.deskripsi()

persegi1.display()
persegi2.display()
persegi3.display()
