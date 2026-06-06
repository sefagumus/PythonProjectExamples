class Harf:
    def __init__(self, val):
        self.val = val

    def Test(self):
        print("Test")

    def Copy(self):
        return Harf(self.val) # class Harf fonksiyonunu çapırıp kopyasını oluşturuyoruz.

original = Harf("A")
print(original.val)
print(original)

copy = original.Copy()
print(copy.val)
print(copy)


