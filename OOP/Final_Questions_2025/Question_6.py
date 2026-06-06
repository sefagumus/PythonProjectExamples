# Question 6: Hata bul.

class Animal:
    def __init__(self, name):
        self.name = name

    def Speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        # 1. HATA DÜZELTİLDİ: Üst sınıfın (Animal) kurucusuna ismi gönderiyoruz
        super().__init__(name) # Bu satır eksikti, eklendi.
        self.breed = breed

    def Speak(self):
        print(f"{self.name} barks.")


dog1 = Dog("Karabas", "kangal")

#2. HATA DÜZELTİLDİ: Metot ismini tanımlandığı gibi büyük 'S' ile çağırıyoruz
dog1.Speak()