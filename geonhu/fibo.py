import time

def iterfibo(num):
    answer = [0,1]   
    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1]

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
    

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
