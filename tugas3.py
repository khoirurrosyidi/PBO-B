class pegawai(object):
    name=""
    id=""
    def nama(self,name):
        self.name = name
    def id(self,ID):
        self.ID = ID
class toko(object):
    toko=""
    def toko(self,toko):
        self.toko = toko
class penempatan(pegawai,toko):
    pass
tempat=penempatan()
tempat.nama("imam")
tempat.toko("alfamart")
print("%s ditempatkan di %s "%(tempat.name,tempat.toko))
       
        
        
        
