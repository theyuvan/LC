# Question : 
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.


# Answer

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        
sol = Solution()
nums = [1,3,5,6]
target = 5
res = sol.searchInsert(nums, target)
print(res)     