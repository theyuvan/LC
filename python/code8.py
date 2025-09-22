# Question : 
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# If the input is "   fly me   to   the moon  " , the last word is "moon" with length 4.


# Answer

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = s[::-1]
        a = b.lstrip()
        l = []
        for i in range(len(a)):
            if ' ' not in a[i]:
                l.append(a[i])
            else:
                break
        n = len(l)
        return n

sol = Solution()
s = "Hello World"
res = sol.lengthOfLastWord(s)
print(res)
