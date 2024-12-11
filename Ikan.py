from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
       super().__init__(nama, makanan, hidup, berkembang_biak)
       self.jenis = jenis
       self.warna = warna

    def cetak_ikan(self): 
        super().cetak() 
        print("jenis \t\t: ", self.jenis,
              "\nwarna\t\t:", self.warna)
        
Paus = Ikan("Paus", "daging", "laut", "beranak", "mamalia", "abu-abu")
Paus.cetak_ikan()

Lele = Ikan("Lele", "pelet", "air tawar", "bertelur", "lele vundu", "abu-abu")
Paus.cetak_ikan()


koi = Ikan("Koi", "pelet", "air tawar", "bertelur", "goromo", "gradasi")
koi.cetak_ikan()