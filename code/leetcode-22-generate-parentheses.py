"""
[Medium] https://leetcode.com/problems/generate-parentheses/
Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List


class Solution:
    # runtime: 76ms, memory: 13.4 Mb
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            result = ['()']
        else:
            # covering n-1 substrings in big parentheses
            result = ['({})'.format(s) for s in self.generateParenthesis(n - 1)]

            # generating smaller pieces
            for first_size in range(1, n):
                all_firsts = self.generateParenthesis(first_size)
                all_seconds = self.generateParenthesis(n - first_size)
                for first in all_firsts:
                    for second in all_seconds:
                        full = first + second
                        if full not in result:
                            result.append(full)

        return result
