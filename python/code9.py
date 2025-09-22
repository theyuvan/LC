# Question : 
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Explanation: If the input is digits = [1,2,3], the array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.Thus, the result should be [1,2,4].


# Answer

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = int("".join(map(str,digits)))
        n +=1
        d = [int(digit) for digit in str(n) ]
        return d
        
sol = Solution()
digits = [1,2,3]
res = sol.plusOne(digits)
print(res)