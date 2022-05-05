#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            # 同一位置不行
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    # print('[',arg1,',',arg2,']')
                    return (i,j)
        # dict = {}
        # for i in range(len(nums)):
        #     if target-nums[i] in dict:
        #         return [dict[target-nums[i]], i]
        #     else:
        #         dict[nums[i]] = i

# @lc code=end


