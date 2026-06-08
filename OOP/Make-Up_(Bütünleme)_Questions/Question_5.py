class Sınav:
    def __init__(self, isim, direksiyon, yazılı):
        self.isim = isim
        self.direksiyon = direksiyon
        self.yazılı = yazılı

    def Hesaplama(self):

        ortalama = (self.yazılı + self.direksiyon) / 2

        if ortalama >= 50:
            sonuc = "başarılı"
        else:
            sonuc = "basarısız"


        print(f"Aday: {self.isim}  Sonuç: {sonuc}")



sinav_listesi = [
    Sınav("Ahmet", 50, 25),
    Sınav("Mehmet", 58, 23),
    Sınav("Caner", 55, 78),
    Sınav("Kemal", 43, 59)
]

for aday in sinav_listesi:
    aday.Hesaplama()