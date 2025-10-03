# Question : 
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Answer

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word.upper() == word or word.lower() == word:
            return True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        else:
            return False

sol = Solution()
word = "USA"
res = sol.detectCapitalUse(word)
print(res)