class mahasiswa(object):
    name=""
    npm=""
    def nama(self,name):
        self.name = name
    def id(self,npm):
        self.npm = npm
class matakuliah(object):
    matkul=[]
    def matkul(self,matkul):
        self.matkul = matkul
class pengambilan(mahasiswa,matakuliah):
    def nilai(self,nilai):
        self.nilai = nilai
        
tempat=pengambilan()
mymatkul=[]
nama=input("nama:")
nilai=int(input("nilai ips:"))
if(nilai>=0):
    nilai=0
if(nilai>=20):
    nilai=1
if(nilai>=30):
    nilai=2
if(nilai>=60):
    nilai=3
if(nilai>=80 or nilai<=100):
    nilai=4
    
jumlahmatkul=int(input("jumlah matkul:"))
for i in range(0,jumlahmatkul):
    matkull=input("masukkan matkul:")
    mymatkul.append(matkull)
    i+1
tempat.matkul(mymatkul)
tempat.nama(nama)
tempat.nilai(nilai)
print("%s ditempatkan di %s nilai ips :%d"%(tempat.name,tempat.matkul,tempat.nilai))

        
        
        
