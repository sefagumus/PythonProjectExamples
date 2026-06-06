# Question 1: Tree Data Structures
import math


#                      n0(2)
#               /                    \
#            n1(35)                n2(16)
#            /        \            /    \
#         n3(42)     n4(60)    n5(38)  n6(96)
#       /    |    \
#  n7(23) n8(44) n9(23)

# Eğer değer çift ise doğrudan değeri eklemekte. Tek ise karekökünü eklemekte.
# Ağaç yapısını tanımlayarak işletimini yapan kodu yaz.



class Node:

    def __init__(self, name, value):
        self.name = name        # isteğe bağlı isim vermek istersen.
        self.value = value      # değer tutuyor
        self.children = []      # alt düğümleri tutuyor.


#TODO -> tek mi ? çift mi? class Node'dan bağımsız fonksiyon.
def control(node):
    if node.value % 2 == 0:   #  ".value % 2 == 0" -> 2'ye tam bölünür.
        print(node.value)
    else:
        print(math.sqrt(node.value)) # "math.sqrt(.value)" -> karekökünü alır.
# Döndürmeyi unutma
    for child in node.children:
        control(child)


#TODO -> her bir node'u oluşturduğumuz kısım.
n0 = Node("N0",2)

n1 = Node("N1",35)
n2 = Node("N2",16)

n3 = Node("N3",42)
n4 = Node("N4",60)

n5 = Node("N5",38)
n6 = Node("N6",96)

n7 = Node("N7",23)
n8 = Node("N8",44)
n9 = Node("N9",23)


#TODO -> ağaç yapısını oluşturduğumuz kısım.
n0.children = [n1, n2]
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [n7, n8, n9]


control(n0)

