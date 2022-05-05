#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1]!=9:
            digits[len(digits)-1]+=1
            return digits
        for i in range(0,len(digits)):
            print(i)
            if digits[len(digits)-i-1]!=9:
                digits[len(digits)-i-1]+=1
                for j in range(len(digits)-i,len(digits)):
                    digits[j]=0
                break
        else:
            digits[0]=1
            for i in range(1,len(digits)):
                digits[i]=0
            digits.append(0)
        return digits
            
# @lc code=end

