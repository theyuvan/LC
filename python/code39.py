# Question : 
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# If the input is [2,3,2] , then output is 2

# Answer

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = None

        for num in nums:
            if count == 0:
                temp = num
            if num == temp:
                count = count + 1
            else:
                count = count - 1
                
        return temp
    
sol = Solution()
nums = [2, 2, 1]
res = sol.majorityElement(nums)
print(res)