#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (51.54%)
# Likes:    16523
# Dislikes: 440
# Total Accepted:    2.2M
# Total Submissions: 4.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
# 
# 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Given an integer target, return true if target is in matrix or false
# otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
       rows, cols = len(matrix), len(matrix[0])
       row = 0
       while row < rows:
            l, r = 0, cols - 1
            if matrix[row][0] <= target <= matrix[row][-1]:  # 只在可能存在的行搜索
                while l <= r:
                    mid = (l + r) // 2
                    midnum = matrix[row][mid]
                    if midnum == target:
                        return True
                    elif midnum < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            row += 1
       return False
        
# @lc code=end

