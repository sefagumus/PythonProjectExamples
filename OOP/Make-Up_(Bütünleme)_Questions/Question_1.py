# Question 1: Tree Structures
import math
from tabnanny import check


class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

def control(x):
    if x.value % 2 == 0:
        print(x.value)
    else:
        print(math.sqrt(x.value))
# Döndürmeyi unutma
    for child in x.children:
        control(child)

n0 = Node("N0", 2)
n1 = Node("N1", 51)
n2 = Node("N2", 19)
n3 = Node("N3", 47)
n4 = Node("N4", 68)
n5 = Node("N5", 14)
n6 = Node("N6", 94)
n7 = Node("N7", 21)
n8 = Node("N8", 64)
n9 = Node("N9", 23)

n0.children = [n1, n2]
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [n7, n8, n9]

control(n0)





