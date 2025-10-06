# Question : 
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# If the input is [2,2,1], then the output should be 1.

# Answer

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummy =  []
        out = []
        for i in range(len(nums)):
            if nums[i] not in dummy:
                dummy.append(nums[i])
            else:
                out.append(nums[i])
        
        dummy = sorted(dummy)
        out = sorted(out)

        for i in range(len(out)):
            if out[i] != dummy[i]:
                return dummy[i]
        return dummy[-1]

sol = Solution()
nums = [4,1,2,1,2]
res = sol.singleNumber(nums)
print(res)