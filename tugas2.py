import fractions

class pecahan():
    def __init__(self,pembilang,penyebut):
       self.pembilang=pembilang
       self.penyebut=penyebut
    def tampilkan(self):
        pecahan=str(self.pembilang)+"/"+str(self.penyebut)
        f = fractions.Fraction (pecahan)
        print("%s = %s" %(pecahan, f))
x=int(input("masukkan penyebut:"))
y=int(input("masukkan pembilang:"))
i=pecahan(x,y)
i.tampilkan()
