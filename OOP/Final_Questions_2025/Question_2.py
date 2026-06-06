import math

class Pizza:

    radius = 2 # class method buna "cls.radius" ile erişir.

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)

    @classmethod
    def area_cls(cls):
        return cls.radius ** 2 * math.pi

    # Static method fonksiyon sınıfın içindedir ama nesneyle ilgilenmez. Sadece matematik yapar.
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

# normal function
p = Pizza(4, ["mozzarella", "tomatoes"])
print(p.area())

# class method
c = Pizza.area_cls()
print(c)

# static method
s = Pizza.circle_area(4)
print(s)