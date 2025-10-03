
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