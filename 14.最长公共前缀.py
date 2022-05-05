#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    # 稍稍改进了点
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 先将全部字符串从短到长排序
        strs.sort(key=lambda x:len(x))
        # print(strs)
        length=len(strs[0])
        #判断首个字符是否是后面的前缀
        for i in range(length):
            for j in strs:
                # print(j,strs[0][0:length-i],j[0:length-i])
                if strs[0][0:length-i] != j[0:length-i]:
                    # print("break")
                    break
            else:
                return strs[0][0:length-i]
        else:
            return ""
    # 初解
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen=min(len(strs[i]) for i in range(len(strs)))
        print(minlen)
        for i in range(0,minlen):
            flag=strs[0][i]
            print(i,flag)
            for j in strs:
                print(j[i])
                if j[i]!=flag:
                    if i==0:
                        return ""
                    else:
                        return j[0:i]
        return strs[0][0:minlen]

# @lc code=end

