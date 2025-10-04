# Question : 
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
# If the input is 6, then the output should be true.

# Answer

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        if n != 1:
            return False
        else:
            return True
            

sol = Solution()
n = 6
res = sol.isUgly(n)
print(res)