#todo ==>  Recursive - Memoization
import  time

def factorial(n):

    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))

print("----------------------------------------------")

def countdown(x):

    if x == 0:
        print("Finished")
        return  # eğer boş return yazmazsan devam eder, durdurmak istediğin yerde return etmelisin

    print(x)

    countdown(x-1)

countdown(5)

print("----------------------------------------------")

# Fibonacci numbers but without memo
#todo ->  Fibonacci is "F(n)=F(n−1)+F(n−2)"

def fib(f):

    if f == 0:
        return 0

    elif f == 1:
        return 1

    else:
        return fib(f-1) + fib(f-2)



print("----------------------------------------------")

# Fibonacci numbers but with memo

memo = {
    0:0,
    1:1
}
def fibwithmemo(n):

    if n in memo:
        return memo[n]
    else:
        memo[n] = fibwithmemo(n-1) + fibwithmemo(n-2)

    return memo[n]
baslangicMemo = time.perf_counter()
print(fibwithmemo(25), memo)
bitisMemo = time.perf_counter()

print(f"Geçen süre with Memo: {bitisMemo - baslangicMemo:.6f} saniye")


baslangicNormal = time.perf_counter()
print(fib(25), memo)
bitisNormal = time.perf_counter()

print(f"Geçen süre without Memo: {bitisNormal - baslangicNormal:.6f} saniye")




"""
Notes for Memoization

memo = {}

def func(n):

    if n in memo:
        return memo[n]

    # base case
    if n == 0:
        return 0

    # hesaplama
    result = n * 2  # örnek işlem

    memo[n] = result
    return result
"""