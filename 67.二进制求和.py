#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #内置函数，py高精度所以不会溢出，其他语言慎用
        #特异情况：0+0，不排除则返回 ""
        if a=="0" and b=="0":
            return "0"
        return bin(int(a,2)+int(b,2)).lstrip("0b")
    #不用py内置函数：从尾部相加
    #为了让各个位置对齐，你可以先反转这个代表二进制数字的字符串，然后低下标对应低位，高下标对应高位
# @lc code=end

