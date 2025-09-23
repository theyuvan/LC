# Question : 
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# By using Hint only I made it.
# Hint 1: Try exploring all integers. (Credits: @annujoshi)
# Hint 2: Use the sorted property of integers to reduce the search space. (Credits: @annujoshi)


# Answer

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l , r = 1 , x // 2
        while l <= r:
            m = (l+r) // 2
            if m <= x // m:
                l = m+1
            else:
                r = m-1
        return r

sol = Solution()
x = 16
res = sol.mySqrt(x)
print(res)