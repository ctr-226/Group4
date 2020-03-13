def Eratoshenes(N, primes):
    if N**0.5 >= 2:
        Eratoshenes(N**0.5, primes)
        N_list = list(range(2, int(N) + 1))
        for prime in primes:
            for i in range(2, int(N / prime) + 1):
                if i * prime in N_list:
                    N_list.remove(i * prime)
        for num in N_list:
            if num not in primes:
                primes.append(num)
    elif N**0.5 < 2:
        for i in range(2, int(N) + 1):
            primes.append(i)
        return

primes = []
N = int(input("Please put in a number."))
Eratoshenes(N, primes)
print(primes)
# changes happen 1
# github test
# change on branch test