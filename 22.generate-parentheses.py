#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.19%)
# Likes:    21858
# Dislikes: 1016
# Total Accepted:    2.2M
# Total Submissions: 2.9M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        stack = []
        def backtrack(nOpen, nClose):
            if nOpen == nClose ==n:
                res.append("".join(stack))
                return
            if nOpen < n :
                stack.append("(")
                backtrack(nOpen+1,nClose)
                stack.pop()
            if nClose < nOpen :
                stack.append(")")
                backtrack(nOpen,nClose +1)
                stack.pop()
        backtrack(0,0)
        return res
        
# @lc code=end

