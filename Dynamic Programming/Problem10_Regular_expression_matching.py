class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for j in range(1, len(s) + 1):
            for i in range(1, len(p) + 1):
                if p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]

        return dp[len(p)][len(s)]

s = Solution()
print(s.isMatch('aab', 'c*a*b'))

