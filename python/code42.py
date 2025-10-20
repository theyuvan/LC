# Question : 
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
# If the input is pattern = "abba" and s = "dog cat cat dog", then the output should be True.

# Answer

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(pattern) != len(s):
            return False

        ctow = {}
        wtoc = {}

        for i in range(len(s)):
            c = pattern[i]
            word = s[i]

            if c in ctow and ctow[c] != word:
                return False
            if word in wtoc and wtoc[word] != c:
                return False

            ctow[c] = word
            wtoc[word] = c

        return True

sol = Solution()
pattern = "aaaa"
s = "dog cat cat dog"
res = sol.wordPattern(pattern, s)
print(res)