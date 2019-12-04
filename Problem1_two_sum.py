class Solution:
    def two_sum(self, nums, target):
        if not nums:
            return []

        s = set(nums)

        for index, num in enumerate(nums):
            remain = target - num
            if remain in s:
                i = nums.index(remain)
                if i == index: continue
                return [index, i]
        return [-1, -1]

    def two_sum_answer(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in h:
                return [h[n], i]
            else:
                h[num] = i


s = Solution()
result1 = s.two_sum([2,7,11,15], 9)
print(result1)
result2 = s.two_sum([0,1,2,3,4,5], 9)
print(result2)
result3 = s.two_sum([0,1,2,3,4,5,6], 12)
print(result3)
result4 = s.two_sum([3,2,4], 6)
print(result4)
result5 = s.two_sum_answer([3,2,4], 6)
print(result5)


