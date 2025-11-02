# Question : 
# You are playing the following Nim Game with your friend:
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally
# Otherwise return false.
# If the input n = 4, then the output should be false.

# Answer

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 != 0:
            return True
        else:
            return False

sol = Solution()
n = 4
res = sol.canWinNim(n)
print(res)