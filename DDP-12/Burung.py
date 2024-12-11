from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
       super().__init__(nama, makanan, hidup, berkembang_biak)
       self.jenis = jenis
       self.warna = warna

    def cetak_Burung(self): 
        super().cetak() 
        print("jenis \t\t: ", self.jenis,
              "\nwarna \t\t:", self.warna)
        
Gereja = Burung("Gereja", "biji jagung", "Udara", "Bertelur", "gereja", "coklat")
Gereja.cetak_Burung()

Beo = Burung("Beo", "biji jagung", "Udara", "Bertelur", "beo srilanka", "gradasi")
Beo.cetak_Burung()

Merpati = Burung("Merpati", "biji jagung", "Udara", "Bertelur", "merpati karolina", "abu-abu")
Merpati.cetak_Burung()