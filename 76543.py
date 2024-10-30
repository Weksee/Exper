def get_even_divisors(x):
    k = 2
    divisors = set()
    while k * k <= x:
        if x % k == 0:
            if k % 2 == 0:
                divisors.add(k)
            if (x // k) != k and (x // k) % 2 == 0:
                divisors.add(x // k)
        k += 1
        return sorted(divisors)

for i in range(1000, 10000):
    even_divisors = get_even_divisors(i)
    if sum(even_divisors) == 9728:
        print(i)

    
    

