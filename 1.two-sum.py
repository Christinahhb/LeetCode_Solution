#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (54.66%)
# Likes:    60216
# Dislikes: 2158
# Total Accepted:    16.1M
# Total Submissions: 29.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        Hashmap = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in Hashmap:
                return [Hashmap[m], i]
            else:
                Hashmap[n] = i
        
# @lc code=end

