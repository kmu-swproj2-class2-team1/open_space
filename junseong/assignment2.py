# Developed by Junseong Kim(codertimo@gmail.com)
# at 17.09.06 / Do not copy this code for assignment

n = int(input("무슨 팩토리얼? :"))

total = 1
for number in range(1, n+1):
    total *= number
print("Result : %d" % total)

