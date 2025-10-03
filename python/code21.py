# Question : 
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# If the input is "IceCreAm", then the output should be "AceCreIm".

# Answer

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0
        r = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u' ,'A', 'E', 'I', 'O', 'U']

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)
    
sol = Solution()
s = "IceCreAm"
res = sol.reverseVowels(s)
print(res)