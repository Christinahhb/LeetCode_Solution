#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (65.88%)
# Likes:    12719
# Dislikes: 422
# Total Accepted:    4.4M
# Total Submissions: 6.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        hashs = {}
        hasht = {}
        if len(s) != len(t):
            return False
            
        else:
            for i in range(0,len(s)):
                hashs[s[i]] = 1 + hashs.get(s[i],0)
                hasht[t[i]] = 1 + hasht.get(t[i],0)
            return hashs == hasht          
        
# @lc code=end

