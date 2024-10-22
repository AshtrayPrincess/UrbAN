#Цикл for. Элементы списка. Полезные функции в цикле


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = list()
not_primes_= list()
for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for z in range(2, i):
        k = i%z
        if k == 0 :
            is_prime = False
            not_primes_.append(i)
            break
    if is_prime:
        primes_.append(i)
print(primes_)
print(not_primes_)

