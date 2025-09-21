# Question : 
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# If the merged array = [1,2,3] and median is 2.
# If the merged array is [1,2,3,4], the median is (2 + 3) / 2 = 2.5.


# Answer

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        total = nums1 + nums2
        total.sort()
        n = len(total)
        print(n)
        if n % 2 == 1:
            return float(total[n // 2])
        else:
            return (total[n // 2 - 1] + total[n // 2]) / 2.0

sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
res = sol.findMedianSortedArrays(nums1,nums2)
print(res)  