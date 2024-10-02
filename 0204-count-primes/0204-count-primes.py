class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        prime = [True] * (n)
        prime[0] = False
        prime[1] = False
        for i in range(2, (n//2) + 1):
            if prime[i]:
                for k in range(i*i, n, i):
                    prime[k] = False
        return sum(prime)