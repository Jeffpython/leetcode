# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


class Solution:
    def is_valid(self, s: str) -> bool:

        parentheses = [
            {"open": "(", "close": ")"},
            {"open": "[", "close": "]"},
            {"open": "{", "close": "}"}
        ]

        opening_paren = ""
        closing_paren = ""
        start_index = -1
        end_index = -1

        while s:
            for i in range(len(s)):
                if start_index == -1:
                    for paren in parentheses:
                        if s[i] == paren["open"]:
                            opening_paren = paren["open"]
                            closing_paren = paren["close"]
                            start_index = i
                            break

                    if start_index != -1 and i < len(s) - 1:
                        if s[i+1] == closing_paren:
                            end_index = i + 1
                            s = s[0:start_index] + s[end_index+1:]

                            opening_paren = ""
                            closing_paren = ""
                            start_index = -1
                            end_index = -1
                            break
                        else:
                            opening_paren = ''
                            closing_paren = ''
                            start_index = -1
                    else:
                        return False

        return True
