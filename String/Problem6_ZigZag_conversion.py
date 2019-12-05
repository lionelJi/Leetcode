class Solution:
    def convert(self, s, numRows):

        # 第一行和最后一行下标间隔都是 interval = 2n - 2
        # 中间行的间隔是周期性的，第i行的间隔是 interval - 2*i, 2*i, interval - 2*i, 2*i

        if numRows == 1:
            return s
        ans = ''
        interval = 2 * numRows - 2

        for i in range(0, len(s), interval):
            ans += s[i]

        for row in range(1, numRows - 1):
            i = row
            inter = 2 * i
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter

        for i in range(numRows - 1, len(s), interval):
            ans += s[i]

        return ans


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))
