# Question : 
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# Hint 1: Most languages support lowercase conversion for a string data type. However, that is certainly not the purpose of the problem. Think about how the implementation of the lowercase function call can be done easily.
# Hint 2: THINK ASCII values!
# Hint 3: Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts. Does there seem to be any pattern there? Any mathematical relationship that we can use?
# If the input is "Hello World!", then the output should be "hello world!".

# Answer

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Built-in function approach
        # return s.lower()
        # Manual ASCII conversion approach by using Given Hints
        res = []
        for char in s:
            if 'A' <= char <= 'Z':      
                res.append(chr(ord(char) + 32))
            else:
                res.append(char)
        return ''.join(res)

sol = Solution()
s = "Hello World!"
res = sol.toLowerCase(s)
print(res)