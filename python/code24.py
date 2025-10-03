# Question : 
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
# If the input is 4, then the output should be 3.

# Answer

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0, 1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                f.append(f[i - 1] + f[i - 2])
            return f[n]
sol = Solution()
n = 4
res = sol.fib(n)
print(res)
