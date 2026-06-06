a = [1, 2]
b = a
b.append(3)
print(a)  # a and b show the same thing.


# Reference with OOP
class A:
    def __init__(self, name):
        self.name = name

x = A("Sefa")
y = x
y.name = "Beyazit"
print(x.name)


# REFERENCE BREAKDOWN
a1 = [1, 2]
b1 = a1
print(b1)

b1 = [3, 4]
print(b1) # b1 is now a new object


# OOP + REFERENCE
# exp 1:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a3 = Node(1)
b3 = Node(2)

a3.next = b3
b3.next = a3  # ❌ INFINITE LOOP (SONSUZ DÖNGÜ),
print(a3.next.value)
print(b3.next.value)

# exp 2:
class A:
    def __init__(self, val):
        self.val = val
        self.next = None

a10 = A(1)
b10 = A(2)

a10.next = b10
b10.next = None

print(a10.next.val) # output = 2

# exp 3:
class A:
    def __init__(self, val):
        self.val = val
        self.next = None

def f(x):
    if x is None:  # zinciri baştan sona dolaşır her node'u yazdırır, en son None döner.
        return
    print(x.val)
    f(x.next)

a = A(1)
b = A(2)
c = A(3)

a.next = b
b.next = c

f(a)


