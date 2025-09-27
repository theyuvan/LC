# Question : 
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# Explanation: If the input is 3, the output should be [1, 3, 3, 1]


# Answer

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri = [[1]]
        for i in range(1,rowIndex+1):
            prev = tri[-1]
            row = [1]
            for j in range(1,len(prev)):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            tri.append(row)
        print(tri)
        final = list(tri[rowIndex])
        if rowIndex == 0:
            return tri[0]
        else:
            return final


sol = Solution()
rowIndex = 0
res = sol.getRow(rowIndex)
print(res)
