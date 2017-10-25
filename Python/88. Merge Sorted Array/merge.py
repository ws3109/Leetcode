class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j, k = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if k < 0 or j >= 0 and nums1[j] >= nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            elif j < 0 or k >=0 and nums1[j] <= nums2[k]:
                nums1[i] = nums2[k]
                k -= 1
        
