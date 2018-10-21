class Pegawai:
    def __init__(self,name,gaji):
        self.name= name
        self.gaji= gaji

    def gaji(self):
        raise NotImplementedError("Subclass mustvImplement abstract class")
        
class Manajer(Pegawai):
    def __init__(self,tunjangan,name,gaji):
        self.tunjangan= tunjangan
        super().__init__(self,tunjungan,name,gaji)

class Programer(Pegawai):
    def __init__(self,bonus):
        self.bonus= bonus



    



        
