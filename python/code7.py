# Question : 
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# Explanation: If the input( haystack = "sadbutsad", needle = "sad") , "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


# Answer

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        for s in range(n-m+1):
            if haystack[s:s+m] == needle:
                return s
        return -1

sol = Solution()
haystack = "sadbutsad"
needle = "sad"
res = sol.strStr(haystack,needle)
print(res)