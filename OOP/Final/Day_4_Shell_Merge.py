# Shell - Merge

# listenin uzunluğunu ikiye böl ve gap ile içerik araklarında elemanları karşılaştır.
# Aralık 1 olduğunda Insertion gibi çalış
# Aralık 0 olduğunda döngüyü sonlandır

def shell_sorting(list):
    gap = len(list) // 2 # Listenin uzunluğu (len(list)): 6 -> 2 ye böl = "3"
    while gap > 0:

        for i in range(gap, len(list)):

            temp = list[i]
            j = i

            while j >= gap and list[j- gap] > temp:
                list[j] = list[j - gap]
                j= j - gap
            list[j] = temp


        gap = gap // 2













    return list

L = shell_sorting([90, 8, 7, 4, 3, 2])
print(L)

print("--------------------------------------------------------")

#Merge
