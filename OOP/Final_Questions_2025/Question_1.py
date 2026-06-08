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

    def __init__(self, value):
        self.value = value
        self.children = []

    def Calculate(self):

        if self.value % 2 == 0:
            print(self.value)
        else:
            print(math.sqrt(self.value))

        for child in self.children:
            child.Calculate()


#TODO -> her bir node'u oluşturduğumuz kısım.
n0 = Node(2)

n1 = Node(35)
n2 = Node(16)

n3 = Node(42)
n4 = Node(60)

n5 = Node(38)
n6 = Node(96)

n7 = Node(23)
n8 = Node(44)
n9 = Node(23)


#TODO -> ağaç yapısını oluşturduğumuz kısım.
n0.children = [n1, n2]
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [n7, n8, n9]


n0.Calculate()
