class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Set p1 and p2 as the pointer to the end of both arrays
        p1 = m - 1
        p2 = n - 1

        # Move p backward through the array each time we write the smallest value pointed at by p1 or p2
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break 
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1