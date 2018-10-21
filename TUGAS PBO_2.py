class KBarang:
    def __init__(self,kode,deskripsi):
        self.kode = kode
        self.deskripsi = deskripsi
class Barang(KBarang):
    def __init__(self,kode,deskripsi,nama,harga,diskon):
        self.nama = nama
        self.harga = harga
        self.diskon = diskon
        KBarang.__init__(self,kode,deskripsi)
    def Tampil(self):
        raise NotImplementedError('subclasses must implement abstract method')
class Makanan(Barang):
    def __init__(self,kode,deskripsi,nama,harga,diskon,exdate,bulan,tahun):
        self.exdate = exdate
        self.bulan = bulan
        self.tahun = tahun
        self.harga = harga
        Barang. __init__(self,kode,deskripsi,nama,harga,diskon)
    def Tampil(self):
        print("KODE               : ",self.kode)
        print("DESKRIPSI          : ",self.deskripsi)
        print("NAMA               : ",self.nama)
        diskon1 = self.harga*self.diskon/100
        print("HARGA MAKANAN      : ",int(self.harga-diskon1))
        print("TANGGAL KADALUARSA : ",self.exdate,self.bulan,self.tahun)
class Pakaian(Barang):
    def __init__(self,kode,deskripsi,nama,harga,diskon,ukuran):
        self.ukuran = ukuran
        self.harga = harga
        Barang. __init__(self,kode,deskripsi,nama,harga,diskon)
    def Tampil(self):
        print("KODE               : ",self.kode)
        print("DESKRIPSI          : ",self.deskripsi)
        print("NAMA               : ",self.nama)
        diskon1 = self.harga*self.diskon/100
        print("HARGA PAKAIAN      : ",int(self.harga - diskon1))
        print("UKURAN PAKAIAN     : ",self.ukuran)

def menampilkan(nampil):
    nampil.Tampil()
Nama = input("Masukkan Nama Makanan : ")
Harga = int(input("Masukkan Harga Makanan : "))
Diskon = float(input("masukkan diskon : "))
Exdate = int(input("Masukkan Tanggal Kadaluarsa : "))
Bulan = input("Masukkan Bulan Kadaluarsa : ")
Tahun = int(input("Masukkan Tahun Kadaluarsa : "))
makanan = Makanan(2212,"MAKANAN TRENDING",Nama,Harga,Diskon,Exdate,Bulan,Tahun)
menampilkan(makanan)
Nama = input("Masukkan Nama Pakaian: ")
Harga = int(input("Masukkan Harga Pakaian : "))
Diskon = float(input("masukkan diskon : "))
Ukuran = input("Ukuran Pakaian : ")
pakaian = Pakaian(121998,"PAKAIAN",Nama,Harga,Diskon,Ukuran)
menampilkan(pakaian)
