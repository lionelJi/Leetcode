class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_left = 0
        max_length = 0
        d = {}

        for window_right in range(len(s)):

            if s[window_right] in d:
                window_left = max(window_left, d[s[window_right]] + 1)
            max_length = max(max_length, window_right - window_left + 1)

            d[s[window_right]] = window_right

        return max_length


