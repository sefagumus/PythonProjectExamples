import math
import random


class Geometry:
    def Volume(self):
        pass


class Cube(Geometry):
    def __init__(self, a):
        self.a = a

    def Volume(self):
        return self.a**3

class RectangularPrism(Geometry):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def Volume(self):
        return  self.a * self.b * self.h

class Cylinder(Geometry):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def Volume(self):
        return  math.pi * self.r**2 * self.h

class Cone(Geometry):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def Volume(self):
        return  1/3 * math.pi * self.r**2 * self.h

class SquarePyramid(Geometry):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def Volume(self):
        return  1/3 * self.a**2 * self.h


class Sphere(Geometry):
    def __init__(self, r):
        self.r = r

    def Volume(self):
        return  4/3 * math.pi * self.r**3

#her bir class'tan nesne oluşturulup, random "random.randint(start, finish)" değer ataması yapılıyor
cube = Cube(random.randint(1, 10))
rectangularPrism = RectangularPrism(random.randint(1,10), random.randint(1,10), random.randint(1,10))
cylinder = Cylinder(random.randint(1,10), random.randint(1,10))
cone = Cone(random.randint(1,10), random.randint(1,10))
squarePyramid = SquarePyramid(random.randint(1,10), random.randint(1,10))
sphere = Sphere(random.randint(1,10))

# soruda liste içine al dediği için aldım
shape_list = [cube, rectangularPrism, cylinder, cone, squarePyramid, sphere]

# liste içindeki her bir elemanı ekrana yazdırdım.
for shape in shape_list:
    print(shape.Volume())
