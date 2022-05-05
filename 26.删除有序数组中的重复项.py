#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        i=1
        cur=1
        while cur<length:
            if nums[i-1]==nums[i]:
                del nums[i]
            else:
                i+=1
            cur+=1
        
# @lc code=end

