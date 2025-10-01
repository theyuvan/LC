# Question : 
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# If the input is ["h","e","l","l","o"], then the output should be ["o","l","l","e","h"].

# Hint: Two-pointer approach to swap characters from both ends of the array until the pointers meet in the middle.
# Reference : https://en.wikipedia.org/wiki/In-place_algorithm#Examples

# Answer

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

sol = Solution()
s = ["h","e","l","l","o"]
res = sol.reverseString(s)
print(res)