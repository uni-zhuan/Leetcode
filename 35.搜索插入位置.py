#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        index=0
        index = self.erfen(nums, 0, len(nums)-1, target)
        print(index)
        return index

    # 实际上是二分查找
    def erfen(self, nums, begin, end, target) -> int:
        # print("begin,end",begin,end)
        if end == begin and nums[begin] < target:
            print("1-", begin+1)
            return begin+1
        elif end == begin and nums[begin] > target:
            print("2-", begin)
            return begin
        else:
            mid = int((begin+end)/2)
            # print("mid,nums[mid]",mid,nums[mid])
            if nums[mid] > target:
                #python 函数递归使用堆栈，递归时要加return
                return self.erfen(nums, begin, mid, target)
            elif nums[mid] < target:
                return self.erfen(nums, mid+1, end, target)
            else:
                print("3-", mid)
                return mid
# @lc code=end
