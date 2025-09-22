# Question : 
# Given two binary strings a and b, return their sum as a binary string.
# Explanation: If the input is a = "11", b = "1" then Output: "100"

# Answer

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Using inbuilt function
        # return format(int(a, 2) + int(b, 2), 'b')

        # manual implementation
        carry = 0
        res = ""
        i, j = len(a) - 1, len(b) - 1

        while i>=0 or j>=0 or carry:
            total = carry
            if i>=0:
                total += int(a[i])
                i -= 1
            if j>=0:
                total += int(b[j])
                j -= 1
            
            res = str(total % 2) + res
            carry = total  // 2
        
        if carry:
            res = "1" + res

        return res
            
sol = Solution()
a = "1010"
b = "1011"
res = sol.addBinary(a, b)
print(res)

