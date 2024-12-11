from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
       super().__init__(nama, makanan, hidup, berkembang_biak)
       self.design = design
       self.racun = racun

    def cetak_ular(self): 
        super().cetak() 
        print("Design \t\t: ", self.design,
              "\nRacun \t\t:", self.racun)
        
anaconda = Ular("Anaconda", "kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

cobra = Ular("cobra", "daging", "hutan", "bertelur", "bersisik", "berbisa")
cobra.cetak_ular()

sanca = Ular("sanca", "tikus", "semak-semak", "bertelur", "bersisik", "tidak berbisa")
sanca.cetak_ular()