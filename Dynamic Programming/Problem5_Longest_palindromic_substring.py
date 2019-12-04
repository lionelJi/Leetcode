class Solution1:
    def longestPalindrome(self, s):

        k = len(s)
        matrix = [[False for i in range(k)] for i in range(k)]
        longestSubStr = ''
        longestLen = 0

        for j in range(k):
            for i in range(j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = True
                        if j - i + 1 > longestLen:
                            longestSubStr = s[i: j + 1]
                            longestLen = j - i + 1

                else:
                    if s[i] == s[j] and matrix[i + 1][j - 1]:
                        matrix[i][j] = True
                        if j - i + 1 > longestLen:
                            longestSubStr = s[i: j + 1]
                            longestLen = j - i + 1
        return longestSubStr


class Solution2:
    def longestPalindrome(self, s):
        # 从中心选取pivot向两边扩张

        # 这个函数被调用 2n-1 次，分别为以n个数和n-1个数之间的空为中心
        def expandAroundCenter(s, left, right):
            L, R = left, right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L, R = L - 1, R + 1
            return R - L - 1

        if not s: return ''

        start = end = 0

        for i in range(len(s)):
            length = max(expandAroundCenter(s, i, i), expandAroundCenter(s, i, i + 1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start: end + 1]
