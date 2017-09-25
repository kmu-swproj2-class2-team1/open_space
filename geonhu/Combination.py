def factorial(n):
	if n <= 1: 
		return 1
	else:
		result = 1
		for i in range(2, n+1):
			result *= i
	return result

def factorial_recursive(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


def combination(n, r):
    return int(factorial_recursive(n)/(factorial_recursive(r)*factorial_recursive(n-r)))


if __name__ == "__main__":
    print(int(combination(5,3)))
    print(factorial_recursive(4))
