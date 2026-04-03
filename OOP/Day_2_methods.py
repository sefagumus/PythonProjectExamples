"""
-- instance method → obje ile çalışır (self)
-- class method → class ile çalışır (cls)
-- static method → sadece fonksiyon, class ile bağı yok -- yardımcı fonksiyon

| Tür             | İlk Parametre | Neye Erişir           | Nereden Çağrılır |
| --------------- | ------------- | --------------------- | ---------------- |
| Instance Method | `self`        | instance + class      | object           |
| Class Method    | `cls`         | sadece class          | class            |
| Static Method   | yok           | hiçbirine bağlı değil | class            |

"""

class School:
    numbers_of_student = 0

    def __init__(self, name):
        self.name = name
        School.numbers_of_student += 1

    # instance method
    def info_student(self):
        print(self.name)

    # class method
    @classmethod
    def total_students(cls):
        print(cls.numbers_of_student)

    # static method
    @staticmethod
    def add(a, b):
        return a + b


s1 = School("Sefa")
s2 = School("Beyazit")

# instance
s1.info_student() # output: Sefa
# x = School.add(a=12,b=10)
# print(x)
# classmethod
School.total_students() # output: 2

# staticmethod
print(School.add(3,5))  # output: 8

"""
| Soru                     | Cevap        |
| ------------------------ | ------------ |
| Bu method objeye mi ait? | instance     |
| Tüm class’a mı ait?      | classmethod  |
| Hiçbirine ait değil mi?  | staticmethod |
"""

print("/////////////////////////////////////////////////////////////////////////////////////////////////")

class User:
    total_users = 0

    def __init__(self, username):
        self.username = username

        User.total_users += 1
        print(f"Added new user : {self.username}")

    def __del__(self):
       # User.total_users -= 1
        print(f"Deleted user: {self.username}")

    @classmethod
    def total(cls):
        print(f"{cls.total_users}")


user1 = User("karavanbeyi")
user2 = User("sefaguemus")

# 1. çağırma yöntemi
x = User.total
print(User.total_users)

# 2. çağırma yöntemi
User.total()

