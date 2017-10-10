import time


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


while True:
    n = int(input("Enter The Fibo Num :"))
    if n < 0:
        break
    start_time = time.time()
    print("Recursive Fibo / result : %d / time : %.6f" % (fibo(n), time.time() - start_time))
    start_time = time.time()
    print("Iterative Fibo / result : %d / time : %.6f\n" % (iterfibo(n), time.time() - start_time))
