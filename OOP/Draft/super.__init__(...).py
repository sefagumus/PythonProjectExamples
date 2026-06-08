# super().__init__() komutuna normal, tek başına duran bir sınıfta asla ihtiyacın yoktur.
# Bu komut sadece "bir sınıf, başka bir sınıftan miras aldığında" sahneye çıkar.

class A:
    def __init__(self, name):
        self.name = name

    def example(self):
        print(f"{self.name} is young boy")


class B(A):
    def __init__(self,name, age):
        super().__init__(name)
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} years old")





p1 = A("Ali")
p1.example()


p2 = B("Berat", 10)
p2.info()
p2.example()

