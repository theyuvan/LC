# Question : 
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# If the input is nums = [-1,0,3,5,9,12], target = 9, then the output should be 4.

# Answer

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)/2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

sol = Solution()
nums = [-1,0,3,5,9,12] 
target = 9  
res = sol.search(nums, target)
print(res)