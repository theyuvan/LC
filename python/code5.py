# Question : 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Answer

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if('(' == s[i] or '{' == s[i] or '[' == s[i]):
                stack.append(s[i])
            else:
                if(s[i] == ')'):
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
                elif(s[i] == '}'):
                    if not stack or stack[-1] != '{':
                        return False
                    stack.pop()
                elif(s[i] == ']'):
                    if not stack or stack[-1] != '[':
                        return False
                    stack.pop()
        if not stack:
            return True
        else:
            return False

sol = Solution()
s = "()[{}]"
res = sol.isValid(s)
print(res)
