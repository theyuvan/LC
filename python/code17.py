# Question : 
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.
# It reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# If the input is "A man, a plan, a canal: Panama", then the output should be true.


# Answer

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lc = s.lower()
        a = ""
        for i in range(len(lc)):
            if lc[i].isalnum() == True:
                a += lc[i]
        
        if a == a[::-1]:
            return True
        else:
            return False

sol = Solution()
s = "A man, a plan, a canal: Panama"
res = sol.isPalindrome(s)
print(res)