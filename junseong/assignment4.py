def combination_recursive(n, m):
    if n == m or m == 0:
        return 1
    else:
        return combination_recursive(n - 1, m - 1) + combination_recursive(n - 1, m)


def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def combination_equation(n, m):
    return int(factorial(n) / (factorial(m) * factorial(n - m)))


while True:
    n = int(input("Enter n: "))
    if n < 1:
        break

    m = int(input("Enter m: "))
    if m < 1:
        break

    # Calculating with combination equation
    print("C(%d, %d) = %d" % (n, m, combination_equation(n, m)))

    # Calculating with recursive equation
    # print("C(%d, %d) = %d" % (n, m, combination_recursive(n, m)))
