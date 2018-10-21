nama = str(input("Masukkan Nama Mahasiswa: "))
dosen = str(input("Masukkan Nama Dosen : "))
pegawai = str(input("Masukkan Nama Karyawan : "))
npm = str(input("Masukkan NPM Mahasiswa : "))
anpm = npm[0]+npm[1]
nip1 = str(input("Masukkan NIP Dosen : "))
nidn = str(input("Masukkan NIDN Dosen : "))
nip = str(input("Masukkan NIP Karyawan : "))
tahun = str(input("Masukkan Tahun Sekarang : "))
atahun = tahun[2]+tahun[3]
semes = str(input("semester ganjil/genap : "))
nama = Mahasiswa1(nama,dosen,pegawai,npm)
print("NAMA MAHASISWA : "+nama.Mahasiswa())
print("NPM            : "+nama.Npm())
print("SEMESTER       : ",nama.semester())
dosen = Dosen(nama,dosen,pegawai,nip1,nidn)
print("NAMA DOSEN     : "+dosen.namaDosen())
print("NIP            : "+dosen.Nip1())
print("NIDN           : "+dosen.Nidn())
pegawai = Pegawai(nama,dosen,pegawai,nip)
print("NAMA PEGAWAI   : "+pegawai.Pegawai())
print("NIP            : "+pegawai.Nip())
class Orang:
    def __init__(self,nama,dosen,pegawai):
        self.nama = nama
        self.dosen = dosen
        self.pegawai = pegawai
    def Mahasiswa(self):
        return self.nama
    def namaDosen (self):
        return self.dosen
    def Pegawai(self):
        return self.pegawai
class Mahasiswa1(Orang):
    def __init__(self,nama,dosen,pegawai,npm):
        self.npm = npm
        Orang. __init__(self,nama,dosen,pegawai)
    def Npm(self):
        return self.npm
    def semester(self):
        if semes == 'ganjil':
            sem = (int(atahun) - int(anpm))*2+1
            return sem
        else:
            sem = (int(atahun) - int(anpm))*2
            return sem
class Pegawai(Orang):
    def __init__(self,nama,dosen,pegawai,nip):
        self.nip = nip
        Orang. __init__(self,nama,dosen,pegawai)
    def Nip(self):
        return self.nip
class Dosen(Orang):
    def __init__(self,nama,dosen,pegawai,nip1,nidn):
        self.nip1 = nip1
        self.nidn = nidn
        Orang. __init__(self,nama,dosen,pegawai)
    def Nip1(self):
        return self.nip1
    def Nidn(self):
        return self.nidn
