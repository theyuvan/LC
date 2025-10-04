# Question : 
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
# If the input is 4, then the output should be true.

# Answer
 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)  


sol = Solution()
n = 16
res = sol.isPowerOfTwo(n)
print(res)
        