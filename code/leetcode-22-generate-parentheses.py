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
    # runtime: 44ms (about median), memory: 13.4 Mb
    def generateParenthesis(self, n: int, cur_opened: int = 0, prefix: str = '') -> List[str]:
        # DFS
        if n * 2 == len(prefix):
            # finished
            result = [prefix]

        elif cur_opened == 0:
            # need to open one more
            if len(prefix) + 2 <= n * 2:
                # have enough space left
                result = self.generateParenthesis(n, 1, prefix + '(')
            else:
                result = []

        else:
            # can either open or close
            # closing is always available
            result = self.generateParenthesis(n, cur_opened - 1, prefix + ')')

            # check if can open one more
            if len(prefix) + cur_opened + 2 <= n * 2:
                result.extend(self.generateParenthesis(n, cur_opened + 1, prefix + '('))

        return result

    # runtime: 76ms, memory: 13.4 Mb
    def generateParenthesis_naive(self, n: int) -> List[str]:
        if n == 1:
            result = ['()']
        else:
            # covering n-1 substrings in big parentheses
            result = ['({})'.format(s) for s in self.generateParenthesis_naive(n - 1)]

            # generating smaller pieces
            for first_size in range(1, n):
                all_firsts = self.generateParenthesis_naive(first_size)
                all_seconds = self.generateParenthesis_naive(n - first_size)
                for first in all_firsts:
                    for second in all_seconds:
                        full = first + second
                        if full not in result:
                            result.append(full)

        return result
