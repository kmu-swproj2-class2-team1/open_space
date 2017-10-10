import time

def fibo(n) :
    if n <= 1 :
        return n
        
    return fibo(n-1) + fibo(n-2)

def iterfibo(n) :
    if n == 0 or n == 1 :
        return n
    else :
        tmp = 1
        current = 1
        last = 0
        for i in range(2, n+1) :
            tmp = current
            current += last
            last = tmp

        return current

while True :
    nbr = int(input("Enter a number : "))
    if nbr == -1 :
        break

    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))