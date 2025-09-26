# Question : 
# Given an integer numRows, return the first numRows of Pascal's triangle
# Explanation: If the input is 5, the output should be [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


# Answer

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = [[1]]
        for i in range(1,numRows):
            prev = tri[-1]
            row = [1]
            for j in range(1,len(prev)):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            tri.append(row)

        return tri
        
sol = Solution()
numRows = 5
res = sol.generate(numRows)
print(res)