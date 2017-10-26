class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index_of_primes = [0 for _ in range(len(primes))]
        ugly = [1 for _ in range(n)]
        for i in range(1, n):
            ugly[i] = float('inf')
            for j in range(len(primes)):
                while primes[j] * ugly[index_of_primes[j]] <= ugly[i-1]:
                    index_of_primes[j] += 1
                ugly[i] = min(ugly[i], primes[j] * ugly[index_of_primes[j]])
        return ugly[n-1]
        
