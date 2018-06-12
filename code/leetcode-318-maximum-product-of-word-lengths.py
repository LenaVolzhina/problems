"""
https://leetcode.com/problems/maximum-product-of-word-lengths/description/
Description
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain
only lower case letters. If no such two words exist, return 0.
"""


class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cur_max = 0
        letters = [set(w) for w in words]
        for n1 in range(len(words)):
            l1 = letters[n1]
            for n2 in range(n1, len(words)):
                l2 = letters[n2]
                if not l1 & l2:
                    cur_max = max(cur_max, len(words[n1]) * len(words[n2]))
        return cur_max
