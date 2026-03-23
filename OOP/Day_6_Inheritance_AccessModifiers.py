class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello", self.name)

class Student(Person):
     pass

# Method Override
class Teacher(Person):
    def greeting(self):
        # super().greeting() # OUTPUT: Hello MFH
        print("Teacher:", self.name)

P1 = Student("Sefa")
P1.greeting()

T1 = Teacher("MFH")
T1.greeting()

print(f"---------------------------------------------------------------------")

# exp 2 - "super()"
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print("BrandVehicle:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) # Burada aslında "self.brand = brand" yazıp "class Vehicle(): ..." silebilirim, ama büyük projelerde üst classtan ortak olanı almak için "super()" kullanmalıyım.
        self.model = model

    def info(self):
        print("BrandCar:", self.brand, "and", "Model:", self.model)

class Bus(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def info(self):
        print("BrandBus:", self.brand, "and", "Capacity:", self.capacity )

C1 = Car("BMW", "M5")
C1.info()

B1 = Bus("Mercedes", 83)
B1.info()

print(f"-----------------------------------------------------------------------------------")

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

b = B()  # output:  A "after" B

print(f"-----------------------------------------------------------------------------------")

# Access Modifiers - 3 Types in Pyhton
class Test:
    def __init__(self):
        self.a = 1      # public
        self._b = 2     # protected
        self.__c = 3    # private


t = Test()

print(t.a)   # works
print(t._b)  # works (but not recommended.)
# print(t.__c) # ❌ error --> as a "t._Test__c"