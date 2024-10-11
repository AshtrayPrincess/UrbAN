# операторы if elif else

n1 = int(input("введите первое число: "))
n2 = int(input("введите второе число: "))
n3 = int(input("введите третье число: "))

if n1 == n2 and n2 == n3 and n3 == n1:
    print(3)
elif n1 == n2 or n2 == n3 or n3 == n1:
    print(2)
else:
    print(0)