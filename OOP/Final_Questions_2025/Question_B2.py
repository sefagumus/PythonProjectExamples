class Ayirici:
    def __init__(self, all):
        self.all = all

        self.tek_sayilar = []
        self.cift_sayilar = []
        self.asal_sayilar = []

    # Eylem bildirdiği için ismini güncelledik
    def tek_yada_cift_ayir(self, number):
        if number % 2 == 1:
            self.tek_sayilar.append(number)
        else:
           self.cift_sayilar.append(number)

    # Liste ile karışmaması için ismini 'asal_ayir' yaptık
    def asal_ayir(self, number):
        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False  # Tam bölündü, asal değil

        self.asal_sayilar.append(number)
        return True

    def islemi_baslat(self):
        for number in self.all:
            # Doğru metodun (makinenin) ismini çağırıyoruz
            self.tek_yada_cift_ayir(number)
            self.asal_ayir(number)

    def sonuclari_goster(self):
        print(f"Orijinal Dizi : {self.all}")
        print(f"Tek Sayılar   : {self.tek_sayilar}")
        print(f"Çift Sayılar  : {self.cift_sayilar}")
        print(f"Asal Sayılar  : {self.asal_sayilar}")


# KULLANIM KISMI (Senin yazdığın kısımla birebir aynı)
karisik_dizi = [1, 2, 3, 4, 5, 8, 9, 11, 15, 17, 20]
makine = Ayirici(karisik_dizi)
makine.islemi_baslat()
makine.sonuclari_goster()