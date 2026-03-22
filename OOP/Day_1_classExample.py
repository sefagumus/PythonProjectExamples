class Student:
    def __init__(self, name, school, age, notes):
        self.name = name
        self.school = school
        self.age = age
        self.notes = notes


# Method
    def getInfo(self):
        print( f"{self.name} isimli öğrenci {self.age} yaşındadır, sınavdan {self.notes} puan almıştır ve {self.school} okulunda okuyordur.")


    def passed(self):
        return self.notes >= 50


first_student = Student(name= "Sefa", school= "Med Üni", age= 25, notes= 49 )  # not ":", you can use "="

print(first_student.getInfo())
print(first_student.passed())

