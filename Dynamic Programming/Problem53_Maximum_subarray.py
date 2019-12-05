class Solution:
    def maxSubArray(self, nums) -> int:

        # ## Space Complexity: O(N)
        # DP 数组每个位置表示以该位置结尾的子数组的最大和，想起来比较直观

        # ans = nums[0]
        # dp = [ans] + [0 for i in range(len(nums) - 1)]
        #
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        #     ans = max(ans, dp[i])
        #
        # return ans

        # ## Space Complexity: O(1)
        # 用一个current sum 的值记录就可以
        ans = curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            ans = max(ans, curr_sum)

        return ans

