# Question 1: Tree Structures
import math
from tabnanny import check
dictionary= {
    0: "sıfır",
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "beş",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz"
}

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None

def control(self):
    if self.value % 2 == 0:
        print(self.value)
    else:
        print(math.sqrt(self.value))


def changetoparent(self):
    if self.parent is not None:
        if self.parent.name in dictionary:
            self.parent.name = dictionary[self.parent.name]

    if len(self.children) == 0:
        if self.name in dictionary:
            self.name = dictionary[self.name]

# Döndürmeyi unutma
    for child in self.children:
        changetoparent(child)


n0 = Node(0, 2)
n1 = Node(1, 51)
n2 = Node(2, 19)
n3 = Node(3, 47)
n4 = Node(4, 68)
n5 = Node(5, 14)
n6 = Node(6, 94)
n7 = Node(7, 21)
n8 = Node(8, 64)
n9 = Node(9, 23)


# Children
n0.children = [n1, n2]
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [n7, n8, n9]


# Parents
n1.parent = n0
n2.parent = n0

n3.parent = n1
n4.parent = n1

n5.parent = n2
n6.parent = n2

n7.parent = n3
n8.parent = n3
n9.parent = n3

# FONKSİYONU ÇALIŞTIRMAYI UNUTMA !!!!!!
changetoparent(n0)

print("--- DEĞİŞİKLİK SONRASI TEST ---")
print(f"Kök (0) yeni adı   : {n0.name} (Kendi çocukları olan 1 ve 2 tarafından değiştirildi)")
print(f"Ara (3) yeni adı   : {n3.name} (Kendi çocukları olan 7, 8 ve 9 tarafından değiştirildi)")
print(f"Yaprak (7) yeni adı: {n7.name} (Çocuğu olmadığı için KENDİSİNİ değiştirdi)")





