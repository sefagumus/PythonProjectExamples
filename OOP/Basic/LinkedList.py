class LinkedList:
    def __init__(self, number):
        self.number = number # kendi verisi
        self.ref = None # sonraki düğüm

    def Calculate(self, param):
        pass


n0 = LinkedList(1)
n1 = LinkedList(2)
n2 = LinkedList(3)
n3 = LinkedList(4)

n0.ref = n1
n1.ref = n2
n2.ref = n3

# n0.Calculate(20)



