# Question : 
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
# If the input is [1,2,2,1] and [2,2], then the output should be [2].

# Answer

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []

        if nums1 and nums2:
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if nums1[i]== nums2[j]:
                        if nums1[i] not in out:
                            out.append(nums1[i])
        return out

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
res = sol.intersection(nums1, nums2)
print(res)