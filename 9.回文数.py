#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
# from sqlalchemy import false, true


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]
# @lc code=end

