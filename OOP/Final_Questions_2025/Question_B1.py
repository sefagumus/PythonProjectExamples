import random


class Node:
    def __init__(self, ID):
        self.ID = ID
        self.value = random.random()

        self.RightChildren = None
        self.LeftChildren = None

    def sum(self):
        result= 0

        if self.value > 0.5:
            result += self.value

        if self.LeftChildren is not None:
            result += self.LeftChildren.sum()

        if self.RightChildren is not None:
            result += self.RightChildren.sum()

        return result



n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n0.LeftChildren = n1
n0.RightChildren = n2

n1.RightChildren = n3
n1.LeftChildren = n4

n2.LeftChildren = n5
n2.RightChildren = n6

print(n0.sum())