# Constructor - Override - Linked List


# constructor
class Cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print("Constructor worked")

my_car = Cars(brand="BMW", model="M5", year=2020)
print(my_car.brand)
print(my_car.model)
print(my_car.year)


print("-------------------------------------------------")

# override
class Animal:
    def sound(self):
        print("This animal makes a generic sound")

class Dog(Animal): # Inheritance from Animal
    def sound(self):
        super().sound() # be careful, added later
        print("Dog barks")

d1 = Dog()
d1.sound()

# TODO -> Eğer "Dog(Animal)" class'ına "super().sound()" eklersem, her ikisi de çalışır, override etmeden ekleme yaparım.
# "OUTPUT:  This animal makes a generic sound
#           Dog barks

# TODO -> Eğer "Dog(Animal)" class'ına pass geçseydim, sadece Animal() "parent" içeriği çalışacaktı
# "OUTPUT: This animal makes a generic sound"

# TODO -> Eğer "Dog(Animal)" class'ına print verirsem, sadece "Dog(Animal)" çalışacak, içindeki metodu override ediyor.
# "OUTPUT: Dog barks"


print("-------------------------------------------------")
