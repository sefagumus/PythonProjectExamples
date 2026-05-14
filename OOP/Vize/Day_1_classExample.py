class Arac:
    def _init_(self):
        self.ad=""
        self.maxHiz=0

    def YakitIkmali(self,y):
        return 0

class Araba(Arac):

    def _init_(self):
        super()._init_()
        self.yakit=10

    def YakitIkmali(self,y):
        self.yakit +=y
        return self.yakit

class Bisiklet(Arac):
    def _init_(self):
        super()._init_()

araba0=Araba()
araba0.ad="myHonda"
araba0.YakitIkmali(20)

bisiklet0=Bisiklet()
bisiklet0.ad="Salcano"