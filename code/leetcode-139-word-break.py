"""
[Medium] https://leetcode.com/problems/word-break/
Description:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.
"""
from typing import List


class Solution:
    def wordBreak_very_long(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            # empty
            return True

        for word in wordDict:
            if s.startswith(word):
                res = self.wordBreak_very_long(s[len(word):], wordDict)
                if res:
                    return True
        return False
