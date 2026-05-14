# Bubble Sort - Selection Sort - Insertion Sort

# TODO Bubble Sort = En baştakini alıyor, sağ taraf ile kıyaslaya kıyaslaya listenin "sonuna kadar" gidiyor.

# Yan yana karşılaştır:
#   büyük olan sağa gider
#   her turda en büyük sona “bubbles”

def bubble_sort(arr):
    n = len(arr)
    for i in  range(n):
        for j in range (0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # SWAP kısmı burası
    return arr

print(bubble_sort([4, 2, 3, 1, 8, 90]))
# OUTPUT: [1, 2, 3, 4, 8, 90]

print("------------------------------------------------")

# TODO  Selection Sort -> En küçüğü alıyor direkt en baştaki eleman ile yer değiştiriyor.

# Mantık
# en küçüğü bul
# başa koy


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # SWAP kısmı burası
    return arr


print(selection_sort([5, 3, 8, 1, 12, 7]))
# OUTPUT: [1, 3, 5, 7, 8, 12]
print("------------------------------------------------")

# Insertion Sort = İlk eleman ile ikinci elaman arasına hayali çizgi ve kıyas yapılıp sonra, ikinci eleman ile üçüncü eleman arasına hayali çizgi vb. gider
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort([5, 3, 6, 7, 1, 80]))
# OUTPUT: [1, 3, 5, 6, 7, 80]


