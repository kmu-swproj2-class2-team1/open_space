def factorial(n):
    if n==1:
        return 1
 
    return n*factorial(n-1)

while True :
    number=int(input("Enter a number : "))
    if number==-1:
        break
    print(str(number)+"!="+str(factorial(number)))
    
