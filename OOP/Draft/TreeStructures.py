class TreeStructures:
    def __init__(self, value):
        self.value = value
        self.children = []

    def calculate(self):
        pass
    # pass'ı sil ve işlemi yap

        for child in self.children:
            child.calculate()


n0 = TreeStructures(60)

n1 = TreeStructures(15)
n2 = TreeStructures(4)

n3 = TreeStructures(5)
n4 = TreeStructures(3)

n0.children = [n1, n2]
n1.children = [n3, n4]

n0.calculate()
