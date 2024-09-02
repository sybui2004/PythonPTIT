MAX = 1000000
MOD = 1000000007
isPrime = [1] * (MAX + 1)
primes = []

def sieve():
    isPrime[0] = 0
    isPrime[1] = 0
    for i in range(2, int(MAX**0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, MAX + 1, i):
                isPrime[j] = 0
                
    for i in range(2, MAX + 1):
        if isPrime[i]:
            primes.append(i)

def count_factors(n, p):
    count = 0
    while n >= p:
        count += n // p
        n //= p
    return count

sieve()
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    ans = 1
    for prime in primes:
        if prime > b:
            break
        ans = ans * (2 * (count_factors(b, prime) - count_factors(a - 1, prime)) + 1) % MOD
    print(ans)