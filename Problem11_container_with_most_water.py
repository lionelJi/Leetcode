class Solution:
    def maxArea(self, height):

        # 列表内的双指针问题，挪动两边之间较矮的一条边，
        # 因为面积是根据矮边的高度算的，所以挪动高边只会让面积减少(宽度减少了，高还是按矮的算)

        max_area = float('-inf')

        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
max_area = s.maxArea([1,8,6,2,5,4,8,3,7])
print(max_area == 49)
