class Solution:
    def isValid(self, s: str) -> bool:

        # 栈中可以只存所有的左括号
        stack = []
        parentheses_map = {'{': '}', '[': ']', '(': ')'}

        for ch in s:
            if ch in parentheses_map.keys():
                stack.append(ch)
            else:
                if stack and ch == parentheses_map[stack[-1]]:
                    # 写成 if ch == parentheses_map[stack[-1]]: 时，输入为 ']' 的时候stack一直为空会报错数组越界
                    stack.pop()
                else:
                    return False
        return not stack

s = Solution()
print(s.isValid('()'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))
