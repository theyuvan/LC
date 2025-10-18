# Question : 
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# If the input is [0,1,0,3,12], then the output should be [1,3,12,0,0].

# Answer

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero = 0
        while i < len(nums) - zero:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zero += 1
            else:
                i += 1
        return nums

sol = Solution()
nums = [0,0,1] 
res = sol.moveZeroes(nums)
print(res)