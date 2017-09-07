def factorial(num):

    a = 1 #선언/초기화

    while(num>1):    #factorial 계산
        a = num * a    #입력받은 정수까지 곱셈
        num-=1    #입력받은 정수에서 1까지 빼줌
    
    return a


jungsu = int(input("펙토리얼 계산을 위한 정수를 입력해주세요: "))
print(factorial(jungsu))
