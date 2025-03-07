#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (70.03%)
# Likes:    20087
# Dislikes: 667
# Total Accepted:    3.5M
# Total Submissions: 5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for n in strs:
            count = [0]*26 #initial a enmpty word count list
            for c in n:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(n)
        return list(res.values())
# @lc code=end

