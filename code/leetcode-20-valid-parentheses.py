"""
[Easy] https://leetcode.com/problems/valid-parentheses/
Description:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paired = {')': '(', '}': '{', ']' : '['}
        for cur_char in s:
            if cur_char in paired:
                # cur_char is closing bracket
                if stack and paired[cur_char] == stack[-1]:
                    # everything is fine
                    stack.pop()
                else:
                    # either bracket is not matching or stack is empty
                    return False
            else:
                # cur_char is opening bracket
                stack.append(cur_char)

        if stack:
            # had some opening brackets
            return False
        return True
