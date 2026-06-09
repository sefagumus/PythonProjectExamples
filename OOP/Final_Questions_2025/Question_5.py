# Question 5: LinkedList - Özyineleme (Recursion) veya Zincirleme Metot Çağrıları

import math

class Node:

    def __init__(self, number):
        self.number = number
        self.ref = None

    def Calculate(self, param):

        # Soruda istenen:
        # Parametrenin logaritmasını al
        result = math.log(param)

        # b şıkkı:
        # Her düğüm kendi sonucunu ve kaçıncı düğüm olduğunu yazsın
        print("Node", self.number, "Result =", result)

        # a şıkkı:
        # Son düğüm ise sonucu ekrana yazdır
        if self.ref == None:
            print("Final Result =", result)
        # Son düğüm değilse sonucu sonraki düğüme gönder
        else:
            self.ref.Calculate(result)
 

n0 = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)

n0.ref = n1
n1.ref = n2
n2.ref = n3

# Zinciri ilk düğümden ve 20 parametresi ile başlatıyoruz
n0.Calculate(20)
