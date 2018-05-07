''' 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
    请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1 + nums2
        num3.sort()
        print(num3)
        n = len(num3)
        if n % 2 == 0:
            a = n // 2
            b = a + 1
            return (num3[a-1] + num3[b-1])/2

        else:
            a = n // 2
            return num3[a]


s = Solution()
nums1 = [1, 3]
nums2 = [2]
s.findMedianSortedArrays(nums1, nums2)