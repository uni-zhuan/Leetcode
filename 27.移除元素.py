#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        i=0
        cur=0
        while cur<length:
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
            cur+=1
# @lc code=end

