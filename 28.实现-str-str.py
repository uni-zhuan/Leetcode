#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start



class Solution:
    #KMP算法实现
    def strStr(self, haystack, needle):
        a, b = len(needle), len(haystack)
        if a == 0: return 0
        # 1、求next数组
        nxt = self.getnext(needle)
        # 2、模式匹配
        p = -1
        for j in range(b):
            #回退的操作
            while p >= 0 and needle[p+1] != haystack[j]:
                p = nxt[p] #回退的操作
            #向右逐个移位
            if needle[p+1] == haystack[j]:
                p += 1
            #移到终点，找到匹配
            if p == a - 1:
                return j - a + 1
        return -1
    # 求next数组
    def getnext(self, needle):
        nxt = [-1] * len(needle)
        j = -1
        for i in range(1, len(needle)):
            # 找相同前缀
            while (j >= 0 and needle[j+1] != needle[i]):
                j = nxt[j]
            if needle[j+1] == needle[i]:
                j += 1
            nxt[i] = j
        return nxt          
            

    #直接调index。。。
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         index=haystack.index(needle)
    #         # print(index)   
    #         return index
    #     except:
    #         # print(-1)
    #         return -1

    #这个超时，sb穷举
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if needle is "" :
    #         return 0
    #     if len(needle)>len(haystack):
    #         return -1
    #     if needle==haystack:
    #         return 0
    #     hlist=list(haystack)
    #     nlist=list(needle)
    #     # print(hlist)
    #     for i in range(0,len(hlist)-len(nlist)+1):
    #         if(hlist[i]==nlist[0]):
    #             j=0
    #             # print(hlist[i])
    #             while j<len(nlist):
    #                 # print(hlist[i+j],nlist[j])
    #                 if hlist[i+j]!=nlist[j]:
    #                     break
    #                 j+=1
    #             else:
    #                 if j==len(nlist):
    #                     return i
    #                 else:
    #                     return -1
    #     else:
    #         return -1


# @lc code=end

