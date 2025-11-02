# Question : 
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. 
# In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.
# If the input num = 16, then the output should be true.

# Answer

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        per =  num**0.5
        n = round(per)
        if num == n*n:
            return True
        else:
            return False
        
sol = Solution()
num = 16
res = sol.isPerfectSquare(num)
print(res)