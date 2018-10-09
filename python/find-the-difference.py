# -*- coding: utf-8 -*-
"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        >>> s = "abcd"
        >>> t= "abcde"
        >>> solution = Solution()
        >>> solution.findTheDifference(s,t)
        'e'
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        r_counter = t_counter - s_counter
        keys = list(r_counter.keys())
        return keys[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)