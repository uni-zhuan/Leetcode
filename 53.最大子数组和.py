#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #考虑全部是负数的情况，直接取最大
        for i in range(len(nums)):
            if nums[i]>=0: break
        else:
            return max(nums)
        sum=0
        num=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum<0:
                sum=0
            elif sum>=0:
                num=max(sum,num)
                print("num,sum,nums[i]:",num,sum,nums[i])
        return num

        
# @lc code=end

