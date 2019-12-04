class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1, n2 = len(nums1), len(nums2)

        # make sure time complexity is O(log(min(n1, n2)))
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2

        left, right = 0, n1
        while left < right:
            p1 = left + (right - left) // 2
            p2 = k - p1
            if nums1[p1] < nums2[p2 - 1]:
                left = p1 + 1
            else:
                right = p1

        p1, p2 = left, k - left

        # c1 = float('-inf') if p1 <= 0 else nums1[p1 - 1]
        # c2 = float('-inf') if p2 <= 0 else nums2[p2 - 1]
        c_left = max(float('-inf') if p1 <= 0 else nums1[p1 - 1], float('-inf') if p2 <= 0 else nums2[p2 - 1])

        if (n1 + n2) % 2 == 1:
            return c_left

        # c1 = float('inf') if p1 >= n1 else nums1[p1]
        # c2 = float('inf') if p2 >= n2 else nums2[p2]
        c_right = min(float('inf') if p1 >= n1 else nums1[p1], float('inf') if p2 >= n2 else nums2[p2])

        return (c_left + c_right) / 2


s = Solution()
print(s.findMedianSortedArrays([-1,1,3,5,7,9], [2,4,6,8,10,12,14]))
print(s.findMedianSortedArrays([-1,1,3,5,7,9], [2,4,6,8,10,12,14,16]))
