# Question : 
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# If the input is [3,0,1], then the output should be 2.

# Answer

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = []
        for i in range(0,len(nums)+1):
            count.append(i)
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != count[i]:
                return count[i]
        return count[-1]

sol = Solution()
nums = [3,0,1]
res = sol.missingNumber(nums)
print(res)