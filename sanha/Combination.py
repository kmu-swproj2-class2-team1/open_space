n = int(input("n ="))

r = int(input("r ="))
def fac(n) :
    if n < 1 :
        return 1

    else :
        fac(n) = n * fac(n-1)

        
    return fac(n)


def com(n, r) :

    if n >= r :

        com(n, r) = fac(n) / (fac(r) * fac(n - r))

    else :
        return 0


print("n C r = " , com(n, r))
    
    
