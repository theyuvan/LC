# Question : 
# Given an integer array nums, return true if any value appears at least twice in the array. 
# And return false if every element is distinct.
# If the input is [1,2,3,1], then the output should be True.

# Answer
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dummy = set()
        out = set()

        for i in range(len(nums)):
            if nums[i] not in dummy:
                dummy.add(nums[i])
            else:
                out.add(nums[i])
        
        if out:
            return True
        else:
            return False

sol = Solution()
nums = [1,2,3,1]
res = sol.containsDuplicate(nums)
print(res)