#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        #尝试二分逼近的方法，精度到一定程度后
        if x<=1:
            return x
        else:
            start=1
            end=x
            return int(self.erfen(start,end,x))
        
    def erfen(self,start,end,x):

        # if int(start)==int(end):
        if int(end)-int(start)<=1:
            # print("1-",start)
            return int(start)
        mid=int((start+end)/2)
        print(start,end,mid)
        addi=mid*mid
        if(addi<x):
            return self.erfen(mid,end,x)
        elif(addi>x):
            return self.erfen(start,mid,x)
        else:
            # print("2-",mid)
            return mid



# @lc code=end

