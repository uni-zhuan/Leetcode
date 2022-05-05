#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
from tracemalloc import start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #单词中无空格或所有空格在尾部情况单独讨论，否则后续倒序遍历列表越界
        temp=s
        if " " not in temp.rstrip(" ") :
            return len(temp.rstrip(" ") )
        slist=list(s)
        print(slist)
        end=-1
        for i in range(1,len(slist)):
            print(len(slist)-i)
            if slist[len(slist)-i]!=" " and end==-1:
                end=len(slist)-i
            if slist[len(slist)-i]!=" " and  slist[len(slist)-i-1]==" ":
                start=len(slist)-i
                break
        # print(str(slist[start:end+1]))
        # if len(slist)==i+1:
        #     retur
        return end-start+1
# @lc code=end

