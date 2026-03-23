class Node:
    def __init__(self, value): # GENEL MANTIK
        self.value = value
        self.next = None

head = Node(1)
second = Node(2)
head.next = second

print(head.value)
print(head.next)        # OUTPUT:   <__main__.Node object at 0x00000162DB8E5590>
print(head.next.value)  # OUTPUT:   2

print(f"--------------------------------------------------------")

# exp 2 - with "while"
class Node2:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node2(5)
b = Node2(10)
c = Node2(15)

a.next = b
b.next = c

"""
print(a.value)
print(b.value)
print(a.next.value) # output: b.value
print(b.next)
"""

# BÜTÜN DEĞERLERİ DÖNEREK ÇALIŞTIRMAK
current = a
while current is not None:
    print(current.value)
    current = current.next

print(f"--------------------------------------------------------")

# exp 3 - with while but "function (def)"
class NodeFunction:
    def __init__(self, value):
        self.value = value
        self.next = None

A = NodeFunction(1)
B = NodeFunction(2)
C = NodeFunction(3)

A.next = B
B.next = C

def print_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

print_list(A)

print(f"---------------------------------------------------------------")

# Question
class NodeQuiz():
    def __init__(self, value):
        self.value = value
        self.next = None

Q1 = NodeQuiz(1)
Q2 = NodeQuiz(2)
Q3 = NodeQuiz(3)
Q4 = NodeQuiz(4)

Q1.next = Q2
Q2.next = Q3
Q3.next = Q4

def print_qs(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

print_qs(Q1)






