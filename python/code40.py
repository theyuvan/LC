# Question : 
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# If the input is 38, then the output should be 2.

# Answer

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        out = sum(int(i) for i in str(num))
        return self.addDigits(out)

sol = Solution()
num = 38
res = sol.addDigits(num)
print(res)  