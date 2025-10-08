# Question : 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# If the input is s = "anagram" and t = "nagaram", then the output should be true.

# Answer

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

sol = Solution()
s = "anagram"
t = "nagaram"
res = sol.isAnagram(s, t)
print(res)
