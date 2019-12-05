class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

s = Solution()
l = ["h","e","l","l","o"]
s.reverseString(l)
print(l)

l = ["h","e","l","l","o","w","o","r","l","d"]
s.reverseString(l)
print(l)
