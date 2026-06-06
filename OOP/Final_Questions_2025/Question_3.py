# Question 3: Inheritance (Kalıtım) + Polymorphism
"""
B ve C sınıfları A sınıfından türemiştir. Sınıflar Hesapla isimli fonk. sahiptir.
A sınıfı içerisinde gönderilen parametrenin sinüsü,
B sınıfı içerisinde gönderilen parametrenin cos'u,
C sınıfı içerisinde gönderilen parametrenin tan'ı alınmaktadır.
Her sınıftan 5'er adet nesne alınıp bir listeye eklenmektedir. Ardından her bir nesneye 1'den 360'a kadar sayılar 3'er artımlı olarak tüm nesnelere gönderilerek hesaplama yürütülmektedir. Hesaplanan değerler bir listeye eklenmektedir. Kodu yaz.
"""
import math

class A:
    def calculate(self, x):
        return math.sin(math.radians(x))


class B(A):
    def calculate(self, x):
        return math.cos(math.radians(x))

class C(A):
    def calculate(self, x):
        return math.tan(math.radians(x))


# her sınıftan 5 nesne oluştur.
List = []
for _ in range(5):
    List.append(A())
    List.append(B())
    List.append(C())

results = []

# 1'den 360'a kadar 3'er artışla tüm nesnelere gönder.
for obj in List:
    for x in range(1,360, 3):
        results.append(obj.calculate(x))

print(len(results))
print(len(List))

