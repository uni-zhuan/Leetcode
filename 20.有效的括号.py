#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    # 代码量很少的题解
    # def isValid(self, s: str) -> bool:
    #     while "{}" in s or "[]"in s or "()" in s:
    #         s=s.replace("()","")
    #         s=s.replace("{}","")
    #         s=s.replace("[]","")
    #     return s==""

    # 我的，用栈实现
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        slist=list(s)   
        left=[]
        sdict={"(":")","[":"]","{":"}"}
        for i in range(len(slist)):
            if slist[i]=="("or slist[i]=="["or slist[i]=="{":
                left.append(slist[i])
            elif len(left)==0:
                return False
            else:
                temp=left.pop()
                if sdict[temp]!=slist[i]:
                    return False
        else:
            if len(left)==0:
                return True
            else:
                return False
# @lc code=end

