# Prime Arrangements
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, Primality Test, Sieve Theory, Prime Number Sieve

"""
This solution first counts how many prime numbers exist between 1 and $n$ using a standard trial-division primality test. It then calculates the number of valid arrangements by multiplying the factorial of the prime count with the factorial of the remaining (composite and 1) count, modulo $10^9 + 7$. The time complexity is $O(n \sqrt{n})$ due to checking primality for numbers up to $n$, and the space complexity is $O(1)$ as it uses a constant amount of extra space.
"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
            
        primes_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        composites_count = n - primes_count
        
        def factorial(x):
            res = 1
            for i in range(1, x + 1):
                res = (res * i) % MOD
            return res
            
        return (factorial(primes_count) * factorial(composites_count)) % MOD