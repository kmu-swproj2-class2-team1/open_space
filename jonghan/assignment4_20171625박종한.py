from sys import exit

def combination(n,r): #combination calculate
    try:
        if r == 0:
            return 1
        elif r == n:
            return 1
        else:
            return combination(n-1,r-1) + combination(n-1,r)

    except RecursionError as e: #재귀 한계 초과 에러 처리
        print(e, "so kill the program")
        exit()
        
    except: #그 외 알 수 없는 에러 처리
        print("Unknow Error so kill the program")
        exit()

arr = list()

for i in range(0,2):
    n = int(input(""))
    arr.append(n)

print(combination(arr[0], arr[1]))
