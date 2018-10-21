class Makanan:
    def __init__(self,nama,harga,diskon,exdate):
        self.nama = nama
        self.harga = harga
        self.diskon = diskon
        self.exdate = exdate
    def Nama(self):
        print("NAMA MAKNAN          : ",self.nama)
    def Harga(self):
        print("HARGA MAKANAN        : ",self.harga)
    def Diskon(self):
        Diskon1 = self.harga*self.diskon/100
        Hasil = self.harga - Diskon1
        print("HASIL DISKON MAKANAN : ",int(Hasil))
    def Exdate(self):
        print("TANGGAL KADALUARSA   : ",self.exdate)
    def Tampil(self):
        print("===============MAKANAN===============")
        makanan.Nama()
        makanan.Harga()
        makanan.Diskon()
        makanan.Exdate()
        print("=====================================")
class Pakaian:
    def __init__(self,nama,harga,diskon,pakaian):
        self.nama = nama
        self.harga = harga
        self.diskon = diskon
        self.pakaian = pakaian
    def Nama(self):
        print("NAMA PAKAIAN         : ",self.nama)
    def Harga(self):
        print("HARGA PAKAIAN        : ",self.harga)
    def Diskon(self):
        Diskon1 = self.harga*self.diskon/100
        Hasil = self.harga - Diskon1
        print("HASIL DISKON PAKAIAN : ",int(Hasil))
    def Ukuran(self):
        print("UKURAN PAKAIAN       : ",self.pakaian)
    def Tampil(self):
        print("===============PAKAIAN===============")
        pakaian.Nama()
        pakaian.Harga()
        pakaian.Diskon()
        pakaian.Ukuran()
        print("=====================================")
makanan = Makanan("SARI ROTI",9000,5,22122018)
makanan.Tampil()
pakaian = Pakaian("BAJU KOKO",150000,10,"L")
pakaian.Tampil()
